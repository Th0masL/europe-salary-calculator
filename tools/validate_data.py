#!/usr/bin/env python3
"""Validate invariants required by the browser interpolation engine."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATASETS = ("ebook", "skuad", "deel", "consensus", "formula", "us")
AXES = ("gross", "cost", "net")


def validate_dataset(name):
    path = ROOT / "data" / f"{name}.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    seen = set()

    wrapper = path.with_suffix(".js")
    if not wrapper.exists():
        errors.append(f"{name}: missing browser wrapper {wrapper.name}")
    else:
        script = wrapper.read_text(encoding="utf-8")
        try:
            wrapped = json.loads(script.split("=", 1)[1].strip().removesuffix(";"))
            if wrapped != doc:
                errors.append(f"{name}: {wrapper.name} is out of sync with {path.name}")
        except (IndexError, json.JSONDecodeError) as error:
            errors.append(f"{name}: invalid browser wrapper: {error}")

    for country in doc.get("countries", []):
        label = country.get("name", "<unnamed>")
        if label in seen:
            errors.append(f"{name}: duplicate location {label}")
        seen.add(label)

        points = country.get("points", [])
        if len(points) < 2:
            errors.append(f"{name}/{label}: needs at least two points")
            continue

        for axis in AXES:
            values = [point[axis] for point in points if point.get(axis) is not None]
            for previous, current in zip(values, values[1:]):
                if current < previous:
                    errors.append(
                        f"{name}/{label}: {axis} decreases from {previous} to {current}"
                    )

        for point in points:
            gross = point.get("gross")
            cost = point.get("cost")
            net = point.get("net")
            if gross is not None and cost is not None and cost < gross:
                errors.append(f"{name}/{label}: employer cost {cost} is below gross {gross}")
            if gross is not None and net is not None and net > gross:
                errors.append(f"{name}/{label}: net {net} exceeds gross {gross}")

    return errors


def main():
    errors = []
    for dataset in DATASETS:
        errors.extend(validate_dataset(dataset))
    if errors:
        print("Data validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(DATASETS)} datasets: interpolation axes are monotonic.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
