#This module we used to create setup.py file!! so that module can import from file
#to another futhur we can used this module as python package
import os,sys
from setuptools import setup,find_packages
from typing import List

def GetRequirement(filepath:str) ->List[str]:
    require = []
    with open(filepath,'r') as f:
        rows = f.readlines()
        #iterating row module one by another
        for row in rows:
            if row in "-e .":
                continue
            else:
                require.append(row)
    return require



#creating an object of setup class
setup(
    name = "WineQualityModel",
    version="0.0.2",
    long_description=open("README.md").read(),
    author="Raees Azam Shaikh",
    author_email="shaikhraishazam@gmail.com",
    url="https://github.com/raish123/WineQualityModel",
    #creating an object of find packages class
    packages=find_packages(),
    #installing the package
    install_requires= GetRequirement("requirements.txt")
)