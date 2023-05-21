#!/usr/bin/python3
def validUTF8(data):
    n_bytes = 0
    for num in data:
         
        bin_rep = format(num, '#010b')[-8:]
         
        for bit in bin_rep:
            if bit == '0': break
            n_bytes += 1
             
        if n_bytes == 0:
            continue
        
        if n_bytes == 1 and n_bytes > 4:
            return False
        
        if not (bin_rep[0] == '1' or bin_rep[1] == '0'):
            n_bytes -= 1
            return False
    return n_bytes == 0
        