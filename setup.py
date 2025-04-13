from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    # removing hyphen-e dot
    # if -e . is present in the requirements
    # then we will remove it
    # from the requirements list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name="mlproject",
    version="0.0.1",
    author="Aakash",
    author_mail = "aakashsurya28@gmail.com",
    packages = find_packages(),
    ###install_requires = ['pandas','numpy','matplotlib','seaborn','scikit-learn']###
    install_requires = get_requirements('requirements.txt')
)