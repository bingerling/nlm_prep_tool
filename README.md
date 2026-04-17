# nlm_prep.py - NotebookLM Upload Prep Tool

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI tool that combines multiple files (Markdown, TXT, DOCX, PDF, SVG) from a directory into a single consolidated document ready for upload to Google's NotebookLM.

## Why This Tool?

Google's NotebookLM only allows single file uploads. If you have study notes spread across many folders with different file types, this tool solves that problem by:

- **Combining everything into ONE file** - Upload a single source to NotebookLM
- **Preserving structure** - Table of contents with clickable links to each section
- **Supporting multiple formats** - Markdown, TXT, DOCX, PDF, and SVG files
- **Preserving DOCX formatting** - Converts headings, bold, italic, lists, and tables to Markdown
- **Extracting PDF text** - Pulls text content from PDF documents page by page
- **Extracting SVG text** - Extracts embedded text from SVG diagrams and illustrations

## Installation

### 1. Download the Script

Save `nlm_prep.py` to your computer.

### 2. Install Dependencies (Optional but Recommended)

For DOCX support, install python-docx:

```bash
pip install python-docx
```

For PDF support, install PyMuPDF:

```bash
pip install pymupdf
```

Without these, DOCX and PDF files will be skipped with a warning.

## Usage

### Basic Usage

```bash
python nlm_prep.py "path\to\your\notes" -o combined.md
```

### Examples

```bash
# Combine all notes in current directory
python nlm_prep.py . -o my_notes.md

# Combine notes from specific folder
python nlm_prep.py "G:\My Study Notes" -o notebook_ready.md

# Show detailed progress while processing
python nlm_prep.py "G:\My Study Notes" -o output.md --verbose

# Skip DOCX files (if you don't have python-docx installed)
python nlm_prep.py "G:\My Study Notes" -o output.md --skip-docx

# Skip PDF files (if you don't have PyMuPDF installed)
python nlm_prep.py "G:\My Study Notes" -o output.md --skip-pdf

# Skip SVG files
python nlm_prep.py "G:\My Study Notes" -o output.md --skip-svg
```

## How It Works

1. **Scans recursively** - Finds all `.md`, `.txt`, `.docx`, `.pdf`, and `.svg` files in the directory
2. **Sorts files** - Orders them alphabetically for consistent, logical flow
3. **Generates Table of Contents** - Creates clickable links to each section
4. **Combines content** - Merges all files with clear section headers
5. **Preserves formatting** - DOCX files are converted to Markdown with formatting intact

## Output Structure

The generated file looks like this:

```markdown
# NotebookLM Combined Notes

*Generated on: 2026-04-17 19:01:25*
*Source: G:\My Study Notes*

## Table of Contents

### Folder Name
- [File Name](#link-to-section)
- [Another File](#link-to-section)

---

## Folder Name\File Name.md

[Content of the file...]

---

## Folder Name\Another File.md

[Content of the file...]
```

## Features

### Supported File Types
- **Markdown (.md)** - Kept as-is
- **Text (.txt)** - Kept as-is
- **Word (.docx)** - Converted to Markdown with formatting preserved
- **PDF (.pdf)** - Text extracted page by page
- **SVG (.svg)** - Text extracted from `<text>`, `<title>`, and `<desc>` elements

### DOCX Formatting Preserved
- Headings (H1-H6) → Markdown headers
- **Bold** → `**bold**`
- *Italic* → `*italic*`
- ***Bold+Italic*** → `***bold+italic***`
- Bullet lists → `- item`
- Numbered lists → `1. item`
- Tables → Markdown tables

### Smart Organization
- Files grouped by parent folder
- Alphabetical sorting within folders
- Clear section separators (`---`)
- Clickable table of contents

## NotebookLM Limits

NotebookLM has the following limits (as of 2024):
- **50 sources per notebook**
- **~500,000 tokens per source** (roughly 375,000 words)

This tool creates ONE combined file, which counts as a single source. If your combined file exceeds the token limit, you may need to split it into multiple files.

## Tips

1. **Use descriptive folder names** - They become section headers in the TOC
2. **Clean up first** - Remove any files you don't want included
3. **Check the word count** - The tool reports total words after processing
4. **Upload to NotebookLM** - Simply drag and drop the output file as a new source

## Troubleshooting

### "python-docx not installed"
Install it with: `pip install python-docx`

### "PyMuPDF not installed"
Install it with: `pip install pymupdf`

### SVG files not extracting text
SVG text extraction only works on SVGs that have embedded `<text>`, `<title>`, or `<desc>` elements. Purely visual SVGs without text content will show "[No extractable text content found in this SVG]".

### File encoding errors
The tool tries UTF-8 first, then falls back to latin-1. Most files should work fine.

### Very large files
If your combined file is too large for NotebookLM, you may need to:
- Process subdirectories separately
- Remove unnecessary files
- Split into multiple output files manually

## License

Free to use for personal and commercial projects.

## Author

Created to solve the NotebookLM single-file upload limitation.
</content>