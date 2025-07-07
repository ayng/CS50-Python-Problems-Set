# 📄 CSV Reading and Writing in Python

Working with CSV files in Python is common for reading data and writing structured output. The `csv` module provides two main interfaces:

---

## 📥 `csv.reader`

Use when reading **CSV files without headers** or when you want to process rows as lists.

### 🔧 Basic Usage:
```python
import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Use to skip the first row
    for row in reader:
        print(row)  # Each row is a list of strings
```

# 🧪 csv.DictReader — Read rows as dictionaries

Use when reading **CSV files with headers.** It automatically maps each row to a dictionary using the headers as keys.
```python
import csv

with open('file.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['house'])  # Output: Harry Potter Gryffindor
```

# ✍️ csv.writer — Write rows as plain lists

Use to write data as plain rows (lists). You are responsible for the structure.
```python
import csv

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'house'])                     # Header
    writer.writerow(['Harry Potter', 'Gryffindor'])        # Data row
```
# ✍️ csv.DictWriter — Write rows as dictionaries

Use to write structured rows as dictionaries — very useful when working with JSON-like data or structured transformations.
Automatically writes headers if you use .writeheader()

```python
import csv

with open('file.csv', 'w', newline='') as f:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Writes: first,last,house
    writer.writerow({'first': 'Harry', 'last': 'Potter', 'house': 'Gryffindor'})
```

### 🧠 When to Use What?

| Task                          | Use This         |
|------------------------------|------------------|
| Quick reading, no headers     | `csv.reader`     |
| Reading structured rows       | `csv.DictReader` |
| Writing rows as lists         | `csv.writer`     |
| Writing rows as dictionaries  | `csv.DictWriter` |
