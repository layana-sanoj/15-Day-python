# the selected loop is  9,41,12,64,72,1,222,68,18,21
sml=None
for numb in [9,41,12,64,72,1,222,68,18,21]:
    if sml is None or numb < sml:
        sml = numb
print('The smallest number in the loop is', sml)
