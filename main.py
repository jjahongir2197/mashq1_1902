class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name):
        if name.islower():
            self.__username = name
            print(f"muaffaqiyatli o'zgardi")
        else:
            print("xatolik Username kichik harflarda emas")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@"  in value:
            self.__email = value
            print(f"muaffaqiyatli o'zgardi")
        else:
            print("xatolik emailda @ yo'q emas")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
            print(f"muaffaqiyatli o'zgardi")
        else:
            print("xatolik  yoshi 0 dan katta")


u1 = User("tom", "tom@gmail.com", 20)
print(f"u1: username = {u1.username}")

u1.username = "tomjon"
print(f"u1: username = {u1.username}")

print(f"u1: email = {u1.email}")

u1.email = "gfsdjkl@dg"
print(f"u1: email = {u1.email}")

print(f"u1: age = {u1.age}")

u1.age = -0
print(f"u1: age = {u1.age}")
