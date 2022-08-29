#P12.1
def is_sorted(A):
    for i in range(len(A)-1):
        if (A[i]>A[i+1]) :
            return False
    return True
	
data = [ 1,2,3,4,5,8,7,6 ]
print(is_sorted(data))

#P12.2
def merge_sort(A, left, right) :
	if left<right :
		mid = (left + right) // 2		
		merge_sort(A, left, mid)		
		merge_sort(A, mid + 1, right)	
		merge(A, left, mid, right)	    

def merge(A, left, mid, right) :
    global sorted		
    k = left			
    i = left			
    j = mid + 1		    
    while i<=mid and j<=right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid :		
        sorted[k:k+right-j+1] = A[j:right+1]	
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]		
    A[left:right+1] = sorted[left:right+1]	    

sorted = []
arr = [ 71, 49, 92,55, 38, 82, 72, 53 ]
sorted = [0]*len(arr)
merge_sort(arr, 0, len(arr)-1) 
print ("MergeSort: ", arr) 
