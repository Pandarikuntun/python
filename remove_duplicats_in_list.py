def duplicate_removed(list):
    seen={}
    result=[]
    for item in list:
        if item not in seen:
            seen[item]=True
            result.append(item)
    return result
list=[1,2,1,2,5,5,6,1,4,2,4,2,4,2,1]
filtered_list=duplicate_removed(list)
print(f"here the duplicate removed list {filtered_list}")