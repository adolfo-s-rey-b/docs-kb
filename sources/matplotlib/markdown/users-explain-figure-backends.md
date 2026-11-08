[Skip to main content](https://matplotlib.org/stable/users/explain/figure/backends.html#main-content)

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
    

Backends[#](https://matplotlib.org/stable/users/explain/figure/backends.html#backends "Link to this heading")

==============================================================================================================

What is a backend?[#](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Backends are used for displaying Matplotlib figures (see [Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-intro)
), on the screen, or for writing to files. A lot of documentation on the website and in the mailing lists refers to the "backend" and many new users are confused by this term. Matplotlib targets many different use cases and output formats. Some people use Matplotlib interactively from the Python shell and have plotting windows pop up when they type commands. Some people run [Jupyter](https://jupyter.org/)
 notebooks and draw inline plots for quick data analysis. Others embed Matplotlib into graphical user interfaces like PyQt or PyGObject to build rich applications. Some people use Matplotlib in batch scripts to generate postscript images from numerical simulations, and still others run web application servers to dynamically serve up graphs.

To support all of these use cases, Matplotlib can target different outputs, and each of these capabilities is called a backend; the "frontend" is the user facing code, i.e., the plotting code, whereas the "backend" does all the hard work behind-the-scenes to make the figure. There are two types of backends: user interface backends (for use in PyQt/PySide, PyGObject, Tkinter, wxPython, or macOS/Cocoa); also referred to as "interactive backends") and hardcopy backends to make image files (PNG, SVG, PDF, PS; also referred to as "non-interactive backends").

Selecting a backend[#](https://matplotlib.org/stable/users/explain/figure/backends.html#selecting-a-backend "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

There are three ways to configure your backend:

*   The `[rcParams["backend"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=backend#rcparam-backend) ` parameter in your `matplotlibrc` file
    
*   The [`MPLBACKEND`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLBACKEND)
     environment variable
    
*   The function [`matplotlib.use()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
    

Below is a more detailed description.

If there is more than one configuration present, the last one from the list takes precedence; e.g. calling [`matplotlib.use()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
 will override the setting in your `matplotlibrc`.

Without a backend explicitly set, Matplotlib automatically detects a usable backend based on what is available on your system and on whether a GUI event loop is already running. The first usable backend in the following list is selected: MacOSX, QtAgg, GTK4Agg, Gtk3Agg, TkAgg, WxAgg, Agg. The last, Agg, is a non-interactive backend that can only write to files. It is used on Linux, if Matplotlib cannot connect to either an X display or a Wayland display.

Here is a detailed description of the configuration methods:

1.  Setting `[rcParams["backend"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=backend#rcparam-backend) ` in your `matplotlibrc` file:
    
    backend : qtagg   \# use pyqt with antigrain (agg) rendering
    
    See also [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
    .
    
2.  Setting the [`MPLBACKEND`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLBACKEND)
     environment variable:
    
    You can set the environment variable either for your current shell or for a single script.
    
    On Unix:
    
    \> export MPLBACKEND\=qtagg
    \> python simple\_plot.py
    
    \> MPLBACKEND\=qtagg python simple\_plot.py
    
    On Windows, only the former is possible:
    
    \> set MPLBACKEND\=qtagg
    \> python simple\_plot.py
    
    Setting this environment variable will override the `backend` parameter in _any_ `matplotlibrc`, even if there is a `matplotlibrc` in your current working directory. Therefore, setting [`MPLBACKEND`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLBACKEND)
     globally, e.g. in your `.bashrc` or `.profile`, is discouraged as it might lead to counter-intuitive behavior.
    
3.  If your script depends on a specific backend you can use the function [`matplotlib.use()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
    :
    
    import matplotlib
    matplotlib.use('qtagg')
    
    This should be done before any figure is created, otherwise Matplotlib may fail to switch the backend and raise an ImportError.
    
    Using [`use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
     will require changes in your code if users want to use a different backend. Therefore, you should avoid explicitly calling [`use`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use "matplotlib.use")
     unless absolutely necessary.
    

The builtin backends[#](https://matplotlib.org/stable/users/explain/figure/backends.html#the-builtin-backends "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

By default, Matplotlib should automatically select a default backend which allows both interactive work and plotting from scripts, with output to the screen and/or to a file, so at least initially, you will not need to worry about the backend. The most common exception is if your Python distribution comes without [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "(in Python v3.14)")
 and you have no other GUI toolkit installed. This happens with certain Linux distributions, where you need to install a Linux package named `python-tk` (or similar).

If, however, you want to write graphical user interfaces, or a web application server ([Embed in a web application server (Flask)](https://matplotlib.org/stable/gallery/user_interfaces/web_application_server_sgskip.html)
), or need a better understanding of what is going on, read on. To make things easily more customizable for graphical user interfaces, Matplotlib separates the concept of the renderer (the thing that actually does the drawing) from the canvas (the place where the drawing goes). The canonical renderer for user interfaces is `Agg` which uses the [Anti-Grain Geometry](http://agg.sourceforge.net/antigrain.com/)
 C++ library to make a raster (pixel) image of the figure; it is used by the `QtAgg`, `GTK4Agg`, `GTK3Agg`, `wxAgg`, `TkAgg`, and `macosx` backends. An alternative renderer is based on the Cairo library, used by `QtCairo`, etc.

For the rendering engines, users can also distinguish between [vector](https://en.wikipedia.org/wiki/Vector_graphics)
 or [raster](https://en.wikipedia.org/wiki/Raster_graphics)
 renderers. Vector graphics languages issue drawing commands like "draw a line from this point to this point" and hence are scale free. Raster backends generate a pixel representation of the line whose accuracy depends on a DPI setting.

### Static backends[#](https://matplotlib.org/stable/users/explain/figure/backends.html#static-backends "Link to this heading")

Here is a summary of the Matplotlib renderers (there is an eponymous backend for each; these are _non-interactive backends_, capable of writing to a file):

| Renderer | Filetypes | Description |
| --- | --- | --- |
| AGG | png | [raster](https://en.wikipedia.org/wiki/Raster_graphics)<br> graphics -- high quality images using the [Anti-Grain Geometry](http://agg.sourceforge.net/antigrain.com/)<br> engine. |
| PDF | pdf | [vector](https://en.wikipedia.org/wiki/Vector_graphics)<br> graphics -- [Portable Document Format](https://en.wikipedia.org/wiki/Portable_Document_Format)<br> output. |
| PS  | ps, eps | [vector](https://en.wikipedia.org/wiki/Vector_graphics)<br> graphics -- [PostScript](https://en.wikipedia.org/wiki/PostScript)<br> output. |
| SVG | svg | [vector](https://en.wikipedia.org/wiki/Vector_graphics)<br> graphics -- [Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)<br> output. |
| PGF | pgf, pdf | [vector](https://en.wikipedia.org/wiki/Vector_graphics)<br> graphics -- using the [pgf](https://ctan.org/pkg/pgf)<br> package. |
| Cairo | png, ps, pdf, svg | [raster](https://en.wikipedia.org/wiki/Raster_graphics)<br> or [vector](https://en.wikipedia.org/wiki/Vector_graphics)<br> graphics -- using the [Cairo](https://www.cairographics.org/)<br> library (requires [pycairo](https://www.cairographics.org/pycairo/)<br> or [cairocffi](https://doc.courtbouillon.org/cairocffi/stable/)<br>). |

To save plots using the non-interactive backends, use the `matplotlib.pyplot.savefig('filename')` method.

### Interactive backends[#](https://matplotlib.org/stable/users/explain/figure/backends.html#interactive-backends "Link to this heading")

These are the user interfaces and renderer combinations supported; these are _interactive backends_, capable of displaying to the screen and using appropriate renderers from the table above to write to a file:

| Backend | Description |
| --- | --- |
| QtAgg | Agg rendering in a [Qt](https://qt.io/)<br> canvas (requires [PyQt](https://riverbankcomputing.com/software/pyqt/intro)<br> or [Qt for Python](https://doc.qt.io/qtforpython/)<br>, a.k.a. PySide). This backend can be activated in IPython with `%matplotlib qt`. The Qt binding can be selected via the [`QT_API`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-QT_API)<br> environment variable; see [Qt Bindings](https://matplotlib.org/stable/api/backend_qt_api.html#qt-bindings)<br> for more details. |
| ipympl | Agg rendering embedded in a Jupyter widget (requires [ipympl](https://www.matplotlib.org/ipympl)<br>). This backend can be enabled in a Jupyter notebook with `%matplotlib ipympl` or `%matplotlib widget`. Works with Jupyter `lab` and `notebook>=7`. |
| GTK3Agg | Agg rendering to a [GTK](https://www.gtk.org/)<br> 3.x canvas (requires [PyGObject](https://pygobject.gnome.org/)<br> and [pycairo](https://www.cairographics.org/pycairo/)<br>). This backend can be activated in IPython with `%matplotlib gtk3`. |
| GTK4Agg | Agg rendering to a [GTK](https://www.gtk.org/)<br> 4.x canvas (requires [PyGObject](https://pygobject.gnome.org/)<br> and [pycairo](https://www.cairographics.org/pycairo/)<br>). This backend can be activated in IPython with `%matplotlib gtk4`. |
| macosx | Agg rendering into a Cocoa canvas in macOS. This backend can be activated in IPython with `%matplotlib osx`. |
| TkAgg | Agg rendering to a [Tk](https://www.tcl.tk/)<br> canvas (requires [TkInter](https://docs.python.org/3/library/tk.html)<br>). This backend can be activated in IPython with `%matplotlib tk`. |
| nbAgg | Embed an interactive figure in a Jupyter classic notebook. This backend can be enabled in Jupyter notebooks via `%matplotlib notebook` or `%matplotlib nbagg`. Works with Jupyter `notebook<7` and `nbclassic`. |
| WebAgg | On `show()` will start a tornado server with an interactive figure. |
| GTK3Cairo | Cairo rendering to a [GTK](https://www.gtk.org/)<br> 3.x canvas (requires [PyGObject](https://pygobject.gnome.org/)<br> and [pycairo](https://www.cairographics.org/pycairo/)<br>). |
| GTK4Cairo | Cairo rendering to a [GTK](https://www.gtk.org/)<br> 4.x canvas (requires [PyGObject](https://pygobject.gnome.org/)<br> and [pycairo](https://www.cairographics.org/pycairo/)<br>). |
| wxAgg | Agg rendering to a [wxWidgets](https://www.wxwidgets.org/)<br> canvas (requires [wxPython](https://www.wxpython.org/)<br> 4). This backend can be activated in IPython with `%matplotlib wx`. |

Note

The names of builtin backends are case-insensitive; e.g., 'QtAgg' and 'qtagg' are equivalent.

### ipympl[#](https://matplotlib.org/stable/users/explain/figure/backends.html#ipympl-install "Link to this heading")

The ipympl backend is in a separate package that must be explicitly installed if you wish to use it, for example:

pip install ipympl

or

conda install ipympl \-c conda-forge

See [installing ipympl](https://matplotlib.org/ipympl/installing.html)
 for more details.

Using non-builtin backends[#](https://matplotlib.org/stable/users/explain/figure/backends.html#using-non-builtin-backends "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

More generally, any importable backend can be selected by using any of the methods above. If `name.of.the.backend` is the module containing the backend, use `module://name.of.the.backend` as the backend name, e.g. `matplotlib.use('module://name.of.the.backend')`.

Information for backend implementers is available at [Writing a backend -- the pyplot interface](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#writing-backend-interface)
.

Backend API versions[#](https://matplotlib.org/stable/users/explain/figure/backends.html#backend-api-versions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Matplotlib aims to maintain backward compatibility on backends. Nevertheless, we want to be able to evolve the backend API to support new features. Defining backend API versions will help to communicate which API is supported by a given version of Matplotlib.

The following backend API versions exist

| API version | Supported since | Description |
| --- | --- | --- |
| 1.0 | Matplotlib 3.10 | This is the starting point for systematic definition of backend versions. Most of the API will work far back, but there is no benefit in retroactively uncovering all prior the changes. |
| 1.1 | Matplotlib 3.11 | [`RendererBase.draw_path_collection`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path_collection "matplotlib.backend_bases.RendererBase.draw_path_collection")<br> gained a new optional parameter _hatchcolor_. The presence of the parameter is inferred by introspection, so that matplotlib 3.11+ will still work with backends implementing API version 1.0. |

There is currently no plan to remove support for older API versions.

Debugging the figure windows not showing[#](https://matplotlib.org/stable/users/explain/figure/backends.html#debugging-the-figure-windows-not-showing "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes things do not work as expected, usually during an install.

If you are using a Notebook or integrated development environment (see [Notebooks and IDEs](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#notebooks-and-ides)
), please consult their documentation for debugging figures not working in their environments.

If you are using one of Matplotlib's graphics backends (see [Standalone scripts and interactive use](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#standalone-scripts-and-interactive-use)
), make sure you know which one is being used:

import matplotlib

print(matplotlib.get\_backend())

Try a simple plot to see if the GUI opens:

import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get\_backend())
plt.plot((1, 4, 6))
plt.show()

If it does not, you perhaps have an installation problem. A good step at this point is to ensure that your GUI toolkit is installed properly, taking Matplotlib out of the testing. Almost all GUI toolkits have a small test program that can be run to test basic functionality. If this test fails, try re-installing.

### QtAgg, QtCairo, Qt5Agg, and Qt5Cairo[#](https://matplotlib.org/stable/users/explain/figure/backends.html#qtagg-qtcairo-qt5agg-and-qt5cairo "Link to this heading")

Test `PyQt6` (if you have `PyQt5`, `PySide2` or `PySide6` installed rather than `PyQt6`, just change the import accordingly):

python3 \-c "from PyQt6.QtWidgets import \*; app = QApplication(\[\]); win = QMainWindow(); win.show(); app.exec()"

### TkAgg and TkCairo[#](https://matplotlib.org/stable/users/explain/figure/backends.html#tkagg-and-tkcairo "Link to this heading")

Test `tkinter`:

python3 \-c "from tkinter import Tk; Tk().mainloop()"

### GTK3Agg, GTK4Agg, GTK3Cairo, GTK4Cairo[#](https://matplotlib.org/stable/users/explain/figure/backends.html#gtk3agg-gtk4agg-gtk3cairo-gtk4cairo "Link to this heading")

Test `Gtk`:

python3 \-c "from gi.repository import Gtk; win = Gtk.Window(); win.connect('destroy', Gtk.main\_quit); win.show(); Gtk.main()"

### wxAgg and wxCairo[#](https://matplotlib.org/stable/users/explain/figure/backends.html#wxagg-and-wxcairo "Link to this heading")

Test `wx`:

python3 \-c "import wx; app = wx.App(); frame = wx.Frame(None); frame.Show(); app.MainLoop()"

If the test works for your desired backend but you still cannot get Matplotlib to display a figure, then contact us (see [Get help](https://matplotlib.org/stable/users/faq.html#get-help)
).

On this page