# Write a python function to find the largest continous sum in a given list of integers
def largest_continuous_sum(numbers):
    max_sum = current_sum = numbers[0]
    for n in numbers[1:]:
        current_sum = max(current_sum + n, n)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(largest_continuous_sum([5,6,7,8,9]))

# for give list [1,2,3,-2,5]
# max_sum = current_sum = numbers[0] = 1
# current_sum = max(1 + 2, 2) = 3
# max_sum = max(1, 3) = 3
# current_sum = max(3 + 3, 3) = 6
# max_sum = max(3, 6) = 6
# current_sum = max(6 - 2, -2) = 4
# max_sum = max(6, 4) = 6
# current_sum = max(4 + 5, 5) = 9
# max_sum = max(6, 9) = 9

