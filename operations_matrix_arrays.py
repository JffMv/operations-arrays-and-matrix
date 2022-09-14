# This five fuctions are the of pass laboratory 
def sum(c1, c2):

    number1 =  c1[0] + c2[0]
    number2 = c1[1] + c2[1]
    print_beatiful (number1, number2)
    return ( number1, number2)

def sustration(c1, c2):

    number1 =  c1[0] - c2[0]
    number2 = c1[1] - c2[1]
    print_beatiful(number1, number2)
    return (number1, number2)

def multiplation (c1, c2):

    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginate = c1[0] * c2[1] + c1[1] * c2[0]

    print_beatiful(real, imaginate)
    return (real, imaginate)
 
    
def print_beatiful (a,b):
    if b == None :
        print (a)
    else:
        print ("( " , a ," , ",b ,"i)")

def conjugate(c1):

    number1 = c1[0]
    nubmer2 = c1[1]*-1
    print_beatiful(number1, nubmer2)
    return (number1, nubmer2)

################################################################

#sum arrays of same dimentions. This fuction receive lists as arrays.
def sumVector(vector1,vector2):
    if len(vector1)!=len(vector2):
        print("The arrays doesn´t have same dimentions")
    else:
        b = [[None for fila in range(1)] for column in range(len(vector1))]

        fila = len(vector1)
        
        for i in range(fila):
            b[i][0] = lab1.suma(vector1[i][0],vector2[i][0])

        return b

def SubtrationVector(vector1,vector2):
    if len(vector1)!=len(vector2):
        print("The arrays doesn´t have same dimentions")
        SubtrationVector(vector1,vector2)
    else:
        a = [[None for fila in range(1)] for column in range(len(a))]
        row = len(vector1)
        for i in range(row):
            a[i][0] = sustration(vector1[i][0],vector2[i][0])

        return a
# Receive complex array and return the sum inverse 

def SumInverse_Vector(array):

    a = [[None for fila in range(1)] for column in range(len(array))]
    row = len(a)
    for i in range(row):
        a[i][0] = multiplation(array [i][0],[-1,0])

    return a

# multiplicate a array whit complex number 
def NumberMultiplication_Vector(array,number):
    row = len(array)
    a = [[None for column in range(len(array[0]))] for row in range(len(array))]
    for i in range(row):
        a[i][0] = multiplation(array[i][0],number)

    return a

#sum two matrix same dimations
def sum_matrix(matrix1,matrix2):
    row = len(matrix1)
    column = len(matrix1[0])
    
    if len(matrix1)!=len(b) or len(matrix1[0])!=len(matrix2[0]):
        print("The matrix doesn´t have same dimentions")
    else:
        matrix = [[None for ji in range(column)] for ij in range(row)]

        for i in range(row):
            for p in range(column):
                matrix[i][p] = sum(matrix1[i][p],matrix2[i][p])

        return matrix

# return the sum inverse of a matrix
def sumInverse_matrix(matrix):
    row = len(matrix)
    column = len(matrix[0])
    
    for i in range(row):
        for j in range(column):
            matrix[i][j] = multiplation(matrix[i][j],[-1,0])

    return matrix


# Multiplication of a matrix whit complex number
def multiplicationNumber_Matrix(matrix,number):

    row = len(matrix)
    column = len(matrix[0])
    ultimate = [[None for ji in range(column)] for ij in range(row)]
    for i in range(row):
        for j in range(column):
            ultimate[i][j] = multiplation(matrix[i][j],number)
    return ultimate

#return the transposed matrix or array
def transposed_matrix_array(hybride):
   
    row = len(hybride)
    column = len(hybride[0])

    transposed = [[None for ji in range(row)] for ij in range(column)]

    for i in range(row):
        for j in range(column):
            transposed[j][i] = hybride[i][j]

    return transposed

# This is the fuction of conjute for matrix and arrar
def conjugate_matrix_array(hybride):
    row = len(hybride)
    column = len(hybride[0])

    a = [[None for ji in range(column)] for ij in range(row)]
    if column > 1:
        for i in range(row):
            for j in range(column):
                a[i][j] = conjugate(hybride[i][j])
    else:
        for i in range(row):
            a[i][0] = conjugate(hybride[i][0])
    return a


#return a matrix attached 
def attached_matrix_array(hybride):
    conjuate = hybride[:]
    newconjuate = conjugate_matrix_array(conjuate)
    transposed = transposed_matrix_array(newconjuate)
    return transposed

def multiplicate_matrix(matrix1,matrix2):
    filaA = len(matrix1)
    filaB = len(matrix2)
    columnaA = len(matrix1[0])
    columnaB = len(matrix2[0])

    if columnaA!=filaB:
       print("The matrix doesn´t have same dimentions")
    else:
        result = [[[0,0] for columna in range(columnaB)] for fila in range(filaA)]
        for i in range(filaA):
            for j in range(columnaB):
                for k in range(filaB):
                    result[i][j] = sum(result[i][j],multiplation(matrix1[i][k],matrix2[k][j]))
        return result

#Multiplation a matrix with the array
def accion_Matrix_multiplation_Vector(matrix,array):
    return multiplicate_matrix(matrix,array)

#Multiplation two arrays and return a number
def productoInterno_Vector(array1,array2):

    newVector = attached_matrix_array(array1)
    return multiplicate_matrix(newVector,array2)

#Return the real number as norm of the array
def norm_of_Vector(array):
    row = len(array)
    column = len(array[0])

    result = 0

    for i in range(row):
        for j in range(column):
            result += array[i][j][0]**2+array[i][j][1]**2
    return (result**1/2)

#Return a real number as distance of two arrays
def distanciaVector(array1,array2):
    sustration = SubtrationVector(array1,array2)
    norm = norm_of_Vector(sustration)

    return norm

#return False o True if the type matrix is unity matrix
def matrix_Unity(matrix):
    knife = attached_matrix_array(matrix)
    operation = multiplicate_matrix(matrix,knife)

    row = len(matrix)
    column = len(matrix[0])
    matrizIdentidad = [[[1,0] if x==y else [0,0] for y in range(column)] for x in range(row)]
    for i in range(row):
        for j in range(column):
            operation[i][j] = [round(operation[i][j][0]),round(operation[i][j][1])]
    if operation==matrizIdentidad:
        return True
    else:
        return False

#return False o True if the type matrix is hermitiana matrix
def matrix_Hermitiana(matrix):
    knife = attached_matrix_array(matrix)

    if knife== matrix:
        return True
    else:
        return False

def Tensor_multiplation_matrix_array(hybride1,hybride2):
    row1 = len(hybride1)
    row2 = len(hybride2)
    column1 = len(hybride1[0])
    column2 = len(hybride2[0])

    newmatrix = [[[0,0] for ji in range(column1*column2)] for ij in range(row1*row2)]

    for i in range(len(newmatrix)):
        for j in range(len(newmatrix[0])):
            newmatrix[i][j] = multiplation(hybride1[i//row2][j//column2],hybride2[i%row2][j%column2])


    return newmatrix