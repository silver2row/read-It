# setup.py

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="read_Everything",
    version="0.0.2",
    description="Read!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/silver2row/read-It",
    author="Real Python / Joe Tatusko / Seth",
    author_email="seth@lafayette-parish.com",
    license="MIT b/c of realpython.com?",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["read_Everything"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "silver2row=reader.__main__:main",
        ]
    },
)
