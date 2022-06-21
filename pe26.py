# project euler problem #26. Cannot use float precision
# for 1-1000 because max repeat length is d-1. This also
# means we can count down and stop when repeat length > d-1
# We don't need the actual fraction, but the length of repeats.
# That means we can analyze when remainders repeat

# initialize length of longest repeating sequence: repeat_length
repeat_length = 0

#loop over all possible denominators
for denom in range(1001, 1, -1)
    if (repeat_length > denom) break
    
    #list of digits found for this denom: digits
    digits = []
    x = 1
    index = 0

    while(x!=0):
        remainder = x%denom
        digits
