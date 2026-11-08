[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#main-content)

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
    

matplotlib.pyplot.setp[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib-pyplot-setp "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.setp(_obj_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L828-L830)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "Link to this definition")

Set one or more properties on an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, or list allowed values.

Parameters:

**obj**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The artist(s) whose properties are being set or queried. When setting properties, all artists are affected; when querying the allowed values, only the first instance in the sequence is queried.

For example, two lines can be made thicker and red with a single call:

\>>> x \= arange(0, 1, 0.01)
\>>> lines \= plot(x, sin(2\*pi\*x), x, sin(4\*pi\*x))
\>>> setp(lines, linewidth\=2, color\='r')

**file**file-like, default: [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "(in Python v3.14)")

Where [`setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
 writes its output when asked to list allowed values.

\>>> with open('output.log') as file:
...     setp(line, file\=file)

The default, `None`, means [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "(in Python v3.14)")
.

**\*args, \*\*kwargs**

The properties to set. The following combinations are supported:

*   Set the linestyle of a line to be dashed:
    
    \>>> line, \= plot(\[1, 2, 3\])
    \>>> setp(line, linestyle\='--')
    
*   Set multiple properties at once:
    
    \>>> setp(line, linewidth\=2, color\='r')
    
*   List allowed values for a line's linestyle:
    
    \>>> setp(line, 'linestyle')
    linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    
*   List all properties that can be set, and their allowed values:
    
    \>>> setp(line)
    agg\_filter: a filter function, ...
    \[long output listing omitted\]
    

[`setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
 also supports MATLAB style string/value pairs. For example, the following are equivalent:

\>>> setp(lines, 'linewidth', 2, 'color', 'r')  \# MATLAB style
\>>> setp(lines, linewidth\=2, color\='r')        \# Python style

See also

[`getp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")

Notes

Note

This is equivalent to [`matplotlib.artist.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp")
.

Examples using `matplotlib.pyplot.setp`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#examples-using-matplotlib-pyplot-setp "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_set_and_get_thumb.png)

[Set and get properties](https://matplotlib.org/stable/gallery/misc/set_and_get.html)

Set and get properties

![](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_thumb.png)

[Topographic hillshading](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html)

Topographic hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_thumb.png)

[The Lifecycle of a Plot](https://matplotlib.org/stable/tutorials/lifecycle.html)

The Lifecycle of a Plot

On this page