
This repository contains a minimalist version of C-grid interpolation schemes for:
* a general quadrilateral (2D)
* a hexahedron resulting from a vertical quadrilateral extrusion with planar faces (3D)

Two master files: `2d_uniform_velocity.py` and `3d_uniform_velocity.py` compute the velocity at a point inside the cell, depending on the cell vertices, the point relative location and the velocities at the cell edges (2D) or faces (3D).

In the current version, the velocities at the cell edges/faces correspond to a uniform velocity and the code asserts that this uniform velocity is correctly interpolated.

The code reproduces the interpolation schemes for C-grids in Parcels v2.0.0 (http://oceanparcels.org).
