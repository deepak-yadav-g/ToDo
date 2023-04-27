from faker import Faker


fake = Faker()
def get_registered_user():
    user = {
        'name': fake.name()
        , 'address': fake.address()
        , 'dob': fake.date()
    }
    return user

if __name__ == '__main__':
    print(get_registered_user())
