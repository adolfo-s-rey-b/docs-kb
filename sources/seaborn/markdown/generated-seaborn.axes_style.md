 

 Ctrl+K

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
    
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
    
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
    
*   [API](https://seaborn.pydata.org/api.html)
    
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
    
*   [Citing](https://seaborn.pydata.org/citing.html)
    
*   [FAQ](https://seaborn.pydata.org/faq.html)
    

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
    
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
    
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")
    

On this page

seaborn.axes\_style[#](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn-axes-style "Permalink to this heading")

====================================================================================================================================

seaborn.axes\_style(_style\=None_, _rc\=None_)[#](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style "Permalink to this definition")

Get the parameters that control the general style of the plots.

The style parameters control properties like the color of the background and whether a grid is enabled by default. This is accomplished using the matplotlib rcParams system.

The options are illustrated in the [aesthetics tutorial](https://seaborn.pydata.org/tutorial/aesthetics.html)
.

This function can also be used as a context manager to temporarily alter the global defaults. See [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
 or [`set_style()`](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style "seaborn.set_style")
 to modify the global defaults for all plots.

Parameters:

**style**None, dict, or one of {darkgrid, whitegrid, dark, white, ticks}

A dictionary of parameters or the name of a preconfigured style.

**rc**dict, optional

Parameter mappings to override the values in the preset seaborn style dictionaries. This only updates parameters that are considered part of the style definition.

Examples

Calling with no arguments will return the current defaults for the style parameters:

sns.axes\_style()

Copy to clipboard

{'axes.facecolor': 'white',
 'axes.edgecolor': 'black',
 'axes.grid': False,
 'axes.axisbelow': 'line',
 'axes.labelcolor': 'black',
 'figure.facecolor': 'white',
 'grid.color': '#b0b0b0',
 'grid.linestyle': '-',
 'text.color': 'black',
 'xtick.color': 'black',
 'ytick.color': 'black',
 'xtick.direction': 'out',
 'ytick.direction': 'out',
 'lines.solid\_capstyle': <CapStyle.projecting: 'projecting'\>,
 'patch.edgecolor': 'black',
 'patch.force\_edgecolor': False,
 'image.cmap': 'viridis',
 'font.family': \['sans-serif'\],
 'font.sans-serif': \['DejaVu Sans',\
  'Bitstream Vera Sans',\
  'Computer Modern Sans Serif',\
  'Lucida Grande',\
  'Verdana',\
  'Geneva',\
  'Lucid',\
  'Arial',\
  'Helvetica',\
  'Avant Garde',\
  'sans-serif'\],
 'xtick.bottom': True,
 'xtick.top': False,
 'ytick.left': True,
 'ytick.right': False,
 'axes.spines.left': True,
 'axes.spines.bottom': True,
 'axes.spines.right': True,
 'axes.spines.top': True}

Copy to clipboard

Calling with the name of a predefined style will show those parameter values:

sns.axes\_style("darkgrid")

Copy to clipboard

{'figure.facecolor': 'white',
 'axes.labelcolor': '.15',
 'xtick.direction': 'out',
 'ytick.direction': 'out',
 'xtick.color': '.15',
 'ytick.color': '.15',
 'axes.axisbelow': True,
 'grid.linestyle': '-',
 'text.color': '.15',
 'font.family': \['sans-serif'\],
 'font.sans-serif': \['Arial',\
  'DejaVu Sans',\
  'Liberation Sans',\
  'Bitstream Vera Sans',\
  'sans-serif'\],
 'lines.solid\_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force\_edgecolor': True,
 'image.cmap': 'rocket',
 'xtick.top': False,
 'ytick.right': False,
 'axes.grid': True,
 'axes.facecolor': '#EAEAF2',
 'axes.edgecolor': 'white',
 'grid.color': 'white',
 'axes.spines.left': True,
 'axes.spines.bottom': True,
 'axes.spines.right': True,
 'axes.spines.top': True,
 'xtick.bottom': False,
 'ytick.left': False}

Copy to clipboard

Use the function as a context manager to temporarily change the style of your plots:

with sns.axes\_style("whitegrid"):
    sns.barplot(x\=\[1, 2, 3\], y\=\[2, 5, 3\])

Copy to clipboard

![../_images/axes_style_5_0.png](https://seaborn.pydata.org/_images/axes_style_5_0.png)