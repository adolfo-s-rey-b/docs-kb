[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_table.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_table.html#sphx-glr-download-gallery-text-labels-and-annotations-font-table-py)
 to download the full example code.

Font table[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_table.html#font-table "Link to this heading")

===================================================================================================================================

Matplotlib's font support is provided by the FreeType library.

Here, we use [`table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.table.html#matplotlib.axes.Axes.table "matplotlib.axes.Axes.table")
 to draw a table that shows the glyphs by Unicode codepoint. For brevity, the table only contains the first 256 glyphs.

The example is a full working script. You can download it and use it to investigate a font by running

python font\_table.py /path/to/font/file

![DejaVuSans.ttf](https://matplotlib.org/stable/_images/sphx_glr_font_table_001_2_00x.png)

import os
from pathlib import [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
import unicodedata

import matplotlib.pyplot as plt

import matplotlib.font\_manager as fm
from matplotlib.ft2font import [FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")

def print\_glyphs(path):
    """
    Print the all glyphs in the given font file to stdout.

    Parameters
    ----------
    path : str or None
        The path to the font file.  If None, use Matplotlib's default font.
    """
    if path is None:
        path \= [fm.findfont](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
([fm.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
())  \# The default font.

    font \= [FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
(path)

    charmap \= font.get\_charmap()
    max\_indices\_len \= len(str(max(charmap.values())))

    print("The font face contains the following glyphs:")
    for char\_code, glyph\_index in charmap.items():
        char \= chr(char\_code)
        name \= [unicodedata.name](https://docs.python.org/3/library/unicodedata.html#unicodedata.name "unicodedata.name")
(
                char,
                f"{char\_code:#x} ({font.get\_glyph\_name(glyph\_index)})")
        print(f"{glyph\_index:\>{max\_indices\_len}} {char} {name}")

def draw\_font\_table(path):
    """
    Draw a font table of the first 255 chars of the given font.

    Parameters
    ----------
    path : str or None
        The path to the font file.  If None, use Matplotlib's default font.
    """
    if path is None:
        path \= [fm.findfont](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.findfont "matplotlib.font_manager.findfont")
([fm.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
())  \# The default font.

    font \= [FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
(path)
    \# A charmap is a mapping of "character codes" (in the sense of a character
    \# encoding, e.g. latin-1) to glyph indices (i.e. the internal storage table
    \# of the font face).
    \# In FreeType>=2.1, a Unicode charmap (i.e. mapping Unicode codepoints)
    \# is selected by default.  Moreover, recent versions of FreeType will
    \# automatically synthesize such a charmap if the font does not include one
    \# (this behavior depends on the font format; for example it is present
    \# since FreeType 2.0 for Type 1 fonts but only since FreeType 2.8 for
    \# TrueType (actually, SFNT) fonts).
    \# The code below (specifically, the \`\`chr(char\_code)\`\` call) assumes that
    \# we have indeed selected a Unicode charmap.
    codes \= font.get\_charmap().items()

    labelc \= \[f"{i:X}" for i in range(16)\]
    labelr \= \[f"{i:02X}" for i in range(0, 16\*16, 16)\]
    chars \= \[\["" for c in range(16)\] for r in range(16)\]

    for char\_code, glyph\_index in codes:
        if char\_code \>= 256:
            continue
        row, col \= divmod(char\_code, 16)
        chars\[row\]\[col\] \= chr(char\_code)

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 4))
    ax.set\_title([os.path.basename](https://docs.python.org/3/library/os.path.html#os.path.basename "os.path.basename")
(path))
    ax.set\_axis\_off()

    table \= ax.table(
        cellText\=chars,
        rowLabels\=labelr,
        colLabels\=labelc,
        rowColours\=\["palegreen"\] \* 16,
        colColours\=\["palegreen"\] \* 16,
        cellColours\=\[\[".95" for c in range(16)\] for r in range(16)\],
        cellLoc\='center',
        loc\='upper left',
    )
    for key, cell in table.get\_celld().items():
        row, col \= key
        if row \> 0 and col \> \-1:  \# Beware of table's idiosyncratic indexing...
            cell.set\_text\_props(font\=[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
(path))

    fig.tight\_layout()
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

if \_\_name\_\_ \== "\_\_main\_\_":
    from argparse import [ArgumentParser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")

    [parser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 \= [ArgumentParser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
(description\="Display a font table.")
    [parser.add\_argument](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
("path", nargs\="?", help\="Path to the font file.")
    [parser.add\_argument](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
("--print-all", action\="store\_true",
                        help\="Additionally, print all chars to stdout.")
    [args](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
 \= [parser.parse\_args](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
()

    if [args.print\_all](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
:
        print\_glyphs([args](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
.path)
    draw\_font\_table([args](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
.path)

**Total running time of the script:** (0 minutes 2.757 seconds)

[`Download Jupyter notebook: font_table.ipynb`](https://matplotlib.org/stable/_downloads/c272bdcecbece4cba783b89e80ea4b70/font_table.ipynb)

[`Download Python source code: font_table.py`](https://matplotlib.org/stable/_downloads/bc9735ba2ce09278809c68b7f82bdee8/font_table.py)

[`Download zipped: font_table.zip`](https://matplotlib.org/stable/_downloads/4a748e2c7dfb900c906c7f95f48a13ac/font_table.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)