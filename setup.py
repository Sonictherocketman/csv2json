import setuptools


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "csv2json.py",
    version = "1.0",
    author = "Brian Schrader",
    author_email = "brian@brianschrader.com",
    description = "A utility to convert CSVs to JSON",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Sonictherocketman/csv2json",
    project_urls = {
        "Bug Tracker": "https://github.com/Sonictherocketman/csv2json/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(),
    python_requires = ">=3.7",
    scripts=(
        'bin/csv2json',
    )
)
