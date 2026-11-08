[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html#sphx-glr-download-gallery-axisartist-demo-parasite-axes-py)
 to download the full example code.

Parasite Axes demo[#](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html#parasite-axes-demo "Link to this heading")

==========================================================================================================================================

Create a parasite Axes. Such Axes would share the x scale with a host Axes, but show a different scale in y direction.

This approach uses [`mpl_toolkits.axes_grid1.parasite_axes.HostAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxes.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxes "mpl_toolkits.axes_grid1.parasite_axes.HostAxes")
 and [`mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes.html#mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes "mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes")
.

The standard and recommended approach is to use instead standard Matplotlib axes, as shown in the [Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)
 example.

An alternative approach using [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 and [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 is shown in the [Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)
 example.

![demo parasite axes](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes_001_2_00x.png)

import matplotlib.pyplot as plt

from mpl\_toolkits.axisartist.parasite\_axes import [HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

host \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.15, 0.1, 0.65, 0.8), axes\_class\=[HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")
)
par1 \= [host.get\_aux\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes")
(viewlim\_mode\=None, sharex\=host)
par2 \= [host.get\_aux\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes")
(viewlim\_mode\=None, sharex\=host)

[host.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].set\_visible(False)

[par1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].set\_visible(True)
[par1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].major\_ticklabels.set\_visible(True)
[par1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].label.set\_visible(True)

[par2.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right2"\] \= [par2.new\_fixed\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_fixed_axis "mpl_toolkits.axisartist.Axes.new_fixed_axis")
(loc\="right", offset\=(60, 0))

[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [host.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1, 2\], \[0, 1, 2\], label\="Density")
[p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [par1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1, 2\], \[0, 3, 2\], label\="Temperature")
[p3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [par2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1, 2\], \[50, 30, 15\], label\="Velocity")

[host.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.set "mpl_toolkits.axisartist.Axes.set")
(xlim\=(0, 2), ylim\=(0, 2), xlabel\="Distance", ylabel\="Density")
[par1.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.set "mpl_toolkits.axisartist.Axes.set")
(ylim\=(0, 4), ylabel\="Temperature")
[par2.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.set "mpl_toolkits.axisartist.Axes.set")
(ylim\=(1, 65), ylabel\="Velocity")

[host.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[host.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["left"\].label.set\_color([p1.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())
[par1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].label.set\_color([p2.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())
[par2.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right2"\].label.set\_color([p3.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_parasite_axes.ipynb`](https://matplotlib.org/stable/_downloads/91da0f31756f11cccb3fc31afb600c4d/demo_parasite_axes.ipynb)

[`Download Python source code: demo_parasite_axes.py`](https://matplotlib.org/stable/_downloads/5922b9d93b49d592301af79dfdddf7de/demo_parasite_axes.py)

[`Download zipped: demo_parasite_axes.zip`](https://matplotlib.org/stable/_downloads/cc3a713011a81447e6ad2e0978390506/demo_parasite_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)