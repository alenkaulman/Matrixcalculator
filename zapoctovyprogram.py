import numpy.linalg
import re

def nactimatici():
    print("Zadejte matici:")
    i = input()
    i = validace(i)
    if i == "chyba":
        return "chyba"
    a = numpy.matrix(i)
    return a

def nactips():
    print("Zadejte pravou stranu:")
    i = input()
    i = validace(i)
    if i == "chyba":
        return "chyba"
    a = numpy.matrix(i)
    if a.shape[1] == 1:
        return a
    else:
        return "chyba"

def validace(i):
    if i == "":
        return "chyba"
    allowed = "0123456789 ;-+."   
    if not all(ch in allowed for ch in i):
        return "chyba"
    s = i.split(";")
    for j in range(len(s)):
        s[j]=s[j].split()
    pocet = len(s[0])
    for j in range(len(s)):
        if len(s[j]) != pocet:
            return "chyba"
    for j in range(len(s)):
        for k in range(len(s[j])):
            if not re.match('^[-+]{0,1}[0-9]+\.{0,1}[0-9]*$', s[j][k]):
                return "chyba"
    return i
    

def help():
    print("Vsechny mozne operace jsou:")
    print("soucet dvou matic --sum--")
    print("soucin dvou matic --multiply--")
    print("n-ty nasobek matice --power--")
    print("transponovani matice --trans--")
    print("vyreseni matice pro zadanou pravou stranu --solve--")
    print("determinant ctvercove matice --det--")
    print("inverzni matice --inverse--")
    print("hodnost matice --rank--")
    print("dolni trojuhelnikovou matici Choleskeho rozkladu --cholesky--")
    print("napoveda --help--")
    print("Pro ukonceni programu staci napsat --exit--.")


def sum(a,b):
    return a+b

def multiply(a,b):
    return a*b

def power(a,n):
    return numpy.linalg.matrix_power(a,n)

def trans(a):
    return a.T

def solve(a,b):
    if a.shape[0] == a.shape[1] and rank(a) == a.shape[0]:
        return numpy.linalg.solve(a,b)
    else:
        print("Priblizna hodnota metodou nejmensich ctvercu je:")
        return numpy.linalg.lstsq(a,b,rcond=None)[0] 

def det(a):
    return numpy.linalg.det(a)

def inverse(a):
    return a.I

def rank(a):
    return numpy.linalg.matrix_rank(a)

def cholesky(a):
    return numpy.linalg.cholesky(a)








help()
while True:
    print("Zadejte operaci:")
    operace = input()
    mozne = ["sum","multiply","power","trans","solve","det","inverse","rank","cholesky","exit","help"]
    if operace not in mozne:
        print("Chyba. Takova operace neexistuje.")

    if operace == "exit":
        break

    if operace == "help":
        help()

    if operace == "sum":
        a = nactimatici()
        b = nactimatici()
        if str(a) == "chyba" or str(b) == "chyba":
            print("Chyba. Spatne zadane matice.")
        else:    
            if a.shape == b.shape:  ##matice jdou secist
                print(sum(a,b))
            else:
                print("Chyba. Matice nejsou stejneho tvaru.")

    if operace == "multiply":
        a = nactimatici()
        b = nactimatici()
        if str(a) == "chyba" or str(b) == "chyba":
            print("Chyba. Spatne zadane matice.")
        else:
            if a.shape[1] == b.shape[0]:    ##matice jdou vynasobit
                print(multiply(a,b))
            else:
                print("Chyba. Matice nejdou vynasobit.")

    if operace == "power":
        a = nactimatici()
        if str(a) == "chyba":
            print("Chyba. Spatne zadana matice.")
        else:
            print("Zadejte exponent:")
            n = input()
            if not re.match('^[-+]{0,1}[0-9]+\.{0,1}[0-9]*$', n):
                print("Chyba.")
            else:    
                print(power(a,int(n)))

    if operace == "trans":
        a = nactimatici()
        if str(a) == "chyba":
            print("Chyba. Spatne zadana matice.")
        else:
            print(trans(a))

    if operace == "solve":
        a = nactimatici()
        b = nactips()
        if str(a) == "chyba" or str(b) == "chyba":
            print("Chyba.Spatne zadane matice.")
        else:
            if a.shape[0] == b.shape[0]:   ##musi sedet pocet radku
                print(solve(a,b))
            else:
                print("Chyba. Pocet radku matice a prave strany se musi rovnat.")

    if operace == "det":
        a = nactimatici()
        if str(a) == "chyba":
            print("Chyba. Spatne zadana matice.")
        else:
            if a.shape[0] == a.shape[1]:    ##jen pro ctvercove matice
                print(det(a))
            else:
                print("Chyba. Matice neni ctvercova.")

    if operace == "inverse":
        a = nactimatici()
        if str(a) == "chyba":
            print("Chyba. Spatne zadana matice.")
        else:
            if rank(a) != a.shape[0]:
                print("Matice je singularni. Nema inverzni matici.")
            else:
                print(inverse(a))

    if operace == "rank":
        a = nactimatici()
        if str(a) == "chyba":
            print("Chyba. Spatne zadana matice.")
        else:
            print(rank(a))


    if operace == "cholesky":
        a = nactimatici()
        if str(a) == "chyba":
            print("Chyba. Spatne zadana matice.")
        else:
            if not numpy.all(numpy.linalg.eigvals(a) > 0) or not numpy.all(a - trans(a) == 0):
                print("Choleskeho rozklad neexistuje.")
            else:
                print(cholesky(a))


