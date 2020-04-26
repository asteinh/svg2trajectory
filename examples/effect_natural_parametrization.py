from svg2trajectory import Parser
import matplotlib.pyplot as plt
import numpy as np

paths = Parser('examples/svg/test_curves.svg')
for i, path in enumerate(paths):
    if i == 1:
        path.natural_parametrization()

    print("Total path length: {}".format(path.length()))

    N = 50
    s = np.linspace(0, 1, N)
    p = path.point(s)

    plt.plot(p[0, :], p[1, :], 'r.', zorder=1)

plt.axis('equal')
plt.grid()
plt.show()
