[Skip to main content](https://matplotlib.org/stable/users/explain/text/pgf.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/text/pgf.html#sphx-glr-download-users-explain-text-pgf-py)
 to download the full example code.

Text rendering with XeLaTeX/LuaLaTeX via the `pgf` backend[#](https://matplotlib.org/stable/users/explain/text/pgf.html#text-rendering-with-xelatex-lualatex-via-the-pgf-backend "Link to this heading")

=========================================================================================================================================================================================================

Using the `pgf` backend, Matplotlib can export figures as pgf drawing commands that can be processed with pdflatex, xelatex or lualatex. XeLaTeX and LuaLaTeX have full Unicode support and can use any font that is installed in the operating system, making use of advanced typographic features of OpenType, AAT and Graphite. Pgf pictures created by `plt.savefig('figure.pgf')` can be embedded as raw commands in LaTeX documents. Figures can also be directly compiled and saved to PDF with `plt.savefig('figure.pdf')` by switching the backend

matplotlib.use('pgf')

or by explicitly requesting the use of the `pgf` backend

plt.savefig('figure.pdf', backend\='pgf')

or by registering it for handling pdf output

from matplotlib.backends.backend\_pgf import FigureCanvasPgf
matplotlib.backend\_bases.register\_backend('pdf', FigureCanvasPgf)

The last method allows you to keep using regular interactive backends and to save xelatex, lualatex or pdflatex compiled PDF files from the graphical user interface. Note that, in that case, the interactive display will still use the standard interactive backends (e.g., QtAgg), and in particular use latex to compile relevant text snippets.

Matplotlib's pgf support requires a recent [LaTeX](http://www.tug.org/)
 installation that includes the TikZ/PGF packages (such as [TeXLive](http://www.tug.org/texlive/)
), preferably with XeLaTeX or LuaLaTeX installed. If either pdftocairo or ghostscript is present on your system, figures can optionally be saved to PNG images as well. The executables for all applications must be located on your [`PATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH)
.

[`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 that control the behavior of the pgf backend:

| Parameter | Documentation |
| --- | --- |
| pgf.preamble | Lines to be included in the LaTeX preamble |
| pgf.rcfonts | Setup fonts from rc params using the fontspec package |
| pgf.texsystem | Either "xelatex" (default), "lualatex" or "pdflatex" |

Note

TeX defines a set of special characters, such as:

\# $ % & ~ \_ ^ \\ { }

Generally, these characters must be escaped correctly. For convenience, some characters (\_, ^, %) are automatically escaped outside of math environments. Other characters are not escaped as they are commonly needed in actual TeX expressions. However, one can configure TeX to treat them as "normal" characters (known as "catcode 12" to TeX) via a custom preamble, such as:

plt.rcParams\["pgf.preamble"\] \= (
    r"\\AtBeginDocument{\\catcode\`\\&=12\\catcode\`\\#=12}")

Multi-Page PDF Files[#](https://matplotlib.org/stable/users/explain/text/pgf.html#multi-page-pdf-files "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

The pgf backend also supports multipage pdf files using [`PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")

from matplotlib.backends.backend\_pgf import PdfPages
import matplotlib.pyplot as plt

with PdfPages('multipage.pdf', metadata\={'author': 'Me'}) as pdf:

    fig1, ax1 \= plt.subplots()
    ax1.plot(\[1, 5, 3\])
    pdf.savefig(fig1)

    fig2, ax2 \= plt.subplots()
    ax2.plot(\[1, 5, 3\])
    pdf.savefig(fig2)

Font specification[#](https://matplotlib.org/stable/users/explain/text/pgf.html#font-specification "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The fonts used for obtaining the size of text elements or when compiling figures to PDF are usually defined in the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
. You can also use the LaTeX default Computer Modern fonts by clearing the lists for `[rcParams["font.serif"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.serif#rcparam-font-serif) ` (default: `['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif']`), `[rcParams["font.sans-serif"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.sans-serif#rcparam-font-sans-serif) ` (default: `['DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']`) or `[rcParams["font.monospace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.monospace#rcparam-font-monospace) ` (default: `['DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Computer Modern Typewriter', 'Andale Mono', 'Nimbus Mono L', 'Courier New', 'Courier', 'Fixed', 'Terminal', 'monospace']`). Please note that the glyph coverage of these fonts is very limited. If you want to keep the Computer Modern font face but require extended Unicode support, consider installing the [Computer Modern Unicode](https://sourceforge.net/projects/cm-unicode/)
 fonts _CMU Serif_, _CMU Sans Serif_, etc.

When saving to `.pgf`, the font configuration Matplotlib used for the layout of the figure is included in the header of the text file.

import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    \# Use LaTeX default serif font.
    "font.serif": \[\],
    \# Use specific cursive fonts.
    "font.cursive": \["Comic Neue", "Comic Sans MS"\],
})

fig, ax \= plt.subplots(figsize\=(4.5, 2.5))

ax.plot(range(5))

ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family\="monospace")
ax.text(2.5, 2., "sans-serif", family\="DejaVu Sans")  \# Use specific sans font.
ax.text(2.5, 1., "comic", family\="cursive")
ax.set\_xlabel("µ is not $\\\\mu$")

Custom preamble[#](https://matplotlib.org/stable/users/explain/text/pgf.html#custom-preamble "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Full customization is possible by adding your own commands to the preamble. Use `[rcParams["pgf.preamble"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pgf.preamble#rcparam-pgf-preamble) ` (default: `''`) if you want to configure the math fonts, using `unicode-math` for example, or for loading additional packages. Also, if you want to do the font configuration yourself instead of using the fonts specified in the rc parameters, make sure to disable `[rcParams["pgf.rcfonts"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pgf.rcfonts#rcparam-pgf-rcfonts) ` (default: `True`).

import matplotlib as mpl

mpl.use("pgf")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",  \# use serif/main font for text elements
    "text.usetex": True,     \# use inline math for ticks
    "pgf.rcfonts": False,    \# don't setup fonts from rc parameters
    "pgf.preamble": "\\n".join(\[\
         r"\\usepackage{url}",            \# load additional packages\
         r"\\usepackage{unicode-math}",   \# unicode math setup\
         r"\\setmainfont{DejaVu Serif}",  \# serif font via preamble\
    \])
})

fig, ax \= plt.subplots(figsize\=(4.5, 2.5))

ax.plot(range(5))

ax.set\_xlabel("unicode text: я, ψ, €, ü")
ax.set\_ylabel(r"\\url{https://matplotlib.org}")
ax.legend(\["unicode math: $λ=∑\_i^∞ μ\_i^2$"\])

Choosing the TeX system[#](https://matplotlib.org/stable/users/explain/text/pgf.html#choosing-the-tex-system "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

The TeX system to be used by Matplotlib is chosen by `[rcParams["pgf.texsystem"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pgf.texsystem#rcparam-pgf-texsystem) ` (default: `'xelatex'`). Possible values are `'xelatex'` (default), `'lualatex'` and `'pdflatex'`. Please note that when selecting pdflatex, the fonts and Unicode handling must be configured in the preamble.

import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": "\\n".join(\[\
         r"\\usepackage\[utf8x\]{inputenc}",\
         r"\\usepackage\[T1\]{fontenc}",\
         r"\\usepackage{cmbright}",\
    \]),
})

fig, ax \= plt.subplots(figsize\=(4.5, 2.5))

ax.plot(range(5))

ax.text(0.5, 3., "serif", family\="serif")
ax.text(0.5, 2., "monospace", family\="monospace")
ax.text(2.5, 2., "sans-serif", family\="sans-serif")
ax.set\_xlabel(r"µ is not $\\mu$")

Troubleshooting[#](https://matplotlib.org/stable/users/explain/text/pgf.html#troubleshooting "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

*   Make sure LaTeX is working and on your [`PATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH)
     (for raster output, pdftocairo or ghostscript is also required). The [`PATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH)
     environment variable may need to be modified (in particular on Windows) to include the directories containing the executable. See [Environment variables](https://matplotlib.org/stable/install/environment_variables_faq.html#environment-variables)
     and [Setting environment variables in Windows](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-windows-environment-variables)
     for details.
    
*   Sometimes the font rendering in figures that are saved to png images is very bad. This happens when the pdftocairo tool is not available and ghostscript is used for the pdf to png conversion.
    
*   Make sure what you are trying to do is possible in a LaTeX document, that your LaTeX syntax is valid and that you are using raw strings if necessary to avoid unintended escape sequences.
    
*   `[rcParams["pgf.preamble"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pgf.preamble#rcparam-pgf-preamble) ` (default: `''`) provides lots of flexibility, and lots of ways to cause problems. When experiencing problems, try to minimalize or disable the custom preamble.
    
*   Configuring an `unicode-math` environment can be a bit tricky. The TeXLive distribution for example provides a set of math fonts which are usually not installed system-wide. XeLaTeX, unlike LuaLaTeX, cannot find these fonts by their name, which is why you might have to specify `\setmathfont{xits-math.otf}` instead of `\setmathfont{XITS Math}` or alternatively make the fonts available to your OS. See this [tex.stackexchange.com question](https://tex.stackexchange.com/q/43642/)
     for more details.
    
*   If the font configuration used by Matplotlib differs from the font setting in yout LaTeX document, the alignment of text elements in imported figures may be off. Check the header of your `.pgf` file if you are unsure about the fonts Matplotlib used for the layout.
    
*   Vector images and hence `.pgf` files can become bloated if there are a lot of objects in the graph. This can be the case for image processing or very big scatter graphs. In an extreme case this can cause TeX to run out of memory: "TeX capacity exceeded, sorry" You can configure latex to increase the amount of memory available to generate the `.pdf` image as discussed on [tex.stackexchange.com](https://tex.stackexchange.com/q/7953/)
    . Another way would be to "rasterize" parts of the graph causing problems using either the `rasterized=True` keyword, or `.set_rasterized(True)` as per [this example](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)
    .
    
*   Various math fonts are compiled and rendered only if corresponding font packages are loaded. Specifically, when using `\mathbf{}` on Greek letters, the default computer modern font may not contain them, in which case the letter is not rendered. In such scenarios, the `lmodern` package should be loaded.
    
*   If you still need help, please see [Get help](https://matplotlib.org/stable/users/faq.html#reporting-problems)
    

[`Download Jupyter notebook: pgf.ipynb`](https://matplotlib.org/stable/_downloads/a4123a58a7384c72d501fe8d2fe988e7/pgf.ipynb)

[`Download Python source code: pgf.py`](https://matplotlib.org/stable/_downloads/ef09ab1ef747b8ef0462b47da4a3a55e/pgf.py)

[`Download zipped: pgf.zip`](https://matplotlib.org/stable/_downloads/5b4db92fe603a1f09193065758cef265/pgf.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page