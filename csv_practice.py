import csv
from datetime import datetime

print("---------- Exercise 2: read and print raw rows ----------")
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---------- Exercises 3-4: skip header, compute totals ----------")
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    total_revenue = 0
    for row in reader:
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{row[0]}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("---------- Exercise 5: filter and write cleaned.csv ----------")
rows_read = 0
rows_written = 0

with open("data/sales.csv", newline="") as f_in, \
     open("data/cleaned.csv", "w", newline="") as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        rows_read += 1
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        if total > 100:
            writer.writerow([row[0], price, quantity, round(total, 2)])
            rows_written += 1

print(f"Rows read: {rows_read}, rows written: {rows_written}")

print("---------- Exercise 6: DictReader ----------")
# (Write your 2 lines here: when would you prefer csv.reader vs DictReader?)
# csv.reader is simpler and fine for quick scripts, but it relies on column positions (row[2]), which break if columns are reordered.
# DictReader uses column names (row["quantity"]), so the code is easier to read and still works if the column order changes.
dict_total = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dict_total += float(row["price"]) * int(row["quantity"])

print(f"DictReader total: ${dict_total:.2f}")

print("---------- Exercise 7: summary by product ----------")
summary = {}
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        revenue = float(row["price"]) * int(row["quantity"])
        name = row["product"]
        summary[name] = summary.get(name, 0) + revenue

for name in sorted(summary):
    print(f"{name}: ${summary[name]:.2f}")

print("---------- Exercise 8: append mode log ----------")
with open("data/run_log.txt", "a") as log:
    log.write(f"{datetime.now()} - total revenue: ${total_revenue:.2f}\n")

