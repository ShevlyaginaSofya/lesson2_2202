def compare(str1,str2):
    if isinstance(str1, str)==False or isinstance(str2, str)==False:
        return 0
    elif str1==str2:
        return 1
    elif len(str1)>len(str2):
        return 2
    elif str2=='learn':
        return 3
str1 =123
print('1 строка', str1)
str2='привет!'
print('2 строка', str2)
out=compare(str1,str2)
print(out)