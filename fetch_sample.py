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

    tmp = []
    cnt = 0
    
    for i in elements_list:

        if cnt == 6:
            break

        if not "<var" in str(i).split(">"): 
            tmp.append(i)
            cnt += 1

    #Delete duplicated elements
    if tmp[0] == tmp[-2] and tmp[1] == tmp[-1]:
        tmp = tmp[0:-2] 


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