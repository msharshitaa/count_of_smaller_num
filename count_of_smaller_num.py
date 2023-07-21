def count_of_smaller_num(arr):
    result=[]
    for i in range(len(arr)):
        count=0
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
        result.append(count)
    return result

arr=list(map(int,input().split()))
print(count_of_smaller_num(arr))
