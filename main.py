import os
import subprocess as sp
import sys

from fetch_sample import *
from util import *


def main():

    url=str(input("URL:"))
    same_url = is_same_url(url)

    if same_url:
        input_list, output_list = load_samples()
        output_list = list(map(lambda x: x.replace("\r\n", ""), output_list))

    else:
        remove_stored_samples()
        update_url(url)
        input_list, output_list = get_samples(url)
        output_list = list(map(lambda x: x.replace("\r\n", ""), output_list))

    length = len(input_list)

    #Load the binary that solve a problem
    binary_path = str(input("Binary path:"))

    try:
        with open(binary_path, "rb") as f:
            code = f.read()

    except FileNotFoundError:
        print("Not found the binary!")
        sys.exit()

    #Move to the work directoly
    move_current_directory()
    
    with open("tmp.out", "wb") as f:
        f.write(code)

    for i in range(0,length):

        with open("input" + str(i + 1), "w") as f:
            f.write(input_list[i]) 

        with open("output" + str(i + 1), "w") as f:
            f.write(output_list[i]) 

    #Execute code
    for i in range(length):

        print("Sample {}:    ".format(i+1), end="")

        cmd = generate_command(i) 

        try:
            output = form_output(str(sp.check_output(cmd, shell=True)))

        except Exception:
            output = "Error"

        expected_output_list = []
        wrong_output_list = []

        if output == output_list[i]:
             emoji = "✔"
             print("{}".format(emoji))

        else:
            emoji = "✖"
            print("{}      Input: {}, Expected: {}, Output: {}".format(emoji, input_list[i].replace("\n", "") ,output_list[i], output))


if __name__ == "__main__":
    main()
