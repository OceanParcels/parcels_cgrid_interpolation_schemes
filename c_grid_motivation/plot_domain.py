import matplotlib.pyplot as plt


def plot_domain(fset_type, only_axes=False):
    fig = plt.figure(figsize=(5, 5), dpi=300, facecolor='w', edgecolor='k')

    # axes
    ax1 = plt.axes(frameon=False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.axes.get_xaxis().set_visible(False)

    plt.plot([-1.05, 1.05], [0, 0], linewidth=1.2, color='gray')
    plt.arrow(.95, 0, .1, 0, width=.0, head_width=.015, head_length=.02, color='gray')
    plt.plot([0, 0], [-.05, 1.05], linewidth=1.2, color='gray')
    plt.arrow(.0, .95, 0, .1, width=.0, head_width=.015, head_length=.02, color='gray')
    plt.axis('scaled')
    plt.xlim(-1.6, 1.6)
    plt.ylim(-.6, 1.6)
    fig.tight_layout()

    if only_axes:
        return fig

    # A grid
    if fset_type in ['A', 'CU', 'CV']:
        plt.plot([-1, 0, 0, -1, -1], [0, 0, 1, 1, 0], '--k', linewidth=1)
        plt.plot([1, 0, 0, 1, 1], [0, 0, 1, 1, 0], '--k', linewidth=1)
        plt.scatter([-1, 0, 1, 1, 0, -1], [0, 0, 0, 1, 1, 1], zorder=3, color='k', s=15)

    # C grid
    if fset_type == 'C':
        plt.plot([-1, 0, 0, -1, -1], [0, 0, 1, 1, 0], '--k', linewidth=1)
        plt.plot([1, 0, 0, 1, 1], [0, 0, 1, 1, 0], '--k', linewidth=1)
        plt.scatter([-1, 0, 1], [.5, .5, .5], zorder=3, color='r', s=15)
        plt.scatter([-.5, .5, .5, -.5], [0, 0, 1, 1], zorder=3, color='g', s=15)

    # CU grid
    if fset_type in ['CU', 'CWrong']:
        plt.plot([-1, 0, 0, -1, -1], [0-.5, 0-.5, 1-.5, 1-.5, 0-.5], '--r', linewidth=1)
        plt.plot([1, 0, 0, 1, 1], [0-.5, 0-.5, 1-.5, 1-.5, 0-.5], '--r', linewidth=1)
        plt.plot([-1, 0, 0, -1, -1], [1+.5, 1+.5, 0+.5, 0+.5, 1+.5], '--r', linewidth=1)
        plt.plot([1, 0, 0, 1, 1], [1+.5, 1+.5, 0+.5, 0+.5, 1+.5], '--r', linewidth=1)
        plt.scatter([-1, 0, 1, -1, 0, 1, -1, 0, 1], [-.5, -.5, -.5, .5, .5, .5, 1.5, 1.5, 1.5], zorder=3, color='r', s=15)

    # CV grid
    if fset_type in ['CV', 'CWrong']:
        plt.plot([-1-.5, 0-.5, 0-.5, -1-.5, -1-.5], [0, 0, 1, 1, 0], '--g', linewidth=1)
        plt.plot([1-.5, 0-.5, 0-.5, 1-.5, 1-.5], [0, 0, 1, 1, 0], '--g', linewidth=1)
        plt.plot([-1+1.5, 0+1.5, 0+1.5, -1+1.5, -1+1.5], [0, 0, 1, 1, 0], '--g', linewidth=1)
        plt.scatter([-1.5, -.5, .5, 1.5, -1.5, -.5, .5, 1.5], [0, 0, 0, 0, 1, 1, 1, 1], zorder=3, color='g', s=15)

    return fig
