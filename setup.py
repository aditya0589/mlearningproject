from setuptools import find_packages, setup
from typing import List
temp = "-e ."
def get_requirements(filename: str) -> List[str]:
    requirements = []
    with open(filename, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if temp in requirements:
            requirements.remove(temp)

        return requirements
    
setup(
    name='mlproject',
    version='0.1',
    author='Yrakaraju Aditya',
    author_email='yraditya895@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)