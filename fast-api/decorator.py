# Là một design pattern dùng để wrapping một hàm trong python lại
# 1. Python đối với function là object, cho nên có thể pass tên function vào function khác để call

def make_pretty(func):

    def inner():
        print("-------Function call----------")
        func()
        print("------Function end call --------")
    return inner

def get_something():
    print("hello world")
result = make_pretty(get_something)

@make_pretty
def ordinary():
    print("I am ordinary")

@make_pretty
def get_something():
    print("get information")

ordinary()  


# #------------------------------- Smart divide ---------------------
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)
