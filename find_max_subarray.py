def find_max_crossing_subarray(A, low, mid, high):
    left_sum = None
    max_left = None
    sum = 0

    for i in reversed(xrange(low, mid + 1)):
        sum = sum + A[i]
        if not left_sum or sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = None
    max_right = None
    sum = 0

    for i in xrange(mid + 1, high + 1):
        sum = sum + A[i]
        if not right_sum or sum > right_sum:
            right_sum = sum
            max_right = i
    
    return max_left, max_right, left_sum + right_sum if left_sum and right_sum else None


def find_max_subarray(A, low, high):

    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2

        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum > right_sum and cross_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and cross_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':

    A = [-1, -2, 3, 4, 2, 1, -1, 200, -100, 100]

    print(find_max_subarray(A, 0, len(A) - 1))

    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    print(find_max_subarray(A, 0, len(A) - 1))

    A = [-10, -20, -31, -42, -2, -10, -1, -200, -100, -100]

    print(find_max_subarray(A, 0, len(A) - 1))