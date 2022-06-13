import numpy as np

#loop over all possible denominators
for denom in range(10, 1001)
    decimal = 1/float(denom)
    decimal_str = str(decimal)
    print('denom: ', str(denom), ', decimal: ', str(decimal_str))

    #initialize digits to check and strip
    repeat_num = ''
    max_len = 0
    decimal_str.strip('0.')

    #loop over different digits in the number and check for repeats (use in keyword)
    for digit in decimal_str:
        repeat_num.append(digit)
        if(repeat_num in )