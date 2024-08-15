def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    left_list, right_list = split(lst)
    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left,right)

def split(lst):
    midpoint = len(lst)//2
    return lst[:midpoint],lst[midpoint:]

def merge(left,right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1
    
    while j < len(right):
        l.append(right[j])
        j+=1

    return l
ls =[5,1,7,2,10,8]
print(merge_sort(ls))
