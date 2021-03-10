import sys

import requests
from bs4 import BeautifulSoup


def get_samples(url):

    try:
        r = requests.get(url, timeout=3)

    except Exception:
        print("Connection error!")
        sys.exit()
    
    #Create a list of elements tagged by "<pre>"
    soup = BeautifulSoup(r.text, "html.parser")
    elements_list = soup.find_all("pre")

    #Delete duplicated and variable elements
    tmp = []
    
    for i in elements_list:

        if not "<var" in str(i).split(">") and not i in tmp:
            tmp.append(i)


    elements_list = tmp
    input_list = []
    output_list = []
    length = len(elements_list) // 2

    for i in range(0, length + 2, 2):

        try:
            input_list.append(elements_list[i].contents[0])
            output_list.append(elements_list[i+1].contents[0])

        except Exception:
            print("Invalid URL")
            sys.exit()

    return input_list, output_list
