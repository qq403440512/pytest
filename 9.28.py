'''
def fahrenheit_converter(c):
    fahrenheit = c * 9/5 + 32
    return str(fahrenheit) + '˚F'
a=fahrenheit_converter(50)
print(a)


n = 0.0
count = True
while 1:
    n = n + 1.0
    if n * n * n > 12000:
        if count:
            print('n**3', n - 1)
            count = False

    # print('hahah')
    if n * n >= 12000:
        print(n * n)
        print('n**2', n)
        break




import requests
def =
html = requests.get(https://translate.google.cn/#en/zh-CN/console)
print(html)
'''

'''
#1
j=1
for n in range (1,100):
	x=n*(3*n-1)/2
	print((x),end=' ')
	j+=1
	if(j==11):
		print('\n')
		j=1
'''
# EP-2	整数的每个数字的和
'''
def sumDigits(n):
	m = 0
	for i in n:
		j = int(i)
		m += j
	print(m)
n = input('输入一个整数：')
sumDigits(n)
'''
# EP-3	排序
'''
def displaySortedNumber(a,b,c):
	if(a>b):
		a,b=b,a
	if(a>c):
		a,c=c,a
	if(b>c):
		b,c=c,b
	print(a,b,c)
a,b,c = eval(input('输入3个数字：'))
displaySortedNumber(a,b,c)
'''
# EP-4	计算利率
'''
def futureInvestmentValue(inves,mon,year):
    return inves*(1+mon)**(year*12)
money=eval(input('投资多少:'))
rate=eval(input('利率为:'))
print('年份      回报')
for i in range(1,31):
    val=futureInvestmentValue(money,rate/12,i)
    print('%-10d%.2f'%(i,val))
'''
# EP-5	字符打印
'''
#ch1,ch2,n = eval(input('输入要打印字符的区间，以及打印几行：'))
def a(ch1,ch2,n):
	x = 0
	for i in range(ord(ch1),ord(ch2)+1):
		print(chr(i),end=' ')
		x += 1
		if(x%n==0):
			print()
a('1','z',10)	
'''
# EP-6	每年有几天
'''
def numberOfDaysInYear():
	for i in range(2010,2021):
		if(i%4==0):
			print('{}年有366天。'.format(i))
		else:
			print('{}年有365天。'.format(i))
numberOfDaysInYear()
'''
# EP-7	计算两点距离
'''
import math 
def distance():
	x1,y1 = eval(input('输入第一个点：'))
	x2,y2 = eval(input('输入第二个点：'))
	x1=math.radians(x1)
	y1=math.radians(y1)
	x2=math.radians(x2)
	y2=math.radians(y2)
	p1 = math.sin(x1)* math.sin(x2)
	p2 = math.cos(x1)* math.cos(x2)
	p3 = math.cos(y1-y2)
	d = 6371.01 * math.acos(p1 + p2 * p3)
	print("距离为{}".format(d))
distance()
'''
# EP-8


# EP-9	显示时间
'''
import time
import datetime
i = datetime.datetime.now()
m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print('Current date and time is ',m[i.month-1],i.day,',',i.year,time.strftime("%H:%M:%S"))
'''

# EP-10	摇色子
'''
import random
n = random.randint(1,6)
m = random.randint(1,6)
print(m,n)
if m+n==2 or m+n==3 or m+n==12:
	print('你输了!')
elif m+n==7 or m+n==11:
	print('你赢了！')
else:
	x = n + m
	n = random.randint(1,6)
	m = random.randint(1,6)
	print(m,n)
	if m+n==7 or n+m==x:
		print('你赢了')
	else:
		print('你输了')
'''

'''
import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
class SendMail(object):
    def __init__(self,username,passwd,recv,title,content,
                 file=None,ssl=False,
                 email_host='smtp.qq.com',port=25,ssl_port=465):

        :param username: 用户名
        :param passwd: 密码
        :param recv: 收件人，多个要传list ['a@qq.com','b@qq.com]
        :param title: 邮件标题
        :param content: 邮件正文
        :param file: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
        :param ssl: 是否安全链接，默认为普通
        :param email_host: smtp服务器地址，默认为163服务器
        :param port: 非安全链接端口，默认为25
        :param ssl_port: 安全链接端口，默认为465

        self.username = username #用户名
        self.passwd = passwd #密码
        self.recv = recv #收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = title #邮件标题
        self.content = content #邮件正文
        self.file = file #附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host #smtp服务器地址
        self.port = port #普通端口
        self.ssl = ssl #是否安全链接
        self.ssl_port = ssl_port #安全链接端口
    def send_mail(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file:#处理附件的
            file_name = os.path.split(self.file)[-1]#只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f,"base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                #base64.b64encode(file_name.encode()).decode()
                new_file_name='=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                #这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"'%(new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))#邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            pass
        except Exception as e:
            print('出错了。。',e)
        else:
            print('发送成功！')
        self.smtp.quit()
if __name__ == '__main__':
    m = SendMail(
        username='1944326662@qq.com',
        passwd='*963.000',
        recv=['diozxc93085@chacuo.net'],
        title='发送邮件20180205',
        content='测试发送邮件，qq发件，接收方一个是163邮箱，另一个是qq邮箱。20180205',
        file=r'E:\\testpy\\python-mpp\\day7\\作业\\data\\mpp.xls',
        ssl=True,
    )
    m.send_mail()
'''



