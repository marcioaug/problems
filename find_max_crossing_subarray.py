def find_max_crossing_subarray(A, low, mid, high):
    left_sum = None
    sum = 0

    for i in reversed(range(low, mid)):
        sum = sum + A[i]
        if sum > left_sum or left_sum == None:
            left_sum = sum
            max_left = i
    
    right_sum = None
    sum = 0

    for i in range(mid, high):
        sum = sum + A[i]
        if sum > right_sum or right_sum == None:
            right_sum = sum
            max_right = i
    
    return max_left, max_right, left_sum + right_sum



if __name__ == '__main__':

    A = [-1, -2, 3, 4, 2, 1, -1, 2, -10]

    print(find_max_crossing_subarray(A, 0, 4, 8))