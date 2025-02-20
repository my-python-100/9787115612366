"""
只要Python函数的主体中有yield 关键字，该函数就是生成器函数
调用生成器函数，返回一个生成器对象
"""
def gen_123():
  yield 1
  yield 2

g = gen_123()
next(g)