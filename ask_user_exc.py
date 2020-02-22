def ask_user():
    while True:
        x=input()
        try:
            if x in answer:
                print(answer.get(x))       
        except KeyboardInterrupt:
            print("Пока!")
            break
answer={"Как дела?":"Хорошо!","Что делаешь?":"Программирую","Как погода?":"Прекрасно!","Который час?":"Не подскажу"}
print(ask_user())
