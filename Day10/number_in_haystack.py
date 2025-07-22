# sum of numbers in a file 
import re
file= 'regex_sum_actual_42.txt' # Change the filename as needed
fhand = open(file)
   
sum = 0
for line in fhand:
    line=line.rstrip()
    x = re.findall('[0-9]+', line)
    for num in x:
        sum += int(num)
        
print(sum)
