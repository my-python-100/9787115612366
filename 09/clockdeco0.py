import time

def clock(func):
  def clocked(*args):
    t0 = time.perf_counter()
    result = func(*args)
  return clocked