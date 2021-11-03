A = {'An', 'Binh','Nam','Long', 'Ngoc', 'Tu'}
B = {'Binh','Linh','Nam','Hai','Long'}

def removeTu():
    A.remove('Tu')

removeTu()
print('A:',A)

def addCuong():
    A.add('Cuong')

addCuong()
print('A:',A)

def createC():
    global C 
    C = set(A^B)

createC()
print('C:',C)

D = set(A|B)
print(D)
E = set(A-B)
print(E)
F = set(A&B)
print(F)