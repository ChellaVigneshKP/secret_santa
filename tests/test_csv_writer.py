import csv
from models.employee import Employee
from models.assignment import Assignment
from services.csv_writer import CSVWriter


def test_write_assignments(tmp_path):
    out_path = tmp_path / "out.csv"

    employees = [
        Employee("A", "a@mail.com"),
        Employee("B", "b@mail.com"),
    ]
    assignments = [
        Assignment(employees[0], employees[1]),
        Assignment(employees[1], employees[0]),
    ]

    CSVWriter.write_assignments(str(out_path), assignments)

    with open(out_path, newline="") as f:
        reader = list(csv.reader(f))

    # Validate header + 2 rows
    assert len(reader) == 3
    assert reader[0] == [
        "Employee_Name",
        "Employee_EmailID",
        "Secret_Child_Name",
        "Secret_Child_EmailID",
    ]
