fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# 반복문
for fruit in fruits:
    print(fruit)

count = 0
for f in fruits:
    if f == '배':
        count+=1
print(count)

def count_fruit(fruit_name):
    fruit = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
    number=0

    for item in fruit:
        if item == fruit_name:
            number+=1

    return number

print(count_fruit('사과'))