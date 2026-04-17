# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-18

### Added
- Initial release of nlm_prep_tool
- Support for Markdown (.md) files
- Support for Text (.txt) files
- Support for Word documents (.docx) with formatting preservation
- Support for PDF files with page-by-page text extraction
- Support for SVG files with text element extraction
- Table of Contents generation with clickable links
- File type reporting and word count statistics
- CLI flags: --skip-docx, --skip-pdf, --skip-svg, --verbose
- MIT License

### Features
- Recursive directory scanning
- Alphabetical file sorting
- Clear section separators in output
- Error handling for missing dependencies
- UTF-8 and latin-1 encoding support
