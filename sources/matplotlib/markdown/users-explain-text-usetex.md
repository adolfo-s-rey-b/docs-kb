[Skip to main content](https://matplotlib.org/stable/users/explain/text/usetex.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/text/usetex.html#sphx-glr-download-users-explain-text-usetex-py)
 to download the full example code.

Text rendering with LaTeX[#](https://matplotlib.org/stable/users/explain/text/usetex.html#text-rendering-with-latex "Link to this heading")

============================================================================================================================================

Matplotlib can use LaTeX to render text. This is activated by setting `text.usetex : True` in your rcParams, or by setting the `usetex` property to True on individual [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects. Text handling through LaTeX is slower than Matplotlib's very capable [mathtext](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
, but is more flexible, since different LaTeX packages (font packages, math packages, etc.) can be used. The results can be striking, especially when you take care to use the same fonts in your figures as in the main document.

Matplotlib's LaTeX support requires a working [LaTeX](http://www.tug.org/)
 installation. For the \*Agg backends, [dvipng](http://www.nongnu.org/dvipng/)
 is additionally required; for the PS backend, [PSfrag](https://ctan.org/pkg/psfrag)
, [dvips](https://tug.org/texinfohtml/dvips.html)
 and [Ghostscript](https://ghostscript.com/)
 are additionally required. For the PDF and SVG backends, if LuaTeX is present, it will be used to speed up some post-processing steps, but note that it is not used to parse the TeX string itself (only LaTeX is supported). The executables for these external dependencies must all be located on your [`PATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH)
.

Only a small number of font families (defined by the [PSNFSS](http://www.ctan.org/tex-archive/macros/latex/required/psnfss/psnfss2e.pdf)
 scheme) are supported. They are listed here, with the corresponding LaTeX font selection commands and LaTeX packages, which are automatically used.

| generic family | fonts |
| --- | --- |
| serif (`\rmfamily`) | Computer Modern Roman, Palatino (`mathpazo`), Times (`mathptmx`), Bookman (`bookman`), New Century Schoolbook (`newcent`), Charter (`charter`) |
| sans-serif (`\sffamily`) | Computer Modern Serif, Helvetica (`helvet`), Avant Garde (`avant`) |
| cursive (`\rmfamily`) | Zapf Chancery (`chancery`) |
| monospace (`\ttfamily`) | Computer Modern Typewriter, Courier (`courier`) |

The default font family (which does not require loading any LaTeX package) is Computer Modern. All other families are Adobe fonts. Times and Palatino each have their own accompanying math fonts, while the other Adobe serif fonts make use of the Computer Modern math fonts.

To enable LaTeX and select a font, use e.g.:

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})

or equivalently, set your [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
 to:

text.usetex : true
font.family : Helvetica

It is also possible to instead set `font.family` to one of the generic family names and then configure the corresponding generic family; e.g.:

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})

(this was the required approach until Matplotlib 3.5).

Here is the standard example, [Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)
:

[![../../../_images/sphx_glr_tex_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_001.png)](https://matplotlib.org/gallery/text_labels_and_annotations/tex_demo.html)

Note that display math mode (`$$ e=mc^2 $$`) is not supported, but adding the command `\displaystyle`, as in the above demo, will produce the same results.

Non-ASCII characters (e.g. the degree sign in the y-label above) are supported to the extent that they are supported by [inputenc](https://ctan.org/pkg/inputenc)
.

Note

For consistency with the non-usetex case, Matplotlib special-cases newlines, so that single-newlines yield linebreaks (rather than being interpreted as whitespace in standard LaTeX).

Matplotlib uses the [underscore](https://ctan.org/pkg/underscore)
 package so that underscores (`_`) are printed "as-is" in text mode (rather than causing an error as in standard LaTeX). Underscores still introduce subscripts in math mode.

Note

Certain characters require special escaping in TeX, such as:

\# $ % & ~ ^ \\ { } \\( \\) \\\[ \\\]

Therefore, these characters will behave differently depending on `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`). As noted above, underscores (`_`) do not require escaping outside of math mode.

Note

LaTeX always defaults to using a serif font for math (even when `rcParams["font.family"] = "sans-serif"`). If desired, adding `\usepackage{sfmath}` to `rcParams["text.latex.preamble"]` lets LaTeX output sans-serif math.

PostScript options[#](https://matplotlib.org/stable/users/explain/text/usetex.html#postscript-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

In order to produce encapsulated PostScript (EPS) files that can be embedded in a new LaTeX document, the default behavior of Matplotlib is to distill the output, which removes some PostScript operators used by LaTeX that are illegal in an EPS file. This step produces results which may be unacceptable to some users, because the text is coarsely rasterized and converted to bitmaps, which are not scalable like standard PostScript, and the text is not searchable. One workaround is to set `[rcParams["ps.distiller.res"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.distiller.res#rcparam-ps-distiller-res) ` (default: `6000`) to a higher value (perhaps 6000) in your rc settings, which will produce larger files but may look better and scale reasonably. A better workaround, which requires [Poppler](https://poppler.freedesktop.org/)
 or [Xpdf](http://www.xpdfreader.com/)
, can be activated by changing `[rcParams["ps.usedistiller"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.usedistiller#rcparam-ps-usedistiller) ` (default: `None`) to `xpdf`. This alternative produces PostScript without rasterizing text, so it scales properly, can be edited in Adobe Illustrator, and searched text in pdf documents.

Troubleshooting[#](https://matplotlib.org/stable/users/explain/text/usetex.html#troubleshooting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

*   Try deleting your `.matplotlib/tex.cache` directory. If you don't know where to find `.matplotlib`, see [matplotlib configuration and cache directory locations](https://matplotlib.org/stable/install/index.html#locating-matplotlib-config-dir)
    .
    
*   Make sure LaTeX, dvipng, and Ghostscript are each working and on your [`PATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH)
    . The [`PATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH)
     environment variable may need to be modified (in particular on Windows) to include the directories containing the executables. See [Environment variables](https://matplotlib.org/stable/install/environment_variables_faq.html#environment-variables)
     and [Setting environment variables in Windows](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-windows-environment-variables)
     for details.
    
*   Make sure what you are trying to do is possible in a LaTeX document, that your LaTeX syntax is valid and that you are using raw strings if necessary to avoid unintended escape sequences.
    
*   `[rcParams["text.latex.preamble"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.latex.preamble#rcparam-text-latex-preamble) ` (default: `''`) is not officially supported. This option provides lots of flexibility, and lots of ways to cause problems. Please disable this option before reporting problems.
    
*   Using MiKTeX with Computer Modern fonts, if you get odd \*Agg and PNG results, go to MiKTeX/Options and update your format files.
    
*   Some required LaTeX packages, such as type1cm, may be missing from minimalist TeX installs. Required packages are listed at [LaTeX dependencies](https://matplotlib.org/stable/install/dependencies.html#tex-dependencies)
    .
    
*   If you still need help, please see [Get help](https://matplotlib.org/stable/users/faq.html#reporting-problems)
    .
    

[`Download Jupyter notebook: usetex.ipynb`](https://matplotlib.org/stable/_downloads/0a2cf45539c4f5419bdc3df46be568cb/usetex.ipynb)

[`Download Python source code: usetex.py`](https://matplotlib.org/stable/_downloads/e7509c9ac8939780fe9a4bbd1e4328a1/usetex.py)

[`Download zipped: usetex.zip`](https://matplotlib.org/stable/_downloads/bca5931f53b43102b6a9b7ee9a4eeb29/usetex.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page