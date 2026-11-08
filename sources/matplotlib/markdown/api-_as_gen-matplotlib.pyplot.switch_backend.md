[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html#main-content)

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
    

matplotlib.pyplot.switch\_backend[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html#matplotlib-pyplot-switch-backend "Link to this heading")

==============================================================================================================================================================================

matplotlib.pyplot.switch\_backend(_newbackend_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L394-L547)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html#matplotlib.pyplot.switch_backend "Link to this definition")

Set the pyplot backend.

Switching to an interactive backend is possible only if no event loop for another interactive backend has started. Switching to and from non-interactive backends is always possible.

Parameters:

**newbackend**str

The case-insensitive name of the backend to use.

On this page