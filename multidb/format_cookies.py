import random
# i = random.randint(0,8)
def format_cookies(i):
    with open("cookies/cookie.txt","r") as f:
        for line in f.readlines()[i:i+1]:
            cookies = eval(line)
    f.close()
    return cookies

def get_cookieUser(i):
    new_cookie = format_cookies(i)
    my_bd_name = new_cookie["pin"]
    my_bd_name_last4 = "****" + my_bd_name[-4:]
    return my_bd_name_last4
# print(get_cookieUser(i))


# print(format_cookies())