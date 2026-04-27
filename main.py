def linear_search(arr, target):
    """Her elemanı tek tek kontrol eder."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Sıralı listede böl-yönet mantığıyla arar."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

def quick_sort(arr):
    """Pivot kullanarak hızlı sıralama yapar."""
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test Senaryosu
if _name_ == "_main_":
    liste = [64, 34, 25, 12, 22, 11, 90]
    print(f"Orijinal Liste: {liste}")
    
    sirali = quick_sort(liste)
    print(f"Sıralanmış Liste (Quick Sort): {sirali}")
    
    hedef = 22
    index = binary_search(sirali, hedef)
    print(f"Eleman {hedef}, {index}. indekste bulundu.")
