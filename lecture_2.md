# 🧠 Lecture 2: Mastering Loops, Lists, and Data Structures
To improve viewability: ⌘ + Shift + V
## 🔁 Loops: Do It Again!

- Loops let your program repeat actions — great when you don’t want to write the same line 500 times!
- Instead of repeating a task manually, use a loop to do it for you automatically.
- Loops help keep code short, flexible, and readable.

## 🔄 While Loops

- A while loop runs as long as a condition is true.
- It’s like saying: “While this is true, keep doing this.”
- You must be careful not to create an infinite loop — use `Ctrl+C` to stop one!
- Each cycle of the loop is called an **iteration**.
- Use while loops when you don’t know how many times you’ll loop in advance.

## 🔂 For Loops

- A for loop runs a fixed number of times or over items in a list.
- It’s great for looping through a sequence like a list of names.
- The `range()` function automatically gives you a series of numbers.
- You can use `_` if you don’t need to use the loop variable.
- For loops are cleaner for known-length repetitions.

## 🎯 Improving Output

- You can multiply strings like `"meow" * 3` to repeat them.
- Use newline characters (`\\n`) to print each on a new line.
- Adding `end=""` prevents unwanted blank lines.

## 🙋‍♂️ Loops + User Input

- A while loop can be used to **validate** input from the user.
- Use `break` to exit a loop early when valid input is received.
- Use `continue` to skip to the next iteration if the input is invalid.
- Combine input, validation, and looping for more robust programs.

## 🧠 Functions Make It Better

- Break your program into small tasks using functions.
- Return values from helper functions to make main code cleaner.
- Combine input collection and output logic into separate blocks for readability.

## 📋 Lists: Ordered Groups of Values

- Lists store multiple items in a specific order.
- You can access each item using its position (starting at 0).
- A for loop can loop through each item in a list automatically.
- Use meaningful variable names like `student` when iterating over lists.

## 📏 len: Measuring a List

- `len` gives you the length of a list.
- Combine `range` and `len` to loop through both positions and values.
- Great when you need to know **where** an item is in a list.

## 🔑 Dictionaries (dict): Key-Value Pairs

- Dicts link keys to values — like a student to a house.
- Keys must be unique and can be words or numbers.
- Use curly braces `{}` to define them.
- Looping over a dict goes through the **keys**.
- You can access values using the key inside square brackets.
- Clean up your print output using separators like commas for clarity.

## 🧱 Lists of Dicts = Structured Data

- You can combine lists and dicts for more detailed data.
- Each item in a list can be its own dictionary with multiple key-value pairs.
- Use `None` for values that are unknown or missing.
- Loop through each dict and access each field to display complete info.

## 🎮 Mario: Looping Rows and Columns

- Use loops to draw shapes like vertical and horizontal lines with symbols.
- Combine loops to draw both **rows and columns** — forming 2D shapes.
- Nesting loops allows you to build **grids** or squares.
- Abstracting logic into functions (like `print_row` or `print_square`) keeps code clean and modular.

## 🧠 Summary: What You Learned

- ✅ How to repeat tasks using `while` and `for` loops
- ✅ How to validate user input using loops and control keywords
- ✅ How to structure data with `list` and `dict`
- ✅ How to measure length using `len`
- ✅ How to combine functions and loops for clean, reusable code
- ✅ How to model grids and shapes using nested loops
- ✅ How to organize and display complex data with lists of dictionaries

Your Python skills have now expanded to include looping, organizing data, and designing logic in repeatable and scalable ways. Keep going — you're building real power! 🚀"
