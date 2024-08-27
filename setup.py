from setuptools import setup
from setuptools import find_packages

long_description= """
# otp
Parse content made with the Obsidian plugin Onto Tracker
"""

required = []

setup(
    name="otp",
    version="0.0.1",
    description="Parse content made with the Obsidian plugin Onto Tracker",
    long_description=long_description,
    author="Jacob Hart",
    author_email="jacob.dchart@gmail.com",
    url="https://github.com/jdchart/onto-tracker-parse",
    install_requires=required,
    packages=find_packages()
)