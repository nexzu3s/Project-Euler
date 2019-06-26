even_sum = 0
fib_nums = [0,1,0] # elements 0 and 1 sum to produce element 2

while fib_nums[2] < 4000000:
    fib_nums[2] = fib_nums[0] +fib_nums[1]
    fib_nums[0],fib_nums[1] = fib_nums[1], fib_nums[2]
    
    if (fib_nums[2] %2 ==0):
        even_sum+= fib_nums[2]

print(even_sum)
