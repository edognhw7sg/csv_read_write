import csv
import numpy as np

def csv_write(path, data):
    with open(path, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def csv_read(path):
    with open(path, encoding = "utf_8") as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    return l
