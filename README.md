<div align="center">

# 🧊 3D Graphics Using Orthogonal Matrices

**Rendering and rotating 3D solids from scratch with linear algebra: orthogonal rotation matrices and orthographic projection, in Matplotlib and Pygame.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-real--time-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)

</div>

---

## 📌 Overview

The project shows how 3D graphics work underneath any engine. Every frame is computed with matrix multiplication:

$$
\mathbf{p}' = P \cdot R_x(\theta)\, R_y(\theta)\, R_z(\theta) \cdot \mathbf{p}
$$

- $R_x, R_y, R_z$ are **orthogonal rotation matrices** ($R^TR = I$, $\det R = 1$), so they preserve lengths and angles and the shape never distorts
- $P = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$ is an **orthographic projection** onto the screen plane

## 🔷 Supported Shapes

Cube · Pyramid · Tetrahedron · Octahedron · Dodecahedron · Icosahedron, each built from its vertex coordinates.

## 🖥️ Two Renderers

| File | Library | Use |
|---|---|---|
| `projection_pygame.py` | Pygame | Real-time interactive rotation |
| `projection_matplotlib.py` | Matplotlib | 3D plots for analysis and visualisation |

## 🚀 Run

```bash
pip install -r requirements.txt
python projection_pygame.py       # interactive
python projection_matplotlib.py   # plotted
```

Pick a shape from the menu:
```
1) Pyramid  2) Cube  3) Tetrahedron  4) Octahedron  5) Dodecahedron  6) Icosahedron
```

## 🧠 Concepts Covered

3D coordinate systems · orthogonal matrices · rotation about the X, Y and Z axes · vertex transformation · projection · edge connectivity

## 👩‍💻 Author

**Ghanasree S**: [GitHub](https://github.com/Ghanasree-S) · [LinkedIn](https://www.linkedin.com/in/ghanasree-s-88976b2b0)
