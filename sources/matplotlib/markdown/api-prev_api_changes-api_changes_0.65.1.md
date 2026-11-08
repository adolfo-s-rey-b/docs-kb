[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.65.1.html#main-content)

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
    

Changes for 0.65.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.65.1.html#changes-for-0-65-1 "Link to this heading")

============================================================================================================================================

removed add\_axes and add\_subplot from backend\_bases.  Use
figure.add\_axes and add\_subplot instead.  The figure now manages the
current axes with gca and sca for get and set current axes.  If you
have code you are porting which called, e.g., figmanager.add\_axes, you
can now simply do figmanager.canvas.figure.add\_axes.