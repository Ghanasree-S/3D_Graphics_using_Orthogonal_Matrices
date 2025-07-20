import pygame
import numpy as np
from math import cos, sin, sqrt

# Colors
WHITE, RED, BLACK = (255, 255, 255), (255, 0, 0), (0, 0, 0)

# Screen setup
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D Projection in Pygame")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Settings
scale = 100
circle_pos = [WIDTH / 2, HEIGHT / 2]
angle = 0
points, projected_points = [], []

# Projection matrix
projection_matrix = np.array([[1, 0, 0], [0, 1, 0]])

# Rotation matrices
def get_rotation_matrices(a):
    return (
        np.array([[1, 0, 0], [0, cos(a), -sin(a)], [0, sin(a), cos(a)]]),
        np.array([[cos(a), 0, sin(a)], [0, 1, 0], [-sin(a), 0, cos(a)]]),
        np.array([[cos(a), -sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1]])
    )

# Connect two points
def connect_points(i, j):
    pygame.draw.line(screen, BLACK, projected_points[i], projected_points[j], 1)

# Shape drawer
def draw_shape():
    global projected_points
    rx, ry, rz = get_rotation_matrices(angle)
    projected_points = []

    for point in points:
        rotated = rz @ point.reshape(3, 1)
        rotated = ry @ rotated
        rotated = rx @ rotated
        projected = projection_matrix @ rotated
        x = int(projected[0][0] * scale + circle_pos[0])
        y = int(projected[1][0] * scale + circle_pos[1])
        projected_points.append((x, y))
        pygame.draw.circle(screen, RED, (x, y), 5)

# Cube
def cube():
    global points
    points = [np.array([x, y, z])
              for x in [-1, 1] for y in [-1, 1] for z in [-1, 1]]
    draw_shape()
    for i in range(4):
        connect_points(i, (i + 1) % 4)
        connect_points(i + 4, ((i + 1) % 4) + 4)
        connect_points(i, i + 4)

# Pyramid
def pyramid():
    global points
    points = [
        np.array([-1, -1, 1]), np.array([1, -1, 1]),
        np.array([1, 1, 1]), np.array([-1, 1, 1]),
        np.array([0, 0, 2])
    ]
    draw_shape()
    for i in range(4):
        connect_points(i, (i + 1) % 4)
        connect_points(i, 4)

# Rectangular Prism
def rectangular_prism():
    global points
    points = [np.array([x, y, z])
              for x in [-1, 1] for y in [-1, 1] for z in [-1, 1]]
    draw_shape()
    for i in range(4):
        connect_points(i, (i + 1) % 4)
        connect_points(i + 4, ((i + 1) % 4) + 4)
        connect_points(i, i + 4)

# Tetrahedron
def tetrahedron():
    global points
    points = [
        np.array([0, 1, 0]),
        np.array([1, -1, -1]),
        np.array([-1, -1, -1]),
        np.array([1, -1, 1]),
        np.array([-1, -1, 1])
    ]
    draw_shape()
    for i in range(1, 5):
        connect_points(0, i)
        connect_points(i, ((i % 4) + 1))

# Octahedron
def octahedron():
    global points
    points = [
        np.array([0, 1, 0]),
        np.array([1, 0, 0]),
        np.array([0, 0, -1]),
        np.array([-1, 0, 0]),
        np.array([0, 0, 1]),
        np.array([0, -1, 0])
    ]
    draw_shape()
    for i in range(1, 5):
        connect_points(0, i)
        connect_points(i, 5)

# Dodecahedron
def dodecahedron():
    global points
    phi = (1 + sqrt(5)) / 2
    points = [np.array(p) for p in [
        [0, 1, phi], [0, -1, phi], [0, 1, -phi], [0, -1, -phi],
        [1, phi, 0], [-1, phi, 0], [1, -phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [-phi, 0, 1], [phi, 0, -1], [-phi, 0, -1]
    ]]
    draw_shape()
    edges = [
        (0, 1), (0, 4), (0, 5), (1, 6), (2, 3), (2, 7), (3, 8),
        (4, 9), (5, 10), (5, 11), (6, 8), (6, 11), (7, 9), (7, 10),
        (8, 10), (9, 11)
    ]
    for i, j in edges:
        connect_points(i, j)

# Icosahedron
def icosahedron():
    global points
    phi = (1 + sqrt(5)) / 2
    points = [np.array(p) for p in [
        [0, 1, phi], [0, -1, phi], [0, 1, -phi], [0, -1, -phi],
        [1, phi, 0], [-1, phi, 0], [1, -phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [-phi, 0, 1], [phi, 0, -1], [-phi, 0, -1]
    ]]
    draw_shape()
    edges = [
        (0, 1), (0, 4), (0, 5), (1, 6), (2, 3), (2, 7), (3, 8),
        (4, 9), (5, 10), (5, 11), (6, 8), (6, 11), (7, 9), (7, 10),
        (8, 10), (9, 11)
    ]
    for i, j in edges:
        connect_points(i, j)

# Main loop
def main():
    global angle
    pygame.init()
    clock = pygame.time.Clock()
    shapes = {
        '1': cube, '2': pyramid, '3': rectangular_prism,
        '4': tetrahedron, '5': octahedron, '6': dodecahedron, '7': icosahedron
    }

    while True:
        clock.tick(60)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return

        print("\nChoose a 3D shape to display:")
        for key, shape in shapes.items():
            print(f"{key}. {shape.__name__.replace('_', ' ').title()}")
        print("Press 'Esc' in the window to quit.")

        choice = input("Your choice: ").strip()
        if choice in shapes:
            shapes[choice]()
        else:
            print("Invalid choice. Try again.")

        angle += 0.01
        pygame.display.update()

if __name__ == "__main__":
    main()
