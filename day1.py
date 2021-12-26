# Below code is from the following YouTube video https://www.youtube.com/watch?v=pkLfyRwDMMw

p1 = 0
p2 = 0

XS = [int(x) for x in open("numbers.txt")]

for i in range(len(XS)):
    if i>=1 and XS[i] > XS[i-1]:
        p1 += 1

    if i>=1 and XS[i]+XS[i-1]+XS[i-2] > XS[i-1]+XS[i-2]+XS[i-3]:
        p2 += 1

print(p1)
print(p2)