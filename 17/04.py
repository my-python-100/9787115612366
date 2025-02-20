class Sentence:

  def __next__(self):
    raise StopIteration

  def __iter__(self):
    return self

s3 = Sentence("Life of Brian")
it = iter(s3)
next(it)