from setuptools import find_packages,setup

from typing import List


def get_requirements(file_path:str)-> List[str]:

    '''
    This will return list of requirements
    '''
    requirements =[]

    with open(file_path) as obj:
        requirements= obj.readlines()
        requirements=[req.replace('\n', " ") for req in requirements]

        if '-e.' in requirements:
            requirements.remove('-e.')

setup(
    name='Ml project',
    version =0.01,
    author='Mohan',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    )