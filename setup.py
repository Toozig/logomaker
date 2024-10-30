from setuptools import setup, find_packages

setup(
    name="logomaker",
    version="0.8.4",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "matplotlib>=2.2.2",
        "pandas"
    ],
) 