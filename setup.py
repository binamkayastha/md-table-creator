import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="md_table_creator",
    version="0.2",
    scripts=["md_table_creator"],
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
)
