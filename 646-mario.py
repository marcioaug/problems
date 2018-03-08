
def binary_search_lower_bound(array, element):

    begin = 0
    end = len(array) - 1
   
    while end >= begin:
        mid = (begin + end) / 2
  
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            end = mid - 1
        else:
            begin = mid + 1
    
    if array[mid] > element:
        return None if mid == 0 else mid - 1

    return mid


def main():
    (n, l) = map(int, raw_input().split())   
    
    while n != 0 or l != 0:
        lockers = map(int, raw_input().split())
        min_changes = None

        for i, locker in enumerate(lockers):
            last_locker = binary_search_lower_bound(lockers, (locker + n) - 1)
            changes = n - (last_locker - i + 1)
       
            if min_changes == None or min_changes > changes:
                min_changes = changes

        print(min_changes)
            
        (n, l) = map(int, raw_input().split())
    
if __name__ == '__main__':
    main()