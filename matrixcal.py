import math
class MatrixCalculator:
    def plus(matrix1,matrix2):
        result = []
        if type(matrix1) != list and type(matrix2) != list:
            raise Exception("Only support type of list")
        elif len(matrix1) != len(matrix2):
            raise Exception("Two matrix have different row")
        elif len(matrix1[0]) != len(matrix2[0]):
             raise Exception("Two matrix have different column")
        else:
            for i in range(len(matrix1)):
                result.append([])
                for j in range(len(matrix1[i])):
                    result[i].append(matrix1[i][j] + matrix2[i][j])
        return result

    def minus(matrix1,matrix2):
        result = []
        if type(matrix1) != list and type(matrix2) != list:
            raise Exception("Only support type of list")
        elif len(matrix1) != len(matrix2):
            raise Exception("Two matrix have different row")
        elif len(matrix1[0]) != len(matrix2[0]):
             raise Exception("Two matrix have different column")
        else:
            for i in range(len(matrix1)):
                result.append([])
                for j in range(len(matrix1[i])):
                    result[i].append(matrix1[i][j] - matrix2[i][j])
        return result

    def matrixtran(matrix):
        result = []
        if type(matrix) != list:
            raise Exception("Only support type of list")
        for i in range(len(matrix[0])):
            result.append([])
            for j in range(len(matrix)):
                result[i].append(matrix[j][i])
        return result



    

    def matrixmultiply(matrix1,matrix2):
        result = []
        newmatrix2 = []
        if type(matrix1) != list and type(matrix2) != list:
            raise Exception("Only support type of list")
        elif len(matrix1[0]) != len(matrix2):
             raise Exception("Two matrix1 column different with matrix2 row")
        else:
            newmatrix2 = MatrixCalculator.matrixtran(matrix2)

            for i in range(len(matrix1)):
                result.append([])
                for j in range(len(newmatrix2)):
                    calbuffer = 0
                    for a in range(len(matrix1[i])):
                        calbuffer += matrix1[i][a] * newmatrix2[j][a]
                    result[i].append(round(calbuffer,4))
            
            return result
    
    def multiply(num,matrix):
        result = []
        if type(matrix) != list:
            raise Exception("Only support type of list")
        else:
            for i in range(len(matrix)):
                result.append([])
                for j in range(len(matrix[i])):
                    result[i].append(matrix[i][j]*num)
        return result

    def dev(matrix):
        if type(matrix) != list:
            raise Exception("Only support type of list")
        else:
            buffera = 0
            bufferb = 0
            if len(matrix) < 3:
                buffera = matrix[0][0] * matrix[1][1]
                bufferb = matrix[0][1] * matrix[1][0]
            return buffera - bufferb

    

    def inv(matrix):
        result = []
        dev = MatrixCalculator.dev(matrix)
        matrix = MatrixCalculator.matrixtran(matrix)
        if type(matrix) != list:
            raise Exception("Only support type of list")
        else:
            if dev != 0:
                for i in range(len(matrix)):
                    result.append([])
                    for j in range(len(matrix[i])):
                        if i!=j:
                            ans = (-2* (matrix[~i][~j]/dev)) + (matrix[~i][~j]/dev)
                            result[i].append(ans)
                        else:
                            result[i].append(matrix[~i][~j]/dev)
        return result

                        
    def matrixpow(matrix,time):
        result = matrix
        for i in range(1,time):
            result = MatrixCalculator.matrixmultiply(result,matrix)
        return result
            


                
                
            

    



    

            
           
        