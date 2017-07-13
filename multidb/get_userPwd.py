#coding:utf-8

def get_user():
    with open("cookies/username.txt","r") as f:
        userPass = {}
        while True:
            line = f.readline()
            if len(line) < 1:
                break
            arr = line.split("----")
            if len(line) < 2:
                break
            if arr[0] not in userPass:
                userPass[arr[0]] = {}
            userPass[arr[0]] = arr[1]
        f.close()
    return userPass #返回一个字典类型，用户的用户名和密码存在字典中
# if __name__ == '__main__':
#     print(get_user())