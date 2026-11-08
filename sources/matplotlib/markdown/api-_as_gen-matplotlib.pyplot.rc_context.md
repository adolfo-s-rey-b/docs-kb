[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#main-content)

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
    

matplotlib.pyplot.rc\_context[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#matplotlib-pyplot-rc-context "Link to this heading")

==================================================================================================================================================================

matplotlib.pyplot.rc\_context(_rc\=None_, _fname\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L800-L805)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#matplotlib.pyplot.rc_context "Link to this definition")

Return a context manager for temporarily changing rcParams.

The `[rcParams["backend"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=backend#rcparam-backend) ` will not be reset by the context manager.

rcParams changed both through the context manager invocation and in the body of the context will be reset on context exit.

Parameters:

**rc**dict

The rcParams to temporarily set.

**fname**str or path-like

A file with Matplotlib rc settings. If both _fname_ and _rc_ are given, settings from _rc_ take precedence.

See also

[The matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)

Notes

Note

This is equivalent to [`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
.

Examples

Passing explicit values via a dict:

with mpl.rc\_context({'interactive': False}):
    fig, ax \= plt.subplots()
    ax.plot(range(3), range(3))
    fig.savefig('example.png')
    plt.close(fig)

Loading settings from a file:

with mpl.rc\_context(fname\='print.rc'):
    plt.plot(x, y)  \# uses 'print.rc'

Setting in the context body:

with mpl.rc\_context():
    \# will be reset
    mpl.rcParams\['lines.linewidth'\] \= 5
    plt.plot(x, y)

Examples using `matplotlib.pyplot.rc_context`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#examples-using-matplotlib-pyplot-rc-context "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_thumb.png)

[Style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

Style sheets reference

![](https://matplotlib.org/stable/_images/sphx_glr_logos2_thumb.png)

[Matplotlib logo](https://matplotlib.org/stable/gallery/misc/logos2.html)

Matplotlib logo

![](https://matplotlib.org/stable/_images/sphx_glr_autoscale_thumb.png)

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)

Axis autoscaling

On this page