# 🧠 Lecture 5: Testing Your Code Like a Pro
To improve viewability: ⌘ + Shift + V
## ✅ Unit Tests: Automated Code Checking

- Instead of checking outputs with print statements, use **unit tests** to check if your code works as expected.
- Unit tests are small, repeatable tests for individual pieces of your program.
- They help catch bugs early and keep your code reliable as it grows.

## 🧪 assert: Built-In Testing Tool

- The `assert` keyword checks that something is true.
- If the condition is false, Python raises an error and stops the program.
- It’s a quick way to validate expected outcomes without print statements.
- You can use `try`/`except` to handle errors more gracefully if needed.

## 🔥 pytest: Powerful Testing Framework

- `pytest` is a third-party tool for running unit tests more efficiently.
- It shows results clearly, highlighting which tests passed or failed.
- You can group tests by function (e.g., positive, negative, zero).
- It continues running even if one test fails — showing all issues at once.
- You can also test for expected errors using `pytest.raises`.

## 🧵 Testing Strings

- If a function prints something, you can’t test it with `assert` directly.
- To test output, the function must **return** a string, not just print it.
- Changing your function to return a value lets you write proper tests.

## 🗂️ Organizing Tests into Folders

- It’s common to store all tests in a dedicated folder, such as `test/`.
- Each test file should follow naming conventions like `test_hello.py`.
- Add a special empty file called `__init__.py` to the test folder so `pytest` can find it.
- Then you can run all tests in the folder using one command.

## 🧠 Summary: What You Learned

- ✅ What unit tests are and why they’re important
- ✅ How to use `assert` to verify outputs
- ✅ How `pytest` simplifies and enhances testing
- ✅ How to handle exceptions in tests
- ✅ Why functions should return values to be testable
- ✅ How to organize and run many tests efficiently

You’re now equipped to test your code with confidence — like a true developer. 🧪🧑‍💻"
