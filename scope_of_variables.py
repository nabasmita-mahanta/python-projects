# Global Scope
# Local Scope
# NonLocal Scope


# these are global scoped variable
name = "abhi"
age =15

def say_my_name():
    #  age is local scope variable,
    #  to make it global scope variable we have to use 'global' keyword

    global age
    age = 30
    print(name)
    print(age)

say_my_name()

print(name)
print(age)

