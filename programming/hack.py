def count(arr1, arr2, n, m):
    freq = {}
    s = 0

    for word in arr1:
        
        word = ' '.join(sorted(word))

        if word in freq.keys():
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    for word in arr2:
        word = ' '.join(sorted(word))

        if word in freq.keys():
            s+=1
        #     print(freq[word], end = " ")
        # else:
        #     print(0, end = " ")
            
    # print() 
    print(s)   

# arr1 = list(map(str, input().split()))
arr1 = eval(input())
n = len(arr1)
    
# arr2 = list(map(str, input().split()))
arr2 = eval(input())
m = len(arr2)

count(arr1, arr2, n, m)
