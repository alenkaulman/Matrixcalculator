import numpy

from matice import Matice

Matice = Matice()

#obchazi konflikt argumentu pro test unit a argparse
if __name__ == '__main__':
    Matice.nacteniParametru()  
if Matice.vystupOK:
    print ('výsledná matice :')
    print (Matice.vystup) 
 