[Skip to main content](https://matplotlib.org/stable/api/quiver_api.html#main-content)

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
    

`matplotlib.quiver`[#](https://matplotlib.org/stable/api/quiver_api.html#module-matplotlib.quiver "Link to this heading")

==========================================================================================================================

Support for plotting vector fields.

Presently this contains Quiver and Barb. Quiver plots an arrow in the direction of the vector, with the size of the arrow related to the magnitude of the vector.

Barbs are like quiver in that they point along a vector, but the magnitude of the vector is given schematically by the presence of barbs or flags on the barb.

This will also become a home for things such as standard deviation ellipses, which can and will be derived very easily from the Quiver code.

Classes[#](https://matplotlib.org/stable/api/quiver_api.html#classes "Link to this heading")

---------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")<br>(ax, \*args\[, scale, headwidth, ...\]) | Specialized PolyCollection for arrows. |
| [`QuiverKey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey "matplotlib.quiver.QuiverKey")<br>(Q, X, Y, U, label, \*\[, angle, ...\]) | Labelled arrow for use as a quiver plot scale key. |
| [`Barbs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Barbs.html#matplotlib.quiver.Barbs "matplotlib.quiver.Barbs")<br>(ax, \*args\[, pivot, length, barbcolor, ...\]) | Specialized PolyCollection for barbs. |

On this page