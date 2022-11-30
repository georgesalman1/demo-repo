




# 

def check_subset_aux(arr, Total, n):
    if  Total==0 :
        return True
    if n==0:
        return False
    return check_subset_aux(arr, Total-arr[n], n-1) or check_subset_aux(arr, Total, n-1)
    


def check_subset(arr, Total):
    return check_subset_aux(arr, Total, len(arr)-1)



arr = [-1,3,5,5,-2]

print(check_subset(arr, 7))




