from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="data-insights",
    version="0.1.0",
    description="A simple data analysis tool for exploratory data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thelkotolsantosh/data_insights",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "data-insights=data_insights.cli:main",
        ],
    },
)
