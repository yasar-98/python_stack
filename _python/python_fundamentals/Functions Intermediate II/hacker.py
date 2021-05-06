def countSwaps(a):
    # Write your code here
    c=0
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if a[j]<a[i]:
                a[j],a[i]=a[i],a[j]
                c+=1
    print(f"Array is sorted in {c} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
countSwaps([1,4,2,6,3])