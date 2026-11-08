[Skip to main content](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html#sphx-glr-download-gallery-widgets-mouse-cursor-py)
 to download the full example code.

Mouse Cursor[#](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html#mouse-cursor "Link to this heading")

=====================================================================================================================

This example sets an alternative cursor on a figure canvas.

Note, this is an interactive example, and must be run to see the effect.

import matplotlib.pyplot as plt

from matplotlib.backend\_tools import [Cursors](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(len([Cursors](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
), figsize\=(6, len([Cursors](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
) + 0.5),
                        gridspec\_kw\={'hspace': 0})
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Hover over an Axes to see alternate Cursors')

for [cursor](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in zip([Cursors](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.cursor\_to\_use](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
 \= [cursor](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, [cursor.name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
            horizontalalignment\='center', verticalalignment\='center')
    [ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xticks\=\[\], yticks\=\[\])

def hover(event):
    if [fig.canvas.widgetlock.locked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw.locked "matplotlib.widgets.LockDraw.locked")
():
        \# Don't do anything if the zoom/pan tools have been enabled.
        return

    [fig.canvas.set\_cursor](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.set_cursor "matplotlib.backend_bases.FigureCanvasBase.set_cursor")
(
        event.inaxes.cursor\_to\_use if event.inaxes else [Cursors.POINTER](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")
)

[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('motion\_notify\_event', hover)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Hover over an Axes to see alternate Cursors](https://matplotlib.org/stable/_images/sphx_glr_mouse_cursor_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.backend_bases.FigureCanvasBase.set_cursor`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.set_cursor "matplotlib.backend_bases.FigureCanvasBase.set_cursor")
    

[`Download Jupyter notebook: mouse_cursor.ipynb`](https://matplotlib.org/stable/_downloads/e00aa6c0f7c3dee563516cbeec608900/mouse_cursor.ipynb)

[`Download Python source code: mouse_cursor.py`](https://matplotlib.org/stable/_downloads/ab3f838084c7ddafe92dade4d05a6f67/mouse_cursor.py)

[`Download zipped: mouse_cursor.zip`](https://matplotlib.org/stable/_downloads/9c3319fce77044b37cb274c0ebaee03b/mouse_cursor.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)