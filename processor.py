def add():
    r1, c1 = [int(x) for x in input("Enter size of first matrix:").split()]
    matrix1 = [[float(x) for x in input("Enter first matrix:").split()] for r_matrix in range(int(r1))]
    r2, c2 = [int(x) for x in input("Enter size of second matrix:").split()]
    matrix2 = [[float(x) for x in input("Enter second matrix:").split()] for r_matrix in range(int(r2))]
    if r1 == r2 and c1 == c2:
        matrix3 = [[(matrix1[r][c]) + matrix2[r][c] for c in range(c1)] for r in range(r1)]
        print("The result is:")
        for row in matrix3:
            for column in row:
                print(column, end=" ")
            print()
    else:
        print("The operation cannot be performed.") 


def mulc():
    r1, c1 = [int(x) for x in input("Enter size of matrix:").split()]
    matrix1 = [[float(x) for x in input("Enter matrix:").split()] for r_matrix in range(int(r1))]  
    m = float(input("Enter constant:"))
    matrix = [[matrix1[r][c] * m for c in range(c1)] for r in range(r1)]
    print("The result is:")
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()


def mul():
    r1, c1 = [int(x) for x in input("Enter size of first matrix:").split()]
    print("Enter first matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    r2, c2 = [int(x) for x in input("Enter size of second matrix:").split()]
    print("Enter second matrix:")
    matrix2 = [[float(x) for x in input().split()] for r_matrix in range(int(r2))]
    matrix3 = [[0]*c2]*r1
    if c1 == r2:
        print("The result is:")
        for r in range(r1):
            print(*[sum([matrix1[r][k]*matrix2[k][j] for k in range(c1)]) for j in range(c2)])
    else:
        print("The operation cannot be performed.")     
        
        
def transpose():
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")        
    x = int(input("Your choice:"))    
    if x == 1:
        main_diag()
    elif x == 2:
        side_diag()
    elif x == 3:
        vertical_diag()
    elif x == 4:
        horizontal_diag()
        
        
def main_diag():
    r1, c1 = [int(x) for x in input("Enter matrix size:").split()]
    print("Enter matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    matrix = [[matrix1[j][i] for j in range(r1)] for i in range(c1)]
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()
   
  
def side_diag():
    r1, c1 = [int(x) for x in input("Enter matrix size:").split()]
    print("Enter matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    matrix = [[matrix1[j][i] for j in reversed(range(r1))] for i in reversed(range(c1))]
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()
             
             
def vertical_diag():
    r1, c1 = [int(x) for x in input("Enter matrix size:").split()]
    print("Enter matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    matrix = [[matrix1[i][j] for j in reversed(range(r1))] for i in range(c1)]
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()     
 
 
def horizontal_diag():
    r1, c1 = [int(x) for x in input("Enter matrix size:").split()]
    print("Enter matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    matrix = [[matrix1[i][j] for j in range(r1)] for i in reversed(range(c1))]
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()     
 
                                              
def determinant():
    r1, c1 = [int(x) for x in input("Enter matrix size:").split()]
    print("Enter matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    if r1 != c1:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        print(det(matrix1))


def det(mat):
    if len(mat) == 1:
        return mat[0][0]
    n = len(mat)
    return sum([(-1) ** k * mat[0][k] * det(rmat(mat, k, 0, n)) for k in range(n)])


def rmat(mat, k, m, n):
    return [[mat[i][j] for j in range(n) if j != k] for i in range(n) if i != m]


def inverse():
    r1, c1 = [int(x) for x in input("Enter matrix size:").split()]
    print("Enter matrix:")
    matrix1 = [[float(x) for x in input().split()] for r_matrix in range(int(r1))]
    if r1 != c1:
        print("The operation cannot be performed.")
    else:
        detmatrix = det(matrix1)
        matrix = [[(-1) ** (i + j) * det(rmat(matrix1, i, j, r1)) / detmatrix for j in range(r1)] for i in range(c1)]
        for r in matrix:
            print(*r)

while True:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n5. Calculate a determinant\n6. Inverse matrix0. Exit")
    x = int(input("Your choice"))
    if x == 1:
        add()
    elif x == 2:
        mulc()
    elif x == 3:
        mul()
    elif x == 4:
        transpose() 
    elif x == 5:
        determinant() 
    elif x == 6:
        inverse()          
    elif x == 0:
        exit()
