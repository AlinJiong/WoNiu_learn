str1 = "西科大"
str2 = "计算机"
str3 = "软件工程"
str4 = "蒋林林"
str5 = "学习"
str6 = "在"
str7 = "专业"
str8 = "系"


res1 = str4+str6+str1+str2+str8+str3+str7+str5
print(res1)

print("%s%s%s%s%s%s%s%s" % (str4, str6, str1, str2, str8, str3, str7, str5))

print("".join((str4, str6, str1, str2, str8, str3, str7, str5)))

res2 = '{}{}{}{}{}{}{}{}'.format(
    str4, str6, str1, str2, str8, str3, str7, str5)
print(res2)

res3 = f'{str4}{str6}{str1}{str2}{str8}{str3}{str7}{str5}'
print(res3)



def func1(num):
    print(num)