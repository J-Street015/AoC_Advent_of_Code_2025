# read the input and add the input to a list of numbers.
num_list = []
with open("input_day3") as f:
    for line in f.readlines():
        num_list.append(int(line.rstrip("\n")))


# function found at https://www.geeksforgeeks.org/dsa/largest-number-possible-after-removal-of-k-digits/
def maxnumber(n, k):
    # Function to return the
    # largest number possible
    for i in range(0, k):
        # Generate the largest number
        # after removal of the least K digits
        # one by one
        ans = 0
        i = 1
        while n // i > 0:
            # Remove the least digit
            # after every iteration
            temp = (n // (i * 10)) * i + (n % i)
            i *= 10
            # Store the numbers formed after
            # removing every digit once

            # Compare and store the maximum
            if temp > ans:
                ans = temp
        n = ans

        # Return the remaining number
    # after K removals
    return ans


# get k for the function.
number_len = len(str(num_list[0]))
final_number_length = 12

k = number_len - final_number_length
updated_num_list = []
for n in num_list:
    updated_num_list.append(maxnumber(n, k))

print(sum(updated_num_list))
