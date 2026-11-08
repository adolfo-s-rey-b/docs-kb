[Skip to main content](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#main-content)

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
    

mplot3d View Angles[#](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#mplot3d-view-angles "Link to this heading")

=======================================================================================================================================

How to define the view angle[#](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#how-to-define-the-view-angle "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

The position of the viewport "camera" in a 3D plot is defined by three angles: _elevation_, _azimuth_, and _roll_. From the resulting position, it always points towards the center of the plot box volume. The angle direction is a common convention, and is shared with [PyVista](https://docs.pyvista.org/api/core/camera.html)
 and [MATLAB](https://www.mathworks.com/help/matlab/ref/view.html)
. Note that a positive roll angle rotates the viewing plane clockwise, so the 3d axes will appear to rotate counter-clockwise.

[![../../../_images/mplot3d_view_angles.png](https://matplotlib.org/stable/_images/mplot3d_view_angles.png)](https://matplotlib.org/stable/_images/mplot3d_view_angles.png)

Rotating the plot using the mouse will control azimuth, elevation, as well as roll, and all three angles can be set programmatically:

import matplotlib.pyplot as plt
ax \= plt.figure().add\_subplot(projection\='3d')
ax.view\_init(elev\=30, azim\=45, roll\=15)

Primary view planes[#](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#primary-view-planes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

To look directly at the primary view planes, the required elevation, azimuth, and roll angles are shown in the diagram of an "unfolded" plot below. These are further documented in the [`mplot3d.axes3d.Axes3D.view_init`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "mpl_toolkits.mplot3d.axes3d.Axes3D.view_init")
 API.

([`Source code`](https://matplotlib.org/stable/_downloads/9aef21aa9ce9dd8058ed993ff799da1e/view_planes_3d.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/4efd809fa85c5bcd6783f8145477ddf6/view_planes_3d_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e3b2d76a4b53889441e8f7238c02ef7a/view_planes_3d_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-toolkits-mplot3d-view_planes_3d_00_00.2x.png)](https://matplotlib.org/stable/_images/api-toolkits-mplot3d-view_planes_3d_00_00.2x.png)

Rotation with mouse[#](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#rotation-with-mouse "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

3D plots can be reoriented by dragging the mouse. There are various ways to accomplish this; the style of mouse rotation can be specified by setting `[rcParams["axes3d.mouserotationstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.mouserotationstyle#rcparam-axes3d-mouserotationstyle) ` (default: `'arcball'`), see [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)
.

Prior to v3.10, the 2D mouse position corresponded directly to azimuth and elevation; this is also how it is done in [MATLAB](https://www.mathworks.com/help/matlab/ref/view.html)
. To keep it this way, set `mouserotationstyle: azel`. This approach works fine for spherical coordinate plots, where the _z_ axis is special; however, it leads to a kind of 'gimbal lock' when looking down the _z_ axis: the plot reacts differently to mouse movement, dependent on the particular orientation at hand. Also, 'roll' cannot be controlled.

As an alternative, there are various mouse rotation styles where the mouse manipulates a virtual 'trackball'. In its simplest form (`mouserotationstyle: trackball`), the trackball rotates around an in-plane axis perpendicular to the mouse motion (it is as if there is a plate laying on the trackball; the plate itself is fixed in orientation, but you can drag the plate with the mouse, thus rotating the ball). This is more natural to work with than the `azel` style; however, the plot cannot be easily rotated around the viewing direction - one has to move the mouse in circles with a handedness opposite to the desired rotation, counterintuitively.

A different variety of trackball rotates along the shortest arc on the virtual sphere (`mouserotationstyle: sphere`). Rotating around the viewing direction is straightforward with it: grab the ball near its edge instead of near the center.

Ken Shoemake's ARCBALL [\[Shoemake1992\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#shoemake1992)
 is also available (`mouserotationstyle: Shoemake`); it resembles the `sphere` style, but is free of hysteresis, i.e., returning mouse to the original position returns the figure to its original orientation; the rotation is independent of the details of the path the mouse took, which could be desirable. However, Shoemake's arcball rotates at twice the angular rate of the mouse movement (it is quite noticeable, especially when adjusting roll), and it lacks an obvious mechanical equivalent; arguably, the path-independent rotation is not natural (however convenient), it could take some getting used to. So it is a trade-off.

Henriksen et al. [\[Henriksen2002\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#henriksen2002)
 provide an overview. In summary:

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |     
| Style | traditional [\[1\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id9) | incl. roll [\[2\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id10) | uniform [\[3\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id11) | path independent [\[4\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id12) | mechanical counterpart [\[5\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id13) |
| azel | ✔️  | ❌   | ❌   | ✔️  | ✔️  |
| trackball | ❌   | ✓ [\[6\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id14) | ✔️  | ❌   | ✔️  |
| sphere | ❌   | ✔️  | ✔️  | ❌   | ✔️  |
| arcball | ❌   | ✔️  | ✔️  | ✔️  | ❌   |

You can try out one of the various mouse rotation styles using:

import matplotlib as mpl
mpl.rcParams\['axes3d.mouserotationstyle'\] \= 'trackball'  \# 'azel', 'trackball', 'sphere', or 'arcball'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

ax \= plt.figure().add\_subplot(projection\='3d')

X \= np.arange(\-5, 5, 0.25)
Y \= np.arange(\-5, 5, 0.25)
X, Y \= np.meshgrid(X, Y)
R \= np.sqrt(X\*\*2 + Y\*\*2)
Z \= np.sin(R)

surf \= ax.plot\_surface(X, Y, Z, cmap\=cm.coolwarm,
                       linewidth\=0, antialiased\=False)

plt.show()

Alternatively, create a file `matplotlibrc`, with contents:

axes3d.mouserotationstyle: trackball

(or any of the other styles, instead of `trackball`), and then run any of the [3D plotting](https://matplotlib.org/stable/gallery/mplot3d/index.html#mplot3d-examples-index)
 examples.

The size of the virtual trackball, sphere, or arcball can be adjusted by setting `[rcParams["axes3d.trackballsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.trackballsize#rcparam-axes3d-trackballsize) ` (default: `0.667`). This specifies how much mouse motion is needed to obtain a given rotation angle (when near the center), and it controls where the edge of the sphere or arcball is (how far from the center, hence how close to the plot edge). The size is specified in units of the Axes bounding box, i.e., to make the arcball span the whole bounding box, set it to 1. A size of about 2/3 appears to work reasonably well; this is the default.

Both arcballs (`mouserotationstyle: sphere` and `mouserotationstyle: arcball`) have a noticeable edge; the edge can be made less abrupt by specifying a border width, `[rcParams["axes3d.trackballborder"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.trackballborder#rcparam-axes3d-trackballborder) ` (default: `0.2`). This works somewhat like Gavin Bell's arcball, which was originally written for OpenGL [\[Bell1988\]](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#bell1988)
, and is used in Blender and Meshlab. Bell's arcball extends the arcball's spherical control surface with a hyperbola; the two are smoothly joined. However, the hyperbola extends all the way beyond the edge of the plot. In the mplot3d sphere and arcball style, the border extends to a radius `trackballsize/2 + trackballborder`. Beyond the border, the style works like the original: it controls roll only. A border width of about 0.2 appears to work well; this is the default. To obtain the original Shoemake's arcball with a sharp border, set the border width to 0. For an extended border similar to Bell's arcball, where the transition from the arcball to the border occurs at 45°, set the border width to \\(\\sqrt 2 \\approx 1.414\\). The border is a circular arc, wrapped around the arcball sphere cylindrically (like a doughnut), joined smoothly to the sphere, much like Bell's hyperbola.

\[[Shoemake1992](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id1)\
\]

Ken Shoemake, "ARCBALL: A user interface for specifying three-dimensional rotation using a mouse", in Proceedings of Graphics Interface '92, 1992, pp. 151-156, [https://doi.org/10.20380/GI1992.18](https://doi.org/10.20380/GI1992.18)

\[[Bell1988](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id15)\
\]

Gavin Bell, in the examples included with the GLUT (OpenGL Utility Toolkit) library, [markkilgard/glut](https://github.com/markkilgard/glut/blob/master/progs/examples/trackball.h)

\[[Henriksen2002](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#id2)\
\]

Knud Henriksen, Jon Sporring, Kasper Hornbæk, "Virtual Trackballs Revisited", in IEEE Transactions on Visualization and Computer Graphics, Volume 10, Issue 2, March-April 2004, pp. 206-216, [https://doi.org/10.1109/TVCG.2004.1260772](https://doi.org/10.1109/TVCG.2004.1260772)
 [\[full-text\]](https://www.researchgate.net/publication/8329656_Virtual_Trackballs_Revisited#fullTextFileContent)
;

On this page