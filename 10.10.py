#ep1

# for i in range(1,1000):
#     urla = 'http://www.baidu.com/?page='
#     urlab = '/wd=xiaopangzi'
#     res = urla +str(i) +urlab
#     print(res)

# a2 = [1,1,1,2,2,2,2,3]
# a3 =[]
# for i in a2:
#     if i not in a3:
#         a3.append(i)
# print(a3)
#
# a3.sort(key=lambda x:x[1])


# a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
# a4.sort(key=lambda x:x[2][1])
# print(a4)



10.11#ep1
# def cenjihafen():
# #     cj = input("please suru cenji")
# #     cj = []
# #     for i in range(cj):
# #         if cj >= cj-10:
# #             print('you cj is {} you is A'.format(cj))
# #         if cj >= cj-20:
# #              print('you cj is {} you is B'.format(cj))
# #     cenjihafen()
# # cenjihafen()



#ep1
# s=str('123-45-6789')
# a = input("请按照ddd-dd-dddd的格式输入")
# if s == a:
#     print('valid SSN')
# else:
#     print('invalid SSN')


#ep2
# a = input('onestr')
# b = input('twostr')
# if a == b.find(a):
#     print('si zi cuan')
# else:
#     print('no')

#ep3
# for i in range(10):
#     passwd = input('请输入你的密码')
#     num = 0 #初始化需要放在循环里，每次输入密码都需要重新初始化
#     lower = 0
#     upper =0
#     if len(passwd)>9 : #判断密码长度大于8位
#         for pwd in passwd:  #循环字符串中的字符
#             if pwd.isdigit(): #字符是否是数字
#                 num += 1
#             elif pwd.islower(): #字符是否是小写字母
#                 lower += 1
#             elif pwd.isupper(): #字符是否是大写字母
#                 upper += 1
#         if num and lower and upper: #若数字、大写及小写均为真，则满足密码包含大小写字母和数字
#             print('密码输入成功')
#         else:
#             print('密码必须包含大小写字母及数字')
#     else:
#         print('密码长度必须在大于8位')



#ep4
# def dsdsdsdsd():
#     s=input('please suru')
#     gesu={}
#     for i in s:
#         gesu[i]=s.count(i)
#     print(gesu)
# dsdsdsdsd()

