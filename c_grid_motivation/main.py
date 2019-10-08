from particle import Particle
from advection import AdvectionRK4
from fieldset import FieldSet_Analytical
from fieldset import FieldSet_A
from fieldset import FieldSet_C
from fieldset import FieldSet_CWrong
from plot_domain import plot_domain


def particle_advection(advection_scheme, fset):
    pset = [Particle(-1, 0.05*i, 0) for i in range(1, 21)]
    pset += [Particle(0.05*i, 1, 0) for i in range(1, 21)]
    for p in pset:
        p.store()
    dt = .0005

    niter = 0
    while pset[0].t < 10:
        for p in pset:
            advection_scheme(p, fset, dt)
        niter += 1
        if niter % 10 == 0:
            for p in pset:
                p.store()
    return pset


fset_type = 'CV'
for fset_type in ['analytical', 'A', 'C', 'CWrong', 'CU', 'CV']:
    if fset_type == 'analytical':
        fset = FieldSet_Analytical()
    elif fset_type == 'A':
        fset = FieldSet_A()
    elif fset_type == 'C':
        fset = FieldSet_C()
    elif fset_type == 'CWrong':
        fset = FieldSet_CWrong()
    else:
        fset = None

    fig = plot_domain(fset_type, only_axes=False)
    if fset:
        pset = particle_advection(AdvectionRK4, fset)
        for p in pset:
            fig = p.plot(fig)
    fig.savefig('pics/two_jets_%s.png' % fset_type)
    # fig.savefig('pics/two_jets_%s_no_result.png' % fset_type)
    # plt.show()
