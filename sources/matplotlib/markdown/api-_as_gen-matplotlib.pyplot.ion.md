[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#main-content)

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
    

matplotlib.pyplot.ion[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib-pyplot-ion "Link to this heading")

============================================================================================================================================

matplotlib.pyplot.ion()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L727-L764)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "Link to this definition")

Enable interactive mode.

See [`pyplot.isinteractive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive "matplotlib.pyplot.isinteractive")
 for more details.

See also

[`ioff`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ioff.html#matplotlib.pyplot.ioff "matplotlib.pyplot.ioff")

Disable interactive mode.

[`isinteractive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive "matplotlib.pyplot.isinteractive")

Whether interactive mode is enabled.

[`show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")

Show all figures (and maybe block).

[`pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")

Show all figures, and block for a time.

Notes

For a temporary change, this can be used as a context manager:

\# if interactive mode is off
\# then figures will not be shown on creation
plt.ioff()
\# This figure will not be shown immediately
fig \= plt.figure()

with plt.ion():
    \# interactive mode will be on
    \# figures will automatically be shown
    fig2 \= plt.figure()
    \# ...

To enable optional usage as a context manager, this function returns a context manager object, which is not intended to be stored or accessed by the user.

On this page