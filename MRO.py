class A:
    def __init__(self):
        print('Running __init__ from class A')
    
    def method1(self):
        print('Running method 1 from class A')
    
    def method2(self):
        print('Running method 2 from class A')
    
    def method3(self):
        print('Running method 3 from class A')

class B(A):
    def __init__(self):
        super().__init__()
        print('Running __init__ from class B')
    
    def method1(self):
        print('Running method 1 from class B')
    
    def method2(self):
        print('Running method 2 from class B')

class C(B):
    def __init__(self):
        super().__init__()
        print('Running __init__ from class C')

class D(A):
    # def __init__(self):
    #     super().__init__()
    #     print('Running __init__ from class D')
    
    def method3(self):
        print('Running method 3 from class D')

class E(C, D):
    pass

if __name__ == "__main__":
    e = E() # calls __init__ in order: A -> B -> C
    e.method1() # Running method 1 from class B
    e.method2() # Running method 2 from class B
    e.method3() # Running method 3 from class D