def compare(str1,str2):
    if type(str1)!=str and type(str2)!=str:
        return 0
    elif str1==str2:
        return 1
    elif str1!=str2 and len(str1)>len(str2):
        return 2
    elif str1!=str2 and str2=='learn':
        return 3
print('Введите 1 строку')
str1 =input()
print('Введите 2 строку')
str2=input()
out=compare(str1,str2)
print(out)