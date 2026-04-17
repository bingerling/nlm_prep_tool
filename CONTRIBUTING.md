# Contributing to nlm_prep_tool

Thank you for your interest in contributing to nlm_prep_tool! This document provides guidelines for contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check if the issue already exists. When creating a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (file paths, commands used)
- **Describe the behavior you observed and what behavior you expected**
- **Include your environment details** (OS, Python version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the enhancement**
- **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests if available
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/nlm_prep_tool.git
cd nlm_prep_tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and modular

## Testing

Before submitting a pull request:

- Test with various file types (.md, .txt, .docx, .pdf, .svg)
- Test with nested directories
- Verify the output markdown is valid
- Check that the tool handles errors gracefully

## Questions?

Feel free to open an issue for any questions or discussions.
