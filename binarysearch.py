def binarysearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            eight=mid-1
        return-1
arr=[5,7,8,55]
target=55
print(binarysearch(arr,target))