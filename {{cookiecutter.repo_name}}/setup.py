from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    packages=find_packages(),
    entry_points={"console_scripts": ["{{cookiecutter.cli_name}}= {{cookiecutter.package_name}}.cli:main"]},
    install_requires=[
        "Click==7.0",
        "SQLAlchemy==1.4.2",
        "pandas==1.0.1",
        "pytest==5.3.5",
        "pytest-cov==2.8.1",
        "pylint==2.4.4",
        "pytest-dotenv==0.4.0",
        "python-dotenv==0.11.0",
        "black==19.10b0"
    ],
    description="{{cookiecutter.project_short_description}}",
    author="Gradiant",
    author_email="dreiriz@gradiant.com",
    keywords=[{{cookiecutter.tags}}],
)
