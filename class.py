class User:
    count = 0
    def __init__(self,name):
        User.count += 1
        self.__name = name
    def say_hi(self):
        print("hi {0}".format(self.__name))        
    
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))
    
print(User.count)
tom = User("tom")
tom.say_hi()

print(tom._User__name);
bob = User("bob")
bob.say_hi()
print(User.count)
tom.abc = 1
print(tom.abc)
