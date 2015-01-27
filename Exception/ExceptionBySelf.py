class MyException(Exception):
   def __call__(self):
       print 'caut MyException'

try:
    length = 5
    raise MyException
except MyException:
    a = MyException()
    a()
else:
    print 'no exception'
finally:
    print 'finished'
