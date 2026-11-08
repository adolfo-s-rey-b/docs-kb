[Skip to main content](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html#sphx-glr-download-gallery-widgets-annotated-cursor-py)
 to download the full example code.

Annotated cursor[#](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html#annotated-cursor "Link to this heading")

=================================================================================================================================

Display a data cursor including a text box, which shows the plot point close to the mouse pointer.

The new cursor inherits from [`Cursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "matplotlib.widgets.Cursor")
 and demonstrates the creation of new widgets and their event callbacks.

See also the [cross hair cursor](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html)
, which implements a cursor tracking the plotted data, but without using inheritance and without displaying the currently tracked coordinates.

Note

The figure related to this example does not show the cursor, because that figure is automatically created in a build queue, where the first mouse movement, which triggers the cursor creation, is missing.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backend\_bases import [MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
from matplotlib.widgets import [Cursor](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "matplotlib.widgets.Cursor")

class AnnotatedCursor([Cursor](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "matplotlib.widgets.Cursor")
):
    """
    A crosshair cursor like \`~matplotlib.widgets.Cursor\` with a text showing \\
    the current coordinates.

    For the cursor to remain responsive you must keep a reference to it.
    The data of the axis specified as \*dataaxis\* must be in ascending
    order. Otherwise, the \`numpy.searchsorted\` call might fail and the text
    disappears. You can satisfy the requirement by sorting the data you plot.
    Usually the data is already sorted (if it was created e.g. using
    \`numpy.linspace\`), but e.g. scatter plots might cause this problem.
    The cursor sticks to the plotted line.

    Parameters
    ----------
    line : \`matplotlib.lines.Line2D\`
        The plot line from which the data coordinates are displayed.

    numberformat : \`python format string <https://docs.python.org/3/\\
    library/string.html#formatstrings>\`\_, optional, default: "{0:.4g};{1:.4g}"
        The displayed text is created by calling \*format()\* on this string
        with the two coordinates.

    offset : (float, float) default: (5, 5)
        The offset in display (pixel) coordinates of the text position
        relative to the cross-hair.

    dataaxis : {"x", "y"}, optional, default: "x"
        If "x" is specified, the vertical cursor line sticks to the mouse
        pointer. The horizontal cursor line sticks to \*line\*
        at that x value. The text shows the data coordinates of \*line\*
        at the pointed x value. If you specify "y", it works in the opposite
        manner. But: For the "y" value, where the mouse points to, there might
        be multiple matching x values, if the plotted function is not biunique.
        Cursor and text coordinate will always refer to only one x value.
        So if you use the parameter value "y", ensure that your function is
        biunique.

    Other Parameters
    ----------------
    textprops : \`matplotlib.text\` properties as dictionary
        Specifies the appearance of the rendered text object.

    \*\*cursorargs : \`matplotlib.widgets.Cursor\` properties
        Arguments passed to the internal \`~matplotlib.widgets.Cursor\` instance.
        The \`matplotlib.axes.Axes\` argument is mandatory! The parameter
        \*useblit\* can be set to \*True\* in order to achieve faster rendering.

    """

    def \_\_init\_\_(self, [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, numberformat\="{0:.4g};{1:.4g}", offset\=(5, 5),
                 dataaxis\='x', textprops\=None, \*\*cursorargs):
        if textprops is None:
            textprops \= {}
        \# The line object, for which the coordinates are displayed
        self.[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
        \# The format string, on which .format() is called for creating the text
        self.numberformat \= numberformat
        \# Text position offset
        self.offset \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(offset)
        \# The axis in which the cursor position is looked up
        self.dataaxis \= dataaxis

        \# First call baseclass constructor.
        \# Draws cursor and remembers background for blitting.
        \# Saves ax as class attribute.
        super().\_\_init\_\_(\*\*cursorargs)

        \# Default value for position of text.
        self.set\_position(self.[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.get\_xdata()\[0\], self.[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.get\_ydata()\[0\])
        \# Create invisible animated text
        self.text \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.text(
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_xbound()\[0\],
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_ybound()\[0\],
            "0, 0",
            animated\=bool(self.useblit),
            visible\=False, \*\*textprops)
        \# The position at which the cursor was last drawn
        self.lastdrawnplotpoint \= None

    def onmove(self, event):
        """
        Overridden draw callback for cursor. Called when moving the mouse.
        """

        \# Leave method under the same conditions as in overridden method
        if self.ignore(event):
            self.lastdrawnplotpoint \= None
            return
        if not self.canvas.widgetlock.available(self):
            self.lastdrawnplotpoint \= None
            return

        \# If the mouse left drawable area, we now make the text invisible.
        \# Baseclass will redraw complete canvas after, which makes both text
        \# and cursor disappear.
        if event.inaxes != self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
:
            self.lastdrawnplotpoint \= None
            self.text.set\_visible(False)
            super().onmove(event)
            return

        \# Get the coordinates, which should be displayed as text,
        \# if the event coordinates are valid.
        plotpoint \= None
        if event.xdata is not None and event.ydata is not None:
            \# Get plot point related to current x position.
            \# These coordinates are displayed in text.
            plotpoint \= self.set\_position(event.xdata, event.ydata)
            \# Modify event, such that the cursor is displayed on the
            \# plotted line, not at the mouse pointer,
            \# if the returned plot point is valid
            if plotpoint is not None:
                event.xdata \= plotpoint\[0\]
                event.ydata \= plotpoint\[1\]

        \# If the plotpoint is given, compare to last drawn plotpoint and
        \# return if they are the same.
        \# Skip even the call of the base class, because this would restore the
        \# background, draw the cursor lines and would leave us the job to
        \# re-draw the text.
        if plotpoint is not None and plotpoint \== self.lastdrawnplotpoint:
            return

        \# Baseclass redraws canvas and cursor. Due to blitting,
        \# the added text is removed in this call, because the
        \# background is redrawn.
        super().onmove(event)

        \# Check if the display of text is still necessary.
        \# If not, just return.
        \# This behaviour is also cloned from the base class.
        if not self.get\_active() or not self.visible:
            return

        \# Draw the widget, if event coordinates are valid.
        if plotpoint is not None:
            \# Update position and displayed text.
            \# Position: Where the event occurred.
            \# Text: Determined by set\_position() method earlier
            \# Position is transformed to pixel coordinates,
            \# an offset is added there and this is transformed back.
            temp \= \[event.xdata, event.ydata\]
            temp \= self.[ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
.transform(temp)
            temp \= temp + self.offset
            temp \= self.[ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
.inverted().transform(temp)
            self.text.set\_position(temp)
            self.text.set\_text(self.numberformat.format(\*plotpoint))
            self.text.set\_visible(self.visible)

            \# Tell base class, that we have drawn something.
            \# Baseclass needs to know, that it needs to restore a clean
            \# background, if the cursor leaves our figure context.
            self.needclear \= True

            \# Remember the recently drawn cursor position, so events for the
            \# same position (mouse moves slightly between two plot points)
            \# can be skipped
            self.lastdrawnplotpoint \= plotpoint
        \# otherwise, make text invisible
        else:
            self.text.set\_visible(False)

        \# Draw changes. Cannot use \_update method of baseclass,
        \# because it would first restore the background, which
        \# is done already and is not necessary.
        if self.useblit:
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.text)
            self.canvas.blit(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)
        else:
            \# If blitting is deactivated, the overridden \_update call made
            \# by the base class immediately returned.
            \# We still have to draw the changes.
            self.canvas.draw\_idle()

    def set\_position(self, xpos, ypos):
        """
        Finds the coordinates, which have to be shown in text.

        The behaviour depends on the \*dataaxis\* attribute. Function looks
        up the matching plot coordinate for the given mouse position.

        Parameters
        ----------
        xpos : float
            The current x position of the cursor in data coordinates.
            Important if \*dataaxis\* is set to 'x'.
        ypos : float
            The current y position of the cursor in data coordinates.
            Important if \*dataaxis\* is set to 'y'.

        Returns
        -------
        ret : {2D array-like, None}
            The coordinates which should be displayed.
            \*None\* is the fallback value.
        """

        \# Get plot line data
        xdata \= self.[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.get\_xdata()
        ydata \= self.[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.get\_ydata()

        \# The dataaxis attribute decides, in which axis we look up which cursor
        \# coordinate.
        if self.dataaxis \== 'x':
            pos \= xpos
            data \= xdata
            lim \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_xlim()
        elif self.dataaxis \== 'y':
            pos \= ypos
            data \= ydata
            lim \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_ylim()
        else:
            raise ValueError(f"The data axis specifier {self.dataaxis} should "
                             f"be 'x' or 'y'")

        \# If position is valid and in valid plot data range.
        if pos is not None and lim\[0\] <= pos <= lim\[\-1\]:
            \# Find closest x value in sorted x vector.
            \# This requires the plotted data to be sorted.
            index \= [np.searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
(data, pos)
            \# Return none, if this index is out of range.
            if index < 0 or index \>= len(data):
                return None
            \# Return plot point as tuple.
            return (xdata\[index\], ydata\[index\])

        \# Return none if there is no good related point for this x position.
        return None

    def clear(self, event):
        """
        Overridden clear callback for cursor, called before drawing the figure.
        """

        \# The base class saves the clean background for blitting.
        \# Text and cursor are invisible,
        \# until the first mouse move event occurs.
        super().clear(event)
        if self.ignore(event):
            return
        self.text.set\_visible(False)

    def \_update(self):
        """
        Overridden method for either blitting or drawing the widget canvas.

        Passes call to base class if blitting is activated, only.
        In other cases, one draw\_idle call is enough, which is placed
        explicitly in this class (see \*onmove()\*).
        In that case, \`~matplotlib.widgets.Cursor\` is not supposed to draw
        something using this method.
        """

        if self.useblit:
            super().\_update()

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 6))
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Cursor Tracking x Position")

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, 1000)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2

[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-5, 5)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 25)

\# A minimum call
\# Set useblit=True on most backends for enhanced performance
\# and pass the ax parameter to the Cursor base class.
\# cursor = AnnotatedCursor(line=lin\[0\], ax=ax, useblit=True)

\# A more advanced call. Properties for text and lines are passed.
\# Watch the passed color names and the color of cursor line and text, to
\# relate the passed options to graphical elements.
\# The dataaxis parameter is still the default.
cursor \= [AnnotatedCursor](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "matplotlib.widgets.Cursor")
(
    [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
\=[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,
    numberformat\="{0:.2f}\\n{1:.2f}",
    dataaxis\='x', offset\=\[10, 10\],
    textprops\={'color': 'blue', 'fontweight': 'bold'},
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    useblit\=True,
    color\='red',
    linewidth\=2)

\# Simulate a mouse move to (-2, 10), needed for online docs
[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
[MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
(
    "motion\_notify\_event", [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
, \*[t.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((\-2, 10))
).\_process()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Cursor Tracking x Position](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_001_2_00x.png)

Trouble with non-biunique functions[#](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html#trouble-with-non-biunique-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

A call demonstrating problems with the _dataaxis=y_ parameter. The text now looks up the matching x value for the current cursor y position instead of vice versa. Hover your cursor to y=4. There are two x values producing this y value: -2 and 2. The function is only unique, but not biunique. Only one value is shown in the text.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 6))
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Cursor Tracking y Position")

[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-5, 5)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 25)

cursor \= [AnnotatedCursor](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Cursor.html#matplotlib.widgets.Cursor "matplotlib.widgets.Cursor")
(
    [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
\=[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,
    numberformat\="{0:.2f}\\n{1:.2f}",
    dataaxis\='y', offset\=\[10, 10\],
    textprops\={'color': 'blue', 'fontweight': 'bold'},
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    useblit\=True,
    color\='red', linewidth\=2)

\# Simulate a mouse move to (-2, 10), needed for online docs
[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
[MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
(
    "motion\_notify\_event", [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
, \*[t.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((\-2, 10))
).\_process()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Cursor Tracking y Position](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_002_2_00x.png)

**Total running time of the script:** (0 minutes 1.323 seconds)

[`Download Jupyter notebook: annotated_cursor.ipynb`](https://matplotlib.org/stable/_downloads/db5cc7baf9240668548384e96a701dd6/annotated_cursor.ipynb)

[`Download Python source code: annotated_cursor.py`](https://matplotlib.org/stable/_downloads/49afaefa9a6da5dbbf0e8baa083505f3/annotated_cursor.py)

[`Download zipped: annotated_cursor.zip`](https://matplotlib.org/stable/_downloads/ee7b347e3a3e182d554f053bec0fb155/annotated_cursor.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page