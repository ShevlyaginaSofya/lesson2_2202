
def action(age):
    if age < 7:
        return 'Вы учитесь в детском саду'
    elif age < 17:
        return 'Вы учитесь в школе'
    elif age < 23:
        return 'Вы учитесь в ВУЗе'
    else:
        return 'Вы работаете'

print('Введите свой возраст')
age = input()
age = int(age)
out = action(age)
print(out)

