# Decorator còn có thể truyền parameter vào nữa, phải sử dụng một hàm bao quanh decorator gốc

def make_pretty(type):
    def decorator(func):
        def inner():
            print(f"-------{type} call----------")
            func()
            print(f"------{type} end call --------")
        return inner
    return decorator

@make_pretty("Function")
def ordinary():
    print("I am ordinary")

ordinary()