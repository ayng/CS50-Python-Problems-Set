# 🧠 Lecture 6: Mastering File Input and Output (File I/O)
To improve viewability: ⌘ + Shift + V
## 📄 File I/O: Storing and Retrieving Data

- So far, all data has lived temporarily in memory and disappeared when the program ends.
- **File I/O** lets your program store data in permanent files or read from existing ones.
- This is crucial for saving user input or using data between program runs.

## 📂 open: Accessing Files

- Use `open()` to create or access a file.
- Modes:
  - `'w'` writes (overwrites)
  - `'a'` appends (adds to file)
  - `'r'` reads from file
- Always close your files when done — or better, use `with`.

## 📥 with: Safer File Handling

- Using `with` automatically closes the file when finished.
- Helps avoid bugs where a file remains open unintentionally.
- Works with both reading and writing.

## 📄 Writing and Reading Text Files

- You can append new lines by adding `\\n` at the end of your input.
- Use `readlines()` to read multiple lines and store them in a list.
- Use `rstrip()` to remove unwanted line breaks.
- Sorting is easy: store names in a list and use `sorted()` before printing.

## 📋 CSV: Comma-Separated Values

- CSV files are simple text files where values are separated by commas.
- Useful for storing rows of structured data like names and houses.
- Use `.split()` to separate each row into individual values.
- Build lists or dictionaries for more readable data access.

## 🧠 CSV with Dictionaries

- Storing each record as a dictionary makes code easier to read and more flexible.
- Sorting a list of dictionaries can be done using `sorted()` and a `key` function.
- Use a **lambda** function to extract the sorting key inline.

## 🔒 Defensive CSV Parsing

- If your CSV file contains commas in values, naive splitting breaks.
- Use Python’s built-in `csv.reader` to safely parse those rows.
- Use `csv.DictReader` to read CSV files as dictionaries — making your code cleaner and safer.

## ✍️ Writing to CSV

- Use `csv.DictWriter` to write rows of dictionary data into a CSV.
- Specify the field names for consistency and clarity.
- Writing structured data in CSV helps future-proof your files.

## 🔢 Binary Files and 📷 PIL (Python Imaging Library)

- Binary files store data as 1s and 0s — including images, audio, and more.
- Use **PIL (Pillow)** to manipulate image files in Python.
- PIL can read, modify, and save images — even combine them into an animated GIF.
- Useful for creative or visual programming tasks.

## 🧠 Summary: What You Learned

- ✅ How to read and write data using file I/O
- ✅ How to use `open()` and `with` for safe file access
- ✅ How to parse and write CSV data, including dictionary-based approaches
- ✅ How to safely sort and display structured data
- ✅ How to process binary files like images using PIL

Your Python programs can now interact with the real world — saving data, reading files, and even creating images. You’ve unlocked a whole new level of capability. 🚀"
