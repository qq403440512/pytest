#1
# def scores(s):
#     for i in range(len(s)):
#         if int(s[i])>=int(max(s))-10:
#             print('Student {} scores is {} and grade is A'.format(i,s[i]))
#         elif int(s[i])>=int(max(s))-20:
#              print('Student {} scores is {} and grade is B'.format(i,s[i]))
#         elif int(s[i])>=int(max(s))-30:
#             print('Student {} scores is {} and grade is C'.format(i,s[i]))
#         elif int(s[i])>=int(max(s))-40:
#             print('Student {} scores is {} and grade is D'.format(i,s[i]))
#         else:
#             print('Student {} scores is {} and grade is F'.format(i,s[i]))
# s = raw_input('qing shu ru cheng ji:')
# q = s.split(' ')
# scores(q)

#2
# def Num(s):
#     s = s [::-1]
#     print ('zhe chuan shu zi de ni xu shi:{}'.format(s))
# s = raw_input('shu ru yi chuan shu zi : ')
# Num(s)

#3
# def NUM(num):
#     for i in set(num):
#         print('{} occurs {} times'.format(i,num.count(i)))
# num = raw_input('Enter integers between 1 and 100:')
# q = num.split(' ')
# NUM(q)

#5
# import random
# def NUM(num):
#     n = set(num)
#     for i in n:
#         print('{} occurs {} times'.format(i,num.count(i)))
# num = [random.randint(0,9) for i in range (1000)]
# NUM(num)

#6
# def indexOfSmallestElenment(lst):
#     ls = min(lst)
#     n = str(lst)
#     m = n.find(ls)
#     print m
# lst=raw_input('shu ru yi ge shu zi lie biao: ')
# indexOfSmallestElenment(lst)

#7
# import random
# def shuffle(lst):
#     new = list(lst)
#     random.shuffle(new)
#     print new
# lst = raw_input('shu ru yi ge shu zi lie biao: ')
# q = lst.split(',')
# shuffle(q)

#8
# def eliminateDuplicates(lst):
#     l = []
#     for i in lst:
#         if i not in l:
#             l.append(i)
#     print l
# lst = raw_input('Enter ten numbers: ' )
# s = lst.split(' ')
# eliminateDuplicates(s)

#9
# def isSorted(lis):
#     s = sorted(lis)
#     lis = list(lis)
#     if lis == s:
#         print('The list is already sorted')
#     else:
#         print ('The list is not sorted')
# lis = raw_input('Enter list : ')
# isSorted(lis)

#10
# def Num(n):
#     for i in range(0,len(n)):
#         for j in range(i+1,len(n)):
#             if n[i] > n[j]:
#                 temp = n[j]
#                 n[j] = n[i]
#                 n[i] = temp
#     print n
# n = raw_input('shu ru 10 ge shu:')
# p = n.split(' ')
# Num(p)






