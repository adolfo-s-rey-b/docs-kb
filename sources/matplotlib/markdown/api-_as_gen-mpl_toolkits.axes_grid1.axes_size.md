[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_size[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "Link to this heading")

==========================================================================================================================================================================================

Provides classes of simple units that will be used with [`AxesDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 class (or others) to determine the size of each Axes. The unit classes define `get_size` method that returns a tuple of two floats, meaning relative and absolute sizes, respectively.

Note that this class is nothing more than a simple tuple of two floats. Take a look at the Divider class to see how these two values are used.

Once created, the unit classes can be modified by simple arithmetic operations: addition /subtraction with another unit type or a real number and scaling (multiplication or division) by a real number.

Classes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#classes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Add`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Add.html#mpl_toolkits.axes_grid1.axes_size.Add "mpl_toolkits.axes_grid1.axes_size.Add")<br>(a, b) | Sum of two sizes. |
| [`AxesX`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")<br>(axes\[, aspect, ref\_ax\]) | Scaled size whose relative part corresponds to the data width of the _axes_ multiplied by the _aspect_. |
| [`AxesY`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")<br>(axes\[, aspect, ref\_ax\]) | Scaled size whose relative part corresponds to the data height of the _axes_ multiplied by the _aspect_. |
| [`Fixed`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")<br>(fixed\_size) | Simple fixed size with absolute part = _fixed\_size_ and relative part = 0. |
| [`Fraction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fraction.html#mpl_toolkits.axes_grid1.axes_size.Fraction "mpl_toolkits.axes_grid1.axes_size.Fraction")<br>(fraction, ref\_size) | An instance whose size is a _fraction_ of the _ref\_size_. |
| [`MaxExtent`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.MaxExtent.html#mpl_toolkits.axes_grid1.axes_size.MaxExtent "mpl_toolkits.axes_grid1.axes_size.MaxExtent")<br>(artist\_list, w\_or\_h) | Size whose absolute part is either the largest width or the largest height of the given _artist\_list_. |
| [`MaxHeight`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.MaxHeight.html#mpl_toolkits.axes_grid1.axes_size.MaxHeight "mpl_toolkits.axes_grid1.axes_size.MaxHeight")<br>(artist\_list) | Size whose absolute part is the largest height of the given _artist\_list_. |
| [`MaxWidth`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.MaxWidth.html#mpl_toolkits.axes_grid1.axes_size.MaxWidth "mpl_toolkits.axes_grid1.axes_size.MaxWidth")<br>(artist\_list) | Size whose absolute part is the largest width of the given _artist\_list_. |
| [`Scalable`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scalable.html#mpl_toolkits.axes_grid1.axes_size.Scalable "mpl_toolkits.axes_grid1.axes_size.Scalable") |     |
| [`Scaled`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")<br>(scalable\_size) | Simple scaled(?) size with absolute part = 0 and relative part = _scalable\_size_. |

Functions[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`from_any`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.from_any.html#mpl_toolkits.axes_grid1.axes_size.from_any "mpl_toolkits.axes_grid1.axes_size.from_any")<br>(size\[, fraction\_ref\]) | Create a Fixed unit when the first argument is a float, or a Fraction unit if that is a string that ends with %. |

On this page