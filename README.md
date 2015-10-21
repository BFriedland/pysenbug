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

#### Altering the behavior of pysenbug
The pysenbug decorator supports, but does not require, certain optional parameters that change its behavior.

One such parameter is *chance*, a float or int between 0 and 1. Lower values reduce the chance that the function will return its normal value in favor of the bugged value.
```
In [12]: @pysenbug(chance=0)
   ...: def polonium_box():
   ...:         print('miao')
   ...:

In [13]: polonium_box()

In [14]: polonium_box()

In [15]: polonium_box()

In [16]: polonium_box()

In [17]: polonium_box()

In [18]: polonium_box()

In [19]: polonium_box()

In [20]: polonium_box()

In [21]: polonium_box()
```

The *return_value* parameter allows pysenbug to return custom values.
```
In [22]: @pysenbug(return_value='bark')
   ...: def uranium_box():
   ...:         return 'miow'
   ...:

In [23]: uranium_box()
Out[23]: 'bark'

In [24]: uranium_box()
Out[24]: 'bark'

In [25]: uranium_box()
Out[25]: 'miow'

In [26]: uranium_box()
Out[26]: 'miow'

In [27]: uranium_box()
Out[27]: 'miow'

In [28]: uranium_box()
Out[28]: 'miow'

In [29]: uranium_box()
Out[29]: 'bark'

In [30]: uranium_box()
Out[30]: 'bark'

In [31]: uranium_box()
Out[31]: 'bark'
```

Supplying a *probability_function* allows customization of failure frequency profiles.
```
In [32]: def hidden_variable():
   ...:         while True:
   ...:                 yield False
   ...:                 yield True
   ...:

In [33]: bohm_interpretation = hidden_variable()

In [34]: @pysenbug(probability_function=bohm_interpretation.next)
   ...: def bismuth_box():
   ...:         print('miau')
   ...:

In [35]: bismuth_box()
miau

In [36]: bismuth_box()

In [37]: bismuth_box()
miau

In [38]: bismuth_box()

In [39]: bismuth_box()
miau

In [40]: bismuth_box()

In [41]: bismuth_box()
miau
```

#### Future development
Future versions of pysenbug will feature metaclasses that infect their descendants' methods, and hopefully, faked tracebacks for maximum fun.
