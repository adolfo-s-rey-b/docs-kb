[Skip to main content](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html#sphx-glr-download-gallery-misc-packed-bubbles-py)
 to download the full example code.

Packed-bubble chart[#](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html#packed-bubble-chart "Link to this heading")

==================================================================================================================================

Create a packed-bubble chart to represent scalar data. The presented algorithm tries to move all bubbles as close to the center of mass as possible while avoiding some collisions by moving around colliding objects. In this example we plot the market share of different desktop browsers. (source: [https://gs.statcounter.com/browser-market-share/desktop/worldwidev](https://gs.statcounter.com/browser-market-share/desktop/worldwidev)
)

![Browser market share](https://matplotlib.org/stable/_images/sphx_glr_packed_bubbles_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

[browser\_market\_share](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'browsers': \['firefox', 'chrome', 'safari', 'edge', 'ie', 'opera'\],
    'market\_share': \[8.61, 69.55, 8.36, 4.12, 2.76, 2.43\],
    'color': \['#5A69AF', '#579E65', '#F9C784', '#FC944A', '#F24C00', '#00B825'\]
}

class BubbleChart:
    def \_\_init\_\_(self, area, bubble\_spacing\=0):
        """
        Setup for bubble collapse.

        Parameters
        ----------
        area : array-like
            Area of the bubbles.
        bubble\_spacing : float, default: 0
            Minimal spacing between bubbles after collapsing.

        Notes
        -----
        If "area" is sorted, the results might look weird.
        """
        area \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(area)
        r \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(area / [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

        self.bubble\_spacing \= bubble\_spacing
        self.bubbles \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
((len(area), 4))
        self.bubbles\[:, 2\] \= r
        self.bubbles\[:, 3\] \= area
        self.maxstep \= 2 \* self.bubbles\[:, 2\].max() + self.bubble\_spacing
        self.step\_dist \= self.maxstep / 2

        \# calculate initial grid layout for bubbles
        length \= [np.ceil](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(len(self.bubbles)))
        grid \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(length) \* self.maxstep
        gx, gy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(grid, grid)
        self.bubbles\[:, 0\] \= gx.flatten()\[:len(self.bubbles)\]
        self.bubbles\[:, 1\] \= gy.flatten()\[:len(self.bubbles)\]

        self.com \= self.center\_of\_mass()

    def center\_of\_mass(self):
        return [np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(
            self.bubbles\[:, :2\], axis\=0, weights\=self.bubbles\[:, 3\]
        )

    def center\_distance(self, bubble, bubbles):
        return [np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(bubble\[0\] \- bubbles\[:, 0\],
                        bubble\[1\] \- bubbles\[:, 1\])

    def outline\_distance(self, bubble, bubbles):
        center\_distance \= self.center\_distance(bubble, bubbles)
        return center\_distance \- bubble\[2\] \- \\
            bubbles\[:, 2\] \- self.bubble\_spacing

    def check\_collisions(self, bubble, bubbles):
        distance \= self.outline\_distance(bubble, bubbles)
        return len(distance\[distance < 0\])

    def collides\_with(self, bubble, bubbles):
        distance \= self.outline\_distance(bubble, bubbles)
        return [np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")
(distance, keepdims\=True)

    def collapse(self, n\_iterations\=50):
        """
        Move bubbles to the center of mass.

        Parameters
        ----------
        n\_iterations : int, default: 50
            Number of moves to perform.
        """
        for \_i in range(n\_iterations):
            moves \= 0
            for i in range(len(self.bubbles)):
                rest\_bub \= [np.delete](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")
(self.bubbles, i, 0)
                \# try to move directly towards the center of mass
                \# direction vector from bubble to the center of mass
                dir\_vec \= self.com \- self.bubbles\[i, :2\]

                \# shorten direction vector to have length of 1
                dir\_vec \= dir\_vec / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(dir\_vec.dot(dir\_vec))

                \# calculate new bubble position
                new\_point \= self.bubbles\[i, :2\] + dir\_vec \* self.step\_dist
                new\_bubble \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(new\_point, self.bubbles\[i, 2:4\])

                \# check whether new bubble collides with other bubbles
                if not self.check\_collisions(new\_bubble, rest\_bub):
                    self.bubbles\[i, :\] \= new\_bubble
                    self.com \= self.center\_of\_mass()
                    moves += 1
                else:
                    \# try to move around a bubble that you collide with
                    \# find colliding bubble
                    for colliding in self.collides\_with(new\_bubble, rest\_bub):
                        \# calculate direction vector
                        dir\_vec \= rest\_bub\[colliding, :2\] \- self.bubbles\[i, :2\]
                        dir\_vec \= dir\_vec / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(dir\_vec.dot(dir\_vec))
                        \# calculate orthogonal vector
                        orth \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[dir\_vec\[1\], \-dir\_vec\[0\]\])
                        \# test which direction to go
                        new\_point1 \= (self.bubbles\[i, :2\] + orth \*
                                      self.step\_dist)
                        new\_point2 \= (self.bubbles\[i, :2\] \- orth \*
                                      self.step\_dist)
                        dist1 \= self.center\_distance(
                            self.com, [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[new\_point1\]))
                        dist2 \= self.center\_distance(
                            self.com, [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[new\_point2\]))
                        new\_point \= new\_point1 if dist1 < dist2 else new\_point2
                        new\_bubble \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(new\_point, self.bubbles\[i, 2:4\])
                        if not self.check\_collisions(new\_bubble, rest\_bub):
                            self.bubbles\[i, :\] \= new\_bubble
                            self.com \= self.center\_of\_mass()

            if moves / len(self.bubbles) < 0.1:
                self.step\_dist \= self.step\_dist / 2

    def plot(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, labels, colors):
        """
        Draw the bubble plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Labels of the bubbles.
        colors : list
            Colors of the bubbles.
        """
        for i in range(len(self.bubbles)):
            circ \= [plt.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
(
                self.bubbles\[i, :2\], self.bubbles\[i, 2\], color\=colors\[i\])
            [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
(circ)
            [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\*self.bubbles\[i, :2\], labels\[i\],
                    horizontalalignment\='center', verticalalignment\='center')

bubble\_chart \= BubbleChart(area\=[browser\_market\_share](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['market\_share'\],
                           bubble\_spacing\=0.1)

bubble\_chart.collapse()

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(aspect\="equal"))
bubble\_chart.plot(
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [browser\_market\_share](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['browsers'\], [browser\_market\_share](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['color'\])
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
("off")
[ax.relim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
()
[ax.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Browser market share')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: packed_bubbles.ipynb`](https://matplotlib.org/stable/_downloads/5603cc695cbb30bf42fce32e93e19cf1/packed_bubbles.ipynb)

[`Download Python source code: packed_bubbles.py`](https://matplotlib.org/stable/_downloads/81bc179821dc9808604c256bcb20b3b0/packed_bubbles.py)

[`Download zipped: packed_bubbles.zip`](https://matplotlib.org/stable/_downloads/a223ec098853b764631883da8e9fe248/packed_bubbles.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)