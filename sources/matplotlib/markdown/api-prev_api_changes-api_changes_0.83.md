[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.83.html#main-content)

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
    

Changes for 0.83[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.83.html#changes-for-0-83 "Link to this heading")

======================================================================================================================================

\- Made HOME/.matplotlib the new config dir where the matplotlibrc
  file, the ttf.cache, and the tex.cache live.  The new default
  filenames in .matplotlib have no leading dot and are not hidden.
  e.g., the new names are matplotlibrc, tex.cache, and ttffont.cache.
  This is how ipython does it so it must be right.

  If old files are found, a warning is issued and they are moved to
  the new location.

- backends/\_\_init\_\_.py no longer imports new\_figure\_manager,
  draw\_if\_interactive and show from the default backend, but puts
  these imports into a call to pylab\_setup.  Also, the Toolbar is no
  longer imported from WX/WXAgg.  New usage:

    from backends import pylab\_setup
    new\_figure\_manager, draw\_if\_interactive, show = pylab\_setup()

- Moved Figure.get\_width\_height() to FigureCanvasBase. It now
  returns int instead of float.