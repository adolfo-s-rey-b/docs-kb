[Skip to main content](https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html#sphx-glr-download-gallery-ticks-ticklabels-rotation-py)
 to download the full example code.

Rotated tick labels[#](https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html#rotated-tick-labels "Link to this heading")

========================================================================================================================================

Rotating tick labels can be useful when the labels are long and overlap with each other. Adjust the tick properties using [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
: Set the angle in degrees via the _rotation_ parameter. Set the _rotation\_mode_ parameter to "xtick" / "ytick" to make the text point towards the tick, see also [`set_rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode")
.

Note: We use `layout="constrained"` to make sure there is enough space for the tick labels so that they are not cut off.

import matplotlib.pyplot as plt

[population](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'India': 1417.492,
    'China': 1404.89,
    'United States': 341.784857,
    'Indonesia': 284.438782,
    'Pakistan': 241.499431,
    'Nigeria': 223.8,
    'Brazil': 213.421037,
    'Bangladesh': 169.828911,
    'Russia': 146.028325,
    'Mexico': 131.001723,
    'Japan': 122.95,
    'Philippines': 114.1236,
    'DR Congo': 112.832,
    'Ethiopia': 111.652998,
    'Egypt': 107.868296,
    'Vietnam': 102.3,
}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\="constrained")
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([population](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys(), [population](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values())
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
("x", rotation\=45, rotation\_mode\="xtick")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("population (millions)")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ticklabels rotation](https://matplotlib.org/stable/_images/sphx_glr_ticklabels_rotation_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
     / [`matplotlib.pyplot.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params")
    

Tags: [component: ticks](https://matplotlib.org/stable/_tags/component-ticks.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)

[`Download Jupyter notebook: ticklabels_rotation.ipynb`](https://matplotlib.org/stable/_downloads/29ab3d9fc06c3c3253f8ac4e28014aee/ticklabels_rotation.ipynb)

[`Download Python source code: ticklabels_rotation.py`](https://matplotlib.org/stable/_downloads/6bf1f86ac14b705a7352333c341c3b82/ticklabels_rotation.py)

[`Download zipped: ticklabels_rotation.zip`](https://matplotlib.org/stable/_downloads/3a13d3ead4ddb2b01958ef9aa4ba440a/ticklabels_rotation.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)