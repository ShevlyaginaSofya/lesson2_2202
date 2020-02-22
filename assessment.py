score=[
    {'school_class': '1a', 'scores': [4,4,5,5,5,3]}, 
    {'school_class': '1b', 'scores': [3,4,4,5,2,2]}, 
    {'school_class': '2a', 'scores': [3,3,3,5,2,4]},
    {'school_class': '2b', 'scores': [3,4,4,5,2,5]}]
score_sum=0
for number in range(len(score)):
    score_sum+=sum(score[number]['scores'])

score_avg=(score_sum/len(score[0]['scores']))/len(score)
print(f'Средний балл по школе:{score_avg}')

for number in range(len(score)):
    score_sum=sum(score[number]['scores'])
    score_avg_cl=(score_sum/len(score[number]['scores']))
    print(f'Средний балл по классу:{score_avg_cl}')