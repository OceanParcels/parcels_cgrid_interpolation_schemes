# C-grid interpolation: motivation and introduction

In [delandmeter et al., 2019](https://www.geosci-model-dev.net/12/3571/2019/), we developed a specific interpolator for C-grids. The construction of this interpolator in 2D and 3D grids, for rectilinear and curvilinear meshes, is described in the paper and implemented in [Parcels code](http://www.oceanparcels.org) and this repository.

In this notebook, we develop the motivation to this approach, showing why a specific interpolator is necessary for C-grids, using a simple benchmark.

## Benchmark: conservative analytical flow

![](c_grid_motivation/pics/two_jets_analytical.pdf)


