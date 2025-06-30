# 🧠 Lecture 4: Using Libraries and APIs to Supercharge Python
To improve viewability: ⌘ + Shift + V
## 📚 What Are Libraries?

- Libraries are reusable code modules written by you or others.
- You can import them into your own programs to avoid reinventing the wheel.
- Python lets you reuse old functions by turning them into shareable libraries.

## 🎲 random: The Built-in Randomness Engine

- The `random` module is built into Python.
- Use it to simulate chance or unpredictability.
- Key functions:
  - `choice()` picks one item randomly from a list.
  - `randint()` gives you a random number between two values.
  - `shuffle()` mixes up a list in place.

## 📊 statistics: Built-In Math Power

- The `statistics` module provides tools like `mean()` to calculate averages.
- Feed it a list of numbers, and it returns the average.
- Useful for programs involving scores, grades, or analytics.

## 🧾 Command-Line Arguments with sys

- The `sys` module lets you grab values typed after a program name.
- `argv` is a list containing what the user typed:
  - `argv[0]` is the name of the program.
  - `argv[1]` and beyond are the extra arguments.
- Validate input length with `len()`.
- Use `sys.exit()` to cleanly exit if something's wrong.

## ✂️ slice: Skipping the First Item

- Slice syntax `[1:]` lets you skip the first item in a list.
- Great for ignoring the program name in command-line arguments.

## 📦 Packages: External Tools You Can Install

- Python’s package manager is `pip`.
- You can install packages like `cowsay` to add fun or functionality.
- Packages live in the **PyPI** repository (Python Package Index).
- Third-party packages make Python incredibly powerful.

## 🌐 APIs: Talking to Other Programs

- APIs let your Python program talk to websites or services.
- Use the `requests` package to behave like a browser and fetch web data.
- APIs often return JSON — a structured text format.
- Use `json.dumps()` to pretty-print the data.
- You can extract specific parts (like song titles) from the JSON dictionary.

## 🛠️ Making Your Own Libraries

- You can write your own module with functions you want to reuse.
- Store them in a separate file and import them into any other script.
- This keeps your code DRY (Don’t Repeat Yourself) and organized.

## 🧠 Summary: What You Learned

- ✅ How to use built-in and external libraries
- ✅ How to use `random` to simulate chance
- ✅ How to use `statistics` for calculations like average
- ✅ How to handle command-line input using `sys.argv`
- ✅ How to use slice syntax to skip parts of a list
- ✅ How to install and use third-party packages with `pip`
- ✅ How to call real APIs and parse the JSON results
- ✅ How to write your own libraries to reuse your code

You now have the power to extend Python far beyond its core features — with randomness, math, web data, and your very own tools! 🚀"
