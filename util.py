import glob
import os

#Gloal
OS_NAME = os.name

#Change directory delimiter by OS
#Windows
if OS_NAME == "nt":
    PATH = __file__.replace(r"\util.py", "") + "\work\\"  

#Posix
else:
    PATH = __file__.replace("/util.py", "") + "/work/"


def form_output(t):

    t = t.replace("\\n", "")
    t = t.replace("\\r", "")
    t = t.replace("'", "")
    return t[1::]


def generate_command(i):

    if OS_NAME == "nt":
        cmd = "type {} | tmp.out".format("input" + str(i+1))

    else:
        cmd = "cat {} | ./tmp.out".format("input" + str(i+1))

    return cmd


def is_same_url(url):

    if OS_NAME == "nt":
        URL_PATH = __file__.replace("util.py", "") + r"\work\url"

    else:
        URL_PATH = __file__.replace("util.py", "") + "/work/url"

    try:
        with open(URL_PATH, "r") as f:
            tmp_url = f.read().replace("\n", "")

    except Exception:
        return False

    if url == tmp_url:
        return True

    else:
        return False


def load_samples():

    input_list = []
    output_list = []
    cnt=1

    while True:

        input_filename = "input" + str(cnt)
        output_filename = "output" + str(cnt)

        try:
            with open(PATH + input_filename, "r") as f:
                input_list.append(f.readline())

            with open(PATH + output_filename, "r") as f:
                output_list.append(f.readline())
            
            cnt +=1

        except Exception:
            break

    return input_list, output_list


def move_current_directory():
        os.chdir(PATH)
    

def remove_stored_samples():

    file_list = glob.glob(PATH + "input*") + glob.glob(PATH + "output*")
    for f in file_list: 

        if os.path.isfile(f):
            os.remove(f)


def reset():

    remove_stored_samples()
    with open(PATH + "url", "w") as f:
        f.write("")

    if os.path.isfile(PATH + "tmp.out"):
        os.remove(PATH + "tmp.out")


def show_help():

    with open(PATH + "help", "r") as f:
        print(f.read())

def update_url(url):

    with open(PATH + "/url", "w") as f:
        f.write(url.replace(r"\n", ""))
