
T = int(raw_input().strip())

def digits_to_bitarray(arr):
    bitarray = []
    val = "1"
    for item in arr:
        bitarray.extend(list(val*item))
        if val == "1":
            val = "0"
        else:
            val = "1"
    return bitarray

def find_rightmost_zero(bitarray):
    for pos in range(len(bitarray)-1, 0, -1):
        if bitarray[pos] == '0':
            return pos
    return None

def encode_bitarray(ba):
    cntarray = []
    count = 0
    lastbit = "1"
    for bit in ba:
        if bit == lastbit:
            count += 1
        else:
            cntarray.append("%s" % count)
            count = 1
        lastbit = bit
    cntarray.append("%s" % count)
    return cntarray

for testcase in range(T):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    #print "arr: %s" % arr
    ba = digits_to_bitarray(arr)
    #print "bitarray: %s" % ba
    rmz = find_rightmost_zero(ba)
    #print "rmz: %s" % rmz
    # if rmz is at the end of the string, just append '0' to the string
    # otherwise swap the zero at rmz with the one on it's right
    if rmz == len(ba)-1:
        ba.append('0')
    else:
        ba[rmz] = '1'
        ba[rmz+1] = '0'
    #print "bitarray: %s" % ba
    eba = encode_bitarray(ba)
    #print "encoded: %s" % eba
    print len(eba)
    print " ".join(eba)

