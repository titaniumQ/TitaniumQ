from setuptools import setup
import os

# README file ko read karne ke liye
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "TitaniumQ programming language launcher by Anshik Pathak"

setup(
    name="titaniumq",
    version="1.0.2", # Version update kiya gaya hai
    author="Anshik Pathak",
    author_email="anshikpathakwork@gmail.com",
    description="TitaniumQ programming language launcher ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/titaniumq/",
    py_modules=["titanium_launcher"],
    entry_points={
        "console_scripts": [
            "tq=titanium_launcher:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
