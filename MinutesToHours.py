import sys
def main(minute):
        time,minuteLeft=divmod(minute,60)
        print(time,'H, ',minuteLeft,'M')
try:
    if int(sys.argv[1])<0:
        raise ValueError('Input number cannot be negative.')
    else:
        main(int(sys.argv[1]))
except:
    print('Parameter Error')
