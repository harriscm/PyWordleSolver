from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="PyWordleSolver",
    version="0.0.1",
    description="Silly utility to solve Wordle words",
    author="Chad Harris",
    author_email="charris1@gmail.com",
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts':['pywordle=PyWordleSolver.solver:solve']
    }
)