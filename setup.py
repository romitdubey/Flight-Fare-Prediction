from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("/n","") for req in requirements]
    return requirements

setup(
    name="Flight Price Prediction",
    version="0.0.1",
    author="Romit Dubey",
    install_requires = get_requirement('requirements.txt'),
    packages=find_packages()
)
