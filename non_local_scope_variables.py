# NonLocal Scope

def say_my_name():
    # this is a local variable
    name = "abhi"

    # we have a nested function
    def say_my_name_in_caps():
        #  name is local scope variable,
        #  to update it from inside the nested function
        #  we have to use 'nonlocal' keyword

        nonlocal name
        name = "AJAY"

        # a nested fn can access local variables within parent fn
        print(name.upper())

    say_my_name_in_caps()
    print(name)

say_my_name()
