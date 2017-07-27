def format_cookies():
    f = open(r'cookies/cookie.txt','r')
    print(f)
    cookies = {}
    for line in f.read().split(';'):   #按照字符：进行划分读取
        #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value  #为字典cookies添加内容
    return cookies
print(format_cookies())
print(type(format_cookies()))