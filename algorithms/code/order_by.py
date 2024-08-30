def bubble_sort(arr):
    n = len(arr)
   
    while True:
        swapped = False
        for i in range(1, n):
            
            if arr[i - 1] > arr[i]:
                print(arr)
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1
       
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


if __name__ == '__main__':
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    print(bubble_sort(arr))
    print(insertion_sort(arr))
    print(merge_sort(arr))

