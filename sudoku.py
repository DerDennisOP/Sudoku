import time

sod = [[3,4,0,7,1,0,0,5,8],
       [0,9,0,0,0,6,0,0,0],
       [7,0,2,0,5,0,3,0,4],
       [4,3,9,0,0,1,7,0,0],
       [0,0,5,0,0,0,8,0,0],
       [0,0,7,3,0,0,1,4,6],
       [2,0,1,0,8,0,4,0,9],
       [0,0,0,5,0,0,0,1,0],
       [6,7,0,0,4,9,0,0,2]]

arry = [0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2,
        0,0,0,1,1,1,2,2,2]

arrrx = [0,0,0,0,0,0,0,0,0,
         1,1,1,1,1,1,1,1,1,
         2,2,2,2,2,2,2,2,2,
         0,0,0,0,0,0,0,0,0,
         1,1,1,1,1,1,1,1,1,
         2,2,2,2,2,2,2,2,2,
         0,0,0,0,0,0,0,0,0,
         1,1,1,1,1,1,1,1,1,
         2,2,2,2,2,2,2,2,2,]

arrry = [0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,
         0,1,2,0,1,2,0,1,2,]


def solve_easy(arr1, arr2, arr3):
    comp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pos = []

    for x in range(len(arr1)):
        rem = True
        if arr1[x] != 0 and arr1[x] in comp:
            rem = False
            comp.remove(arr1[x])
        if arr2[x] != 0 and arr2[x] in comp:
            rem = False
            comp.remove(arr2[x])
        if arr3[x] != 0 and arr3[x] in comp:
            rem = False
            comp.remove(arr3[x])
        if rem:
            pos.append(x)
    return (comp, pos)

t1 = time.time()
for n in range(100000):
    changes = True
    while changes:
        changes = False
        for index in range(81):
            x = math.floor(index/27)
            y = arry[index]
            rx = arrrx[index]
            ry = arrry[index]
            if sod[y*3+ry][x*3+rx] == 0:
                res = 284
                arr1 = [sod[y*3+0][x*3+0],sod[y*3+0][x*3+1],sod[y*3+0][x*3+2],
                        sod[y*3+1][x*3+0],sod[y*3+1][x*3+1],sod[y*3+1][x*3+2],
                        sod[y*3+2][x*3+0],sod[y*3+2][x*3+1],sod[y*3+2][x*3+2]]
                comp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(9):
                    if arr1[x] != 0 and arr1[x] in comp:
                        res -= arr1[x]**2
                    if sod[i][x*3+rx] != 0 and sod[i][x*3+rx] in comp:
                        res -= sod[i][x*3+rx]**2
                    if sod[y*3+ry][i] != 0 and sod[y*3+ry][i] in comp:
                        res -= sod[y*3+ry][i]**2
                res = math.sqrt(res)
                if res == round(res):
                    sod[y*3+ry][x*3+rx] = res
                    changes = True
t2 = time.time()
print(f"Solved in: {t2-t1}s")
print(sod)
