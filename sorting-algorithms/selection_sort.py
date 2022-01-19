#User function Template for python3

class Solution: 
    def select(self, arr):
        index = 0
        for j in range(len(arr)):
            if arr[j] > arr[index]:
                index = j
        return index
    
    def selectionSort(self, arr,n):
        for i in range(n-1,0,-1):
            index = self.select(arr[:i+1])
            if arr[index] > arr[i]:
                arr[i] , arr[index] = arr[index],arr[i]
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends