import numpy as np

def phi1D_lin(xsi):
    phi = [1-xsi,
           xsi]

    return phi


def phi1D_quad(xsi):
    phi = [2*xsi**2-3*xsi+1,
           -4*xsi**2+4*xsi,
           2*xsi**2-xsi]

    return phi


def phi3D_lin(xsi, eta, zet):
    phi = [(1-xsi) * (1-eta) * (1-zet),
              xsi  * (1-eta) * (1-zet),
              xsi  *    eta  * (1-zet),
           (1-xsi) *    eta  * (1-zet),
           (1-xsi) * (1-eta) *    zet ,
              xsi  * (1-eta) *    zet ,
              xsi  *    eta  *    zet ,
           (1-xsi) *    eta  *    zet ]

    return phi


def dphidxsi3D_lin(xsi, eta, zet):
    dphidxsi = [ - (1-eta) * (1-zet),
                   (1-eta) * (1-zet),
                   (  eta) * (1-zet),
                 - (  eta) * (1-zet),
                 - (1-eta) * (  zet),
                   (1-eta) * (  zet),
                   (  eta) * (  zet),
                 - (  eta) * (  zet)]
    dphideta = [ - (1-xsi) * (1-zet),
                 - (  xsi) * (1-zet),
                   (  xsi) * (1-zet),
                   (1-xsi) * (1-zet),
                 - (1-xsi) * (  zet),
                 - (  xsi) * (  zet),
                   (  xsi) * (  zet),
                   (1-xsi) * (  zet)]
    dphidzet = [ - (1-xsi) * (1-eta),
                 - (  xsi) * (1-eta),
                 - (  xsi) * (  eta),
                 - (1-xsi) * (  eta),
                   (1-xsi) * (1-eta),
                   (  xsi) * (1-eta),
                   (  xsi) * (  eta),
                   (1-xsi) * (  eta)]

    return dphidxsi, dphideta, dphidzet


def dxdxsi3D_lin(hexa_x, hexa_y, hexa_z, xsi, eta, zet):
    dphidxsi, dphideta, dphidzet = dphidxsi3D_lin(xsi, eta, zet)

    dxdxsi = np.dot(hexa_x, dphidxsi)
    dxdeta = np.dot(hexa_x, dphideta)
    dxdzet = np.dot(hexa_x, dphidzet)
    dydxsi = np.dot(hexa_y, dphidxsi)
    dydeta = np.dot(hexa_y, dphideta)
    dydzet = np.dot(hexa_y, dphidzet)
    dzdxsi = np.dot(hexa_z, dphidxsi)
    dzdeta = np.dot(hexa_z, dphideta)
    dzdzet = np.dot(hexa_z, dphidzet)

    return dxdxsi, dxdeta, dxdzet, dydxsi, dydeta, dydzet, dzdxsi, dzdeta, dzdzet


def jacobian3D_lin(hexa_x, hexa_y, hexa_z, xsi, eta, zet):
    dxdxsi, dxdeta, dxdzet, dydxsi, dydeta, dydzet, dzdxsi, dzdeta, dzdzet = dxdxsi3D_lin(hexa_x, hexa_y, hexa_z, xsi, eta, zet)

    jac = dxdxsi * (dydeta*dzdzet - dzdeta*dydzet)\
        - dxdeta * (dydxsi*dzdzet - dzdxsi*dydzet)\
        + dxdzet * (dydxsi*dzdeta - dzdxsi*dydeta)
    if jac < 0:
        print 'bou'
    return abs(jac)


def jacobian3D_lin_face(hexa_x, hexa_y, hexa_z, xsi, eta, zet, orientation):
    dxdxsi, dxdeta, dxdzet, dydxsi, dydeta, dydzet, dzdxsi, dzdeta, dzdzet = dxdxsi3D_lin(hexa_x, hexa_y, hexa_z, xsi, eta, zet)

    if orientation is 'zonal':
        j = [dydeta*dzdzet-dydzet*dzdeta,
            -dxdeta*dzdzet+dxdzet*dzdeta,
             dxdeta*dydzet-dxdzet*dydeta]
    elif orientation is 'meridional':
        j = [dydxsi*dzdzet-dydzet*dzdxsi,
            -dxdxsi*dzdzet+dxdzet*dzdxsi,
             dxdxsi*dydzet-dxdzet*dydxsi]
    elif orientation is 'vertical':
        j = [dydxsi*dzdeta-dydeta*dzdxsi,
            -dxdxsi*dzdeta+dxdeta*dzdxsi,
             dxdxsi*dydeta-dxdeta*dydxsi]

    jac = np.sqrt(j[0]**2+j[1]**2+j[2]**2)
    return jac


def dphidxsi2D_lin(xsi, eta):
    dphidxsi = [-(1-eta),
                  1-eta,
                    eta,
                -   eta]
    dphideta = [-(1-xsi),
                -   xsi,
                    xsi,
                  1-xsi]

    return dphidxsi, dphideta


def dxdxsi2D_lin(quad_x, quad_y, xsi, eta,):
    dphidxsi, dphideta = dphidxsi2D_lin(xsi, eta)

    dxdxsi = np.dot(quad_x, dphidxsi)
    dxdeta = np.dot(quad_x, dphideta)
    dydxsi = np.dot(quad_y, dphidxsi)
    dydeta = np.dot(quad_y, dphideta)

    return dxdxsi, dxdeta, dydxsi, dydeta


def jacobian2D_lin(quad_x, quad_y, xsi, eta):
    dxdxsi, dxdeta, dydxsi, dydeta = dxdxsi2D_lin(quad_x, quad_y, xsi, eta)

    jac = dxdxsi*dydeta - dxdeta*dydxsi
    return jac


def length2d_lin_edge(quad_x, quad_y, ids):
    xe = [quad_x[ids[0]], quad_x[ids[1]]]
    ye = [quad_y[ids[0]], quad_y[ids[1]]]
    return np.sqrt((xe[1]-xe[0])**2+(ye[1]-ye[0])**2)


def interpolate(phi, f, xsi):
    return np.dot(phi(xsi), f)
