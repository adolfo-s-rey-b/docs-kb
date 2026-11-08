[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_anchored_direction_arrows.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_anchored_direction_arrows.html#sphx-glr-download-gallery-axes-grid1-demo-anchored-direction-arrows-py)
 to download the full example code.

Anchored Direction Arrow[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_anchored_direction_arrows.html#anchored-direction-arrow "Link to this heading")

==================================================================================================================================================================

![demo anchored direction arrows](https://matplotlib.org/stable/_images/sphx_glr_demo_anchored_direction_arrows_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font\_manager as fm
from mpl\_toolkits.axes\_grid1.anchored\_artists import [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
((10, 10)))

\# Simple example
[simple\_arrow](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
([ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, 'X', 'Y')
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([simple\_arrow](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

\# High contrast arrow
[high\_contrast\_part\_1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
(
                            [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
                            '111', r'11$\\overline{2}$',
                            loc\='upper right',
                            arrow\_props\={'ec': 'w', 'fc': 'none', 'alpha': 1,
                                         'lw': 2}
                            )
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([high\_contrast\_part\_1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

[high\_contrast\_part\_2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
(
                            [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
                            '111', r'11$\\overline{2}$',
                            loc\='upper right',
                            arrow\_props\={'ec': 'none', 'fc': 'k'},
                            text\_props\={'ec': 'w', 'fc': 'k', 'lw': 0.4}
                            )
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([high\_contrast\_part\_2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

\# Rotated arrow
[fontprops](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 \= [fm.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(family\='serif')

[rotated\_arrow](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
(
                    [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
                    '30', '120',
                    loc\='center',
                    color\='w',
                    angle\=30,
                    fontproperties\=[fontprops](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
                    )
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([rotated\_arrow](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

\# Altering arrow directions
[a1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
(
        [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, 'A', 'B', loc\='lower center',
        length\=-0.15,
        sep\_x\=0.03, sep\_y\=0.03,
        color\='r'
    )
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([a1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

[a2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
(
        [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, 'A', ' B', loc\='lower left',
        aspect\_ratio\=-1,
        sep\_x\=0.01, sep\_y\=-0.02,
        color\='orange'
        )
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([a2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

[a3](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 \= [AnchoredDirectionArrows](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
(
        [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, ' A', 'B', loc\='lower right',
        length\=-0.15,
        aspect\_ratio\=-1,
        sep\_y\=-0.1, sep\_x\=0.04,
        color\='cyan'
        )
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([a3](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_anchored_direction_arrows.ipynb`](https://matplotlib.org/stable/_downloads/af125fa66a3ddaf7ff8145913de95397/demo_anchored_direction_arrows.ipynb)

[`Download Python source code: demo_anchored_direction_arrows.py`](https://matplotlib.org/stable/_downloads/82ac862070a073a69fc9b974db5ab46b/demo_anchored_direction_arrows.py)

[`Download zipped: demo_anchored_direction_arrows.zip`](https://matplotlib.org/stable/_downloads/b464a80bb9f43fc4250570849b2e4a86/demo_anchored_direction_arrows.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)