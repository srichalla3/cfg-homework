matrix=[[1,4,7,12,15,1000],
    [2,5,19,31,32,1001],
    [3,8,24,33,35,1002],
    [40,41,42,44,45,1003],
    [99,100,103,106,128,1004]
]

for i,j in enumerate(matrix):
    for k,target in enumerate(j):
        if target==44:
            print([i,k])
        else:
            print([-1, -1])
