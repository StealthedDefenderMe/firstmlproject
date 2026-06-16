from setuptools import find_packages, setup
# This maps entire application folders structure & makes packange for each folder
from typing import List

# HYPEN_E_DOT = '-e .' #Why we wrote this, we need to ignore this while installing libraries because this is not a package

def get_requirements(file_path:str)->List[str]:
    # This function returns the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "")for req in requirements]

        # if HYPEN_E_DOT in requirements:
        #     requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Karan',
    author_email='dograkaran826@gmail.com',
    packages=find_packages(),
    # install_requires=['numpy', 'pandas'] #basic libraries need to be installed to run project
    # Above you can also set all packages from requirements.txt, like below
    install_requires=get_requirements('requirements.txt')
)

# Whenever you run this file whichever folder has __init__.py file, package will be created for that folder.
# This will create build, dist,mlproect.egg-info
# You can also create this all without even calling the setup.py
# Just simply add the -e . in requirements.py and run this file by 'pip install -r requirements.txt'
# -e . automatically triggers the setup.py file