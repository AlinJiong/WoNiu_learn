import requests
import json

# response = requests.get("http://xawn.f3322.net:8060/woniusales/")
# print(response,type(response))
# print(response.status_code) #状态码
# print(response.text) #字符串
# print(response.content) #二进制
# print(response.content.decode("utf-8")) #二进制转换成字符
# with open("str1.html",'w',encoding='utf-8') as f:
#     f.write(response.text)


# query_string = {"ie":"utf-8", 'word':'requests'} #有参数的情况
# resp = requests.get("https://www.baidu.com",params=query_string)
# print(resp.text)


# post请求发送,可以将参数带入链接发送
body = {'username': 'admin', 'password': 'Milor123', 'verifycode': '0000'}
headers = {'ContentType': 'application/x-www-form-urlencoded'}

# headers默认为x-www-form-urlencoded形式，可以不加
# response = requests.post(
# #     "http://xawn.f3322.net:8060/woniusales/user/login", body, headers=headers)
# response = requests.post(
#     "http://xawn.f3322.net:8060/woniusales/user/login", body)

# 获取cookie的两种方式
# print(response.status_code)
# print(response.text)
# cookies = response.cookies
# print(cookies.get_dict())


# cookies = response.headers['Set-Cookie']
# print(cookies)
# headers = {'Cookie':cookies}
# response = requests.post(
#     "http://xawn.f3322.net:8060/woniusales/sale", headers=headers)


# 使用session,使用tcp长链接保持登录
# session = requests.session()
# response = session.post(
#     "http://xawn.f3322.net:8060/woniusales/user/login", body)

# re2 = session.post(
#     "http://xawn.f3322.net:8060/woniusales/sale")
# print(re2.text)

# session.close()   #关闭tcp链接


# with requests.session() as s:
#     re1 = s.post(
#         "http://xawn.f3322.net:8060/woniusales/user/login", body)

#     #print(re1.text)

#     re2 = s.post("http://xawn.f3322.net:8060/woniusales/sell/barcode",{"barcode":11111111})
#     print(re2.text)

# # print(type(re2))
# # print(re2)
# #返回值转换成json格式
# re2_value = json.loads(re2.text)
# print(re2_value)


# with requests.session() as s:
#     res = s.post(
#         "http://xawn.f3322.net:8060/woniusales/user/login", body)
#     获取请求URL，文件头
#     print(res.request.url)
#     print(res.request.headers)
#     print(res.request.body)


# 上传文件的方法：
# with requests.session() as s:
#     res = s.post(
#         "http://xawn.f3322.net:8060/woniusales/user/login", body)
#     body = {"batchname": "GB20210426"}
#     upload_file = {"batchfile": ('abc.txt', open(
#         'report.html', 'r', encoding="utf-8"))}

#     re1 = s.post("http://xawn.f3322.net:8060/woniusales/goods/upload",
#                  body, files=upload_file)
#     print(re1.text)
#     print(re1.status_code)
#     print(re1.request.url)

# #上传文件的方法2
# with requests.session() as s:
#     res = s.post(
#         "http://xawn.f3322.net:8060/woniusales/user/login", body)
#     upload_file = {"batchname": (None,"GB20210426"),"batchfile": ('abc.txt', open(
#         'report.html', 'r', encoding="utf-8"))}

#     re1 = s.post("http://xawn.f3322.net:8060/woniusales/goods/upload",
#                 files=upload_file)
#     print(re1.text)
#     print(re1.status_code)
#     print(re1.request.url)

# requests.urllib3.disable_warnings()
# with requests.session() as s:
#     # https去除校验,避免SSLError错误产生
#     s.verify = False
#     res = s.post(
#         "https://xawn.f3322.net:18443/woniusales/user/login", body)
#     print(res.status_code)
#     print(res.text)

#     re2 = s.post(
#         "https://xawn.f3322.net:18443/woniusales/sell/barcode", {"barcode": 11111111})
#     print(re2.text)


# 重定向
with requests.session() as s:
    # https去除校验,避免SSLError错误产生
    s.verify = False
    res = s.post(
        "https://www.baidu.com", allow_redirects=False)
    print(res.status_code)
    print(res.history)
