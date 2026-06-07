# Program to find two numbers that occur odd number of times

def print_two_odd(arr):
    # XOR of all elements = XOR of the two odd-occurring numbers
    xorof2 = 0
    for num in arr:
        xorof2 ^= num

    # Rightmost set bit in xorof2
    setbit = xorof2 & ~(xorof2 - 1)

    x = 0
    y = 0

    # Divide numbers into two groups and XOR separately
    for num in arr:
        if num & setbit:
            x ^= num
        else:
            y ^= num

    print("The two ODD elements are", x, "&", y)


# Input
arr = []
arr_size = int(input("Enter size of the array: "))

for _ in range(arr_size):
    arr.append(int(input("Enter element: ")))

print_two_odd(arr)