#with as
#way_1 <=> way_2
#way_1
with open('data.txt') as f:
    f.readline()

#way_2
try:
    f = open('data.txt')
except:
    pass
else:
    f.readline()
finally:
    f.close()