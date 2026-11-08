[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#main-content)

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
    

matplotlib.figure.Figure.autofmt\_xdate[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#matplotlib-figure-figure-autofmt-xdate "Link to this heading")

================================================================================================================================================================================================

Figure.autofmt\_xdate(_bottom\=0.2_, _rotation\=30_, _ha\='right'_, _which\='major'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L175-L218)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#matplotlib.figure.Figure.autofmt_xdate "Link to this definition")

Date ticklabels often overlap, so it is useful to rotate them and right align them. Also, a common use case is a number of subplots with shared x-axis where the x-axis is date data. The ticklabels are often long, and it helps to rotate them on the bottom subplot and turn them off on other subplots, as well as turn off xlabels.

Parameters:

**bottom**float, default: 0.2

The bottom of the subplots for [`subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
.

**rotation**float, default: 30 degrees

The rotation angle of the xtick labels in degrees.

**ha**{'left', 'center', 'right'}, default: 'right'

The horizontal alignment of the xticklabels.

**which**{'major', 'minor', 'both'}, default: 'major'

Selects which ticklabels to rotate.

Examples using `matplotlib.figure.Figure.autofmt_xdate`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#examples-using-matplotlib-figure-figure-autofmt-xdate "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)

[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)

fill\_between with transparency

![](https://matplotlib.org/stable/_images/sphx_glr_date_demo_convert_thumb.png)

[Date converter demo](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html)

Date converter demo

On this page