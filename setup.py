from setuptools import setup, find_packages

setup(
    name="mymodule",
    version="0.1.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["mymodule=mymodule.cli:main"]},
    description="Modulo genérico",
    author="Gradiant",
    author_email="dreiriz@gradiant.com",
    keywords=[],
)
