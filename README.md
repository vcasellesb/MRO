# Simple example of Multiple Resolution Order
Sources:
* https://python-history.blogspot.com/2010/06/method-resolution-order.html
* https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
* https://docs.python.org/3/howto/mro.html#python-2-3-mro
* https://aran-fey.github.io/programming-guides/super.html

From the second to last link (this is important for understanding how a class' MRO is constructed):

> take the head of the first list, i.e L[B1][0]; if this head is not in the tail of any of the other lists, then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the head of the next list and take it, if it is a good head. Then repeat the operation until all the class are removed or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3 will refuse to create the class C and will raise an exception.

And in the last one:
> [if FooBar inherits from Bar and Foo] remember, `super(Foo, self)` looks at the MRO of `type(self)` (FooBar) and **skips everything up to Foo**. When self is an instance of Foo, the `super().__init__()` in Foo calls object.`__init__`. But when self is an instance of FooBar, it calls `Bar.__init__`.

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

e = E()
````

The output produces:

```bash
Running __init__ from class A
Running __init__ from class D
Running __init__ from class B
Running __init__ from class C
```

However!! Switching the two lines in the `__init__` definition of `class D(A)`, i.e.:

```python
class D(A):
    def __init__(self):
        print('Running __init__ from class D')
        super().__init__()
```

The output becomes:

```bash
Running __init__ from class D
Running __init__ from class A
Running __init__ from class B
Running __init__ from class C
```

Because `type(self)` (`E`) 's MRO is: 

`(<class '__main__.E'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>)`

And as the second quote says, the first `super().__init__()` call is called within class `C`, which calls `super().__init__` from within `B`, and thus the MRO algorithm "looks at the MRO of `type(self)` and **skips everything up to `B`**."!, in which case the next class in the MRO with an `__init__` defined is `D`, which is what we're seeing in this example. It can either print something first (last example), or call `super.__init__()` first, which in turn calls `A`'s `__init__` method.