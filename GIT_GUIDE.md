# 🧠 Beginner-Friendly Git + VS Code Cheat Sheet

Welcome to your personal Git guide for VS Code! Whether you're working solo or collaborating, this will help you understand what's going on with version control — and avoid panic when things get weird. Let's dive in 🚀

---

## 🛠 Git Basics

| Term      | Meaning                                                                 |
|-----------|-------------------------------------------------------------------------|
| `git`     | A tool that tracks file changes over time.                             |
| Repo      | A folder Git is tracking. A project.                                   |
| Commit    | A saved snapshot of your code.                                         |
| Stage     | Choosing which changes to include in a commit.                         |
| Push      | Upload your commits to GitHub (or other remote).                       |
| Pull      | Download changes from GitHub to your computer.                         |

---

## ✅ The Git Workflow (2-Step Process)

1. **Stage** the files you want to save
2. **Commit** those staged changes with a message

### ⛓ Why 2 Steps?
So you can:
- Choose what to commit (even if multiple files changed)
- Review before saving

---

## 🧑‍💻 VS Code: What the Icons Mean

| Symbol | Meaning                    | Action Needed?                 |
|--------|-----------------------------|--------------------------------|
| `M`    | Modified (file was edited) | Stage it when ready            |
| `A`    | Added (new file)           | Stage it when ready            |
| `U`    | Untracked (Git doesn't know this file) | Stage it if you want it in Git |

---

## 🔼 How to Push to GitHub (Step-by-Step)

1. **Open Source Control Tab** on the sidebar
2. **Stage your changes**:
   - Click the `+` next to the files in "Changes"
   - Or click `+` at the top to stage everything
3. **Write a commit message** at the top (e.g., `Fix bug in fuel.py`)
4. Click `✅ Commit`
5. Open the Terminal and type:
   ```bash
   git push
   ```
   ✅ You just pushed your changes to GitHub!

---

## 🔄 If You Want to Undo

| Situation                       | What to Do                                              |
|--------------------------------|----------------------------------------------------------|
| File changed but not saved     | Use `Undo` or `Cmd + Z`                                  |
| File saved but not committed   | Right-click file in Source Control > `Discard Changes`   |
| Committed but not pushed       | Use `git reset HEAD~1` (advanced, ask for help first)     |

---

## 🚨 Common Popups Explained

### ⚠ "There are no staged changes to commit"
- Git sees your edits, but you haven’t selected them yet.
- Click `Yes` to stage and commit them together.

### "Would you like to stage all your changes?"
- This is just a helpful shortcut. Say `Yes` if you’re ready to save all changes.

---

## 🧼 Pro Tips

- Use `.gitignore` to exclude files like `.DS_Store`, `.env`, and `__pycache__`
- Use branches when experimenting or working on features
- You can always type `git status` in terminal to see what’s going on

---

## 🔁 Useful Terminal Commands

```bash
git status         # See what’s changed

git add filename   # Stage a specific file
git add .          # Stage everything

git commit -m "Your message"  # Save your changes

git push           # Upload to GitHub
git pull           # Download from GitHub
```

---

## 🙋 Need Help?
Run into an issue? Take a screenshot of your VS Code like you’ve been doing, or copy-paste your terminal error, and I’ve got your back.

Happy coding! 🚀

