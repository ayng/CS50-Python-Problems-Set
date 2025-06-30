# 🧠 Lecture 1: Mastering Conditionals in Python
To improve viewability: ⌘ + Shift + V
## 🔀 Conditionals: The Fork in the Road

- Conditionals give your program the power to choose between different paths.
- Think of them like a fork in the road — the program chooses left or right based on a condition.
- You use **comparison operators** to create these conditions:
  - > means greater than
  - < means less than
  - >= means greater than or equal to
  - <= means less than or equal to
  - == means equal to (double equals!)
  - != means not equal to
- These checks return **True** or **False**, and the program responds accordingly.

## 🧱 The if Statement

- An if statement checks a condition.
- If the condition is true, the code inside it runs.
- The input values are often cast as integers before comparison.
- This is your first building block of control flow.

## 🔄 Control Flow with elif and else

- You can stack conditions:
  - `if` checks the first condition.
  - `elif` checks another if the first is false.
  - `else` runs if nothing above is true.
- This makes your code **efficient** and **clean**.
- Only the first true condition will trigger — others are skipped.
- Replacing a final `elif` with `else` creates a catch-all result, simplifying logic.

## ⚖️ or: One or the Other

- The `or` keyword checks if **at least one** condition is true.
- Great for reducing redundant logic.
- You can replace multiple conditions with a single `!=` check to simplify things.
- Efficiency improves when you ask **one good question** instead of many smaller ones.

## 🔗 and: All Must Be True

- The `and` keyword checks if **both** conditions are true.
- Ideal for checking whether a number falls within a range.
- Python allows clean syntax like `90 <= score <= 100`, which is uncommon in other languages.
- Reduce complexity by removing unneeded checks — simpler is better.

## ➗ Modulo: Finding Even or Odd

- The `%` (modulo) operator finds the **remainder** after division.
- A number is even if dividing by 2 leaves no remainder (`% 2 == 0`).
- This is how we check parity (even vs. odd) in Python.

## 🧪 Creating Our Own Parity Function

- You can define your own function to check if a number is even.
- The function returns `True` or `False` — a **Boolean**.
- Your main program can use this returned value to decide what to print.
- This is reusable, clean, and keeps logic organized.

## 🐍 Pythonic Style

- “Pythonic” means writing code in a way that’s elegant, readable, and uniquely Python.
- Python allows concise expressions like:
  - Returning a condition directly
  - Writing logic that almost reads like English
- Pythonic code = less clutter, more clarity.

## 🧬 match Statements

- A `match` statement works like a cleaner version of many `if/elif` statements.
- It compares a variable to a set of known cases and runs code for the first match.
- A special case (`_`) acts like an `else`, catching anything not matched above.
- You can use `|` to match multiple values in a single case.
- match = organized, readable decision-making.

## 🧠 Summary: What You Learned

- ✅ How to use conditional logic to make decisions
- ✅ Comparison operators: >, <, ==, !=, etc.
- ✅ How if, elif, and else build control flow
- ✅ How `or` checks if either condition is true
- ✅ How `and` checks if both conditions are true
- ✅ How `%` finds if a number is even or odd
- ✅ How to build your own reusable functions
- ✅ What makes code Pythonic
- ✅ How to simplify logic using match statements

With this knowledge, you’ve leveled up your ability to make your Python programs think, react, and respond based on any condition. 🚀"
