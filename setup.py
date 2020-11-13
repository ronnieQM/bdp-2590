import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acexml",
    version="0.0.1",
    author="Roni Quinonez",
    author_email="",
    description="package used to move xml data into RDBS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7.5",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7.5',
)