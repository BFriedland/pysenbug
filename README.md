# pysenbug
Alter the functionality of your code. Unpredictably.

#### Usage
This version of the pysenbug module operates through a decorator.

```
In [1]: from pysenbug import pysenbug

In [2]: @pysenbug
   ...: def open_box():
   ...:     print("meow")
   ...:     

In [3]: open_box()

In [4]: open_box()
meow

In [5]: open_box()

In [6]: open_box()

In [7]: open_box()

In [8]: open_box()
meow

In [9]: open_box()

In [10]: open_box()
meow

In [11]: open_box()
meow
```

#### Future development
Future versions of pysenbug will feature a parameterized decorator, metaclasses that infect their descendants' methods, and hopefully, faked tracebacks for maximum fun.
