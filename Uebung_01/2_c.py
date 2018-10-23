import numpy as np

# 2 C)
mat = np.random.randint(-10,11,(6,6))
print(mat)
print("\n")

# Ausschneiden der 1. Zeile Ihrer Matrix
a = mat[0]
print(a)
print("\n")

# Ausschneiden der 5. Spalte Ihrer Matrix
b = mat[:,4]
print(b)
print("\n")

# Multiplizieren der 5. Zeile Ihrer Matrix mit 2
# c
mat[4] = mat[4]*2
print(mat)
print("\n")

# Ausschneiden jeweils nur der geraden Zeilen
d = mat[[i%2==0 for i in range(mat.shape[0])]] # vieleicht etwas kompliziert :)
print(d)
print("\n")

# Ausschneiden jeweils nur ungeraden Spalten
e = mat[:,[i%2==1 for i in range(mat.shape[1])]] # vieleicht etwas kompliziert :)
print(e)
print("\n")

# Ausschneiden einer neuen 3x3 Matrix aus Ihrer Matrix
f = mat[:3,:3]
print(f)
print("\n")

# Setzen aller negativen Zahlen Ihrer Matrix auf 0
mat[mat < 0] = 0
print(mat)
print("\n")

#print(mat)
