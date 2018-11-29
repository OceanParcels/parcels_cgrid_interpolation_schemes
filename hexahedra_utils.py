import numpy as np


def generate_extrudedPlanarHexahedra(x_in, y_in, z_in):
    """Function generating an extruded hexahedra containing only planar faces.
    By extruded hexahedra, we mean that x and y coordinates of first four nodes are the same as next four ones,
    as it is often the case in oceanography meshes.
    The order of the nodes of the hexahedra are the following.

       7 +--------+ 6
        /        /|
       /        / |
    4 +--------+ 5|
      |        |  |
      |   3    |  + 2
      |        | /
      |        |/
    0 +--------+ 1

    :param x_in: list of x coordinates of the first 4 nodes [x_0, x_1, x_2, x_3].
    :param y_in: list of y coordinates of the first 4 nodes [y_0, y_1, y_2, y_3].
    :param z_in: list of z coordinates of nodes [z_0, z_1, z_2, z_4, z_5, z_6].
    """

    assert isinstance(x_in, list)
    assert isinstance(y_in, list)
    assert isinstance(z_in, list)

    x = x_in + x_in
    y = y_in + y_in

    A = np.array([[x_in[1]-x_in[0], x_in[2]-x_in[0]],
                 [y_in[1]-y_in[0], y_in[2]-y_in[0]]])
    b = np.array([[x_in[3]-x_in[0]], [y_in[3]-y_in[0]]])
    param = np.linalg.solve(A, b)

    z3 = z_in[0] + param[0][0] * (z_in[1]-z_in[0]) + param[1][0] * (z_in[2]-z_in[0])
    z7 = z_in[3] + param[0][0] * (z_in[4]-z_in[3]) + param[1][0] * (z_in[5]-z_in[3])
    z = z_in[:3] + [z3] + z_in[3:] + [z7]
    return x, y, z


def get_faceNormalVelocity(vel, x, y, z, ids):
    """Compute the velocity normal to a hexahedra planar face.

    :param vel: velocity vector: [u,v,w]
    :param x: x coordinates of hexahedra
    :param y: y coordinates of hexahedra
    :param z: z coordinates of hexahedra
    :param ids: indices of the 4 face nodes
    """

    xf = [x[ids[0]], x[ids[1]], x[ids[2]], x[ids[3]]]
    yf = [y[ids[0]], y[ids[1]], y[ids[2]], y[ids[3]]]
    zf = [z[ids[0]], z[ids[1]], z[ids[2]], z[ids[3]]]

    v0 = [xf[1]-xf[0], yf[1]-yf[0], zf[1]-zf[0]]
    v1 = [xf[2]-xf[0], yf[2]-yf[0], zf[2]-zf[0]]
    n = np.zeros(3)
    n[0] =  v0[1]*v1[2] - v1[1]*v0[2]
    n[1] = -v0[0]*v1[2] + v1[0]*v0[2]
    n[2] =  v0[0]*v1[1] - v1[0]*v0[1]
    nn = np.sqrt(n[0]**2+n[1]**2+n[2]**2)
    n = n / nn
    return np.dot(n, vel)


def get_edgeNormalVelocity(vel, x, y, ids):
    """Compute the velocity normal to a quadrilateral linear edge (2D)..

    :param vel: velocity vector: [u,v]
    :param x: x coordinates of quadrilateral
    :param y: y coordinates of quadrilateral
    :param ids: indices of the 2 edge nodes
    """

    xe = [x[ids[0]], x[ids[1]]]
    ye = [y[ids[0]], y[ids[1]]]
    n = np.zeros(2)
    n[0] =  (ye[1]-ye[0])
    n[1] = -(xe[1]-xe[0])
    nn = np.sqrt(n[0]**2+n[1]**2)
    n = n / nn
    return np.dot(n, vel)
