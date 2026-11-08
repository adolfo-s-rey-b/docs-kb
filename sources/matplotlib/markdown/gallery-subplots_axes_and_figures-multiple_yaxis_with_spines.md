[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html#sphx-glr-download-gallery-subplots-axes-and-figures-multiple-yaxis-with-spines-py)
 to download the full example code.

Multiple y-axis with Spines[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html#multiple-y-axis-with-spines "Link to this heading")

===================================================================================================================================================================================

Create multiple y axes with a shared x-axis. This is done by creating a [`twinx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
 Axes, turning all spines but the right one invisible and offset its position using [`set_position`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
.

Note that this approach uses [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 and their [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
s. Alternative approaches using non-standard Axes are shown in the [Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)
 and [Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)
 examples.

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(right\=0.75)

[twin1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
()
[twin2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
()

\# Offset the right spine of twin2.  The ticks and label have already been
\# placed on the right by twinx above.
[twin2.spines.right.set\_position](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
(("axes", 1.2))

[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1, 2\], \[0, 1, 2\], "C0", label\="Density")
[p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [twin1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1, 2\], \[0, 3, 2\], "C1", label\="Temperature")
[p3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [twin2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1, 2\], \[50, 30, 15\], "C2", label\="Velocity")

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 2), ylim\=(0, 2), xlabel\="Distance", ylabel\="Density")
[twin1.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(ylim\=(0, 4), ylabel\="Temperature")
[twin2.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(ylim\=(1, 65), ylabel\="Velocity")

[ax.yaxis.label.set\_color](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")
([p1.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())
[twin1.yaxis.label.set\_color](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")
([p2.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())
[twin2.yaxis.label.set\_color](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")
([p3.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())

[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='y', colors\=[p1.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())
[twin1.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='y', colors\=[p2.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())
[twin2.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='y', colors\=[p3.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
())

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [p3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![multiple yaxis with spines](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_001_2_00x.png)

Tags: [component: spines](https://matplotlib.org/stable/_tags/component-spines.html)

[`Download Jupyter notebook: multiple_yaxis_with_spines.ipynb`](https://matplotlib.org/stable/_downloads/7ede73ac9ffde49f866167ea70f9553d/multiple_yaxis_with_spines.ipynb)

[`Download Python source code: multiple_yaxis_with_spines.py`](https://matplotlib.org/stable/_downloads/a0bec26bdc993876d053435944b038d5/multiple_yaxis_with_spines.py)

[`Download zipped: multiple_yaxis_with_spines.zip`](https://matplotlib.org/stable/_downloads/2f9ee6722500c236c0d2a1eb55801f38/multiple_yaxis_with_spines.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)