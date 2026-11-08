[Skip to main content](https://matplotlib.org/stable/gallery/animation/double_pendulum.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/animation/double_pendulum.html#sphx-glr-download-gallery-animation-double-pendulum-py)
 to download the full example code.

The double pendulum problem[#](https://matplotlib.org/stable/gallery/animation/double_pendulum.html#the-double-pendulum-problem "Link to this heading")

========================================================================================================================================================

This animation illustrates the double pendulum problem.

Double pendulum formula translated from the C code at [http://www.physics.usyd.edu.au/~wheat/dpend\_html/solve\_dpend.c](http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c)

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np
from numpy import [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
, [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")

import matplotlib.animation as animation

[G](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 9.8  \# acceleration due to gravity, in m/s^2
[L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1.0  \# length of pendulum 1 in m
[L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1.0  \# length of pendulum 2 in m
[L](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
  \# maximal length of the combined pendulum
[M1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1.0  \# mass of pendulum 1 in kg
[M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1.0  \# mass of pendulum 2 in kg
[t\_stop](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 2.5  \# how many seconds to simulate
[history\_len](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 500  \# how many trajectory points to display

def derivs([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    dydx \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
([state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    dydx\[0\] \= [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]

    delta \= [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\] \- [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
    den1 \= ([M1](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* [L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- [M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta) \* [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
    dydx\[1\] \= (([M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\] \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\] \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta) \* [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
                + [M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [G](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\]) \* [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
                + [M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\] \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\] \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
                \- ([M1](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* [G](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]))
               / den1)

    dydx\[2\] \= [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\]

    den2 \= ([L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
/[L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* den1
    dydx\[3\] \= ((\- [M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\] \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\] \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta) \* [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
                + ([M1](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* [G](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]) \* [cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
                \- ([M1](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* [L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\] \* [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\] \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(delta)
                \- ([M1](https://docs.python.org/3/library/functions.html#float "builtins.float")
+[M2](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* [G](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\]))
               / den2)

    return dydx

\# create a time array from 0..t\_stop sampled at 0.01 second steps
[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.01
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, [t\_stop](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

\# th1 and th2 are the initial angles (degrees)
\# w10 and w20 are the initial angular velocities (degrees per second)
[th1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 120.0
[w1](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.0
[th2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= \-10.0
[w2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.0

\# initial state
[state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.radians](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\[[th1](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [w1](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [th2](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [w2](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\])

\# integrate the ODE using Euler's method
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
((len([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), 4))
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\] \= [state](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(1, len([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)):
    [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \= [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 \- 1\] + derivs([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 \- 1\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 \- 1\]) \* [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")

\# A more accurate estimate could be obtained e.g. using scipy:
#
\#   y = scipy.integrate.solve\_ivp(derivs, t\[\[0, -1\]\], state, t\_eval=t).y.T

[x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\])
[y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \-[L1](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\])

[x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 2\]) + [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \-[L2](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 2\]) + [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 4))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(autoscale\_on\=False, xlim\=(\-[L](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [L](https://docs.python.org/3/library/functions.html#float "builtins.float")
), ylim\=(\-[L](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 1.))
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
('equal')
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()

[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[\], \[\], 'o-', lw\=2)
[trace](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[\], \[\], '.-', lw\=1, ms\=2)
[time\_template](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'time = %.1fs'
[time\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.05, 0.9, '', transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

def animate([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    thisx \= \[0, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]\]
    thisy \= \[0, [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]\]

    history\_x \= [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
    history\_y \= [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]

    [line.set\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
(thisx, thisy)
    [trace.set\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
(history\_x, history\_y)
    [time\_text.set\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
([time\_template](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 % ([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
    return [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [trace](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [time\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, animate, len([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), interval\=[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*1000, blit\=True)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (1 minutes 16.140 seconds)

[`Download Jupyter notebook: double_pendulum.ipynb`](https://matplotlib.org/stable/_downloads/1327fecca76444ef703683cc4610086e/double_pendulum.ipynb)

[`Download Python source code: double_pendulum.py`](https://matplotlib.org/stable/_downloads/244e0cb4bead5cfd5f8e9d6aeca0ba31/double_pendulum.py)

[`Download zipped: double_pendulum.zip`](https://matplotlib.org/stable/_downloads/02383bbfb2fce48594c5851fb5283fa4/double_pendulum.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)