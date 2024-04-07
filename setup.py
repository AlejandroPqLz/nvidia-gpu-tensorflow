"""
setup.py

Funcionality: This file is used to create a package that can be installed using pip. 
It is used to install the package in the local environment.

"""

import setuptools

requirements = [
    "numpy",
    "pandas",
    "matplotlib",
    "tqdm",
    "tensorflow == 2.16.1",
    "keras == 3.1",
    "mlflow",
    "pexpect",
    "ipykernel",
    "numba",
    "gradio",
]  # Add or remove the required packages for the package to work properly

setuptools.setup(
    name="project_name",
    version="0.0.1",
    author="Name LastName",
    author_email="email@email.com",
    description="A package to develop projects using NVIDIA GPUs",
    long_description_content_type="text/markdown",
    url="https://url/to/your/project",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10,<=3.12",
)
