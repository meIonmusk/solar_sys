import matplotlib.pyplot as plot
import numpy as np


def draw_graphics(v, r, time):
    plot.subplots(2, 2, figsize=(10, 7))
    t = np.arange(0, time, time/len(v))
    # subplot v(t)
    graph = plot.subplot(221)
    plot.plot(t, v)
    plot.title('v(t)')
    plot.xlabel('t, s')
    plot.ylabel('v, m/s')

    # subplot r(t)
    graph = plot.subplot(222)
    plot.plot(t, r)
    plot.title('r(t)')
    plot.xlabel('t, s')
    plot.ylabel('r, m')

    # subplot v(r)
    graph = plot.subplot(223)
    plot.plot(t, v)
    plot.title('v(r)')
    plot.xlabel('r, m')
    plot.ylabel('v, m/s')

    plot.show()
