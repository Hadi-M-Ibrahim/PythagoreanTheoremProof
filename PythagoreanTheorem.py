import matplotlib.pyplot as plt
import numpy as np

def PythagoreanTheorem(a, b):
    c = np.sqrt(a**2 + b**2)
    angle = np.arctan2(b, a)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    triangle = np.array([[0, 0], [a, 0], [0, b], [0, 0]])
    ax.plot(triangle[:, 0], triangle[:, 1], 'blue')

    ax.text(a / 2, -0.3, f'a = {a}', fontsize=12, ha='center')
    ax.text(-0.3, b / 2, f'b = {b}', fontsize=12, va='center', rotation=90)
    ax.text((a / 2) + .22 , (b / 2) - 0.5, f'c = {c:.2f}', fontsize=12, ha='center', rotation= -(angle * 180 / np.pi))

    squareA = np.array([[0, 0], [a, 0], [a, -a], [0, -a], [0, 0]])
    squareB = np.array([[0, 0], [0, b], [-b, b], [-b, 0], [0, 0]])

    squareC = np.array([
        [0, 0], 
        [c, 0], 
        [c, c], 
        [0, c],
        [0, 0]
    ])
    rotationMatrix = np.array([
        [np.cos(angle), -np.sin(angle)], 
        [np.sin(angle), np.cos(angle)]
    ])
    squareC = squareC @ rotationMatrix
    squareC += np.array([a, 0])
    constantOffset = c / 2
    hypotenuseMidpoint = np.array([a / 2, b / 2])
    squareCCenter = np.mean(squareC[:4], axis=0)
    translationVector = hypotenuseMidpoint - squareCCenter + constantOffset
    squareC += translationVector

    ax.plot(squareA[:, 0], squareA[:, 1], 'red')
    ax.plot(squareB[:, 0], squareB[:, 1], 'green')
    ax.plot(squareC[:, 0], squareC[:, 1], 'orange')

    ax.fill(squareA[:, 0], squareA[:, 1], 'red', alpha=0.3)
    ax.fill(squareB[:, 0], squareB[:, 1], 'green', alpha=0.3)
    ax.fill(squareC[:, 0], squareC[:, 1], 'orange', alpha=0.3)

    ax.text(a / 2, -a / 2, 'a²', fontsize=12, ha='center', color='red')
    ax.text(-b / 2, b / 2, 'b²', fontsize=12, ha='center', color='green')
    ax.text((squareC[0, 0] + squareC[2, 0]) / 2, (squareC[0, 1] + squareC[2, 1]) / 2, 'c²', fontsize=12, ha='center', color='orange')

    ax.axis('off')

    plt.title("Pythagorean Theorem")
    plt.show()

a = int(input("Enter a value for side A: "))
b = int(input("Enter a value for side B: "))
PythagoreanTheorem(a, b)
