# Optimierungsvorlesung - Gradientenverfahren

## Aufgabe 1
### Setup
Für die Vorlesung benötigen wir die Python Bibliotheken
`matplotlib numpy scipy PIL`
Sie können diese entweder direkt mit `pip` installieren, oder eine Python Umgebung erstellen. Dafür haben Sie zwei Möglichkeiten `anaconda` und `virtual-environment`. Diese sind besonders sinnvoll wenn Sie Projekte haben, die unterschiedliche Python Versionen benötigen.

### Anaconda
Installieren Sie anaconda: https://docs.anaconda.com/anaconda/install/
auf Linux:
Erzeugen Sie eine neue Umgebung
```shell
conda create -n dev python=3.6
conda activate dev
```
(evtl auch: ```source activate dev```)

Jetzt ist Ihre Umgebung aktiv.
Alles was Sie jetzt mit conda oder pip installieren landet in dieser Umgebung.

Installieren der benötigten Pakete:
```shell
conda install matplotlib numpy scipy pillow
```

Beachten Sie, dass die `dev` Umgebung nach einem Neustart wieder aktiviert werden muss. Wenn Sie einen Editor / eine IDE benutzen, geben Sie die Conda Umgebung als build environment an, bzw den Pfad zur Python Binary in der Conda Umgebung. Hier ist eine Übersicht für Pycharm: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html

### Einführung
Arbeiten Sie die Datei PythonIntroduction durch.
Machen Sie sich mit der Syntax von Python vertraut. Recherchieren Sie insbesondere wie Sie die üblichen Operationen der linearen Algebra (z.B. Matrix-Vektor-Multiplikationen, inverse Matrizen, Eigenwertzerlegung) mit Hilfe von Numpy umsetzen können. Finden Sie heraus wie Sie Daten in Python mit Matplotlib visualisieren können (z.B. pyplot). Schauen Sie sich außerdem die Dokumentation von dem Scipy Optimierungsmodul an (https://docs.scipy.org/doc/scipy/reference/optimize.html). Auf die Funktionalität der Toolbox werden wir in späteren Übungen noch zurückkommen.

**Referenzen:**
- Python:
```python
import scipy.optimize
print("Optimization Toolbox:")
help(scipy.optimize) # uncomment for a long info
print("More info at: https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html")
```
- Matlab (as reference):
`help optimtool`
http://de.mathworks.com/products/optimization/


## Aufgabe 2
Minimieren Sie die Funktion:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\frac{1}{2}x^4&space;&plus;&space;2x^3&space;-&space;3x&space;-&space;4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\frac{1}{4}x^4&space;&plus;&space;2x^3&space;-&space;3x&space;-&space;4" title="f(x) = \frac{1}{4}x^4 + 2x^3 - 3x - 4" /></a>

- Visualisieren Sie die Funktion. Ist sie konvex?
- Berechnen Sie den Gradienten.
- Optimieren Sie die Funktion mit Gradientenabstieg. Benutzen Sie den zuvor analytisch berechneten Gradienten in der Implementierung. Verwenden Sie bitte Ihre eigene Implementierung und keine Funktion aus der Optimization Toolbox. Probieren Sie verschiedene Startpunkte aus. Implementieren Sie Backtracking Line Search zur Bestimmung der Schrittweite.
- Visualisieren Sie, was während der Optimierung geschieht. Für diese 1D-Funktion geht dies sehr schön, bei hochdimensionalen Problemen aus der Praxis nicht mehr.

## Aufgabe 3
Minimieren Sie die zweidimensionale Funktion:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x1,&space;x2)&space;=&space;2x^{2}_{1}&space;&plus;&space;2x^{2}_{2}&space;&plus;&space;3x_{1}x_2&space;-&space;x_1&space;&plus;&space;x_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x1,&space;x2)&space;=&space;2x^{2}_{1}&space;&plus;&space;2x^{2}_{2}&space;&plus;&space;3x_{1}x_2&space;-&space;x_1&space;&plus;&space;x_2" title="f(x1, x2) = 2x^{2}_{1} + 2x^{2}_{2} + 3x_{1}x_2 - x_1 + x_2" /></a>

- Visualisieren Sie die Isolinien der Funktion mithilfe von contour. Ist die Funktion konvex?
- Berechnen Sie den Gradienten.
- Optimieren Sie die Funktion mit Gradientenabstieg. Verwenden Sie bitte Ihre eigene Implementierung.
- Optimieren Sie die Funktion analytisch. Stimmt Ihre numerische Lösung mit dem Minimum überein?

##

Implementieren Sie dabei alle Stub-Methoden definiert in `ex2.py` und `ex3.py`.
