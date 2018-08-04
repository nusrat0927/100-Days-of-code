def findMissingno(array, start, end):
    if (start > end):
        return end + 1
    if (start != array[start]):
        return start
    mid = int((start + end) / 2)
    if (array[mid] == mid):
        return findMissingno(array,
                          mid+1, end)
    return findMissingno(array, 
                          start, mid)
arr = [0, 1, 2, 4, 7, 8]
n = len(arr)
print("Smallest missing element is",
      findMissingno(arr, 0, n-1))
