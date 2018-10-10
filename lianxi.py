# def text_create(name,msg):
#     desktop_path = 'X:/pytest/'
#     full_path = desktop_path + name +'.txt'
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('Done')
# text_create('hello','hello word')
# def text_filter(word, censored_word='lame', changed_word='Awesome'):
#     return word.replace(censored_word, changed_word)
# text_filter('Python is lame!')
# def censored_text_create(name, msg):
#     clean_msg = text_filter(msg)
#     text_create(name,clean_msg)
# censored_text_create('Try','lame!lame!lame!')
# def account_login():
#     password = input('password:')
#     if password == '12345':
#         print('login success')
#     else:
#         print('wrong password word or inbalid inpout!')
#         account_login()
# account_login()


# def duimima():
#     password = input("password:")
#     passwordtrue = password == '123123'
#     if passwordtrue:
#         print('you are right')
#     else:
#         print('try again pleass')
#         duimima() #成立并退出
# duimima()




# def testpassword():
#     pssword = input("password:")
#     turepassword = pssword == '123456'
#     if turepassword:
#         print('youare right')
#     else:
#         print('try again')
#     testpassword()  #无限循环
# testpassword()



# 密码设置
# password_list = ['*#*#','12345']
# def account_login():
#     password = input('password:')
#     password_cusi = password == password_list[-1]
#     password_congzi = password == password_list[0]
#     if password_cusi:
#         print('you are right')
#     elif password_congzi:
#         new_password = input("please try new password")
#         password_list.append(new_password)
#         print('your new password is successfully!')
#         account_login()
#     else:
#         print('you password is wrong')
#         account_login()
# account_login()









# for every_letter in 'Hello world':
#     print(every_letter)






# for num in range(1,10):
#     print(str(num)+'+1=',num+1)



# songlist = ['9527','spead of you','jongjiajia']
# for song in songlist:
#     if song == '9527':
#         print('深7')
#     elif song == 'spead of you':
#         print('jfla')
#     else:
#         print('???')
#



# for i in range(1,10):
#     for j in range(1,10):
#         print('{}x{}={}'.format(i,j,i*j))

# while 1<3:
#     print('i love yuo')



# file = open('X://pytest//wangan.txt',encoding='gbk',errors='ignore')
# file.readline()
# file.close()
# file = open('X://pytest//wangan.txt','r',encoding='utf8',errors='ignore')
# while 1:
#     line = file.readline()
#     if '富强' in line:
#         print(line)

file= open('X://pytest//wangan.txt','r',encoding='utf8',errors='ignore')
for line in file:
    xinming = line.split(',')[0]
    youxiao = line.split(',')[9]
    xinxi = xinming + ',' + youxiao
    print(xinxi)






