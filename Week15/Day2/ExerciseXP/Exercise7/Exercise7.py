import faker
users = []

for i in range(5):
    user = {}
    fake = faker.Faker()
    user['name'] =  fake.name()
    user['address'] = fake.address()
    user['language-code'] = fake.language_code()

    users.append(user)

