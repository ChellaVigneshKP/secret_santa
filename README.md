# Secret Santa Assignment Generator

---

# Description
This project automates Secret Santa assignments for Acme employees using employee data from CSV files.
It ensures that each employee is assigned a unique secret child following company rules and constraints.


---

## Features

- Parses employee list from CSV
- Ensures each employee gets exactly one unique secret child
- Prevents self-assignment
- Prevents assigning the same secret child as previous year
- Generates output CSV with final pairings
- Modular OOP design using industry best practices
- Comprehensive test coverage using `pytest`
- Clean error handling and validation


---

## Input Format

### Employees CSV

```
Employee_Name,Employee_EmailID
Alice,alice@acme.com
Bob,bob@acme.com
```

### Previous Year Assignments (optional)

```
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Alice,alice@acme.com,Bob,bob@acme.com
```

---

## How to Run

Run from the project root:

```sh
python -m src.main
```

Optional arguments:

```sh
python -m src.main \
  --employees data/employees.csv \
  --previous data/previous_assignments.csv \
  --output data/output/secret_santa_output.csv
```

After success, output file is created in:

```
data/output/secret_santa_output.csv
```

---

## Running Tests

Install dependencies:

```sh
pip install -r requirements.txt
```

Execute tests:

```sh
pytest -q
```

---