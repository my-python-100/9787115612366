# 第 7 章 函数是一等对象

## 7.2 把函数视为对象

```python
factorial.__doc__
type(factorial)
help(factorial)
```

## 7.3 高阶函数

* 在 Python 3 中，map 和 filter 还是内 置函数，但是由于引入了列表推导式和生成器表达式，因此二者就变 得没那么重要了。

```python
from functools import reduce
from operator import add
```

## 7.4 匿名函数

* 在高阶函数的参数列表中最适合使用匿名函数


## 7.5 9种可调用对象

* 判断对象能否调 用，最安全的方法是使用内置函数 callable()

## 7.6 用户定义的可调用类型

* 只需实现实例方法 `__call__`

## 7.7　从位置参数到仅限关键字参数

* 定义函 数时，如果想指定仅限关键字参数，就要把它们放到前面有 * 的参数 后面
* 如果不想支持数量不定的位置参数，但是想支持仅限关键字参 数，则可以在签名中放一个 *

```python
def f(a, *, b):
	pass
f(1, b=2)
```

**仅限位置参数**

* 从 Python 3.8 开始，用户定义的函数签名可以指定仅限位置参数
* 如果想定义只接受位置参数的函数，则可以在参数列表中使用 `/`
* / 左边均是仅限位置参数。在 / 后面，可以指定其他参数，处理方式 一同往常。

```python
def tag(name, /, *content, class_=None, **attrs):
	...
```

## 7.8 支持函数式编程的包

**7.8.1　operator 模块**

* 工厂函数 `itemgetter` 和 `attrgetter`，能`替代`从序列中取出项或读取对象属性的 `lambda 表 达式`
* methodcaller 创建的函数会在对象上调用参数指定的方法

**7.8.2　使用 functools.partial 冻结参数**

* partial 为原可调用对象的某些参数绑定预定的值
