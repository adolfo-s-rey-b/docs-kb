[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.2.html#main-content)

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
    

API Changes in 2.1.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.2.html#api-changes-in-2-1-2 "Link to this heading")

===============================================================================================================================================

[`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 no longer checks for repeated lines to ignore[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_2.1.2.html#figure-legend-no-longer-checks-for-repeated-lines-to-ignore "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`matplotlib.figure.Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 used to check if a line had the same label as an existing legend entry. If it also had the same line color or marker color legend didn't add a new entry for that line. However, the list of conditions was incomplete, didn't handle RGB tuples, didn't handle linewidths or linestyles etc.

This logic did not exist in [`axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
. It was included (erroneously) in Matplotlib 2.1.1 when the legend argument parsing was unified [PR #9324](https://github.com/matplotlib/matplotlib/pull/9324/)
. This change removes that check in [`axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 again to restore the old behavior.

This logic has also been dropped from [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
, where it was previously undocumented. Repeated lines with the same label will now each have an entry in the legend. If you do not want the duplicate entries, don't add a label to the line, or prepend the label with an underscore.

On this page