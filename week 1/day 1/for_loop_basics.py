# print all integers from 0 -150

for x in range(0, 151):
    print(x)
# print multiples of 5 from 5 to 1,000

for x in range(5, 1005, 5):
    print (x)
# counting, the dojo way - Print integers 1 to 100. if divisible by 5, print "coding" instead. If divisible by 10, print "coding Dojo"

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
# woah that suckers huge - Add odd integers from 0 - 500,000 and print the final sum

sum = 0
for x in range(1, 500001, 2):
    sum = sum + x
print(sum)
# countdown by fours - Print positive numbers starting at 2018, counting down by fours

for x in range(2018, 0, -4):
    print(x)
#Flexible Counter - set three variables: lownum, highnum, mult. start at lownum to highnum, print only integers that are a multiple of mult

low_num = 1
high_num = 10
mult = 2
for x in range(low_num, high_num):
    if x % mult == 0:
        print(x)
