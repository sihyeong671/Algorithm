class Test:
    def __init__(self):
        self.x = 0
    
    def get_self(self):
        return self.x

test1 = Test()
print(id(test1))

def print_class(T):
    print(id(T))
    print(T.get_self())

print_class(test1)