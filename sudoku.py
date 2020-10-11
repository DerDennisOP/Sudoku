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
changes = True
while changes:
    changes = False
    for x in range(3):
        for y in range(3):
            zcount = 0
            for rx in range(3):
                for ry in range(3):
                    if sod[y*3+ry][x*3+rx] == 0:
                        arr1 = [sod[y*3+0][x*3+0],sod[y*3+0][x*3+1],sod[y*3+0][x*3+2],
                                sod[y*3+1][x*3+0],sod[y*3+1][x*3+1],sod[y*3+1][x*3+2],
                                sod[y*3+2][x*3+0],sod[y*3+2][x*3+1],sod[y*3+2][x*3+2]]
                        res = solve_easy(arr1, [row[x*3+rx] for row in sod], sod[y*3+ry])
                        if len(res[0]) == 1:
                            sod[y*3+ry][x*3+rx] = res[0][0]
                            changes = True
t2 = time.time()
print(f"Solved in: {t2-t1}s")
print(sod)
