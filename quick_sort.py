def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst)//2
    pivot_candidates = [lst[0], lst[mid], lst[-1]]
    pivot = sorted(pivot_candidates)[1]

    less_than_pivot = [value for value in lst if value<pivot]
    more_than_pivot = [value for value in lst if value>pivot]
    equal_to_pivot = [value for value in lst if value == pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot +quick_sort(more_than_pivot)

ls =[5, 1, 7, 2, 10, 8, 1, 1] 
print(quick_sort(ls))