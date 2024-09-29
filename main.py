#!/usr/bin/env python3

import requests as req
import json


def banner(): 
    print(

        """

                                                                                            
        
                                                                                            
           88                                                                               
           88                                                                               
           88                                                                               
,adPPYba,  88,dPPYba,    ,adPPYba,   8b      db      d8     88,dPYba,,adPYba,    ,adPPYba,  
I8[    ""  88P'    "8a  a8"     "8a  `8b    d88b    d8'     88P'   "88"    "8a  a8P_____88  
 `"Y8ba,   88       88  8b       d8   `8b  d8'`8b  d8'      88      88      88  8PP"""""""  
aa    ]8I  88       88  "8a,   ,a8"    `8bd8'  `8bd8'       88      88      88  "8b,   ,aa  
`"YbbdP"'  88       88   `"YbbdP"'       YP      YP         88      88      88   `"Ybbd8"'  
                                                                                            
                                                                                            
                                                                                      
A script created by Timothy Maraj to show CVEs realted to an IP or URL. 


OPTIONS: 

default: look up using an URL
    -i : look up an IP address

        
         
 """

    )


def userInput(): 
    return input("Enter in a URL or IP w/o flags: ")

def validate_url():
    """
    - using url provided by user
    - make a request to that url 
    - if 200 likely ok and procded with 
    
    """


def 