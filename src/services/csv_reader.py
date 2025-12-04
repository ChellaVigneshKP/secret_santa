import csv
import os
from typing import List

from models.assignment import Assignment
from models.employee import Employee
from utils.exceptions import InvalidCSVError


class CSVReader:
    REQUIRED_EMPLOYEE_COLUMNS = {"Employee_Name", "Employee_EmailID"}
    REQUIRED_PREVIOUS_COLUMNS = {
        "Employee_Name",
        "Employee_EmailID",
        "Secret_Child_Name",
        "Secret_Child_EmailID",
    }

    @staticmethod
    def _validate_file_exists(path: str) -> None:
        if not os.path.exists(path):
            raise InvalidCSVError(f"File not found: {path}")

    @classmethod
    def read_employees(cls, filepath: str) -> List[Employee]:
        """Reads current year employees from CSV."""
        cls._validate_file_exists(filepath)

        employees: List[Employee] = []
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = cls.REQUIRED_EMPLOYEE_COLUMNS - set(reader.fieldnames or [])
            if missing:
                raise InvalidCSVError(
                    f"Employees CSV missing columns: {', '.join(sorted(missing))}"
                )

            for row in reader:
                name = row["Employee_Name"].strip()
                email = row["Employee_EmailID"].strip()
                if not name or not email:
                    continue
                employees.append(Employee(name=name, email=email))

        if len(employees) < 2:
            raise InvalidCSVError("At least 2 employees are required for Secret Santa.")

        return employees

    @classmethod
    def read_previous_assignments(cls, filepath: str) -> List[Assignment]:
        """Reads previous year assignments if file exists, else returns empty list."""
        if not os.path.exists(filepath):
            return []

        assignments: List[Assignment] = []
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = cls.REQUIRED_PREVIOUS_COLUMNS - set(reader.fieldnames or [])
            if missing:
                raise InvalidCSVError(f"Previous assignments CSV missing columns: {', '.join(sorted(missing))}")

            for row in reader:
                giver = Employee(
                    name=row["Employee_Name"].strip(),
                    email=row["Employee_EmailID"].strip(),
                )
                receiver = Employee(
                    name=row["Secret_Child_Name"].strip(),
                    email=row["Secret_Child_EmailID"].strip(),
                )
                assignments.append(Assignment(giver=giver, receiver=receiver))

        return assignments
