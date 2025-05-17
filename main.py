"""Command-line tool that prints the sum of two numbers."""

from __future__ import annotations

import argparse


def sum_two_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    """Parse command-line arguments and print the sum."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    result = sum_two_numbers(args.a, args.b)
    print(f"The sum of {args.a} and {args.b} is {result}")


if __name__ == "__main__":
    main()
