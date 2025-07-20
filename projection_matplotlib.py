import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def initial():
    # Initial plot
    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    return fig, ax1

def rotated(vertices, R_y):
    # Apply rotation to all vertices
    rotated_vertices = np.dot(vertices, R_y.T)
    ax2 = fig.add_subplot(122, projection='3d')
    return ax2, rotated_vertices

def cube():
    # Define the cube's vertices
    vertices = np.array([
        [1, 1, 1], [1, 1, -1],
        [1, -1, 1], [1, -1, -1],
        [-1, 1, 1], [-1, 1, -1],
        [-1, -1, 1], [-1, -1, -1]
    ])
    return vertices

def pyramid():
    # Define the pyramid's vertices
    vertices = np.array([
        [1, 1, 1], [-1, 1, 1], [-1, -1, 1],
        [1, -1, 1], [0, 0, -1]
    ])  # Apex of the pyramid
    return vertices

def tetrahedron():
    # Define the tetrahedron's vertices
    vertices = np.array([[1, 1, 1],[-1, -1, 1],
    [1, -1, -1],[-1, 1, -1]])
    return vertices

def octahedron():
    # Define the octahedron's vertices
    vertices = np.array([[1, 0, 0],[-1, 0, 0],
    [0, 1, 0],[0, -1, 0],[0, 0, 1],[0, 0, -1]])
    return vertices

def dodecahedron():
    # Define the dodecahedron's vertices
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    vertices = np.array([[-1, -1, -1],[1, -1, -1],
    [1, 1, -1],[-1, 1, -1],[0, -1/phi, -phi],
    [0, 1/phi, -phi],[-1/phi, -phi, 0],
    [1/phi, -phi, 0],[1/phi, phi, 0],
    [-1/phi, phi, 0],[0, -1/phi, phi],
    [0, 1/phi, phi],[-1, -1, 1],
    [1, -1, 1],[1, 1, 1],[-1, 1, 1]])
    return vertices

def icosahedron():
    # Define the icosahedron's vertices
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    vertices = np.array([[0, 1, phi],[0, -1, phi],
    [0, 1, -phi],[0, -1, -phi],[1, phi, 0],
    [-1, phi, 0],[1, -phi, 0],[-1, -phi, 0],
    [phi, 0, 1],[-phi, 0, 1],[phi, 0, -1],[-phi, 0, -1]])
    return vertices

def plot(ax, vertices, title):
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Rotation matrix for y-axis
angle = np.radians(45)
R_y = np.array([
    [np.cos(angle), 0, np.sin(angle)],
    [0, 1, 0],
    [-np.sin(angle), 0, np.cos(angle)]
])

# User input
ch = int(input("1)Pyramid\n 2)Cube\n 3)Tetrahedron\n 4)Octahedron\n 5)Dodecahedron\n 6)Icosahedron\n Enter your choice:\n "))

if ch == 1:
    vertices = pyramid()
    fig, ax1 = initial()
    plot(ax1, vertices, 'Original Pyramid')
    
    ax2, rotated_vertices = rotated(vertices, R_y)
    plot(ax2, rotated_vertices, 'Rotated Pyramid')

elif ch == 2:
    vertices = cube()
    fig, ax1 = initial()
    plot(ax1, vertices, 'Original Cube')
    
    ax2, rotated_vertices = rotated(vertices, R_y)
    plot(ax2, rotated_vertices, 'Rotated Cube')

elif ch==3:
    vertices = tetrahedron()
    fig, ax1 = initial()
    plot(ax1, vertices, 'Original Tetrahedron')
    
    ax2, rotated_vertices = rotated(vertices, R_y)
    plot(ax2, rotated_vertices, 'Rotated Tetrahedron')

elif ch==4:
    vertices = octahedron()
    fig, ax1 = initial()
    plot(ax1, vertices, 'Original Octahedron')
    
    ax2, rotated_vertices = rotated(vertices, R_y)
    plot(ax2, rotated_vertices, 'Rotated Octahedron')

elif ch==5:
    vertices = dodecahedron()
    fig, ax1 = initial()
    plot(ax1, vertices, 'Original Dodecahedron')
    
    ax2, rotated_vertices = rotated(vertices, R_y)
    plot(ax2, rotated_vertices, 'Rotated Dodecahedron')

elif ch==6:
    vertices = icosahedron()
    fig, ax1 = initial()
    plot(ax1, vertices, 'Original Icosahedron')
    
    ax2, rotated_vertices = rotated(vertices, R_y)
    plot(ax2, rotated_vertices, 'Rotated Icosahedron')

plt.show()
