""" Kurze Python Einführung im Rahmen der Vorlesung Optimierung 
    basierend auf der Matlab Einführung von Peter Ochs, 2017
    (https://lmb.informatik.uni-freiburg.de/lectures/optimierung_ochs/)

    @author Jan Bechtold, 2019 (bechtolj@cs.uni-freiburg.de)
"""

## Allgemeines zu Python (https://www.python.org/about/)
# 
# Python ist eine sehr populäre Programmiersprache, die für verschiedenste
# Anwendungsgebiete geeignet ist. Wie Matlab nutzt sie einen Interpreter, sodass
# Code ausgeführt werden kann, sobald er geschrieben wurde. Zudem gibt es für Python 
# eine riesige Toolbox, unter anderem mit Modulen zur (numerischen) Lösung
# mathematischer Probleme.
# Aufgrund der Popularität von Python gibt es eine Menge von Einführungen:
    # https://wiki.python.org/moin/BeginnersGuide/Programmers
    # https://www.w3schools.com/python/python_intro.asp
# die die grundlegenden Aspekte und Syntax der Sprache (Tab Indentation, keywords)
# abdecken. Für die Programmierung mit Python eignet sich nahezu jeder Editor
# und jedes Betriebssystem.
# Häufig genutzte Editoren und IDE's sind:
    # Sublime Text
    # Visual Studio Code
    # PyCharm (student license available)
    # Atom
    # Vim
    # Spyder
    # Jupyter Notebook (Schritt für Schritt Ausführung von Code)
# In dieser (sehr kurzen) Einführung liegt der Fokus auf der Verwendung von 
# Numpy und SciPy für Vektoren und Matrizen

# Module werden importiert und deren Namen optional mit 'as' abgekürzt
# Nicht-Standard Module müssen zuvor mit 'pip install <name>'
# oder 'conda install <name>' installiert werden.
import numpy as np

## Grundlegendes

# Variablen können direkt beschrieben werden
a = 1
print(a)

print()
print("------Matrix------")
# Definition einer 3x3 Matrix mit verschiedenen Datentypen
A = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # int
A = np.asarray([[1.0, 2, 3], [4, 5, 6], [7, 8, 9]]) # float, notice the point
print(A)
print(type(A)) # numpy array
print(A.dtype)
# Der Datentyp kann auch mit dtype festgelegt werden:
A = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32)
print(A.dtype)

# Definition der Matrix erfolgt mit geschachtelten Klammern.
print(A.shape)
# Kurzhilfe zu Funktionen erhält man von IDE's standardmäßig, bei fast allen
# Editoren als Plugin (auto-completion) oder via Suche der Dokumentation im Internet.
# Gängige Suchmaschinen helfen meist weiter.

print()
print("------Zugriffe------")
# Zugriffe auf die Matrix
print(A[1, 2])
# Zeigt Wert in 1. Reihe und 2. Spalte an
# Python beginnt also Indizierung bei 0 und nicht bei 1 (wie Matlab)

# Mit Hilfe des Doppelpunkts lassen sich Bereiche angeben, sogenannets slicing
# https://stackoverflow.com/questions/509211/understanding-slice-notation
print(A[0:2, 2])

# Ohne Anfangs- und Endwerte erhält man den gesamten Bereich
print(A[2, :])

print()
print("------Lineare Algebra------")
## Lineare Algebra
a = np.array([1, 2, 3]) # Vektor
M = np.array([[7, 0,  6],
              [0, 4,  0],
              [6, 0, -2]]) # Matrix

# In Python-Numpy funktionieren die Standardoperatoren element-weise.
B = M * a # ergibt eine 3 x 3 Matrix / Array, wohingegen
print(B)
b = M.dot(a) #  eine Matrix-Vektor-Multiplikation ist (3x3 * 3x1 -> 3x1)
print("b {}".format(b))
print()
# mehr Details und Varianten dazu hier:
# (https://stackoverflow.com/questions/21562986/numpy-matrix-vector-multiplication)

D = np.linalg.inv(M) # Inverse Matrix
print(D.dot(b)) # Ergibt wieder den Vektor a

