[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/gtk4_spreadsheet_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/gtk4_spreadsheet_sgskip.html#sphx-glr-download-gallery-user-interfaces-gtk4-spreadsheet-sgskip-py)
 to download the full example code.

GTK4 spreadsheet[#](https://matplotlib.org/stable/gallery/user_interfaces/gtk4_spreadsheet_sgskip.html#gtk4-spreadsheet "Link to this heading")

================================================================================================================================================

Example of embedding Matplotlib in an application and interacting with a treeview to store data. Double-click on an entry to update plot data.

import gi

gi.require\_version('Gtk', '4.0')
gi.require\_version('Gdk', '4.0')
from gi.repository import Gtk

from numpy.random import [random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")

from matplotlib.backends.backend\_gtk4agg import FigureCanvas  \# or gtk4cairo.
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

class DataManager(Gtk.ApplicationWindow):
    num\_rows, num\_cols \= 20, 10

    data \= [random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
((num\_rows, num\_cols))

    def \_\_init\_\_(self, \*args, \*\*kwargs):
        super().\_\_init\_\_(\*args, \*\*kwargs)
        self.set\_default\_size(600, 600)

        self.set\_title('GtkListStore demo')

        vbox \= Gtk.Box(orientation\=Gtk.Orientation.VERTICAL, homogeneous\=False,
                       spacing\=8)
        self.set\_child(vbox)

        label \= Gtk.Label(label\='Double click a row to plot the data')
        vbox.append(label)

        sw \= Gtk.ScrolledWindow()
        sw.set\_has\_frame(True)
        sw.set\_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        sw.set\_hexpand(True)
        sw.set\_vexpand(True)
        vbox.append(sw)

        model \= self.create\_model()
        self.treeview \= Gtk.TreeView(model\=model)
        self.treeview.connect('row-activated', self.plot\_row)
        sw.set\_child(self.treeview)

        \# Matplotlib stuff
        fig \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(figsize\=(6, 4), layout\='constrained')

        self.canvas \= FigureCanvas(fig)  \# a Gtk.DrawingArea
        self.canvas.set\_hexpand(True)
        self.canvas.set\_vexpand(True)
        vbox.append(self.canvas)
        ax \= fig.add\_subplot()
        self.line, \= ax.plot(self.data\[0, :\], 'go')  \# plot the first row

        self.add\_columns()

    def plot\_row(self, treeview, path, view\_column):
        ind, \= path  \# get the index into data
        points \= self.data\[ind, :\]
        self.line.set\_ydata(points)
        self.canvas.draw()

    def add\_columns(self):
        for i in range(self.num\_cols):
            column \= Gtk.TreeViewColumn(str(i), Gtk.CellRendererText(), text\=i)
            self.treeview.append\_column(column)

    def create\_model(self):
        types \= \[float\] \* self.num\_cols
        store \= Gtk.ListStore(\*types)
        for row in self.data:
            \# Gtk.ListStore.append is broken in PyGObject, so insert manually.
            it \= store.insert(\-1)
            store.set(it, {i: val for i, val in enumerate(row)})
        return store

def on\_activate(app):
    manager \= DataManager(application\=app)
    manager.show()

app \= Gtk.Application(application\_id\='org.matplotlib.examples.GTK4Spreadsheet')
app.connect('activate', on\_activate)
app.run()

[`Download Jupyter notebook: gtk4_spreadsheet_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/63c3f047d0d7a15dd4d944f233371b01/gtk4_spreadsheet_sgskip.ipynb)

[`Download Python source code: gtk4_spreadsheet_sgskip.py`](https://matplotlib.org/stable/_downloads/609e4ae8a3631a6eb9c7d84bbc7d8de3/gtk4_spreadsheet_sgskip.py)

[`Download zipped: gtk4_spreadsheet_sgskip.zip`](https://matplotlib.org/stable/_downloads/124b59aadad62637160fa1453b44b747/gtk4_spreadsheet_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)