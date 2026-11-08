[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html#sphx-glr-download-gallery-specialty-plots-ishikawa-diagram-py)
 to download the full example code.

Ishikawa Diagram[#](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html#ishikawa-diagram "Link to this heading")

=========================================================================================================================================

Ishikawa Diagrams, fishbone diagrams, herringbone diagrams, or cause-and-effect diagrams are used to identify problems in a system by showing how causes and effects are linked. Source: [https://en.wikipedia.org/wiki/Ishikawa\_diagram](https://en.wikipedia.org/wiki/Ishikawa_diagram)

![ishikawa diagram](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_001_2_00x.png)

import math

import matplotlib.pyplot as plt

from matplotlib.patches import [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
, [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 6), layout\='constrained')
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-5, 5)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-5, 5)
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')

def problems(data: str,
             problem\_x: float, problem\_y: float,
             angle\_x: float, angle\_y: float):
    """
    Draw each problem section of the Ishikawa plot.

    Parameters
    ----------
    data : str
        The name of the problem category.
    problem\_x, problem\_y : float, optional
        The \`X\` and \`Y\` positions of the problem arrows (\`Y\` defaults to zero).
    angle\_x, angle\_y : float, optional
        The angle of the problem annotations. They are always angled towards
        the tail of the plot.

    Returns
    -------
    None.

    """
    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(str.upper(data), xy\=(problem\_x, problem\_y),
                xytext\=(angle\_x, angle\_y),
                fontsize\=10,
                color\='white',
                weight\='bold',
                xycoords\='data',
                verticalalignment\='center',
                horizontalalignment\='center',
                textcoords\='offset fontsize',
                arrowprops\=dict(arrowstyle\="->", facecolor\='black'),
                bbox\=dict(boxstyle\='square',
                          facecolor\='tab:blue',
                          pad\=0.8))

def causes(data: list,
           cause\_x: float, cause\_y: float,
           cause\_xytext\=(\-9, \-0.3), top: bool \= True):
    """
    Place each cause to a position relative to the problems
    annotations.

    Parameters
    ----------
    data : indexable object
        The input data. IndexError is
        raised if more than six arguments are passed.
    cause\_x, cause\_y : float
        The \`X\` and \`Y\` position of the cause annotations.
    cause\_xytext : tuple, optional
        Adjust to set the distance of the cause text from the problem
        arrow in fontsize units.
    top : bool, default: True
        Determines whether the next cause annotation will be
        plotted above or below the previous one.

    Returns
    -------
    None.

    """
    for index, cause in enumerate(data):
        \# \[<x pos>, <y pos>\]
        coords \= \[\[0.02, 0\],\
                  \[0.23, 0.5\],\
                  \[\-0.46, \-1\],\
                  \[0.69, 1.5\],\
                  \[\-0.92, \-2\],\
                  \[1.15, 2.5\]\]

        \# First 'cause' annotation is placed in the middle of the 'problems' arrow
        \# and each subsequent cause is plotted above or below it in succession.
        cause\_x \-= coords\[index\]\[0\]
        cause\_y += coords\[index\]\[1\] if top else \-coords\[index\]\[1\]

        [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(cause, xy\=(cause\_x, cause\_y),
                    horizontalalignment\='center',
                    xytext\=cause\_xytext,
                    fontsize\=9,
                    xycoords\='data',
                    textcoords\='offset fontsize',
                    arrowprops\=dict(arrowstyle\="->",
                                    facecolor\='black'))

def draw\_body(data: dict):
    """
    Place each problem section in its correct place by changing
    the coordinates on each loop.

    Parameters
    ----------
    data : dict
        The input data (can be a dict of lists or tuples). ValueError
        is raised if more than six arguments are passed.

    Returns
    -------
    None.

    """
    \# Set the length of the spine according to the number of 'problem' categories.
    length \= ([math.ceil](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
(len(data) / 2)) \- 1
    draw\_spine(\-2 \- length, 2 + length)

    \# Change the coordinates of the 'problem' annotations after each one is rendered.
    offset \= 0
    prob\_section \= \[1.55, 0.8\]
    for index, problem in enumerate(data.values()):
        plot\_above \= index % 2 \== 0
        cause\_arrow\_y \= 1.7 if plot\_above else \-1.7
        y\_prob\_angle \= 16 if plot\_above else \-16

        \# Plot each section in pairs along the main spine.
        prob\_arrow\_x \= prob\_section\[0\] + length + offset
        cause\_arrow\_x \= prob\_section\[1\] + length + offset
        if not plot\_above:
            offset \-= 2.5
        if index \> 5:
            raise ValueError(f'Maximum number of problems is 6, you have entered '
                             f'{len(data)}')

        problems(list(data.keys())\[index\], prob\_arrow\_x, 0, \-12, y\_prob\_angle)
        causes(problem, cause\_arrow\_x, cause\_arrow\_y, top\=plot\_above)

def draw\_spine(xmin: int, xmax: int):
    """
    Draw main spine, head and tail.

    Parameters
    ----------
    xmin : int
        The default position of the head of the spine's
        x-coordinate.
    xmax : int
        The default position of the tail of the spine's
        x-coordinate.

    Returns
    -------
    None.

    """
    \# draw main spine
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[xmin \- 0.1, xmax\], \[0, 0\], color\='tab:blue', linewidth\=2)
    \# draw fish head
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(xmax + 0.1, \- 0.05, 'PROBLEM', fontsize\=10,
            weight\='bold', color\='white')
    semicircle \= [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
((xmax, 0), 1, 270, 90, fc\='tab:blue')
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
(semicircle)
    \# draw fish tail
    tail\_pos \= \[\[xmin \- 0.8, 0.8\], \[xmin \- 0.8, \-0.8\], \[xmin, \-0.01\]\]
    triangle \= [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
(tail\_pos, fc\='tab:blue')
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
(triangle)

\# Input data
[categories](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'Method': \['Time consumption', 'Cost', 'Procedures', 'Inefficient process',\
               'Sampling'\],
    'Machine': \['Faulty equipment', 'Compatibility'\],
    'Material': \['Poor-quality input', 'Raw materials', 'Supplier',\
                 'Shortage'\],
    'Measurement': \['Calibration', 'Performance', 'Wrong measurements'\],
    'Environment': \['Bad conditions'\],
    'People': \['Lack of training', 'Managers', 'Labor shortage',\
               'Procedures', 'Sales strategy'\]
}

draw\_body([categories](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 2.286 seconds)

[`Download Jupyter notebook: ishikawa_diagram.ipynb`](https://matplotlib.org/stable/_downloads/7d99c3aa73e6c40a9f897008b1317fd0/ishikawa_diagram.ipynb)

[`Download Python source code: ishikawa_diagram.py`](https://matplotlib.org/stable/_downloads/62d302782de8431ec58cf4a62e047c8a/ishikawa_diagram.py)

[`Download zipped: ishikawa_diagram.zip`](https://matplotlib.org/stable/_downloads/3e57e1c0a6063ec6f3de7624ed59bb40/ishikawa_diagram.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)