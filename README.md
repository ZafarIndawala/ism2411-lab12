# ISM2411 Lab 12 — Read a Sales CSV, Write a Cleaned Report

**Name:** Zafar Indawala

**Semester:** Fall 2026

**Instructor:** Markum Reed

## About This Repo

This repository contains my Lab 12 submission for ISM2411. The script
`csv_practice.py` reads `data/sales.csv`, calculates totals, writes a
filtered `data/cleaned.csv`, summarizes revenue by product, and logs
each run to `data/run_log.txt`.

## Files

- `csv_practice.py`: Exercises 2-8
- `data/sales.csv`: input data (header row plus 12 data rows)
- `data/cleaned.csv`: output file with orders over $100
- `data/run_log.txt`: one line per run with timestamp and total revenue
- `.gitignore`: Python and OS exclusions

## Exercises

- **Exercise 1: Get the file.** Downloaded `sales.csv` into `data/` and
  confirmed it has the columns `product`, `price`, `quantity` and 12 data rows.
- **Exercise 2: Read and print raw rows.** Used `csv.reader` inside a
  `with` block to print every row, including the header. All values are
  strings.
- **Exercise 3: Skip the header.** Used `next(reader)` to store and print
  the header once, so the loop starts at the first data row.
- **Exercise 4: Compute totals.** Converted price to `float` and quantity
  to `int`, printed each line as units × price = total, then printed the
  overall total revenue.
- **Exercise 5: Filter and write.** Wrote `data/cleaned.csv` with the
  columns Product, Price, Qty, Total, keeping only orders over $100, and
  printed rows read versus rows written.
- **Exercise 6: csv.DictReader.** Re-read the file by column name and
  confirmed the total matches Exercise 4. A comment in the code compares
  `csv.reader` and `DictReader`.
- **Exercise 7: Sales summary by product.** Built a dictionary of total
  revenue per product and printed it sorted by product name.
- **Exercise 8: Append mode log.** Appended a timestamp and the total
  revenue to `data/run_log.txt` on each run, using append mode so the log
  accumulates.

## How to Run

Open a terminal in this folder and run:

```
python csv_practice.py
```


