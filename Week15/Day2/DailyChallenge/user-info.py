from collections import namedtuple

User = namedtuple('User', 'name, age, score')
users = []

for i in range(5):
    print(f'------#{i+1}-------')
    name, age, score = input("Enter name,age,score : ").split(",")
    

    new_user = User(name, int(age), int(score))
    users.append(new_user)

users.sort(key=lambda x : (x.name, x.age, x.score))
print(users)