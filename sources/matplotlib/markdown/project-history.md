[Skip to main content](https://matplotlib.org/stable/project/history.html#main-content)

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
    

History[#](https://matplotlib.org/stable/project/history.html#history "Link to this heading")

==============================================================================================

Note

The following introductory text was written in 2008 by John D. Hunter (1968-2012), the original author of Matplotlib.

Matplotlib is a library for making 2D plots of arrays in [Python](https://www.python.org/)
. Although it has its origins in emulating the MATLAB graphics commands, it is independent of MATLAB, and can be used in a Pythonic, object-oriented way. Although Matplotlib is written primarily in pure Python, it makes heavy use of [NumPy](https://numpy.org/)
 and other extension code to provide good performance even for large arrays.

Matplotlib is designed with the philosophy that you should be able to create simple plots with just a few commands, or just one! If you want to see a histogram of your data, you shouldn't need to instantiate objects, call methods, set properties, and so on; it should just work.

For years, I used to use MATLAB exclusively for data analysis and visualization. MATLAB excels at making nice looking plots easy. When I began working with EEG data, I found that I needed to write applications to interact with my data, and developed an EEG analysis application in MATLAB. As the application grew in complexity, interacting with databases, http servers, manipulating complex data structures, I began to strain against the limitations of MATLAB as a programming language, and decided to start over in Python. Python more than makes up for all of MATLAB's deficiencies as a programming language, but I was having difficulty finding a 2D plotting package (for 3D [VTK](http://www.vtk.org/)
 more than exceeds all of my needs).

When I went searching for a Python plotting package, I had several requirements:

*   Plots should look great - publication quality. One important requirement for me is that the text looks good (antialiased, etc.)
    
*   Postscript output for inclusion with TeX documents
    
*   Embeddable in a graphical user interface for application development
    
*   Code should be easy enough that I can understand it and extend it
    
*   Making plots should be easy
    

Finding no package that suited me just right, I did what any self-respecting Python programmer would do: rolled up my sleeves and dived in. Not having any real experience with computer graphics, I decided to emulate MATLAB's plotting capabilities because that is something MATLAB does very well. This had the added advantage that many people have a lot of MATLAB experience, and thus they can quickly get up to steam plotting in python. From a developer's perspective, having a fixed user interface (the pylab interface) has been very useful, because the guts of the code base can be redesigned without affecting user code.

The Matplotlib code is conceptually divided into three parts: the _pylab interface_ is the set of functions provided by [`pylab`](https://matplotlib.org/stable/api/pylab.html#module-pylab "pylab")
 which allow the user to create plots with code quite similar to MATLAB figure generating code ([Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html#pyplot-tutorial)
). The _Matplotlib frontend_ or _Matplotlib API_ is the set of classes that do the heavy lifting, creating and managing figures, text, lines, plots and so on ([Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html#artists-tutorial)
). This is an abstract interface that knows nothing about output. The _backends_ are device-dependent drawing devices, aka renderers, that transform the frontend representation to hardcopy or a display device ([What is a backend?](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
). Example backends: PS creates [PostScript®](https://www.adobe.com/products/postscript.html)
 hardcopy, SVG creates [Scalable Vector Graphics](https://www.w3.org/Graphics/SVG/)
 hardcopy, Agg creates PNG output using the high quality [Anti-Grain Geometry](http://agg.sourceforge.net/antigrain.com/)
 library that ships with Matplotlib, GTK embeds Matplotlib in a [Gtk+](https://www.gtk.org/)
 application, GTKAgg uses the Anti-Grain renderer to create a figure and embed it in a Gtk+ application, and so on for [PDF](https://acrobat.adobe.com/us/en/acrobat/about-adobe-pdf.html)
, [WxWidgets](https://www.wxpython.org/)
, [Tkinter](https://docs.python.org/3/library/tkinter.html)
, etc.

Matplotlib is used by many people in many different contexts. Some people want to automatically generate PostScript files to send to a printer or publishers. Others deploy Matplotlib on a web application server to generate PNG output for inclusion in dynamically-generated web pages. Some use Matplotlib interactively from the Python shell in Tkinter on Windows. My primary use is to embed Matplotlib in a Gtk+ EEG application that runs on Windows, Linux and Macintosh OS X.

* * *

Matplotlib's original logo (2003 -- 2008).

([`Source code`](https://matplotlib.org/stable/_downloads/d63062b379e9152c153f754e3459b8a2/history-1.py)
)

Matplotlib logo (2008 - 2015).

([`Source code`](https://matplotlib.org/stable/_downloads/95ad1ba96e7dbac6ff07ec3be3454ba1/history-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/fb8ae30dcaaeaaa78bf0166fe4f2b0b7/history-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/1329602fe8c6478c6ab2c51a8f109775/history-2.png)
)

[![](https://matplotlib.org/stable/_images/project-history-2.2x.png)](https://matplotlib.org/stable/_images/project-history-2.2x.png)