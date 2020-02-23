def ask_user():
    try:
        answer_by_question = {"Как дела?":"Хорошо!","Что делаешь?":"Программирую","Как погода?":"Прекрасно!","Который час?":"Не подскажу"}
        while True:
           x=input()
           if x in answer_by_question:
                print(answer_by_question[x])       
    except KeyboardInterrupt:
        print("Пока!")
print(ask_user())
