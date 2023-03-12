from setuptools import find_packages,setup
from typing import List

HEPEN_E_DOT = '-e .'

def get_req(file_path:str)-> List[str]: 
    '''
    this function will return the list of requirements
    '''
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[ r.replace('\n','') for r in req]
    
    if HEPEN_E_DOT in req:
        req.remove(HEPEN_E_DOT)

    return req

result=[]
result=get_req('requirements.txt')
print(result)