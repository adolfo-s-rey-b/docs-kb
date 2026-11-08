[Skip to main content](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#main-content)

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
    

Matplotlib Application Interfaces (APIs)[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#matplotlib-application-interfaces-apis "Link to this heading")

==================================================================================================================================================================================

Matplotlib has two major application interfaces, or styles of using the library:

*   An explicit "Axes" interface that uses methods on a Figure or Axes object to create other Artists, and build a visualization step by step. This has also been called an "object-oriented" interface.
    
*   An implicit "pyplot" interface that keeps track of the last Figure and Axes created, and adds Artists to the object it thinks the user wants.
    

In addition, a number of downstream libraries (like [`pandas`](https://pandas.pydata.org/docs/index.html#module-pandas "(in pandas v3.0.5)")
 and [xarray](https://xarray.pydata.org/)
) offer a `plot` method implemented directly on their data classes so that users can call `data.plot()`.

The difference between these interfaces can be a bit confusing, particularly given snippets on the web that use one or the other, or sometimes multiple interfaces in the same example. Here we attempt to point out how the "pyplot" and downstream interfaces relate to the explicit "Axes" interface to help users better navigate the library.

Native Matplotlib interfaces[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#native-matplotlib-interfaces "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

### The explicit "Axes" interface[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#the-explicit-axes-interface "Link to this heading")

The "Axes" interface is how Matplotlib is implemented, and many customizations and fine-tuning end up being done at this level.

This interface works by instantiating an instance of a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class (`fig` below), using a [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 method (or similar) on that object to create one or more [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 objects (`ax` below), and then calling drawing methods on the Axes (`plot` in this example):

import matplotlib.pyplot as plt

fig \= plt.figure()
ax \= fig.subplots()
ax.plot(\[1, 2, 3, 4\], \[0, 0.5, 1, 0.2\])

([`Source code`](https://matplotlib.org/stable/_downloads/0650ac31ae865e1ee5c066918050ed70/api_interfaces-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/74b74f830127b0972d831d7a52ebb3ba/api_interfaces-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/482ca5c1a817a9a4e57e96cea74d57a0/api_interfaces-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-1.2x.png)

We call this an "explicit" interface because each object is explicitly referenced, and used to make the next object. Keeping references to the objects is very flexible, and allows us to customize the objects after they are created, but before they are displayed.

### The implicit "pyplot" interface[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#the-implicit-pyplot-interface "Link to this heading")

The [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 module shadows most of the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 plotting methods to give the equivalent of the above, where the creation of the Figure and Axes is done for the user:

import matplotlib.pyplot as plt

plt.plot(\[1, 2, 3, 4\], \[0, 0.5, 1, 0.2\])

([`Source code`](https://matplotlib.org/stable/_downloads/1cd05998172b1e84cc01002b92058f74/api_interfaces-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/0c0aeafa6cb4182ac2a253e9a829df45/api_interfaces-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5708861e7abc2ea4a560f608922dea2e/api_interfaces-2.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-2.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-2.2x.png)

This can be convenient, particularly when doing interactive work or simple scripts. A reference to the current Figure can be retrieved using [`gcf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf")
 and to the current Axes by [`gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
. The [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 module retains a list of Figures, and each Figure retains a list of Axes on the figure for the user so that the following:

import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot(\[1, 2, 3\], \[0, 0.5, 0.2\])

plt.subplot(1, 2, 2)
plt.plot(\[3, 2, 1\], \[0, 0.5, 0.2\])

([`Source code`](https://matplotlib.org/stable/_downloads/d88ac9e699cfda725236b50cc469f54d/api_interfaces-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/2725411fdf4f3d8a95a0b9d10c218a55/api_interfaces-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/1a995d0861603b3fa93a99554b72f6a3/api_interfaces-3.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-3.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-3.2x.png)

is equivalent to:

import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
ax \= plt.gca()
ax.plot(\[1, 2, 3\], \[0, 0.5, 0.2\])

plt.subplot(1, 2, 2)
ax \= plt.gca()
ax.plot(\[3, 2, 1\], \[0, 0.5, 0.2\])

([`Source code`](https://matplotlib.org/stable/_downloads/4b6a5243faccf249b74270520c9b3eb8/api_interfaces-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ca099c09640e59438f30cc412cc86de8/api_interfaces-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/cad1bd51961e161a44e6d7589bc53da7/api_interfaces-4.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-4.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-4.2x.png)

In the explicit interface, this would be:

import matplotlib.pyplot as plt

fig, axs \= plt.subplots(1, 2)
axs\[0\].plot(\[1, 2, 3\], \[0, 0.5, 0.2\])
axs\[1\].plot(\[3, 2, 1\], \[0, 0.5, 0.2\])

([`Source code`](https://matplotlib.org/stable/_downloads/bb3a764581890aea3c0ea53b61d597e3/api_interfaces-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/16fdf5a8ba72d589d6057adf5472c030/api_interfaces-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ff53fbea1f06d4e260ecc522254311ae/api_interfaces-5.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-5.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-5.2x.png)

### Translating between the Axes interface and the pyplot interface[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#translating-between-the-axes-interface-and-the-pyplot-interface "Link to this heading")

You may find either interface in existing code, and unfortunately sometimes even mixtures. This section describes the patterns for specific operations in both interfaces and how to translate from one to the other.

*   Creating figures is the same for both interfaces: Use the respective [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
     functions `plt.figure()`, `plt.subplots()`, `plt.subplot_mosaic()`. For the Axes interface, you typically store the created Figure (and possibly Axes) in variables for later use. When using the pyplot interface, these values are typically not stored. Example:
    
    *   Axes: `fig, ax = plt.subplots()`
        
    *   pyplot: `plt.subplots()`
        
*   "Plotting" functions, i.e. functions that add data, are named the same and have identical parameters on the Axes and in pyplot. Example:
    
    *   Axes: `ax.plot(x, y)`
        
    *   pyplot: `plt.plot(x, y)`
        
*   Functions that retrieve properties are named like the property in pyplot and are prefixed with `get_` on the Axes. Example:
    
    *   Axes: `label = ax.get_xlabel()`
        
    *   pyplot: `label = plt.xlabel()`
        
*   Functions that set properties are named like the property in pyplot and are prefixed with `set_` on the Axes. Example:
    
    *   Axes: `ax.set_xlabel("time")`
        
    *   pyplot: `plt.xlabel("time")`
        

Here is a short summary of the examples again as a side-by-side comparison:

| Operation | Axes interface | pyplot interface |
| --- | --- | --- |
| Creating figures | `fig, ax = plt.subplots()` | `plt.subplots()` |
| Plotting data | `ax.plot(x, y)` | `plt.plot(x, y)` |
| Getting properties | `label = ax.get_xlabel()` | `label = plt.xlabel()` |
| Setting properties | `ax.set_xlabel("time")` | `plt.xlabel("time")` |

### Why be explicit?[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#why-be-explicit "Link to this heading")

What happens if you have to backtrack, and operate on an old axes that is not referenced by `plt.gca()`? One simple way is to call `subplot` again with the same arguments. However, that quickly becomes inelegant. You can also inspect the Figure object and get its list of Axes objects, however, that can be misleading (colorbars are Axes too!). The best solution is probably to save a handle to every Axes you create, but if you do that, why not simply create all the Axes objects at the start?

The first approach is to call `plt.subplot` again:

import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot(\[1, 2, 3\], \[0, 0.5, 0.2\])

plt.subplot(1, 2, 2)
plt.plot(\[3, 2, 1\], \[0, 0.5, 0.2\])

plt.suptitle('Implicit Interface: re-call subplot')

for i in range(1, 3):
    plt.subplot(1, 2, i)
    plt.xlabel('Boo')

([`Source code`](https://matplotlib.org/stable/_downloads/4037ef6e8624f96e1aa65f9faa6d73a5/api_interfaces-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/3755d435d2a2eb506641101aba2636e0/api_interfaces-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/aa65d45a4b0e6b02a468903a5ff56b62/api_interfaces-6.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-6.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-6.2x.png)

The second is to save a handle:

import matplotlib.pyplot as plt

axs \= \[\]
ax \= plt.subplot(1, 2, 1)
axs += \[ax\]
plt.plot(\[1, 2, 3\], \[0, 0.5, 0.2\])

ax \= plt.subplot(1, 2, 2)
axs += \[ax\]
plt.plot(\[3, 2, 1\], \[0, 0.5, 0.2\])

plt.suptitle('Implicit Interface: save handles')

for i in range(2):
    plt.sca(axs\[i\])
    plt.xlabel('Boo')

([`Source code`](https://matplotlib.org/stable/_downloads/d65b494e46f993c3dd8298551d10d62e/api_interfaces-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/008dacd6028779838d22c9578023d145/api_interfaces-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b5cd78a232ed13be054e401f1b5a4b41/api_interfaces-7.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-7.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-7.2x.png)

However, the recommended way would be to be explicit from the outset:

import matplotlib.pyplot as plt

fig, axs \= plt.subplots(1, 2)
axs\[0\].plot(\[1, 2, 3\], \[0, 0.5, 0.2\])
axs\[1\].plot(\[3, 2, 1\], \[0, 0.5, 0.2\])
fig.suptitle('Explicit Interface')
for i in range(2):
    axs\[i\].set\_xlabel('Boo')

([`Source code`](https://matplotlib.org/stable/_downloads/63cb67f11f576b6be9799d352dac1fdc/api_interfaces-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d093959bcafba2bcf9aa8270549c0e8f/api_interfaces-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/2fc83304602bbbc3a533a61de7b69b69/api_interfaces-8.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-8.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-8.2x.png)

Third-party library "Data-object" interfaces[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#third-party-library-data-object-interfaces "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some third party libraries have chosen to implement plotting for their data objects, e.g. `data.plot()`, is seen in [`pandas`](https://pandas.pydata.org/docs/index.html#module-pandas "(in pandas v3.0.5)")
, [xarray](https://xarray.pydata.org/)
, and other third-party libraries. For illustrative purposes, a downstream library may implement a simple data container that has `x` and `y` data stored together, and then implements a `plot` method:

import matplotlib.pyplot as plt

\# supplied by downstream library:
class DataContainer:

    def \_\_init\_\_(self, x, y):
        """
        Proper docstring here!
        """
        self.\_x \= x
        self.\_y \= y

    def plot(self, ax\=None, \*\*kwargs):
        if ax is None:
            ax \= plt.gca()
        ax.plot(self.\_x, self.\_y, \*\*kwargs)
        ax.set\_title('Plotted from DataClass!')
        return ax

\# what the user usually calls:
data \= DataContainer(\[0, 1, 2, 3\], \[0, 0.2, 0.5, 0.3\])
data.plot()

([`Source code`](https://matplotlib.org/stable/_downloads/e254f51219e9f0f791dcf17ddeaa8b51/api_interfaces-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f0549ca694abefdc5beda90850a4e5b3/api_interfaces-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/14842da3d0ac83ee94939c43e18fa880/api_interfaces-9.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-9.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-9.2x.png)

So the library can hide all the nitty-gritty from the user, and can make a visualization appropriate to the data type, often with good labels, choices of colormaps, and other convenient features.

In the above, however, we may not have liked the title the library provided. Thankfully, they pass us back the Axes from the `plot()` method, and understanding the explicit Axes interface, we could call: `ax.set_title('My preferred title')` to customize the title.

Many libraries also allow their `plot` methods to accept an optional _ax_ argument. This allows us to place the visualization in an Axes that we have placed and perhaps customized.

Summary[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#summary "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Overall, it is useful to understand the explicit "Axes" interface since it is the most flexible and underlies the other interfaces. A user can usually figure out how to drop down to the explicit interface and operate on the underlying objects. While the explicit interface can be a bit more verbose to setup, complicated plots will often end up simpler than trying to use the implicit "pyplot" interface.

Note

It is sometimes confusing to people that we import `pyplot` for both interfaces. Currently, the `pyplot` module implements the "pyplot" interface, but it also provides top-level Figure and Axes creation methods, and ultimately spins up the graphical user interface, if one is being used. So `pyplot` is still needed regardless of the interface chosen.

Similarly, the declarative interfaces provided by partner libraries use the objects accessible by the "Axes" interface, and often accept these as arguments or pass them back from methods. It is usually essential to use the explicit "Axes" interface to perform any customization of the default visualization, or to unpack the data into NumPy arrays and pass directly to Matplotlib.

Appendix: "Axes" interface with data structures[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#appendix-axes-interface-with-data-structures "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 methods allow yet another API addressing by passing a _data_ object to the method and specifying the arguments as strings:

import matplotlib.pyplot as plt

data \= {'xdat': \[0, 1, 2, 3\], 'ydat': \[0, 0.2, 0.4, 0.1\]}
fig, ax \= plt.subplots(figsize\=(2, 2))
ax.plot('xdat', 'ydat', data\=data)

([`Source code`](https://matplotlib.org/stable/_downloads/697d1cdf15045a9e483b588c2ea18f6b/api_interfaces-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/30c80c6b924f5a0568a404661deae0a3/api_interfaces-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/42ab4c8d63aff184c5e6301050273e3c/api_interfaces-10.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-10.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-api_interfaces-10.2x.png)

Appendix: "pylab" interface[#](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#appendix-pylab-interface "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

There is one further interface that is highly discouraged, and that is to basically do `from matplotlib.pylab import *`. This imports all the functions from `matplotlib.pyplot`, `numpy`, `numpy.fft`, `numpy.linalg`, and `numpy.random`, and some additional functions into the global namespace.

Such a pattern is considered bad practice in modern python, as it clutters the global namespace. Even more severely, in the case of `pylab`, this will overwrite some builtin functions (e.g. the builtin `sum` will be replaced by `numpy.sum`), which can lead to unexpected behavior.

On this page