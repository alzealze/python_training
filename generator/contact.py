from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    # n- задает количество генерируемых данных, f-файл в который записываются n
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# L_6_10
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", mobile="", nickname="")] + [
    Contact(firstname=random_string("firstname", 15), lastname=random_string("lastname", 15),
            address=random_string("address", 15), mobile=random_string("mobile", 10),
            nickname=random_string("nickname", 20), homephone=random_string("homephone", 10),
            workphone=random_string("workphone", 10),
            secondaryphone=random_string("secondaryphone", 10),
            email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(n)
]

file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
