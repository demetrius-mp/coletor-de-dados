from __future__ import annotations

import csv
import os


def save_as_csv(data: list[dict], file: os.PathLike | bytes):
    first_row = data[0]
    headers = tuple(first_row.keys())
    with open(file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
