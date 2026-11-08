[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html#sphx-glr-download-gallery-text-labels-and-annotations-multiline-py)
 to download the full example code.

Multiline text[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html#multiline-text "Link to this heading")

==========================================================================================================================================

Texts may contain newlines to create multiline text.

The text alignment of the individual lines can be controlled by the `multialignment` parameter. If not set, the alignment of the lines is inferred from the `horizontalalignment` and `verticalalignment` parameters, which primarily control the alignment of the bounding box of the text to its anchor point; e.g. if the text has the anchor point to its right, all text lines will be aligned to the right so that they pick up that anchor point.

When using mutli-line labels, it is recommended to use a layout manager (e.g. `layout="constrained"`) to ensure that there is enough space for the labels..

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\="constrained")

[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(range(6), \[0.3, 0.5, 0.8, 1.5, 2.5, 8\], alpha\=0.3)

[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('labels are centered,\\nso is their multi-line text by default')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('xlabel with\\nmultialignment="left"', multialignment\="left")

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(
    4.5, 6,
    'these lines\\n'
    'are right aligned\\n'
    'because of horizontalalignment',
    horizontalalignment\='right',
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(
    4.5, 4,
    'but\\n'
    'we can override this\\n'
    'with an explicit multialingment="left"',
    horizontalalignment\='right',
    multialignment\='left',
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![multiline](https://matplotlib.org/stable/_images/sphx_glr_multiline_001_2_00x.png)

Each line has the same height irrespective of the used characters unless there is math text involved, which may need more vertical space

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.1, 0.4, "Mat\\nTTp\\n123", size\=18,
        va\="baseline", bbox\=dict(fc\="none", ec\="tab:orange"))

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.3, 0.4, "Mag\\nTTT\\n123", size\=18,
        va\="baseline", bbox\=dict(fc\="none", ec\="tab:orange"))

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.4, "Mag\\nTTT$^{A^A}$\\n123", size\=18,
        va\="baseline", bbox\=dict(fc\="none", ec\="tab:orange"))

[ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(0.4)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("test line spacing for multiline text")
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 0.7)
[ax.yaxis.minorticks\_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#matplotlib.axis.Axis.minorticks_on "matplotlib.axis.Axis.minorticks_on")
()
[ax.yaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(which\="minor", grid\_color\="0.9")
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(which\="both")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![test line spacing for multiline text](https://matplotlib.org/stable/_images/sphx_glr_multiline_002_2_00x.png)

**Total running time of the script:** (0 minutes 1.251 seconds)

[`Download Jupyter notebook: multiline.ipynb`](https://matplotlib.org/stable/_downloads/c6761544e9275747ef2762700a87d329/multiline.ipynb)

[`Download Python source code: multiline.py`](https://matplotlib.org/stable/_downloads/54f178535adde28359d49641be996dbf/multiline.py)

[`Download zipped: multiline.zip`](https://matplotlib.org/stable/_downloads/d0948ed345f18a030cd4a4fdb06ba3d1/multiline.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)