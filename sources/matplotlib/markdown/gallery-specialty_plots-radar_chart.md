[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html#sphx-glr-download-gallery-specialty-plots-radar-chart-py)
 to download the full example code.

Radar chart (aka spider or star chart)[#](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html#radar-chart-aka-spider-or-star-chart "Link to this heading")

==============================================================================================================================================================================

This example creates a radar chart, also known as a spider or star chart [\[1\]](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html#id2)
.

Although this example allows a frame of either 'circle' or 'polygon', polygon frames don't have proper gridlines (the lines are circles instead of polygons). It's possible to get a polygon grid by setting GRIDLINE\_INTERPOLATION\_STEPS in [`matplotlib.axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 to the desired number of vertices, but the orientation of the polygon is not aligned with the radial axis.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
, [RegularPolygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.RegularPolygon.html#matplotlib.patches.RegularPolygon "matplotlib.patches.RegularPolygon")
from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.projections import [register\_projection](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
from matplotlib.projections.polar import [PolarAxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
from matplotlib.spines import [Spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

def radar\_factory(num\_vars, frame\='circle'):
    """
    Create a radar chart with \`num\_vars\` Axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num\_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding Axes.

    """
    \# calculate evenly-spaced axis angles
    [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, num\_vars, endpoint\=False)

    class RadarTransform([PolarAxes.PolarTransform](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
):

        def transform\_path\_non\_affine(self, path):
            \# Paths with non-unit interpolation steps correspond to gridlines,
            \# in which case we force interpolation (to defeat PolarTransform's
            \# autoconversion to circular arcs).
            if path.\_interpolation\_steps \> 1:
                path \= path.interpolated(num\_vars)
            return [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(self.transform(path.vertices), path.codes)

    class RadarAxes([PolarAxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):

        name \= 'radar'
        PolarTransform \= RadarTransform

        def \_\_init\_\_(self, \*args, \*\*kwargs):
            super().\_\_init\_\_(\*args, \*\*kwargs)
            \# rotate plot such that the first axis is at the top
            self.set\_theta\_zero\_location('N')

        def fill(self, \*args, closed\=True, \*\*kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed\=closed, \*args, \*\*kwargs)

        def plot(self, \*args, \*\*kwargs):
            """Override plot so that line is closed by default"""
            lines \= super().plot(\*args, \*\*kwargs)
            for line in lines:
                self.\_close\_line(line)

        def \_close\_line(self, line):
            x, y \= line.get\_data()
            \# FIXME: markers at x\[0\], y\[0\] get doubled-up
            if x\[0\] != x\[\-1\]:
                x \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(x, x\[0\])
                y \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(y, y\[0\])
                line.set\_data(x, y)

        def set\_varlabels(self, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
            self.set\_thetagrids([np.degrees](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

        def \_gen\_axes\_patch(self):
            \# The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            \# in axes coordinates.
            if frame \== 'circle':
                return [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((0.5, 0.5), 0.5)
            elif frame \== 'polygon':
                return [RegularPolygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.RegularPolygon.html#matplotlib.patches.RegularPolygon "matplotlib.patches.RegularPolygon")
((0.5, 0.5), num\_vars,
                                      radius\=.5, edgecolor\="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def \_gen\_axes\_spines(self):
            if frame \== 'circle':
                return super().\_gen\_axes\_spines()
            elif frame \== 'polygon':
                \# spine\_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine \= [Spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
(axes\=self,
                              spine\_type\='circle',
                              path\=[Path.unit\_regular\_polygon](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_regular_polygon "matplotlib.path.Path.unit_regular_polygon")
(num\_vars))
                \# unit\_regular\_polygon gives a polygon of radius 1 centered at
                \# (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                \# 0.5) in axes coordinates.
                spine.set\_transform([Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    [register\_projection](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
(RadarAxes)
    return [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

def example\_data():
    \# The following data is from the Denver Aerosol Sources and Health study.
    \# See doi:10.1016/j.atmosenv.2008.12.017
    #
    \# The data are pollution source profile estimates for five modeled
    \# pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical
    \# species. The radar charts are experimented with here to see if we can
    \# nicely visualize how the modeled source profiles change across four
    \# scenarios:
    \#  1) No gas-phase species present, just seven particulate counts on
    \#     Sulfate
    \#     Nitrate
    \#     Elemental Carbon (EC)
    \#     Organic Carbon fraction 1 (OC)
    \#     Organic Carbon fraction 2 (OC2)
    \#     Organic Carbon fraction 3 (OC3)
    \#     Pyrolyzed Organic Carbon (OP)
    \#  2)Inclusion of gas-phase specie carbon monoxide (CO)
    \#  3)Inclusion of gas-phase specie ozone (O3).
    \#  4)Inclusion of both gas-phase species is present...
    [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
        \['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'\],\
        ('Basecase', \[\
            \[0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00\],\
            \[0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00\],\
            \[0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00\],\
            \[0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00\],\
            \[0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00\]\]),\
        ('With CO', \[\
            \[0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00\],\
            \[0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00\],\
            \[0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00\],\
            \[0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00\],\
            \[0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00\]\]),\
        ('With O3', \[\
            \[0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03\],\
            \[0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00\],\
            \[0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00\],\
            \[0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95\],\
            \[0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00\]\]),\
        ('CO & O3', \[\
            \[0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01\],\
            \[0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00\],\
            \[0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00\],\
            \[0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88\],\
            \[0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16\]\])\
    \]
    return [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

if \_\_name\_\_ \== '\_\_main\_\_':
    [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 9
    [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= radar\_factory([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, frame\='polygon')

    [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= example\_data()
    [spoke\_labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.pop(0)

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(9, 9), nrows\=2, ncols\=2,
                            subplot\_kw\=dict(projection\='radar'))
    [fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(wspace\=0.25, hspace\=0.20, top\=0.85, bottom\=0.05)

    [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['b', 'r', 'g', 'm', 'y'\]
    \# Plot the four cases from the example data on separate Axes
    for ax, ([title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [case\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        ax.set\_rgrids(\[0.2, 0.4, 0.6, 0.8\])
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, weight\='bold', size\='medium', position\=(0.5, 1.1),
                     horizontalalignment\='center', verticalalignment\='center')
        for [d](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([case\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
            [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [d](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
            [ax.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [d](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, facecolor\=[color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, alpha\=0.25, label\='\_nolegend\_')
        ax.set\_varlabels([spoke\_labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

    \# add legend relative to top-left plot
    [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ('Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5')
    [legend](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].[legend](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
([labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, loc\=(0.9, .95),
                              labelspacing\=0.1, fontsize\='small')

    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, 0.965, '5-Factor Solution Profiles Across Four Scenarios',
             horizontalalignment\='center', [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='black', weight\='bold',
             size\='large')

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Basecase, With CO, With O3, CO & O3](https://matplotlib.org/stable/_images/sphx_glr_radar_chart_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.spines`](https://matplotlib.org/stable/api/spines_api.html#module-matplotlib.spines "matplotlib.spines")
    
*   [`matplotlib.spines.Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
    
*   [`matplotlib.projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
    
*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    
*   [`matplotlib.projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
    
*   [`matplotlib.projections.register_projection`](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
    

**Total running time of the script:** (0 minutes 2.328 seconds)

[`Download Jupyter notebook: radar_chart.ipynb`](https://matplotlib.org/stable/_downloads/674ef13b0b149ddb5f4beaa73790ba4d/radar_chart.ipynb)

[`Download Python source code: radar_chart.py`](https://matplotlib.org/stable/_downloads/5eab8801e2724e6355c7a280335527fc/radar_chart.py)

[`Download zipped: radar_chart.zip`](https://matplotlib.org/stable/_downloads/2068fd57f57c04265355d99e64d0339b/radar_chart.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)