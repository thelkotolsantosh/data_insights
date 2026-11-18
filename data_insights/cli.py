import argparse
import json

import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Summarize the columns in a CSV file.")
    parser.add_argument("csv", help="CSV file with a header row")
    args = parser.parse_args()
    try:
        frame = pd.read_csv(args.csv)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Could not read CSV: {error}\n")
    columns = {}
    for name, values in frame.items():
        columns[name] = {
            "type": str(values.dtype),
            "missing": int(values.isna().sum()),
            "distinct": int(values.nunique()),
        }
    print(json.dumps({"rows": len(frame), "columns": columns}, indent=2))


if __name__ == "__main__":
    main()
