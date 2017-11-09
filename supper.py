#import mypackage.user as mymodule
from mypackage.user import User,AdminUser

bob = AdminUser("bob",23)
tom = User("tom")
print(bob.name)
bob.say_hello()
bob.say_hi()
tom.say_hi()
