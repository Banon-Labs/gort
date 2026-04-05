#!/usr/bin/env python3
"""Fail on accidental adjacent duplicate Markdown lines outside fenced code blocks."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def iter_markdown_files(paths: list[str]) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            found.extend(sorted(p for p in path.rglob("*.md") if p.is_file()))
        elif path.is_file() and path.suffix.lower() == ".md":
            found.append(path)
    deduped: list[Path] = []
    seen: set[Path] = set()
    for path in found:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            deduped.append(path)
    return deduped


def find_adjacent_duplicates(path: Path) -> list[tuple[int, int, str]]:
    duplicates: list[tuple[int, int, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    previous_line: str | None = None
    previous_number: int | None = None

    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            previous_line = None
            previous_number = None
            continue

        if in_fence or not stripped:
            previous_line = None
            previous_number = None
            continue

        if previous_line == line and previous_number is not None:
            duplicates.append((previous_number, number, line))

        previous_line = line
        previous_number = number

    return duplicates


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Detect accidental adjacent duplicate non-empty Markdown lines "
            "outside fenced code blocks."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Files or directories to scan (default: current directory).",
    )
    args = parser.parse_args()

    markdown_files = iter_markdown_files(args.paths)
    if not markdown_files:
        print("No Markdown files found.")
        return 0

    failures: list[str] = []
    for path in markdown_files:
        for start, end, line in find_adjacent_duplicates(path):
            failures.append(f"{path}:{start}-{end}: {line}")

    if failures:
        print("Adjacent duplicate Markdown lines detected:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print(f"No adjacent duplicate Markdown lines found in {len(markdown_files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
