
with requests.session() as s:
    re1 = s.post(
        "http://xawn.f3322.net:8060/woniusales/user/login", body)

    #print(re1.text)

    re2 = s.post("http://xawn.f3322.net:8060/woniusales/sale/barcode",{"barcode":11111111})
    print(re2.text)

返回值转换成json格式
re1_value = json.loads(re2.text)
print(re1_value)
