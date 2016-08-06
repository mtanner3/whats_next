
T = int(raw_input().strip())

for testcase in range(T):
    n = int(raw_input().strip())
    arr = raw_input().strip().split()
    #print arr
    if len(arr) % 2 == 0: # even - ends in zeros
        #print "ends in zeros"
        last = arr.pop()
        arr.append("%s" % (int(last) + 1))
    else: # odd. Last 2 are 
        #print "ends in zeros then ones"
        last = arr.pop()
        nextlast = arr.pop()
        if nextlast == '1':
            thirdlast = arr.pop()
            arr.append("%s" % (int(thirdlast) + 1))
        else:
            arr.append("%s" % (int(nextlast) - 1))
            arr.append('1')
        arr.append('1')
        arr.append("%s" % (int(last) - 1))
    print len(arr)
    print " ".join(arr)


