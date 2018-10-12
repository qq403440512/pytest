# import crypt
# def tesrPass(cryptPass):
#     salt = cryptPass[0:2]
#     dictFile = open('X://pytest//test.txt')
#     for word in dictFile.readlines():
#         word = word.strip('\n')
#         cryptWord = crypt.crypt(word,salt)
#         if cryptWord == cryptPass:
#             print('[+] found password:'+word)
#         else:
#             print('[-] pssword {} not found'.format(word))
# def mian():
#     passFile = open('X://pytest//haxima.txt')
#     for line in passFile.readlines():
#         if ':' in line:
#             user = line.split(':')[0]
#             cryptPass = line.split(':')[1].strip(' ')
#             print("[*] Cracking Password For:" + user)
#             tesrPass(cryptPass)
# if __name__ == "__main__":
#         mian()


#制造字典
# import itertools
# import string
# test = (''.join(x) for x in itertools.product('1234567890',repeat=3))
# with open("X://pytest//dictionary.txt",'a',encoding='utf-8') as f:
#     while 1:
#         try:
#             f.write(next(test)+'\n')
#             print('写入成功')
#         except Exception as e:
#             print(e)
#             break

# import zipfile
# fize = zipfile.ZipFile('X://pytest//eve.zip')
# passfile = open('X://pytest//test.txt')
# for line in passfile.readlines():
#         password = line.strip('\n')
#         try:
#             fize.extractall(pwd=password)
#             print('[+] password ='+password+'\n')
#         except :
#             print("no")



#制造字典
# import itertools
# import string
# test = (''.join(x) for x in itertools.product('1234567890',repeat=3))
# with open("X://pytest//dict.txt",'a',encoding='utf-8') as f:
#     while 3:
#         f.write(next(test) + '\n')

import zipfile
import threading
flag = True
def checkPassword(zFile,password):
    global flag
    try:
        zFile.extractall(pwd=password.encode('utf8'))
        print('[+] pasword found:'+password)
        flag = False
    except Exception as e:
        pass
zip_path = 'X://pytest/test.zip'
password_path = 'X://pytest/dict.txt'
file_password = open(password_path,'r')
lines = file_password.readlines()
zFile = zipfile.ZipFile(zip_path)
for line in lines:
    password = line.strip('\n')
    if flag:
        mytrhead = threading.Thread(target=checkPassword,args=(zFile, password))
        mytrhead.start()
        print(mytrhead.getName(),'Start')
    else:
        break


