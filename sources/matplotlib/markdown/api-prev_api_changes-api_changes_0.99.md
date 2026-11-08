[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.99.html#main-content)

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
    

Changes in 0.99[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.99.html#changes-in-0-99 "Link to this heading")

====================================================================================================================================

*   pylab no longer provides a load and save function. These are available in matplotlib.mlab, or you can use numpy.loadtxt and numpy.savetxt for text files, or np.save and np.load for binary NumPy arrays.
    
*   User-generated colormaps can now be added to the set recognized by `matplotlib.cm.get_cmap`. Colormaps can be made the default and applied to the current image using [`matplotlib.pyplot.set_cmap()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_cmap.html#matplotlib.pyplot.set_cmap "matplotlib.pyplot.set_cmap")
    .
    
*   changed use\_mrecords default to False in mlab.csv2rec since this is partially broken
    
*   Axes instances no longer have a "frame" attribute. Instead, use the new "spines" attribute. Spines is a dictionary where the keys are the names of the spines (e.g., 'left','right' and so on) and the values are the artists that draw the spines. For normal (rectilinear) axes, these artists are Line2D instances. For other axes (such as polar axes), these artists may be Patch instances.
    
*   Polar plots no longer accept a resolution kwarg. Instead, each Path must specify its own number of interpolation steps. This is unlikely to be a user-visible change -- if interpolation of data is required, that should be done before passing it to Matplotlib.