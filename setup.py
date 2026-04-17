from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="nlm-prep-tool",
    version="1.0.0",
    author="nlm_prep_tool contributors",
    description="A CLI tool to combine multiple files into a single document for Google's NotebookLM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bingerling/nlm_prep_tool",
    py_modules=["nlm_prep"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Processing :: General",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "nlm-prep=nlm_prep:main",
        ],
    },
)
