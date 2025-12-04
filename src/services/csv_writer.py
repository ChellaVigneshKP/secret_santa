import csv
import os
from typing import List

from models.assignment import Assignment


class CSVWriter:
    @staticmethod
    def write_assignments(output_path: str, assignments: List[Assignment]) -> None:
        """Writes Secret Santa assignments to CSV."""
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "Employee_Name",
                    "Employee_EmailID",
                    "Secret_Child_Name",
                    "Secret_Child_EmailID",
                ]
            )

            for a in assignments:
                writer.writerow(
                    [
                        a.giver.name,
                        a.giver.email,
                        a.receiver.name,
                        a.receiver.email,
                    ]
                )
