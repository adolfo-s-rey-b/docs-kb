[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html#sphx-glr-download-gallery-axisartist-demo-parasite-axes2-py)
 to download the full example code.

Parasite axis demo[#](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html#parasite-axis-demo "Link to this heading")

===========================================================================================================================================

This example demonstrates the use of parasite axis to plot multiple datasets onto one single plot.

Notice how in this example, _par1_ and _par2_ are both obtained by calling `twinx()`, which ties their x-limits with the host's x-axis. From there, each of those two axis behave separately from each other: different datasets can be plotted, and the y-limits are adjusted separately.

This approach uses [`mpl_toolkits.axes_grid1.parasite_axes.host_subplot`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.host_subplot.html#mpl_toolkits.axes_grid1.parasite_axes.host_subplot "mpl_toolkits.axes_grid1.parasite_axes.host_subplot")
 and [`mpl_toolkits.axisartist.axislines.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")
.

The standard and recommended approach is to use instead standard Matplotlib axes, as shown in the [Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)
 example.

An alternative approach using [`mpl_toolkits.axes_grid1.parasite_axes.HostAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxes.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxes "mpl_toolkits.axes_grid1.parasite_axes.HostAxes")
 and [`mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes.html#mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes "mpl_toolkits.axes_grid1.parasite_axes.ParasiteAxes")
 is shown in the [Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)
 example.

![demo parasite axes2](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_001_2_00x.png)

import matplotlib.pyplot as plt

from mpl\_toolkits import axisartist
from mpl\_toolkits.axes\_grid1 import host\_subplot

host \= host\_subplot(111, axes\_class\=[axisartist.Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(right\=0.75)

par1 \= [host.twinx](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.twinx "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.twinx")
()
par2 \= [host.twinx](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.twinx "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.twinx")
()

[par2.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\] \= [par2.new\_fixed\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_fixed_axis "mpl_toolkits.axisartist.Axes.new_fixed_axis")
(loc\="right", offset\=(60, 0))

[par1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].toggle(all\=True)
[par2.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].toggle(all\=True)

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
\["right"\].label.set\_color([p3.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_parasite_axes2.ipynb`](https://matplotlib.org/stable/_downloads/b0a91ad840eadf7342c2f79811560889/demo_parasite_axes2.ipynb)

[`Download Python source code: demo_parasite_axes2.py`](https://matplotlib.org/stable/_downloads/07a9488814cca10d5122c0c5527bcaaf/demo_parasite_axes2.py)

[`Download zipped: demo_parasite_axes2.zip`](https://matplotlib.org/stable/_downloads/014a880826469dce2e3ad8104270a00a/demo_parasite_axes2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)