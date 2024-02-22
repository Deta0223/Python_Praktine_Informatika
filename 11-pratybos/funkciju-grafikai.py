# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:22:05 2023

@author: Deivydas
"""

import numpy as np
import matplotlib.pyplot as  plt


def f1(x):
    return 1/(np.cbrt(x))
    
def f2(x):
    return 1/x

def f3(x):
    return 1/(x*x)

X = np.linspace(-6, 6, 1000) 
Y = np.sin(X*X)


plt.title(r"$f \left(x \right) = \sin \left(x^{2} \right)$")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X, Y, linestyle=":")
plt.savefig("sin.pdf")
plt.show()
plt.close()

X = np.linspace(-5, 5, 50001)
Y = f1(X)
plt.xlim(-5, 5)
plt.ylim(-15, 15)
plt.plot(X, Y, label = r"$f_{1} \left(x\right) = \frac{1}{\sqrt[3]{x}} $")
Y=f2(X)
plt.plot(X, Y, linestyle="--", label = r"$f_{2} \left(x\right) = \frac{1}{x} $")
Y=f3(X)
plt.plot(X, Y, linestyle=":", label = r"$f_{3} \left(x\right) = \frac{1}{x^2} $")
plt.title("Hiperbolės")
plt.legend(loc = "upper right")
plt.savefig("grafikas.pdf")
plt.show()