[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#main-content)

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
    

matplotlib.figure.Figure.set\_size\_inches[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#matplotlib-figure-figure-set-size-inches "Link to this heading")

=======================================================================================================================================================================================================

Figure.set\_size\_inches(_w_, _h\=None_, _forward\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L3129-L3173)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#matplotlib.figure.Figure.set_size_inches "Link to this definition")

Set the figure size in inches.

Call signatures:

fig.set\_size\_inches(w, h)  \# OR
fig.set\_size\_inches((w, h))

Parameters:

**w**(float, float) or float

Width and height in inches (if height not specified as a separate argument) or width.

**h**float

Height in inches.

**forward**bool, default: True

If `True`, the canvas size is automatically updated, e.g., you can resize the figure window from the shell.

See also

[`matplotlib.figure.Figure.get_size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_size_inches.html#matplotlib.figure.Figure.get_size_inches "matplotlib.figure.Figure.get_size_inches")

[`matplotlib.figure.Figure.set_figwidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html#matplotlib.figure.Figure.set_figwidth "matplotlib.figure.Figure.set_figwidth")

[`matplotlib.figure.Figure.set_figheight`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html#matplotlib.figure.Figure.set_figheight "matplotlib.figure.Figure.set_figheight")

Notes

To transform from pixels to inches divide by [`Figure.dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.dpi.html#matplotlib.figure.Figure.dpi "matplotlib.figure.Figure.dpi")
.

On this page