[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-tex-demo-py)
 to download the full example code.

Render math equations using TeX[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html#render-math-equations-using-tex "Link to this heading")

===========================================================================================================================================================================

You can use TeX to render all of your Matplotlib text by setting `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) to True. This requires that you have TeX and the other dependencies described in the [Text rendering with LaTeX](https://matplotlib.org/stable/users/explain/text/usetex.html#usetex)
 tutorial properly installed on your system. Matplotlib caches processed TeX expressions, so that only the first occurrence of an expression triggers a TeX compilation. Later occurrences reuse the rendered image from the cache and are thus faster.

Unicode input is supported, e.g. for the y-axis label in this example.

import matplotlib.pyplot as plt
import numpy as np

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['text.usetex'\] \= True

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, 100)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + 2

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 4), tight\_layout\=True)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
(r'\\textbf{time (s)}')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('\\\\textit{Velocity (\\N{DEGREE SIGN}/sec)}', fontsize\=16)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(r'\\TeX\\ is Number $\\displaystyle\\sum\_{n=1}^\\infty'
             r'\\frac{-e^{i\\pi}}{2^n}$!', fontsize\=16, color\='r')

![\TeX\ is Number $\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_001_2_00x.png)

A more complex example.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
\# interface tracking profiles
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 500
[delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.6
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, (1 \- [np.tanh](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4 \* [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
)) / 2,    \# phase field tanh profiles
        [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, (1.4 + [np.tanh](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4 \* [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
)) / 4, "C2",  \# composition profile
        [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 < 0, "k--")                        \# sharp interface

\# legend
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(("phase field", "level set", "sharp interface"),
          shadow\=True, loc\=(0.01, 0.48), handlelength\=1.5, fontsize\=16)

\# the arrow
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
("", xy\=(\-[delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2., 0.1), xytext\=([delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2., 0.1),
            arrowprops\=dict(arrowstyle\="<->", connectionstyle\="arc3"))
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0, 0.1, r"$\\delta$",
        color\="black", fontsize\=24,
        horizontalalignment\="center", verticalalignment\="center",
        bbox\=dict(boxstyle\="round", fc\="white", ec\="black", pad\=0.2))

\# Use tex in labels
[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[\-1, 0, 1\])
[ax.set\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
(\["$-1$", r"$\\pm 0$", "$+1$"\], color\="k", size\=20)

\# Left Y-axis labels, combine math mode and text mode
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
(r"\\bf{phase field} $\\phi$", color\="C0", fontsize\=20)
[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[0, 0.5, 1\])
[ax.set\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
(\[r"\\bf{0}", r"\\bf{.5}", r"\\bf{1}"\], color\="k", size\=20)

\# Right Y-axis labels
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1.02, 0.5, r"\\bf{level set} $\\phi$",
        color\="C2", fontsize\=20, rotation\=90,
        horizontalalignment\="left", verticalalignment\="center",
        clip\_on\=False, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

\# Use multiline environment inside a \`text\`.
\# level set equations
[eq1](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= (r"\\begin{eqnarray\*}"
       r"|\\nabla\\phi| &=& 1,\\\\"
       r"\\frac{\\partial \\phi}{\\partial t} + U|\\nabla \\phi| &=& 0 "
       r"\\end{eqnarray\*}")
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1, 0.9, [eq1](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, color\="C2", fontsize\=18,
        horizontalalignment\="right", verticalalignment\="top")

\# phase field equations
[eq2](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= (r"\\begin{eqnarray\*}"
       r"\\mathcal{F} &=& \\int f\\left( \\phi, c \\right) dV, \\\\ "
       r"\\frac{ \\partial \\phi } { \\partial t } &=& -M\_{ \\phi } "
       r"\\frac{ \\delta \\mathcal{F} } { \\delta \\phi }"
       r"\\end{eqnarray\*}")
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.18, 0.18, [eq2](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, color\="C0", fontsize\=16)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-1, .30, r"gamma: $\\gamma$", color\="r", fontsize\=20)
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-1, .18, r"Omega: $\\Omega$", color\="b", fontsize\=20)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tex demo](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_002_2_00x.png)

**Total running time of the script:** (0 minutes 1.350 seconds)

[`Download Jupyter notebook: tex_demo.ipynb`](https://matplotlib.org/stable/_downloads/84173137b190a55e7ea7a5a3a20037e1/tex_demo.ipynb)

[`Download Python source code: tex_demo.py`](https://matplotlib.org/stable/_downloads/3e49b41bad58a5fe4ed136d033412e7c/tex_demo.py)

[`Download zipped: tex_demo.zip`](https://matplotlib.org/stable/_downloads/23f9461a3f38495a2c49660e20f0ef34/tex_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)