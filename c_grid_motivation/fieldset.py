import numpy as np


class FieldSet_C(object):
    def eval(self, t, x, y):
        if y > 1. or x > 1.:
            return (0, 0)
        if x < 0:
            x = x+1
            u = (1-x)*1+x*0
            v = (1-y)*0+y*1
        else:
            u = (1-x)*0+x*1
            v = (1-y)*0+y*(-1)
        return (u, v)


class FieldSet_A(object):
    def eval(self, t, x, y):
        if y > 1. or x > 1.:
            return (0, 0)
        if x < 0:
            x = x+1
            u = (1-x)*(1-y)*1+(1-x)*y*1
            v = x*y*1 + (1-x)*y*1
        else:
            u = x*(1-y)*1+x*y*1
            v = x*y*(-1)+(1-x)*y*(-1)
        return (u, v)


class FieldSet_CWrong(object):
    def eval(self, t, x, y):
        if y > 1. or x > 1.:
            return (0, 0)
        yv = y
        if x < -.5:
            xv = x+1.5
            v0=0; v1=0; v2=1; v3=1
        elif x < .5:
            xv = x+.5
            v0=0; v1=0; v2=-1; v3=1
        else:
            xv = x-.5
            v0=0; v1=0; v2=-1; v3=-1

        if y < .5 and x < 0:
            yu = y+.5
            xu = x+1
            u0=0; u1=0; u2=0; u3=1
        elif y < .5 and x >= 0:
            yu = y+.5
            xu = x
            u0=0; u1=0; u2=1; u3=0
        elif y >= .5 and x < 0:
            yu = y-.5
            xu = x+1
            u0=1; u1=0; u2=0; u3=1
        elif y >= .5 and x >= 0:
            yu = y-.5
            xu = x
            u0=0; u1=1; u2=1; u3=0
        else:
            print('error')
            print(x, y)
            exit(-1)

        u = (1-xu)*(1-yu)*u0 + xu*(1-yu)*u1 + xu*yu*u2 + (1-xu)*yu*u3
        v = (1-xv)*(1-yv)*v0 + xv*(1-yv)*v1 + xv*yv*v2 + (1-xv)*yv*v3
        return (u, v)


class FieldSet_Analytical(object):
    def eval(self, t, x, y):
        if y > 1. or x > 1.:
            return (0, 0)
        u = abs(x)
        v = -y*np.sign(x)
        return (u, v)
