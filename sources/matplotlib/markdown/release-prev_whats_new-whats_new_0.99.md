[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#main-content)

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
    

[What's new in Matplotlib 0.99 (Aug 29, 2009)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#what-s-new-in-matplotlib-0-99-aug-29-2009 "Link to this heading")

============================================================================================================================================================================================================================================================================

[New documentation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#new-documentation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Jae-Joon Lee has written two new guides [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 and [Advanced annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#plotting-guide-annotation)
. Michael Sarahan has written [Image tutorial](https://matplotlib.org/stable/tutorials/images.html#image-tutorial)
. John Hunter has written two new tutorials on working with paths and transformations: [Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html#paths)
 and [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)
.

[mplot3d](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#mplot3d "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Reinier Heeres has ported John Porter's mplot3d over to the new matplotlib transformations framework, and it is now available as a toolkit mpl\_toolkits.mplot3d (which now comes standard with all mpl installs). See [3D plotting](https://matplotlib.org/stable/gallery/mplot3d/index.html#mplot3d-examples-index)
 and [The mplot3d toolkit](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#mplot3d)
.

([`Source code`](https://matplotlib.org/stable/_downloads/f8a9ea8cc6d9570e68c3c28dfac814c3/whats_new_0-99-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/6fed2466ce4ae8af3024159c129aa933/whats_new_0-99-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/33a389d0323875d9273037dc93ab6a79/whats_new_0-99-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_0-99-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_0-99-1.2x.png)

[axes grid toolkit](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#axes-grid-toolkit "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Jae-Joon Lee has added a new toolkit to ease displaying multiple images in matplotlib, as well as some support for curvilinear grids to support the world coordinate system. The toolkit is included standard with all new mpl installs. See [Module - axes\_grid1](https://matplotlib.org/stable/gallery/axes_grid1/index.html#axes-grid1-examples-index)
, [Module - axisartist](https://matplotlib.org/stable/gallery/axisartist/index.html#axisartist-examples-index)
, [The axes\_grid1 toolkit](https://matplotlib.org/stable/users/explain/toolkits/axes_grid.html#axes-grid1-users-guide-index)
 and [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)

([`Source code`](https://matplotlib.org/stable/_downloads/2ea4a4f81086a7474b7ea1bb73eab1f0/whats_new_0-99-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/466b81efe097c82ec09ca08d29f47353/whats_new_0-99-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8a4e9103061e644f1168777f78799864/whats_new_0-99-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_0-99-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_0-99-2.2x.png)

[Axis spine placement](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_0.99.html#axis-spine-placement "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Andrew Straw has added the ability to place "axis spines" -- the lines that denote the data limits -- in various arbitrary locations. No longer are your axis lines constrained to be a simple rectangle around the figure -- you can turn on or off left, bottom, right and top, as well as "detach" the spine to offset it away from the data. See [Spine placement](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html)
 and [`matplotlib.spines.Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
.

([`Source code`](https://matplotlib.org/stable/_downloads/9ce17c096d08e5e24fc802ff4bab8d21/whats_new_0-99-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/02a71cfe2eaf860bbec69c8efc80ee7b/whats_new_0-99-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/6888749f73328b08b077cea61e8c58ff/whats_new_0-99-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_0-99-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_0-99-3.2x.png)

On this page