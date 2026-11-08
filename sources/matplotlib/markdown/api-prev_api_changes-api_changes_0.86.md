[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.86.html#main-content)

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
    

Changes for 0.86[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.86.html#changes-for-0-86 "Link to this heading")

======================================================================================================================================

Matplotlib data is installed into the matplotlib module.
This is similar to package\_data.  This should get rid of
having to check for many possibilities in \_get\_data\_path().
The MATPLOTLIBDATA env key is still checked first to allow
for flexibility.

1) Separated the color table data from cm.py out into
a new file, \_cm.py, to make it easier to find the actual
code in cm.py and to add new colormaps. Everything
from \_cm.py is imported by cm.py, so the split should be
transparent.
2) Enabled automatic generation of a colormap from
a list of colors in contour; see modified
examples/contour\_demo.py.
3) Support for imshow of a masked array, with the
ability to specify colors (or no color at all) for
masked regions, and for regions that are above or
below the normally mapped region.  See
examples/image\_masked.py.
4) In support of the above, added two new classes,
ListedColormap, and no\_norm, to colors.py, and modified
the Colormap class to include common functionality. Added
a clip kwarg to the normalize class.