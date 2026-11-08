[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html#sphx-glr-download-gallery-axes-grid1-make-room-for-ylabel-using-axesgrid-py)
 to download the full example code.

Make room for ylabel using axes\_grid[#](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html#make-room-for-ylabel-using-axes-grid "Link to this heading")

================================================================================================================================================================================================

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1 import [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
from mpl\_toolkits.axes\_grid1.axes\_divider import [make\_axes\_area\_auto\_adjustable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable "mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1))

[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[0.5\], labels\=\["very long label"\])

[make\_axes\_area\_auto\_adjustable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable "mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![make room for ylabel using axesgrid](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_001_2_00x.png)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 0.5))
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0.5, 1, 0.5))

[ax1.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[0.5\], labels\=\["very long label"\])
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Y label")

[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Title")

[make\_axes\_area\_auto\_adjustable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable "mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable")
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, pad\=0.1, use\_axes\=\[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\])
[make\_axes\_area\_auto\_adjustable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable "mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, pad\=0.1, use\_axes\=\[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\])

![Title](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_002_2_00x.png)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1))
[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 \= [make\_axes\_locatable](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.make_axes_locatable")
([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [divider.append\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
("right", "100%", pad\=0.3, sharey\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax2.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labelleft\=False)
[fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[divider.add\_auto\_adjustable\_area](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.add_auto_adjustable_area "mpl_toolkits.axes_grid1.Divider.add_auto_adjustable_area")
(use\_axes\=\[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\], pad\=0.1,
                                 adjust\_dirs\=\["left"\])
[divider.add\_auto\_adjustable\_area](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.add_auto_adjustable_area "mpl_toolkits.axes_grid1.Divider.add_auto_adjustable_area")
(use\_axes\=\[[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\], pad\=0.1,
                                 adjust\_dirs\=\["right"\])
[divider.add\_auto\_adjustable\_area](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.add_auto_adjustable_area "mpl_toolkits.axes_grid1.Divider.add_auto_adjustable_area")
(use\_axes\=\[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\], pad\=0.1,
                                 adjust\_dirs\=\["top", "bottom"\])

[ax1.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[0.5\], labels\=\["very long label"\])

[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Title")
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("X - Label")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Title](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_003_2_00x.png)

**Total running time of the script:** (0 minutes 2.555 seconds)

[`Download Jupyter notebook: make_room_for_ylabel_using_axesgrid.ipynb`](https://matplotlib.org/stable/_downloads/673eb94321c0a9961bd707dd0167411f/make_room_for_ylabel_using_axesgrid.ipynb)

[`Download Python source code: make_room_for_ylabel_using_axesgrid.py`](https://matplotlib.org/stable/_downloads/21d8ee22ee349956af371690a5d55865/make_room_for_ylabel_using_axesgrid.py)

[`Download zipped: make_room_for_ylabel_using_axesgrid.zip`](https://matplotlib.org/stable/_downloads/c3efbfa3847f54e06983ee9363637bf2/make_room_for_ylabel_using_axesgrid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)