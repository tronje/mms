#!/usr/bin/env python3
import numpy as np

"""
Aufgabe 2

a)
Input: np.ones((1, 10))
Output: array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])
Kommentar: np.ones erzeugt einen Array von Einsen, mit dem angegebenen shape, also in diesem Fall 1,10.
           Der Datentyp ist  default float64.
 

Input: np.ones((10, 1))
Output: array([[1.],
               [1.],
               [1.],
               [1.],
               [1.],
               [1.],
               [1.],
               [1.],
               [1.],
               [1.]])
Kommentar: Hier wurde nur der shape geändert.

Input: np.ones((10))
Output: array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
Kommentar: Da hier nur eine Zahl als shape angegeben wird, wird ein eindimensionaler Array erzeugt.

Input: np.ones(10)
Output: array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
Kommentar: Es macht keinen Unterschied, ob der shape bei einem eindim. Array in Klammern oder nicht
           in Klammern angegeben wird.

Input: np.ones(10, np.int)
Output: array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
Kommentar: Hier wurde der Datentyp auf int spezifiziert und ist daher nicht mehr float64.

Input: np.arange(1, 10, 0.5)
Output: array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. ,
               7.5, 8. , 8.5, 9. , 9.5])
Kommenar: np.arange erzeugt einen Array mit Werten zwischen einem Start- und Stopwert und einer
          Schrittgröße.

Input: np.arange(100, 50, -1)
Output: array([100,  99,  98,  97,  96,  95,  94,  93,  92,  91,  90,  89,  88,
            87,  86,  85,  84,  83,  82,  81,  80,  79,  78,  77,  76,  75,
            74,  73,  72,  71,  70,  69,  68,  67,  66,  65,  64,  63,  62,
            61,  60,  59,  58,  57,  56,  55,  54,  53,  52,  51])
Kommentar: Hier wird eine Schrittgröße von -1 angegeben und damit der Array umgedreht.

Input: np.pi*np.arange(0, 2, 0.1)
Putput: array([0.        , 0.31415927, 0.62831853, 0.9424778 , 1.25663706,
           1.57079633, 1.88495559, 2.19911486, 2.51327412, 2.82743339,
           3.14159265, 3.45575192, 3.76991118, 4.08407045, 4.39822972,
           4.71238898, 5.02654825, 5.34070751, 5.65486678, 5.96902604])
Kommentar: Hier wird der Array, der mit np.arange erstellt wird, elementweise mit pi aus
           np.pi multipliziert.

b)
a = np.array([[1, 2],[3, 4]])
m = np.matrix(a)

Input: a*a
Output: array([[ 1,  4],
               [ 9, 16]])
Kommentar: Bei np.array werden die Zahlen im Array elementweise multipliziert.

Input: m*m
Output: matrix([[ 7, 10],
                [15, 22]])
Kommentar: Bei np.matrix wird Matrixmultiplikation verwendet.
    
Input: a**a
Output: array([[  1,   4],
               [ 27, 256]])
Kommentar: Auch hier wird wieder elemtweise potenziert.

Input: m**m
Output: TypeError: exponent must be an integer
Kommentar: Da man nicht eine Matrix als Potenz verwenden kann, wird hier eine Fehlermeldung
           geworfen.

Input: np.dot(a, a)
Output: array([[ 7, 10],
               [15, 22]])
Kommentar: np.dot gibt das dot Produkt zweier Arrays, bei 2 dim. Arrays entspricht dieses der
           Matrixmultiplikation.

Input: np.dot(m, m)
Output: array([[ 7, 10],
               [15, 22]])
Kommentar: Wie eben schon gesagt, entspricht np.dot bei 2 dim. Arrays der Matrixmultiplikation.
           Daher ist her der output von np.dot(a, a) und np.dot(m, m) identisch.

"""

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
d = mat[1::2]
print(d)
print("\n")

# Ausschneiden jeweils nur ungeraden Spalten
e = mat[:,::2]
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
