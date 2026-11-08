[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/mplcvd.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/mplcvd.html#sphx-glr-download-gallery-user-interfaces-mplcvd-py)
 to download the full example code.

mplcvd -- an example of figure hook[#](https://matplotlib.org/stable/gallery/user_interfaces/mplcvd.html#mplcvd-an-example-of-figure-hook "Link to this heading")

==================================================================================================================================================================

To use this hook, ensure that this module is in your `PYTHONPATH`, and set `rcParams["figure.hooks"] = ["mplcvd:setup"]`. This hook depends on the `colorspacious` third-party module.

![mplcvd](https://matplotlib.org/stable/_images/sphx_glr_mplcvd_001_2_00x.png)

import functools
from pathlib import [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")

from PIL import Image
import colorspacious

import numpy as np

[\_BUTTON\_NAME](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= "Filter"
[\_BUTTON\_HELP](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= "Simulate color vision deficiencies"
[\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    "None": None,
    "Greyscale": "greyscale",
    "Deuteranopia": "deuteranomaly",
    "Protanopia": "protanomaly",
    "Tritanopia": "tritanomaly",
}

def \_get\_color\_filter(name):
    """
    Given a color filter name, create a color filter function.

    Parameters
    ----------
    name : str
        The color filter name, one of the following:

        - \`\`"none"\`\`: ...
        - \`\`"greyscale"\`\`: Convert the input to luminosity.
        - \`\`"deuteranopia"\`\`: Simulate the most common form of red-green
          colorblindness.
        - \`\`"protanopia"\`\`: Simulate a rarer form of red-green colorblindness.
        - \`\`"tritanopia"\`\`: Simulate the rare form of blue-yellow
          colorblindness.

        Color conversions use \`colorspacious\`\_.

    Returns
    -------
    callable
        A color filter function that has the form:

        def filter(input: np.ndarray\[M, N, D\])-> np.ndarray\[M, N, D\]

        where (M, N) are the image dimensions, and D is the color depth (3 for
        RGB, 4 for RGBA). Alpha is passed through unchanged and otherwise
        ignored.
    """
    if name not in [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
:
        raise ValueError(f"Unsupported filter name: {name!r}")
    name \= [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[name\]

    if name is None:
        return None

    elif name \== "greyscale":
        rgb\_to\_jch \= colorspacious.cspace\_converter("sRGB1", "JCh")
        jch\_to\_rgb \= colorspacious.cspace\_converter("JCh", "sRGB1")

        def convert(im):
            greyscale\_JCh \= rgb\_to\_jch(im)
            greyscale\_JCh\[..., 1\] \= 0
            im \= jch\_to\_rgb(greyscale\_JCh)
            return im

    else:
        cvd\_space \= {"name": "sRGB1+CVD", "cvd\_type": name, "severity": 100}
        convert \= colorspacious.cspace\_converter(cvd\_space, "sRGB1")

    def filter\_func(im, dpi):
        alpha \= None
        if im.shape\[\-1\] \== 4:
            im, alpha \= im\[..., :3\], im\[..., 3\]
        im \= convert(im)
        if alpha is not None:
            im \= [np.dstack](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")
((im, alpha))
        return [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(im, 0, 1), 0, 0

    return filter\_func

def \_set\_menu\_entry(tb, name):
    tb.canvas.figure.set\_agg\_filter(\_get\_color\_filter(name))
    tb.canvas.draw\_idle()

def setup(figure):
    tb \= figure.canvas.toolbar
    if tb is None:
        return
    for cls in type(tb).\_\_mro\_\_:
        pkg \= cls.\_\_module\_\_.split(".")\[0\]
        if pkg != "matplotlib":
            break
    if pkg \== "gi":
        \_setup\_gtk(tb)
    elif pkg in ("PyQt5", "PySide2", "PyQt6", "PySide6"):
        \_setup\_qt(tb)
    elif pkg \== "tkinter":
        \_setup\_tk(tb)
    elif pkg \== "wx":
        \_setup\_wx(tb)
    else:
        raise NotImplementedError("The current backend is not supported")

def \_setup\_gtk(tb):
    from gi.repository import Gio, GLib, Gtk

    for idx in range(tb.get\_n\_items()):
        children \= tb.get\_nth\_item(idx).get\_children()
        if children and isinstance(children\[0\], Gtk.Label):
            break

    toolitem \= Gtk.SeparatorToolItem()
    tb.insert(toolitem, idx)

    image \= Gtk.Image.new\_from\_gicon(
        Gio.Icon.new\_for\_string(
            str([Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
(\_\_file\_\_).parent / "images/eye-symbolic.svg")),
        Gtk.IconSize.LARGE\_TOOLBAR)

    \# The type of menu is progressively downgraded depending on GTK version.
    if Gtk.check\_version(3, 6, 0) is None:

        group \= Gio.SimpleActionGroup.new()
        action \= Gio.SimpleAction.new\_stateful("cvdsim",
                                               GLib.VariantType("s"),
                                               GLib.Variant("s", "none"))
        group.add\_action(action)

        @functools.partial(action.connect, "activate")
        def set\_filter(action, parameter):
            \_set\_menu\_entry(tb, parameter.get\_string())
            action.set\_state(parameter)

        menu \= Gio.Menu()
        for name in [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
:
            menu.append(name, f"local.cvdsim::{name}")

        button \= Gtk.MenuButton.new()
        button.remove(button.get\_children()\[0\])
        button.add(image)
        button.insert\_action\_group("local", group)
        button.set\_menu\_model(menu)
        button.get\_style\_context().add\_class("flat")

        item \= Gtk.ToolItem()
        item.add(button)
        tb.insert(item, idx + 1)

    else:

        menu \= Gtk.Menu()
        group \= \[\]
        for name in [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
:
            item \= Gtk.RadioMenuItem.new\_with\_label(group, name)
            item.set\_active(name \== "None")
            item.connect(
                "activate", lambda item: \_set\_menu\_entry(tb, item.get\_label()))
            group.append(item)
            menu.append(item)
        menu.show\_all()

        tbutton \= Gtk.MenuToolButton.new(image, [\_BUTTON\_NAME](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
        tbutton.set\_menu(menu)
        tb.insert(tbutton, idx + 1)

    tb.show\_all()

def \_setup\_qt(tb):
    from matplotlib.backends.qt\_compat import QtGui, QtWidgets

    menu \= QtWidgets.QMenu()
    try:
        QActionGroup \= QtGui.QActionGroup  \# Qt6
    except AttributeError:
        QActionGroup \= QtWidgets.QActionGroup  \# Qt5
    group \= QActionGroup(menu)
    group.triggered.connect(lambda action: \_set\_menu\_entry(tb, action.text()))

    for name in [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
:
        action \= menu.addAction(name)
        action.setCheckable(True)
        action.setActionGroup(group)
        action.setChecked(name \== "None")

    actions \= tb.actions()
    before \= next(
        (action for action in actions
         if isinstance(tb.widgetForAction(action), QtWidgets.QLabel)), None)

    tb.insertSeparator(before)
    button \= QtWidgets.QToolButton()
    \# FIXME: \_icon needs public API.
    button.setIcon(tb.\_icon(str([Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
(\_\_file\_\_).parent / "images/eye.png")))
    button.setText([\_BUTTON\_NAME](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    button.setToolTip([\_BUTTON\_HELP](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    button.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
    button.setMenu(menu)
    tb.insertWidget(before, button)

def \_setup\_tk(tb):
    import tkinter as tk

    tb.\_Spacer()  \# FIXME: \_Spacer needs public API.

    button \= [tk.Menubutton](https://docs.python.org/3/library/tkinter.html#tkinter.Menubutton "tkinter.Menubutton")
(master\=tb, relief\="raised")
    button.\_image\_file \= str([Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
(\_\_file\_\_).parent / "images/eye.png")
    \# FIXME: \_set\_image\_for\_button needs public API (perhaps like \_icon).
    tb.\_set\_image\_for\_button(button)
    button.pack(side\=[tk.LEFT](https://docs.python.org/3/library/tkinter.html#tkinter.LEFT "tkinter.LEFT")
)

    menu \= [tk.Menu](https://docs.python.org/3/library/tkinter.html#tkinter.Menu "tkinter.Menu")
(master\=button, tearoff\=False)
    for name in [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
:
        menu.add("radiobutton", label\=name,
                 command\=lambda \_name\=name: \_set\_menu\_entry(tb, \_name))
    menu.invoke(0)
    button.config(menu\=menu)

def \_setup\_wx(tb):
    import wx

    idx \= next(idx for idx in range(tb.ToolsCount)
               if tb.GetToolByPos(idx).IsStretchableSpace())
    tb.InsertSeparator(idx)
    tool \= tb.InsertTool(
        idx + 1, \-1, [\_BUTTON\_NAME](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
        \# FIXME: \_icon needs public API.
        tb.\_icon(str([Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
(\_\_file\_\_).parent / "images/eye.png")),
        \# FIXME: ITEM\_DROPDOWN is not supported on macOS.
        kind\=wx.ITEM\_DROPDOWN, shortHelp\=[\_BUTTON\_HELP](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

    menu \= [wx.Menu](https://docs.wxpython.org/wx.Menu.html#wx.Menu "wx.Menu")
()
    for name in [\_MENU\_ENTRIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
:
        item \= menu.AppendRadioItem(\-1, name)
        menu.Bind(
            wx.EVT\_MENU,
            lambda event, \_name\=name: \_set\_menu\_entry(tb, \_name),
            id\=item.Id,
        )
    tb.SetDropdownMenu(tool.Id, menu)

if \_\_name\_\_ \== '\_\_main\_\_':
    import matplotlib.pyplot as plt

    from matplotlib import cbook

    [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['figure.hooks'\].append('mplcvd:setup')

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(
        \[\
            \['viridis', 'turbo'\],\
            \['photo', 'lines'\]\
        \]
    )

    [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.025
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3.0, 3.0, [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
    [Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2 \- ([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2)
    [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* 2

    [imv](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['viridis'\].imshow(
        [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\='bilinear',
        origin\='lower', extent\=\[\-3, 3, \-3, 3\],
        vmax\=abs([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
).max(), vmin\=-abs([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
).max()
    )
    [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([imv](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)
    [imt](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['turbo'\].imshow(
        [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\='bilinear', cmap\='turbo',
        origin\='lower', extent\=\[\-3, 3, \-3, 3\],
        vmax\=abs([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
).max(), vmin\=-abs([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
).max()
    )
    [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([imt](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)

    \# A sample image
    [photo](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.JpegImagePlugin.JpegImageFile "PIL.JpegImagePlugin.JpegImageFile")
 \= [Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
([cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("grace\_hopper.jpg"))
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['photo'\].imshow([photo](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.JpegImagePlugin.JpegImageFile "PIL.JpegImagePlugin.JpegImageFile")
)

    [th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 1024)
    for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in \[1, 2, 4, 6\]:
        [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['lines'\].plot([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([th](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
), label\=f'$\\\\omega={[j](https://docs.python.org/3/library/functions.html#int "builtins.int")
}$')
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['lines'\].legend(ncols\=2, loc\='upper right')
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: mplcvd.ipynb`](https://matplotlib.org/stable/_downloads/39a3d569f6f4511ef5146ca55946aadd/mplcvd.ipynb)

[`Download Python source code: mplcvd.py`](https://matplotlib.org/stable/_downloads/d9f4b1654a82f25de62373447d69707c/mplcvd.py)

[`Download zipped: mplcvd.zip`](https://matplotlib.org/stable/_downloads/19ce71c9d86780706b1f82f0c789f648/mplcvd.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)