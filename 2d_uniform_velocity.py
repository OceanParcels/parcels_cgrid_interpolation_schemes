#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on December 1 2018

@author: Philippe Delandmeter

Master file interpolating a 2D uniform velocity in an unstructured quadrilateral
"""


import numpy as np
import hexahedra_utils as h_u
import interpolation_utils as i_u

x = [0, 2, 1.5, .4]
y = [0, -.5, .5, .8]

xsi = .3
eta = .6
globVel = [1.,1.]

u0 = h_u.get_edgeNormalVelocity(globVel, x, y, [0,3])
u0 = 2
U0 = u0 * i_u.length2d_lin_edge(x, y, [0,3])
u1 = h_u.get_edgeNormalVelocity(globVel, x, y, [1,2])
U1 = u1 * i_u.length2d_lin_edge(x, y, [1,2])
v0 = h_u.get_edgeNormalVelocity(globVel, x, y, [1,0])
V0 = v0 * i_u.length2d_lin_edge(x, y, [1,0])
v1 = h_u.get_edgeNormalVelocity(globVel, x, y, [2,3])
V1 = v1 * i_u.length2d_lin_edge(x, y, [2,3])

V1 = U0+V0-U1
v1 = V1 / i_u.length2d_lin_edge(x, y, [2,3])
print U0+V0-U1-V1
print v1

jac = i_u.jacobian2D_lin(x, y, xsi, eta)
dxsidt = i_u.interpolate(i_u.phi1D_lin, [U0, U1], xsi) / jac
detadt = i_u.interpolate(i_u.phi1D_lin, [V0, V1], eta) / jac

dphidxsi, dphideta = i_u.dphidxsi2D_lin(xsi, eta)

u = np.dot(dphidxsi, x) * dxsidt + np.dot(dphideta, x) * detadt 
v = np.dot(dphidxsi, y) * dxsidt + np.dot(dphideta, y) * detadt 
print 'uv analytical', u, v

assert np.allclose([u,v], globVel)
