# Publishing nlm_prep_tool to GitHub

This guide will walk you through publishing your tool to GitHub step by step.

## Prerequisites

- Git installed on your computer
- A GitHub account (free at https://github.com)

---

## Step 1: Initialize Git Repository

Open PowerShell or Command Prompt and run:

```bash
cd G:\Projects\nlm_prep_tool
git init
```

---

## Step 2: Configure Git (if not already done)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 3: Add All Files to Git

```bash
git add .
```

---

## Step 4: Create Initial Commit

```bash
git commit -m "Initial commit: nlm_prep_tool v1.0.0

- Combine multiple files (MD, TXT, DOCX, PDF, SVG) into one
- Generate table of contents with clickable links
- Preserve DOCX formatting
- Extract PDF text page by page
- Extract SVG text elements
- CLI with verbose output and skip options"
```

---

## Step 5: Create GitHub Repository

### Option A: Using GitHub Website

1. Go to https://github.com/new
2. Repository name: `nlm_prep_tool`
3. Description: `A CLI tool to combine multiple files (MD, TXT, DOCX, PDF, SVG) into a single document for Google's NotebookLM`
4. Choose: **Public** (or Private if you prefer)
5. **DO NOT** initialize with README (you already have one)
6. Click **Create repository**

### Option B: Using GitHub CLI (if installed)

```bash
gh repo create nlm_prep_tool --public --source=. --remote=origin --push
```

---

## Step 6: Connect Local Repo to GitHub

After creating the repository on GitHub, run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/nlm_prep_tool.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 7: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

## Step 8: Add Repository Description & Topics

1. Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/nlm_prep_tool`
2. Click the **gear icon** ⚙️ next to "About"
3. Add description:
   ```
   A CLI tool to combine multiple files (MD, TXT, DOCX, PDF, SVG) into a single document for Google's NotebookLM
   ```
4. Add topics (click "Add topics"):
   - notebooklm
   - google-notebooklm
   - markdown
   - pdf
   - docx
   - svg
   - cli-tool
   - python
   - study-notes
   - document-converter
5. Click **Save changes**

---

## Step 9: Create a Release (Optional but Recommended)

1. On GitHub, click **Releases** on the right side
2. Click **Create a new release**
3. Tag version: `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. Description:
   ```markdown
   ## What's New
   
   - Combine multiple file types (MD, TXT, DOCX, PDF, SVG) into one
   - Table of contents with clickable links
   - Preserve DOCX formatting (headings, bold, italic, tables)
   - Extract PDF text page by page
   - Extract SVG text elements
   - CLI with verbose output and skip options
   
   ## Installation
   
   ```bash
   pip install -r requirements.txt
   python nlm_prep.py "path/to/notes" -o combined.md
   ```
   ```
6. Click **Publish release**

---

## Step 10: Share Your Tool!

Now you can share your repository URL:
```
https://github.com/YOUR_USERNAME/nlm_prep_tool
```

Consider sharing on:
- Twitter/X
- Reddit (r/NoteTaking, r/Python)
- NotebookLM community forums
- Your personal blog

---

## Quick Reference Commands

```bash
# Full setup in one go
cd G:\Projects\nlm_prep_tool
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/nlm_prep_tool.git
git branch -M main
git push -u origin main
```

---

## Troubleshooting

### "git is not recognized"
Install Git from: https://git-scm.com/download/win

### "Permission denied"
Make sure you're logged into GitHub and have the correct repository URL

### "fatal: remote origin already exists"
Run: `git remote remove origin` then add it again

### "failed to push some refs"
Run: `git pull origin main --rebase` then push again

---

## Next Steps After Publishing

1. **Enable GitHub Discussions** (Settings > Features > Discussions)
2. **Add a screenshot** to README showing the tool in action
3. **Create a simple website** with GitHub Pages
4. **Submit to PyPI** so people can `pip install nlm-prep-tool`

Good luck! 🚀
