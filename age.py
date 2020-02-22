
def action(age):
    if int(age) <7:
        return 'Вы учитесь в детском саду'
    elif 7<=int(age)<17:
        return 'Вы учитесь в школе'
    elif 17<=int(age)<23:
        return 'Вы учитесь в ВУЗе'
    else:
        return 'Вы работаете'

print('Введите свой возраст')
age =input()
out=action(age)
print(out)

