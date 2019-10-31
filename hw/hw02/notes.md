# 由church numerals引发的关于higher-order function的思考

```
def zero(f):
    return lambda x: x

def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))

def three(f):
    return lambda x: f(f(f(x)))
```

以上的函数的含义都十分好理解，一个church numeral就是把函数`f`算那么多次。所以可以定义

```
def church_to_int(m):
    return m(lambda x: x + 1)(0)
```

我们再来定义加法，乘法，幂

```
def add_church(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    return lambda f: m(n(f))

def pow_church(m, n):
    return n(m)
```

我觉得`add_church`和`mul_church`都是很好理解的，但却始终没有弄明白`pow_church`的魔力在哪里。我觉得我的问题出在没有完全理解how a function works，就是说对于how to draw an environment diagram我也没搞太清

When a function is defined: Create a function value: `func <name>(<formal parameters>)[parent=<lab>]`. Its parent is the current frame. Bind `<name>` to the function value in the current frame.

When a function is called: Add a local frame, titled with the name of the function being called. Copy the parent of the function to the local frame: `[parent=<lab>]`. Bind the `<formal parameters>` to the arguments in the local frame. Execute the body of the function in the environment that starts with the local frame.

我用[visualize](http://pythontutor.com/)

10.24更新，在这个美妙的日子里，我顿悟了。`n(m)`的含义是，`n`次调用`m`，大概就是这样`m(...(m(m(f)))...)`，内层返回的函数会作为下一次的输入。好好对比一下与`n(m(f))`的区别。

