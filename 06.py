

def kthSmallest(arr, N, K):

    # Sort the given array
    arr.sort()

    # Return k'th element in the
    # sorted array
    return arr[K-1]


# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2

    # Function call
    print("K'th smallest element is",
          kthSmallest(arr, N, K))