from setuptools import setup, find_packages

setup(
    name="PACKAGE NAME",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["PACKAGE NAME= PACKAGE NAME.cli:main"]},
    install_requires=[
        "Click==7.0",
        "SQLAlchemy==1.3.13",
        "psycopg2-binary==2.8.4",
        "requests==2.22.0",
        "pandas==1.0.1",
        "pytest==5.3.5",
        "pytest-cov==2.8.1",
        "pylint==2.4.4",
        "pytest-dotenv==0.4.0",
        "python-dotenv==0.11.0",
        "black==19.10b0"
    ],
    description="description",
    author="Gradiant",
    author_email="dreiriz@gradiant.com",
    keywords=["one", "two"],
)
