from setuptools import setup, find_packages

setup(
    name="clib",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "clib = clib.main:main"
        ]
    }
)

