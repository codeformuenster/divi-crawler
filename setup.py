from glob import glob
from setuptools import setup, find_packages

setup(
    name="divi-crawler",
    version="0.1.0",
    author="CodeForMuenster",
    url="https://github.com/codeformuenster/divi-crawler",
    license="MIT",
    # source
    packages=find_packages(),
    scripts=glob("scripts/*.py"),
    # dependencies
    install_requires=["bs4", "requests", "pymongo"],
    extras_require={
        "dev": ["black", "pylama", "rope"],
    },
)
