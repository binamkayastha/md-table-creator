import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="md_table_creator",
    version="v0.0.1",
    data_files=[("bin", ["runnable/md_table_creator"])],
    author="Binam Kayastha",
    author_email="binamkayastha@gmail.com",
    description="A python script that converts mysql create tables to markdown tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/binamkayastha/md-table-creator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
