import csv
import json
from pathlib import Path


def main():
    activity_dir = Path(__file__).resolve().parents[1]
    input_file = activity_dir / "data" / "drivers.csv"
    output_file = activity_dir / "submission" / "drivers.json"

    fields = ("driverId", "name", "certified", "wage-plan")
    with input_file.open("r", encoding="utf-8", newline="") as csv_file:
        records = [
            {field: row[field] for field in fields}
            for row in csv.DictReader(csv_file)
        ]

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as json_file:
        json.dump(records, json_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