(D, V) = np.linalg.eig(M) # Eigenvektoren V und Eigenwerte in D von M
idx = np.argsort(D) # negativ um aufsteigende indices zu erhalten
print(D)
D = D[idx]
V = V[:,idx]
print("D {}".format(D))
print("V {}".format(V))


# Transformation V, die M auf die Diagonalmatrix D abbildet
K = np.linalg.inv(V).dot(M).dot(V)
print("K {}".format(K))
print()
print("--Matrixprodukt--")
M1 = M.dot(M) # Matrixprodukt
print("M1 {}".format(M1))

print("--Hadamardprodukt--")
M2 = M*M # Hadamardprodukt (elementweise Multiplikation)
print("M2 {}".format(M2))

print("--Elementwise Division--")
M3 = M/M # Elementweise Division
print("M3 {}".format(M3))


## Erstellen von Diagrammen mit matplotlib (https://matplotlib.org/)
x = [1, 2, 3]
y = [1, 1, 2]

from matplotlib import pyplot as plt
plt.figure() # Öffnet neues Fenster
plt.plot(x, y) # Zeichnet ein Diagramm vom Typ Plot in das Fenster
plt.show()

## Besitzt Funktionen zur Bildverarbeitung
# (https://matplotlib.org/users/image_tutorial.html)

# Ermöglicht einfaches öffnen und anzeigen von Bildern
image = plt.imread('Lenna.png')
plt.figure()
plt.imshow(image)
plt.show()

# verwende nur jeden zweiten Pixel
img_half = image[::2, ::2]
img_by_eight = image[::8, ::8]

# Subplot ermöglich mehrere Diagramme in ein Fenster zu zeichnen
plt.subplot(1,3,1)
plt.imshow(image)
plt.subplot(1,3,2)
plt.imshow(img_half)
plt.subplot(1,3,3)
plt.imshow(img_by_eight)
plt.show()


## Strukturierung mit Hilfe von Funktionen lokal und in separaten Dateien

# Zur besseren Lesbarkeit und bei wiederholtem Bedarf verschiedener
# Abfolgen von Befehlen bietet sich das Anlegen von Funktionen an
def my_local_func(arg):
    """ docstring for documentation
        use tab indentation for everything that happens in the function"""
    local_variable = "my local string"
    return local_variable

# Funktionen können ebenfalls in seperaten Dateien definiert werden und
# dann hier verwendet werden
from helper import my_square_function

# Definition einer Funktion in einer separaten Datei siehe: helper.py
plt.figure('my square function')
square, grad = my_square_function([1, 2, 3, 4])
plt.plot([1, 2, 3, 4], square)
plt.show()

# Contour plot einer zweidimensionalen Funktion und deren Gradient
# Für einfache Funktionen bietet sich auch folgende Art der Definition an:
my_func = lambda x1,x2: x1**2 + x1 * x2
my_gradn = lambda x1,x2: np.array([2*x1 + x2, x1])

x1_range = np.linspace(-5, 5, 20)
x2_range = np.linspace(-5, 5, 20)

X1, X2 = np.meshgrid(x1_range, x2_range)
func_values = my_func(X1, X2)
grad_values = my_gradn(X1.flatten(), X2.flatten())

print(grad_values.shape)

plt.contour(X1, X2, func_values)
plt.quiver(X1, X2, grad_values[0,:], grad_values[1,:])
plt.show()



## Programmierstrukturen

# For - Schleife und Bedingung
for i in range(1, 3):  # 1:3 steht für alle Zahlen zwischen 1 und 3 mit der Schrittweite 1
    r = np.random.rand()
    print('Zufallszahl {:.2f}'.format(r), end = '')
    
    if r > 0.5:
        print(' ist groeßer als 0.5')
    else:
        print(' ist kleiner als 0.5')


# While Schleife und Bedingung
cond = True
i = 0
while(cond):
    if i == 0:
        print('Fall 0')
        i = 2
    elif i == 1:
        print('Fall 1: Passiert nie!')
    elif i == 2:
        print('Fall 2')
        i = -1
    else:
        print('Nicht definierter Fall: Schleife wird beendet.')
        cond=False

print("Finished")