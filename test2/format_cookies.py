# import random
import re
from urllib import parse
# i = random.randint(0,10)
def format_cookies(i):
    cookies = {}
    with open("cookie.txt","r") as f:
        for line in f.readlines()[i:i+1]:
            cookies = eval(line)
    f.close()
    return cookies

def get_cookieUser(i):
    new_cookie = format_cookies(i)
    my_bd_name = new_cookie["pin"]
    my_bd_nick = new_cookie["unick"]
    if  re.search(u"%",my_bd_nick):
        my_bd_nick = parse.unquote(my_bd_nick)
    # my_bd_name_last4 = "****" + my_bd_name[-4:]
    return (my_bd_name,my_bd_nick)

# print(get_cookieUser(i))


# print(format_cookies(i))