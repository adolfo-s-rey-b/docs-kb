[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html#main-content)

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
    

matplotlib.pyplot.rcdefaults[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html#matplotlib-pyplot-rcdefaults "Link to this heading")

=================================================================================================================================================================

matplotlib.pyplot.rcdefaults()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L808-L812)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html#matplotlib.pyplot.rcdefaults "Link to this definition")

Restore the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 from Matplotlib's internal default style.

Style-blacklisted [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 (defined in `matplotlib.style.core.STYLE_BLACKLIST`) are not updated.

See also

[`matplotlib.rc_file_defaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults "matplotlib.rc_file_defaults")

Restore the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 from the rc file originally loaded by Matplotlib.

[`matplotlib.style.use`](https://matplotlib.org/stable/api/style_api.html#matplotlib.style.use "matplotlib.style.use")

Use a specific style file. Call `style.use('default')` to restore the default style.

Notes

Note

This is equivalent to [`matplotlib.rcdefaults`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "matplotlib.rcdefaults")
.

Examples using `matplotlib.pyplot.rcdefaults`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html#examples-using-matplotlib-pyplot-rcdefaults "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_customize_rc_thumb.png)

[Customize Rc](https://matplotlib.org/stable/gallery/misc/customize_rc.html)

Customize Rc

On this page