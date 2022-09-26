import numpy, argparse 
import operaceMatic as OM
import timeit


class Matice:
    def __init__(self, operace = "nedefinovano",matrix1 = numpy.zeros, matrix2 = numpy.zeros, vystupniSoubor = None, mereni = False):
        self.operace = operace
        self.matrix1 = matrix1
        self.matrix2 = matrix2 
        self.vystupniSoubor = vystupniSoubor
        self.mereni = mereni
        self.vystup = numpy.zeros
        self.vystupOK = False

    # operace s maticemi
    def provedOperaci(self):
        vystup = OM.OperaceMatic(self.matrix1, self.matrix2)
        match self.operace:
            case "sum":     
                vystup.Sum()     
            case "multiply":  
                #testRychlosti 
                if self.mereni:  
                    print(timeit.timeit(stmt=''' 
def mereni(): 
    return vystup.Multiply()
''', setup="import operaceMatic",number=1000000))
                vystup.Multiply()             
            case "power":     
                vystup.Power()   
            case "trans":     
                vystup.Trans()   
            case "solve":     
                vystup.Solve()     
            case "det":     
                vystup.Det()    
            case "inverse":     
                vystup.Inverse()   
            case "rank":     
                vystup.Rank()  
            case "vec":
                vystup.Vec()
            case "hmult":
                vystup.Hmult()
            case "cholesky":     
                vystup.Cholesky()  
            # operace mimo numpy
            case "multiply2": 
                #testRychlosti    
                if self.mereni:  
                    print(timeit.timeit(stmt=''' 
def mereni(): 
    return vystup.Multiply2()
''', setup="import operaceMatic",number=1000000))             
                vystup.Multiply2() 
            case "multiply3":   
                #testRychlosti   
                if self.mereni:  
                    print(timeit.timeit(stmt=''' 
def mereni(): 
    return vystup.Multiply3()
''', setup="import operaceMatic",number=1000000))            
                vystup.Multiply3()         
            # operace co neexistuje    
            case _:
                vystup.Neznama()   
        #vystup
        if vystup.jeChyba == True:
            print (vystup.errorMessage)
        else:
            #print ('výsledná matice :')
            #print (vystup.vystup) 
            self.vystup = vystup.vystup 
            self.vystupOK = True
            try: 
                if self.vystupniSoubor is not None : 
                    numpy.savetxt(self.vystupniSoubor,numpy.atleast_2d(vystup.vystup), delimiter=' ')                    
            except:
                print('chyba vystupu do souboru')


    # chyba pri nacitani hodnot matic
    def spatnaMatice():
        print('chyba souboru matice - zadejte ve formátu : ')
        print('5 4 3')
        print('6 1 8')

    # argv obchazi konflikt pro test unit a argparse, at nedochazi k nacitani argumentu pro testunit do argparse
    def nacteniParametru(self,argv=None):
        # nacteni prikazoveho radku
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('--matice1', metavar='mat1.txt', help="soubor matice 1, např. mat1.txt", type=argparse.FileType(mode="r"))
        parser.add_argument('--matice2', metavar='mat2.txt', help="soubor matice 2, např. mat2.txt", type=argparse.FileType(mode="r"))
        parser.add_argument('--vystup', metavar='out.txt', help="výstupní soubor, např. out.txt", type=argparse.FileType(mode="w"))
        parser.add_argument('--operace', metavar='sum', type=str, help=('dostupné operace : \n'
            'sum : soucet dvou matic \n'
            'multiply : soucin dvou matic \n'
            'power : n-ty nasobek matice - hodnotu urcuje prvni element matice2 \n'
            'trans : transponovani matice\n'
            'solve : vyreseni matice pro zadanou pravou stranu\n'
            'det : determinant ctvercove matice\n'
            'inverse : inverzni matice\n'
            'rank : hodnost matice\n'
            'vec : funkce dle matlabu - matice do jednoho vektoru\n'
            'hmult : Hadamard Product'
            'cholesky : dolni trojuhelnikovou matici Choleskeho rozkladu'))
        parser.add_argument('--mereni', help="aktivuje mereni casu - pouzito jen u multiply, multiply2, multiply3 - 1.000.000 cyklu", default=False, action='store_true')
        # nacteni matic ze souboru
        try: 
            args = parser.parse_args(argv) 
            if not args.matice1 == None: self.matrix1 = numpy.loadtxt (args.matice1)
            #nacteni druheho souboru matic pro operace, co ho vyzaduji (v pripade power se nacita jen prvni hodnota)
            if not args.matice2 == None: self.matrix2 = numpy.loadtxt (args.matice2)        
        except ValueError:
            self.spatnaMatice()
        except: 
            print('chyba')
        else:
            self.operace = args.operace
            self.vystupniSoubor = args.vystup
            self.mereni = args.mereni
            self.provedOperaci()