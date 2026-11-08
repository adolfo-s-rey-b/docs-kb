[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html#sphx-glr-download-gallery-user-interfaces-embedding-in-qt-sgskip-py)
 to download the full example code.

Embed in Qt[#](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html#embed-in-qt "Link to this heading")

=====================================================================================================================================

Simple Qt application embedding Matplotlib canvases. This program will work equally well using any Qt binding (PyQt6, PySide6, PyQt5, PySide2). The binding can be selected by setting the [`QT_API`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-QT_API)
 environment variable to the binding name, or by first importing it.

import sys
import time

import numpy as np

from matplotlib.backends.backend\_qtagg import FigureCanvas
from matplotlib.backends.backend\_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt\_compat import QtWidgets
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

class ApplicationWindow(QtWidgets.QMainWindow):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.\_main \= QtWidgets.QWidget()
        self.setCentralWidget(self.\_main)
        layout \= QtWidgets.QVBoxLayout(self.\_main)

        static\_canvas \= FigureCanvas([Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(figsize\=(5, 3)))
        \# Ideally one would use self.addToolBar here, but it is slightly
        \# incompatible between PyQt6 and other bindings, so we just add the
        \# toolbar as a plain widget instead.
        layout.addWidget(NavigationToolbar(static\_canvas, self))
        layout.addWidget(static\_canvas)

        dynamic\_canvas \= FigureCanvas([Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(figsize\=(5, 3)))
        layout.addWidget(dynamic\_canvas)
        layout.addWidget(NavigationToolbar(dynamic\_canvas, self))

        self.\_static\_ax \= static\_canvas.figure.subplots()
        t \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 501)
        self.\_static\_ax.plot(t, [np.tan](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")
(t), ".")

        self.\_dynamic\_ax \= dynamic\_canvas.figure.subplots()
        \# Set up a Line2D.
        self.xdata \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 101)
        self.\_update\_ydata()
        self.\_line, \= self.\_dynamic\_ax.plot(self.xdata, self.ydata)
        \# The below two timers must be attributes of self, so that the garbage
        \# collector won't clean them after we finish with \_\_init\_\_...

        \# The data retrieval may be fast as possible (Using QRunnable could be
        \# even faster).
        self.data\_timer \= dynamic\_canvas.new\_timer(1)
        self.data\_timer.add\_callback(self.\_update\_ydata)
        self.data\_timer.start()
        \# Drawing at 50Hz should be fast enough for the GUI to feel smooth, and
        \# not too fast for the GUI to be overloaded with events that need to be
        \# processed while the GUI element is changed.
        self.drawing\_timer \= dynamic\_canvas.new\_timer(20)
        self.drawing\_timer.add\_callback(self.\_update\_canvas)
        self.drawing\_timer.start()

    def \_update\_ydata(self):
        \# Shift the sinusoid as a function of time.
        self.ydata \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(self.xdata + [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
())

    def \_update\_canvas(self):
        self.\_line.set\_data(self.xdata, self.ydata)
        \# It should be safe to use the synchronous draw() method for most drawing
        \# frequencies, but it is safer to use draw\_idle().
        self.\_line.figure.canvas.draw\_idle()

if \_\_name\_\_ \== "\_\_main\_\_":
    \# Check whether there is already a running QApplication (e.g., if running
    \# from an IDE).
    qapp \= QtWidgets.QApplication.instance()
    if not qapp:
        qapp \= QtWidgets.QApplication([sys.argv](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
)

    app \= ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise\_()
    qapp.exec()

[`Download Jupyter notebook: embedding_in_qt_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/2d9cfa13c32d1c42c7c8afa1f29c6702/embedding_in_qt_sgskip.ipynb)

[`Download Python source code: embedding_in_qt_sgskip.py`](https://matplotlib.org/stable/_downloads/d2dda06b1bb885ef976948ef6ce4650e/embedding_in_qt_sgskip.py)

[`Download zipped: embedding_in_qt_sgskip.zip`](https://matplotlib.org/stable/_downloads/b64bfdd9a139ffc77be638e4527dc49b/embedding_in_qt_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)