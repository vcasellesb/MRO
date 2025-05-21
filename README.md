# Simple example of Multiple Resolution Order
Sources:
* https://python-history.blogspot.com/2010/06/method-resolution-order.html
* https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
* https://docs.python.org/3/howto/mro.html#python-2-3-mro

From the last link:

> take the head of the first list, i.e L[B1][0]; if this head is not in the tail of any of the other lists, then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the head of the next list and take it, if it is a good head. Then repeat the operation until all the class are removed or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3 will refuse to create the class C and will raise an exception.

Essentially, this means that in the following:

```python
class A:
    def __init__(self):
        print('Running __init__ from class A')

class B(A):
    def __init__(self):
        super().__init__()
        print('Running __init__ from class B')

class C(B):
    def __init__(self):
        super().__init__()
        print('Running __init__ from class C')

class D(A):
    def __init__(self):
        super().__init__()
        print('Running __init__ from class D')

class E(C, D):
    pass
````

Since `A` is found at the tail of the list to the right (i.e. it is found also inherited by `B(A)`), it won't be appended when processing D! It is a breadth first algorithm, not a depth first.