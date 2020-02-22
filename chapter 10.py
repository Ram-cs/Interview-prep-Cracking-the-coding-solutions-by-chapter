##################################
####### Sorting and Searching ####
##################################


#1 Sorted Merge:
A = [1,3,7,19]
B = [2,5,16]
c = (A+B)
c.sort()
print(c)

Ai = 0
Bi = 0
result = []
while Ai < len(A) or Bi < len(B):
    if Ai < len(A) and Bi < len(B):
        if A[Ai] < B[Bi]:
            result.append(A[Ai])
            Ai += 1

        elif B[Bi] < A[Ai]:
            result.append(B[Bi])
            Bi += 1
        else:
            result.append(A[Ai])
            result.append(B[Bi])
            Ai, Bi = Ai+1, Bi+1
    elif Ai < len(A):
        result.extend(A[Ai:])
        break
    else:
        result.extend(B[Bi:])
        break

print(result)


#2 Group Anargams
#3
A = [15,16,19,20,25,1,3,4,5,7,10,14]
print(A.index(5))


#5
A = ["at","","","","ball","","","car"]
print(A.index("ball"))


#6

