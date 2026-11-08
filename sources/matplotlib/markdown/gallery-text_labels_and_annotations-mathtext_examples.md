[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_examples.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_examples.html#sphx-glr-download-gallery-text-labels-and-annotations-mathtext-examples-py)
 to download the full example code.

Mathematical expressions[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_examples.html#mathematical-expressions "Link to this heading")

======================================================================================================================================================================

Selected features of Matplotlib's math rendering engine.

![Matplotlib's math rendering engine](https://matplotlib.org/stable/_images/sphx_glr_mathtext_examples_001_2_00x.png)

0 $W^{3\\beta}\_{\\delta\_1 \\rho\_1 \\sigma\_2} = U^{3\\beta}\_{\\delta\_1 \\rho\_1} + \\frac{1}{8 \\pi 2} \\int^{\\alpha\_2}\_{\\alpha\_2} d \\alpha^\\prime\_2 \\left\[\\frac{ U^{2\\beta}\_{\\delta\_1 \\rho\_1} - \\alpha^\\prime\_2U^{1\\beta}\_{\\rho\_1 \\sigma\_2} }{U^{0\\beta}\_{\\rho\_1 \\sigma\_2}}\\right\]$
1 $\\alpha\_i > \\beta\_i,\\ \\alpha\_{i+1}^j = {\\rm sin}(2\\pi f\_j t\_i) e^{-5 t\_i/\\tau},\\ \\ldots$
2 $\\frac{3}{4},\\ \\binom{3}{4},\\ \\genfrac{}{}{0}{}{3}{4},\\ \\left(\\frac{5 - \\frac{1}{x}}{4}\\right),\\ \\ldots$
3 $\\sqrt{2},\\ \\sqrt\[3\]{x},\\ \\ldots$
4 $\\mathrm{Roman}\\ , \\ \\mathit{Italic}\\ , \\ \\mathtt{Typewriter} \\ \\mathrm{or}\\ \\mathcal{CALLIGRAPHY}$
5 $\\acute a,\\ \\bar a,\\ \\breve a,\\ \\dot a,\\ \\ddot a, \\ \\grave a, \\ \\hat a,\\ \\tilde a,\\ \\vec a,\\ \\widehat{xyz},\\ \\widetilde{xyz},\\ \\ldots$
6 $\\alpha,\\ \\beta,\\ \\chi,\\ \\delta,\\ \\lambda,\\ \\mu,\\ \\Delta,\\ \\Gamma,\\ \\Omega,\\ \\Phi,\\ \\Pi,\\ \\Upsilon,\\ \\nabla,\\ \\aleph,\\ \\beth,\\ \\daleth,\\ \\gimel,\\ \\ldots$
7 $\\coprod,\\ \\int,\\ \\oint,\\ \\prod,\\ \\sum,\\ \\log,\\ \\sin,\\ \\approx,\\ \\oplus,\\ \\star,\\ \\varpropto,\\ \\infty,\\ \\partial,\\ \\Re,\\ \\leftrightsquigarrow, \\ \\ldots$

  

import re
import subprocess
import sys

import matplotlib.pyplot as plt

\# Selection of features following "Writing mathematical expressions" tutorial,
\# with randomly picked examples.
[mathtext\_demos](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    "Header demo":
        r"$W^{3\\beta}\_{\\delta\_1 \\rho\_1 \\sigma\_2} = "
        r"U^{3\\beta}\_{\\delta\_1 \\rho\_1} + \\frac{1}{8 \\pi 2} "
        r"\\int^{\\alpha\_2}\_{\\alpha\_2} d \\alpha^\\prime\_2 \\left\[\\frac{ "\
        r"U^{2\\beta}\_{\\delta\_1 \\rho\_1} - \\alpha^\\prime\_2U^{1\\beta}\_"\
        r"{\\rho\_1 \\sigma\_2} }{U^{0\\beta}\_{\\rho\_1 \\sigma\_2}}\\right\]$",

    "Subscripts and superscripts":
        r"$\\alpha\_i > \\beta\_i,\\ "
        r"\\alpha\_{i+1}^j = {\\rm sin}(2\\pi f\_j t\_i) e^{-5 t\_i/\\tau},\\ "
        r"\\ldots$",

    "Fractions, binomials and stacked numbers":
        r"$\\frac{3}{4},\\ \\binom{3}{4},\\ \\genfrac{}{}{0}{}{3}{4},\\ "
        r"\\left(\\frac{5 - \\frac{1}{x}}{4}\\right),\\ \\ldots$",

    "Radicals":
        r"$\\sqrt{2},\\ \\sqrt\[3\]{x},\\ \\ldots$",

    "Fonts":
        r"$\\mathrm{Roman}\\ , \\ \\mathit{Italic}\\ , \\ \\mathtt{Typewriter} \\ "
        r"\\mathrm{or}\\ \\mathcal{CALLIGRAPHY}$",

    "Accents":
        r"$\\acute a,\\ \\bar a,\\ \\breve a,\\ \\dot a,\\ \\ddot a, \\ \\grave a, \\ "
        r"\\hat a,\\ \\tilde a,\\ \\vec a,\\ \\widehat{xyz},\\ \\widetilde{xyz},\\ "
        r"\\ldots$",

    "Greek, Hebrew":
        r"$\\alpha,\\ \\beta,\\ \\chi,\\ \\delta,\\ \\lambda,\\ \\mu,\\ "
        r"\\Delta,\\ \\Gamma,\\ \\Omega,\\ \\Phi,\\ \\Pi,\\ \\Upsilon,\\ \\nabla,\\ "
        r"\\aleph,\\ \\beth,\\ \\daleth,\\ \\gimel,\\ \\ldots$",

    "Delimiters, functions and Symbols":
        r"$\\coprod,\\ \\int,\\ \\oint,\\ \\prod,\\ \\sum,\\ "
        r"\\log,\\ \\sin,\\ \\approx,\\ \\oplus,\\ \\star,\\ \\varpropto,\\ "
        r"\\infty,\\ \\partial,\\ \\Re,\\ \\leftrightsquigarrow, \\ \\ldots$",
}
[n\_lines](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([mathtext\_demos](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

def doall():
    \# Colors used in Matplotlib online documentation.
    mpl\_grey\_rgb \= (51 / 255, 51 / 255, 51 / 255)

    \# Creating figure and axis.
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 7))
    ax \= fig.add\_axes((0.01, 0.01, 0.98, 0.90),
                      facecolor\="white", frameon\=True)
    ax.set\_xlim(0, 1)
    ax.set\_ylim(0, 1)
    ax.set\_title("Matplotlib's math rendering engine",
                 color\=mpl\_grey\_rgb, fontsize\=14, weight\='bold')
    ax.set\_xticks(\[\])
    ax.set\_yticks(\[\])

    \# Gap between lines in axes coords
    line\_axesfrac \= 1 / [n\_lines](https://docs.python.org/3/library/functions.html#int "builtins.int")

    \# Plot header demonstration formula.
    full\_demo \= [mathtext\_demos](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['Header demo'\]
    ax.annotate(full\_demo,
                xy\=(0.5, 1. \- 0.59 \* line\_axesfrac),
                color\='tab:orange', ha\='center', fontsize\=20)

    \# Plot feature demonstration formulae.
    for i\_line, (title, demo) in enumerate([mathtext\_demos](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items()):
        print(i\_line, demo)
        if i\_line \== 0:
            continue

        baseline \= 1 \- i\_line \* line\_axesfrac
        baseline\_next \= baseline \- line\_axesfrac
        fill\_color \= \['white', 'tab:blue'\]\[i\_line % 2\]
        ax.axhspan(baseline, baseline\_next, color\=fill\_color, alpha\=0.2)
        ax.annotate(f'{title}:',
                    xy\=(0.06, baseline \- 0.3 \* line\_axesfrac),
                    color\=mpl\_grey\_rgb, weight\='bold')
        ax.annotate(demo,
                    xy\=(0.04, baseline \- 0.75 \* line\_axesfrac),
                    color\=mpl\_grey\_rgb, fontsize\=16)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

if '--latex' in [sys.argv](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    \# Run: python mathtext\_examples.py --latex
    \# Need amsmath and amssymb packages.
    with open("mathtext\_examples.ltx", "w") as fd:
        fd.write("\\\\documentclass{article}\\n")
        fd.write("\\\\usepackage{amsmath, amssymb}\\n")
        fd.write("\\\\begin{document}\\n")
        fd.write("\\\\begin{enumerate}\\n")

        for s in [mathtext\_demos](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values():
            s \= [re.sub](https://docs.python.org/3/library/re.html#re.sub "re.sub")
(r"(?<!\\\\)\\$", "$$", s)
            fd.write("\\\\item %s\\n" % s)

        fd.write("\\\\end{enumerate}\\n")
        fd.write("\\\\end{document}\\n")

    [subprocess.call](https://docs.python.org/3/library/subprocess.html#subprocess.call "subprocess.call")
(\["pdflatex", "mathtext\_examples.ltx"\])
else:
    doall()

**Total running time of the script:** (0 minutes 1.182 seconds)

[`Download Jupyter notebook: mathtext_examples.ipynb`](https://matplotlib.org/stable/_downloads/983012f0c1ca50a7d8560886c8b27470/mathtext_examples.ipynb)

[`Download Python source code: mathtext_examples.py`](https://matplotlib.org/stable/_downloads/23eac6456b32a7aa35c13776e6b555a4/mathtext_examples.py)

[`Download zipped: mathtext_examples.zip`](https://matplotlib.org/stable/_downloads/3a35875b1f3ffaca847532a67d848112/mathtext_examples.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)