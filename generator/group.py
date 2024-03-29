from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    # n- задает количество генерируемых данных, f-файл в который записываются n
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])

except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
# L_6_10

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group("", "", "")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]

file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
