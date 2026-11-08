[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#main-content)

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
    

matplotlib.artist.Artist.sticky\_edges[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib-artist-artist-sticky-edges "Link to this heading")

=============================================================================================================================================================================================

property Artist.sticky\_edges[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "Link to this definition")

`x` and `y` sticky edge lists for autoscaling.

When performing autoscaling, if a data limit coincides with a value in the corresponding sticky\_edges list, then no margin will be added--the view limit "sticks" to the edge. A typical use case is histograms, where one usually expects no margin on the bottom edge (0) of the histogram.

Moreover, margin expansion "bumps" against sticky edges and cannot cross them. For example, if the upper data limit is 1.0, the upper view limit computed by simple margin application is 1.2, but there is a sticky edge at 1.1, then the actual upper view limit will be 1.1.

This attribute cannot be assigned to; however, the `x` and `y` lists can be modified in place as needed.

Examples

\>>> artist.sticky\_edges.x\[:\] \= (xmin, xmax)
\>>> artist.sticky\_edges.y\[:\] \= (ymin, ymax)

On this page