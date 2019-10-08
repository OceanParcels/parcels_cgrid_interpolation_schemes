def AdvectionRK4(particle, fset, dt):
    """Advection of particle using fourth-order Runge-Kutta integration. """

    (u1, v1) = fset.eval(particle.t, particle.x, particle.y)
    x1, y1 = (particle.x + u1*.5*dt, particle.y + v1*.5*dt)
    (u2, v2) = fset.eval(particle.t + .5*dt, x1, y1)
    x2, y2 = (particle.x + u2*.5*dt, particle.y + v2*.5*dt)
    (u3, v3) = fset.eval(particle.t + .5*dt, x2, y2)
    x3, y3 = (particle.x + u3*dt, particle.y + v3*dt)
    (u4, v4) = fset.eval(particle.t + dt, x3, y3)
    particle.x += (u1 + 2*u2 + 2*u3 + u4) / 6. * dt
    particle.y += (v1 + 2*v2 + 2*v3 + v4) / 6. * dt
    particle.t += dt


def AdvectionEE(particle, fset, dt):
    """Advection of particle using Explicit Euler integration."""

    (u1, v1) = fset.eval(particle.t, particle.x, particle.y)
    particle.x += u1 * dt
    particle.y += v1 * dt
    particle.t += dt
