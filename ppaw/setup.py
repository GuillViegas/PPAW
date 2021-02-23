from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="ppaw",
    author="Guilherme Viegas",
    author_email="guivfaria@gmail.com",
    python_requires=">=3.8",
    install_requires=required,
    packages=find_packages(),
    version="0.1.0",
    description="Python Poloniex API Wrapper",
    license="MIT",
)