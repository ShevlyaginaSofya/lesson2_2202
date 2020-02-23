score=[
    {'school_class': '1a', 'scores': [4,4,5,5,5,3]}, 
    {'school_class': '1b', 'scores': [3,4,4,5,2,2]}, 
    {'school_class': '2a', 'scores': [3,3,3,5,2,4]},
    {'school_class': '2b', 'scores': []}]
score_sum=0
score_count=0
for number in range(len(score)):
    score_sum += sum(score[number]['scores'])
    score_count += len(score[number]['scores'])

print(f'Количество оценок:{score_count}')
score_avg=(score_sum/score_count)
print(f'Средний балл по школе:{score_avg}')

for number in range(len(score)):
    try:
        score_sum = sum(score[number]['scores'])
        score_avg_cl = (score_sum/len(score[number]['scores']))
        print(f'Средний балл по классу:{score_avg_cl}')
    except ZeroDivisionError:
        print('В классе нет оценок')
        