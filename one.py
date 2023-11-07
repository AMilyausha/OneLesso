def sortMassivImperative(arr):
    # flag = True
    # while flag:
    #     flag = False
    #     for i in range(len(arr) - 1):
    #         if arr[i] < arr[i + 1]:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #             flag = True
    maxlest=arr[0]
    sminindex=0
    for i in range(1,len(arr)):
        if arr[i]>maxlest:
            maxlest=arr[i]
            sminindex=i
    return sminindex

def sort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=sortMassivImperative(arr)
        newArr.append(arr.pop(smallest))
    return newArr



def sortMassivDeclarative(arr):
    arr.sort(reverse=True)
    return arr


print(f"Imperative style -> {sortMassivImperative([35, 9, 2, 7, -4, 2, 3, 78])}")
# print(f"Declarative style -> {sortMassivDeclarative([35, 9, 2, 7, -4, 2, 3, 78])}")
print(f"Declarative style -> {sort([35, 9, 2, 7, -4, 2, 3, 78])}")