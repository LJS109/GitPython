'''
 Test Exception
'''
try:
    number = raw_input('enter a number')
    number = int(number)
    if(number < 10):
        pass
    else:
        raise IoException
except:
    print 'caut exception'
else:
    print 'no exception'
finally:
    print 'finished'
