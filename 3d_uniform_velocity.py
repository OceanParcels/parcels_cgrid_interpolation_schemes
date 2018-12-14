#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on December 1 2018

@author: Philippe Delandmeter

Master file interpolating a 3D uniform velocity in an unstructured hexahedra
"""


import numpy as np
import hexahedra_utils as h_u
import interpolation_utils as i_u

x_in = [0, 2, 1.5, .4]
y_in = [0, -.5, .5, .8]
z_in = [-1, -.6, -.9, 1, 1.5, .8]
x, y, z = h_u.generate_extrudedPlanarHexahedra(x_in, y_in, z_in)
z = [0, 0, 0, 0, 1, 1, 1, 1]

xsi = .3
eta = .6
zet = .5
globVel = [1,1,1]

u0 = h_u.get_faceNormalVelocity(globVel, x, y, z, [0,3,7,4])
u0 = 2
U0 = u0 * i_u.jacobian3D_lin_face(x, y, z, 0, eta, zet, 'zonal')
u1 = h_u.get_faceNormalVelocity(globVel, x, y, z, [1,2,6,5])
U1 = u1 * i_u.jacobian3D_lin_face(x, y, z, 1, eta, zet, 'zonal')
v0 = h_u.get_faceNormalVelocity(globVel, x, y, z, [0,4,5,1])
V0 = v0 * i_u.jacobian3D_lin_face(x, y, z, xsi, 0, zet, 'meridional')
v1 = h_u.get_faceNormalVelocity(globVel, x, y, z, [3,7,6,2])
v1 = 2.44598710041
V1 = v1 * i_u.jacobian3D_lin_face(x, y, z, xsi, 1, zet, 'meridional')
w0 = h_u.get_faceNormalVelocity(globVel, x, y, z, [0,1,2,3])
W0 = w0 * i_u.jacobian3D_lin_face(x, y, z, xsi, eta, 0, 'vertical')
w1 = h_u.get_faceNormalVelocity(globVel, x, y, z, [4,5,6,7])
W1 = w1 * i_u.jacobian3D_lin_face(x, y, z, xsi, eta, 1, 'vertical')

# Computing fluxes in half left hexahedron -> flux_u05
xx = [x[0], (x[0]+x[1])/2, (x[2]+x[3])/2, x[3], x[4], (x[4]+x[5])/2, (x[6]+x[7])/2, x[7]]
yy = [y[0], (y[0]+y[1])/2, (y[2]+y[3])/2, y[3], y[4], (y[4]+y[5])/2, (y[6]+y[7])/2, y[7]]
zz = [z[0], (z[0]+z[1])/2, (z[2]+z[3])/2, z[3], z[4], (z[4]+z[5])/2, (z[6]+z[7])/2, z[7]]
flux_u0 = u0 * i_u.jacobian3D_lin_face(xx, yy, zz, 0, .5, .5, 'zonal')
flux_v0_halfx = v0 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, 0, .5, 'meridional')
flux_v1_halfx = v1 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, 1, .5, 'meridional')
flux_w0_halfx = w0 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, .5, 0, 'vertical')
flux_w1_halfx = w1 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, .5, 1, 'vertical')
flux_u05 = flux_u0 + flux_v0_halfx - flux_v1_halfx + flux_w0_halfx - flux_w1_halfx

# Computing fluxes in half front hexahedron -> flux_v05
xx = [x[0], x[1], (x[1]+x[2])/2, (x[0]+x[3])/2, x[4], x[5], (x[5]+x[6])/2, (x[4]+x[7])/2]
yy = [y[0], y[1], (y[1]+y[2])/2, (y[0]+y[3])/2, y[4], y[5], (y[5]+y[6])/2, (y[4]+y[7])/2]
zz = [z[0], z[1], (z[1]+z[2])/2, (z[0]+z[3])/2, z[4], z[5], (z[5]+z[6])/2, (z[4]+z[7])/2]
flux_u0_halfy = u0 * i_u.jacobian3D_lin_face(xx, yy, zz, 0, .5, .5, 'zonal')
flux_u1_halfy = u1 * i_u.jacobian3D_lin_face(xx, yy, zz, 1, .5, .5, 'zonal')
flux_v0 = v0 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, 0, .5, 'meridional')
flux_w0_halfy = w0 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, .5, 0, 'vertical')
flux_w1_halfy = w1 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, .5, 1, 'vertical')
flux_v05 = flux_u0_halfy - flux_u1_halfy + flux_v0 + flux_w0_halfy - flux_w1_halfy

# Computing fluxes in half lower hexahedron -> flux_w05
xx = [x[0], x[1], x[2], x[3], (x[0]+x[4])/2, (x[1]+x[5])/2, (x[2]+x[6])/2, (x[3]+x[7])/2]
yy = [y[0], y[1], y[2], y[3], (y[0]+y[4])/2, (y[1]+y[5])/2, (y[2]+y[6])/2, (y[3]+y[7])/2]
zz = [z[0], z[1], z[2], z[3], (z[0]+z[4])/2, (z[1]+z[5])/2, (z[2]+z[6])/2, (z[3]+z[7])/2]
flux_u0_halfz = u0 * i_u.jacobian3D_lin_face(xx, yy, zz, 0, .5, .5, 'zonal')
flux_u1_halfz = u1 * i_u.jacobian3D_lin_face(xx, yy, zz, 1, .5, .5, 'zonal')
flux_v0_halfz = v0 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, 0, .5, 'meridional')
flux_v1_halfz = v1 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, 1, .5, 'meridional')
flux_w0 = w0 * i_u.jacobian3D_lin_face(xx, yy, zz, .5, .5, 0, 'vertical')
flux_w05 = flux_u0_halfz - flux_u1_halfz + flux_v0_halfz - flux_v1_halfz + flux_w0

surf_u05 = i_u.jacobian3D_lin_face(x, y, z, .5, .5, .5, 'zonal')
jac_u05 = i_u.jacobian3D_lin_face(x, y, z, .5, eta, zet, 'zonal')
U05 = flux_u05 / surf_u05 * jac_u05

surf_v05 = i_u.jacobian3D_lin_face(x, y, z, .5, .5, .5, 'meridional')
jac_v05 = i_u.jacobian3D_lin_face(x, y, z, xsi, .5, zet, 'meridional')
V05 = flux_v05 / surf_v05 * jac_v05

surf_w05 = i_u.jacobian3D_lin_face(x, y, z, .5, .5, .5, 'vertical')
jac_w05 = i_u.jacobian3D_lin_face(x, y, z, xsi, eta, .5, 'vertical')
W05 = flux_w05 / surf_w05 * jac_w05

jac = i_u.jacobian3D_lin(x, y, z, xsi, eta, zet)
dxsidt = i_u.interpolate(i_u.phi1D_quad, [U0, U05, U1], xsi) / jac
detadt = i_u.interpolate(i_u.phi1D_quad, [V0, V05, V1], eta) / jac
dzetdt = i_u.interpolate(i_u.phi1D_quad, [W0, W05, W1], zet) / jac

dphidxsi, dphideta, dphidzet = i_u.dphidxsi3D_lin(xsi, eta, zet)

u = np.dot(dphidxsi, x) * dxsidt + np.dot(dphideta, x) * detadt + np.dot(dphidzet, x) * dzetdt 
v = np.dot(dphidxsi, y) * dxsidt + np.dot(dphideta, y) * detadt + np.dot(dphidzet, y) * dzetdt 
w = np.dot(dphidxsi, z) * dxsidt + np.dot(dphideta, z) * detadt + np.dot(dphidzet, z) * dzetdt 
print 'uvw analytical', u, v, w

assert np.allclose([u, v, w], globVel)
