# 🧠 Lecture 3: Handling Errors with Grace in Python
To improve viewability: ⌘ + Shift + V
## 🚨 Exceptions: When Things Go Wrong

- **Exceptions** are problems that occur while your program is running.
- They can crash your program if not handled properly.
- Common causes: missing symbols, invalid input, unexpected behavior.
- A **syntax error** happens when your code is typed incorrectly.
- A **runtime error** happens during execution — often due to user input.

## 💥 Runtime Errors: The Unexpected

- Runtime errors are triggered by things like:
  - Typing a word instead of a number
  - Hitting enter with no input
- You must assume users will make mistakes — and protect your code from crashing!

## 🧪 try: Safely Testing Risky Code

- Use `try` to test code that could go wrong.
- If the risky part fails, Python jumps to `except`.
- This keeps your program alive instead of crashing.
- Only wrap the code that might fail — not everything!

## 🙅‍♂️ else: When Things Go Right

- Use `else` with `try` to run code **only if no error occurs**.
- This keeps your logic clean and helps you avoid using undefined variables.
- `else` gives you more control after a successful try.

## 🔁 Loops + Error Handling = Resilient Programs

- Combine `while True` and `try` to keep asking the user until they give valid input.
- If they mess up, catch the error and reprompt.
- Once they get it right, `break` out of the loop and continue.
- This is a pattern you’ll use often for user-friendly input handling.

## 🧩 Creating a Function to Get an Integer

- Wrap your input-checking logic into a function.
- Now you can reuse this logic in other programs!
- Functions like `get_int()` make your main code shorter and cleaner.
- Returning the value from inside `else` is good — but even better is returning directly inside `try`.

## 🤫 pass: Silently Try Again

- Sometimes, instead of warning the user, you just want to reprompt quietly.
- Use `pass` to skip the error message but continue looping.
- Whether you inform the user or not is up to you — be intentional about it.

## 🗣️ Custom Prompts

- You can pass a prompt into your function to control what the user sees.
- This makes your code more flexible and personalized.

## 🧠 Summary: What You Learned

- ✅ What exceptions are and how they happen
- ✅ The difference between syntax and runtime errors
- ✅ How to use `try` and `except` to catch mistakes
- ✅ How `else` helps run code when no error occurs
- ✅ How to use loops to validate user input
- ✅ How to create clean input functions with `return`
- ✅ How `pass` lets you silently ignore exceptions
- ✅ How to make your functions reusable with custom prompts

With these skills, you can now build Python programs that don’t just work — they recover from mistakes and guide users gently. 🛡️"
