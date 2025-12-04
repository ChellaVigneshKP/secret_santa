import argparse
import sys

from services.assignment_generator import AssignmentGenerator
from services.csv_reader import CSVReader
from services.csv_writer import CSVWriter
from utils.exceptions import SecretSantaError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Secret Santa assignment generator for Acme."
    )
    parser.add_argument(
        "--employees",
        default="../data/employees.csv",
        help="Path to employees CSV (default: data/employees.csv)",
    )
    parser.add_argument(
        "--previous",
        default="data/previous_assignments.csv",
        help="Path to previous assignments CSV (optional). "
             "If file is missing, it will be ignored.",
    )
    parser.add_argument(
        "--output",
        default="data/output/secret_santa_output.csv",
        help="Path to output CSV (default: data/output/secret_santa_output.csv)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        employees = CSVReader.read_employees(args.employees)
        previous_assignments = CSVReader.read_previous_assignments(args.previous)

        generator = AssignmentGenerator(
            employees=employees,
            previous_assignments=previous_assignments,
        )
        assignments = generator.generate()

        CSVWriter.write_assignments(args.output, assignments)

        print(f"Successfully generated {len(assignments)} Secret Santa assignments.")
        print(f"Output written to: {args.output}")
        return 0

    except SecretSantaError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1
    except Exception as e:
        # Catch-all for unexpected issues
        print(f"[UNEXPECTED ERROR] {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())