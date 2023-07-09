from setuptools import  find_packages,setup

from typing import List

HYPHEM_E_DOT = "-e ."

def get_requirments(file_path:str)->List[str]:
    """
    this function will return the list of requirment
    """
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n"," ") for req in requirments]

        if HYPHEM_E_DOT in requirments:
            requirments.remove(HYPHEM_E_DOT)
    
    return requirments


setup(
name ="mlproject",
version ="0.0.1",
author="Aditya",
author_email ="adityasunny147@gmail.com",
packages=find_packages(),
install_requires =get_requirments('requirments.txt')

)