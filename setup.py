import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nasspython",
    version="1.0.0",
    description="Wrapper for the NASS Quickstats database",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jackheinemann/nass_python",
    author="Jack Heinemann",
    author_email="jack@oenoke.com",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["requests"],
)
