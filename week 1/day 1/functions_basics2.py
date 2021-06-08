# 1. Countdown 
my_list = []
def countdown(x):
    for x in range(x, -1, -1):
        my_list.append(x)
    return my_list
start = countdown(5)
print(start)

# 2. Print and Return 
def print_and_return(x, y):
    print(x)
    return y
call = print_and_return(1,2)
print(call)

# 3. First Plus Length
def first_plus_length(arr):
    sum = arr[0] + len(arr)
    return sum
math_time = first_plus_length([1,2,3,4,5])
print(math_time)

# 4. Values Greater than Second
my_list = []
def values_greater_than_second(arr):
    count = 0
    end = len(arr)
    for x in range(0, end):
        if len(arr) < 2:
            return "False"
        elif arr[x] > arr[1]:
            my_list.append(arr[x])
            count = count + 1
    print(count)
    print(my_list)
new_list = values_greater_than_second([5,2,3,1,4])
print(new_list)

# 5. this length, that value
new_list = []
def length_and_value(x, repeat = y):
    new_list.append(x)
    repeat y
    print(new_list)
print(length_and_value(2, repeat = 5))