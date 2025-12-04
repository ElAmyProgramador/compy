from .complejos import Complejo
import matplotlib.pyplot as plt

def graficar(z : Complejo):
    plt.axhline(0, color = "black", lw = 0.5)
    plt.axvline(0, color = "black", lw = 0.5)
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.grid(True)
    plt.axis("equal")
    plt.scatter(z.real, z.imag, s = 120)
    plt.text(z.real, z.imag, f"{z}")
    plt.show()

def graficar_array(array):
    xs = [z.real for z in array]
    ys = [z.imag for z in array]
    plt.axhline(0, color = "black", lw = 0.5)
    plt.axvline(0, color = "black", lw = 0.5)
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.axis("equal")
    plt.grid(True)
    plt.scatter(xs, ys)
    for z in array:
        plt.text(z.real, z.imag, f"{z}")
    plt.show()
