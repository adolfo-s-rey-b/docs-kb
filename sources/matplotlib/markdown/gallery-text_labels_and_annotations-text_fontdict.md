[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#sphx-glr-download-gallery-text-labels-and-annotations-text-fontdict-py)
 to download the full example code.

Controlling style of text and labels using a dictionary[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#controlling-style-of-text-and-labels-using-a-dictionary "Link to this heading")

================================================================================================================================================================================================================================

This example shows how to share parameters across many text objects and labels by creating a dictionary of options passed across several functions.

![Damped exponential decay](https://matplotlib.org/stable/_images/sphx_glr_text_fontdict_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

[font](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 5.0, 100)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k')
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Damped exponential decay', fontdict\=[font](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(2, 0.65, r'$\\cos(2 \\pi t) \\exp(-t)$', fontdict\=[font](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
('time (s)', fontdict\=[font](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
('voltage (mV)', fontdict\=[font](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Tweak spacing to prevent clipping of ylabel
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(left\=0.15)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: text_fontdict.ipynb`](https://matplotlib.org/stable/_downloads/77fe2f922beea3ee690c61c6bf96e13f/text_fontdict.ipynb)

[`Download Python source code: text_fontdict.py`](https://matplotlib.org/stable/_downloads/26217c4473de44985babfe2e37d1d431/text_fontdict.py)

[`Download zipped: text_fontdict.zip`](https://matplotlib.org/stable/_downloads/04a6bde47d76891d5a78ff2aaf0ddee8/text_fontdict.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)