# OpenO1 Private module 
import requests

"""
BOT <=> GITHU DL LINKS (api)
"""


release_version = 0.2
then = None

"""
ERROR CODES :

0 : False
1 : True
2 : Product(s) still not available 

"""

def get(type, object:str):
    global release_version
    type_exist(type)  
    if then == False:
        print(f"Type {type} doesn't match with any of written types. (Code 0)")
    if type == "web":    
        return f'https://github.com/OpenO1/frameworks/releases/download/{release_version}/{object}.css'
    elif type == "python":

        p_url = f'https://github.com/OpenO1/frameworks/releases/download/{release_version}/{object}.py'
        res = requests.get(p_url, timeout=5)

        if res.status_code == 200:
            return f'https://github.com/OpenO1/frameworks/releases/download/{release_version}/{object}.py'
        else:
            return False

def type_exist(type):
    global then
    if isinstance(type, str) == False:
        then = False

def goto_source(type):
    p_url = f'https://github.com/OpenO1/frameworks/tree/main/{type}'
    res = requests.get(p_url, timeout=5)

    if res.status_code == 200:
        return f'https://github.com/OpenO1/frameworks/tree/main/{type}'
    else:
        return False

def list():
    listing = "**__Available frameworks:__**\n __Section: Web__\n - post\n __Section: Python__\n - openo1-linker"
    return listing

''' USAGE EXAMPLE
get('web','post')
'''
