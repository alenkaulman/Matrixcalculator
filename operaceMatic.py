from asyncio.windows_events import NULL
import numpy


#trida operaci - jednoduche na rozsirovani - u techto z knihovny to nema logiku, ale je to 
#   vhodne pro pridani novych delanych rucne
class OperaceMatic:
    def __init__(self,matrix1,matrix2):
        self.vystup = NULL
        self.jeChyba = False   
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.errorMessage = ""

# u chyb se da pripadne zachytit podrobnejsi hlaska a rozdelit to na vice kategorii - nebo vypsat detail anglicky dle numpy viz Sum
    def Sum(self):
        try :
           self.vystup = numpy.add(self.matrix1,self.matrix2)
        except Exception as chyba:
            self.jeChyba = True
            #self.errorMessage = f"{type(chyba).__name__} was raised: {chyba}" # vcetne nazvu
            self.errorMessage = f"{chyba}" 
        return self

    def Multiply(self):
        try :
            self.vystup = numpy.matmul(self.matrix1,self.matrix2)
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self

    def Power(self):
        try :
            self.vystup = numpy.linalg.matrix_power(self.matrix1,int(self.matrix2.item(0)))
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self      

    def Trans(self):
        try :
            self.vystup = self.matrix1.T
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self         

    def Solve(self):
        try :           
                if self.matrix1.shape[0] == self.matrix1.shape[1] and numpy.linalg.matrix_rank(self.matrix1) == self.matrix1.shape[0]:
                    self.vystup = numpy.linalg.solve(self.matrix1,self.matrix2)
                else:
                    print("Priblizna hodnota metodou nejmensich ctvercu je:")
                    self.vystup = numpy.linalg.lstsq(self.matrix1,self.matrix2,rcond=None)[0] 
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self      

    def Det(self):
        try :
            self.vystup = numpy.linalg.det(self.matrix1)
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self     

    def Inverse(self):
        try :
            self.vystup = self.matrix1.I
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self   

    def Rank(self):   
        try :
            self.vystup = numpy.linalg.matrix_rank(self.matrix1)
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self   

    def Cholesky(self):   
        try :
            self.vystup = numpy.linalg.cholesky(self.matrix1)
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage = f"{chyba}"
        return self                    

    def Vec(self):
        try:
             self.vystup = numpy.reshape(self.matrix1,(-1,1), order='F')
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage =  f"{chyba}"
        return self 

    def Hmult(self):
        try:
             self.vystup = numpy.multiply(self.matrix1, self.matrix2)
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage =  f"{chyba}"
        return self        


    #operace mimo numpy

    #zakladni vypocet nasobeni matice
    def Multiply2(self):
        try :
            self.vystup = numpy.zeros(shape=(len(self.matrix1), len(self.matrix2[0])))
            # iterate through rows of X
            for i in range(len(self.matrix1)):
                # iterate through columns of Y
                for j in range(len(self.matrix2[0])):
                    # iterate through rows of Y
                    for k in range(len(self.matrix2)):
                        self.vystup[i][j] += self.matrix1[i][k] * self.matrix2[k][j]
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage =  f"{chyba}"
        return self

    #jiny vypocet nasobeni matice
    def Multiply3(self):
        try :
            self.vystup = [[sum(a*b for a,b in zip(self.matrix1_row,self.matrix2_col)) for self.matrix2_col in zip(*self.matrix2)] for self.matrix1_row in self.matrix1]   
        except Exception as chyba:
            self.jeChyba = True
            self.errorMessage =  f"{chyba}"
        return self   


    def Neznama(self):
        self.jeChyba = True
        self.errorMessage = "neznama operace"





