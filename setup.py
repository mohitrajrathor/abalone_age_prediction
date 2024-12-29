# 
# setup.py
#   - project setup file.
# 

# imports 
from setuptools import find_packages, setup
from typing import List

# const
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    get list of the requirements
    '''
    requirements = []
    with open(file_path) as fh:
        requirements = fh.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


setup(
    name="Abalone Age Prediction Project",
    version='1.0.0',
    author='mohitrajrathor',
    author_email='mohitrajrathor@yahoo.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
