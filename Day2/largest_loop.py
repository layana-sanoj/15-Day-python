# the selected loop is 9,41,12,64,72,1,222,68,18,21
lar=None
for numb in [9,41,12,64,72,1,222,68,18,21]:
    if lar is None or numb > lar:
        lar=numb
print('The largest number in the loop is',lar)
        
