print("hello world!")

# 사칙연산
a =1
b =2
c =3
a_plus_b = a+b
print(a+b)

# 자료형
nam = 'bob'
age = 14
isAdult = age>19
print(isAdult)

# 리스트
shop = ["수박","사과","참외"]
print(shop)
print(shop[1])
print(shop[-1]) #참외 (뒤에서부터)
print(shop[-2])
print(shop[-3])

# dictionary
bk = {
    'name': "남병관",
    "age" : 18,
    "address": "경기도"
}
print(bk['name'])
print(bk['age'])
print(bk['address'])

# 보통 어떻게 하나면
people = [{'name':'bob','age':20},{'name':'carry','age':38}]

# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name':'john','age':7}
people.append(person)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'
print(people[2]['name'])
print(people[2]['age'])


