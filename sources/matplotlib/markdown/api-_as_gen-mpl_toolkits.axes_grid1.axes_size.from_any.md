[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.from_any.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_size.from\_any[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.from_any.html#mpl-toolkits-axes-grid1-axes-size-from-any "Link to this heading")

===============================================================================================================================================================================================================

mpl\_toolkits.axes\_grid1.axes\_size.from\_any(_size_, _fraction\_ref\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_size.py#L228-L243)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.from_any.html#mpl_toolkits.axes_grid1.axes_size.from_any "Link to this definition")

Create a Fixed unit when the first argument is a float, or a Fraction unit if that is a string that ends with %. The second argument is only meaningful when Fraction unit is created.

\>>> from mpl\_toolkits.axes\_grid1.axes\_size import from\_any
\>>> a \= from\_any(1.2) \# => Fixed(1.2)
\>>> from\_any("50%", a) \# => Fraction(0.5, a)

On this page