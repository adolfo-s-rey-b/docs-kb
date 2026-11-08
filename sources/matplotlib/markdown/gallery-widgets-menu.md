[Skip to main content](https://matplotlib.org/stable/gallery/widgets/menu.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/menu.html#sphx-glr-download-gallery-widgets-menu-py)
 to download the full example code.

Menu[#](https://matplotlib.org/stable/gallery/widgets/menu.html#menu "Link to this heading")

=============================================================================================

Using texts to construct a simple menu.

![menu](https://matplotlib.org/stable/_images/sphx_glr_menu_001_2_00x.png)

from dataclasses import [dataclass](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass")

import matplotlib.pyplot as plt

import matplotlib.artist as artist
import matplotlib.patches as patches
from matplotlib.typing import [ColorType](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")

@dataclass
class ItemProperties:
    fontsize: float \= 14
    labelcolor: [ColorType](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")
 \= 'black'
    bgcolor: [ColorType](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")
 \= 'yellow'
    alpha: float \= 1.0

class MenuItem([artist.Artist](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
):
    padx \= 0.05  \# inches
    pady \= 0.05

    def \_\_init\_\_(self, [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, labelstr, props\=None, hoverprops\=None,
                 on\_select\=None):
        super().\_\_init\_\_()

        self.set\_figure([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
        self.labelstr \= labelstr

        self.props \= props if props is not None else ItemProperties()
        self.hoverprops \= (
            hoverprops if hoverprops is not None else ItemProperties())
        if self.[props.fontsize](https://docs.python.org/3/library/functions.html#int "builtins.int")
 != self.hoverprops.fontsize:
            raise NotImplementedError(
                'support for different font sizes not implemented')

        self.on\_select \= on\_select

        \# specify coordinates in inches.
        self.[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0, 0, labelstr, transform\=[fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
,
                              size\=[props.fontsize](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
        self.text\_bbox \= self.[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.get\_window\_extent(
            [fig.canvas.get\_renderer](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
())
        self.text\_bbox \= [fig.dpi\_scale\_trans.inverted](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.inverted "matplotlib.transforms.Affine2DBase.inverted")
().transform\_bbox(self.text\_bbox)

        self.rect \= [patches.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(
            (0, 0), 1, 1, transform\=[fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
        )  \# Will be updated later.

        self.set\_hover\_props(False)

        [fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('button\_release\_event', self.check\_select)

    def check\_select(self, event):
        over, \_ \= self.rect.contains(event)
        if not over:
            return
        if self.on\_select is not None:
            self.on\_select(self)

    def set\_extent(self, x, y, w, h, depth):
        self.rect.set(x\=x, y\=y, width\=w, height\=h)
        self.[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.set(position\=(x + self.padx, y + depth + self.pady / 2))
        self.hover \= False

    def draw(self, renderer):
        self.rect.draw(renderer)
        self.[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.draw(renderer)

    def set\_hover\_props(self, b):
        props \= self.hoverprops if b else self.props
        self.[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.set(color\=[props.labelcolor](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
        self.rect.set(facecolor\=[props.bgcolor](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, alpha\=[props.alpha](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

    def set\_hover(self, event):
        """
        Update the hover status of event and return whether it was changed.
        """
        b, \_ \= self.rect.contains(event)
        changed \= (b != self.hover)
        if changed:
            self.set\_hover\_props(b)
        self.hover \= b
        return changed

class Menu:
    def \_\_init\_\_(self, [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        self.figure \= [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

        self.[menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

        maxw \= max([item.text\_bbox.width](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.width "matplotlib.transforms.BboxBase.width")
 for item in [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
        maxh \= max([item.text\_bbox.height](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.height "matplotlib.transforms.BboxBase.height")
 for item in [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
        depth \= max(\-[item.text\_bbox.y0](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y0 "matplotlib.transforms.Bbox.y0")
 for item in [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

        x0 \= 1
        y0 \= 4

        width \= maxw + 2 \* [MenuItem.padx](https://docs.python.org/3/library/functions.html#float "builtins.float")
        height \= maxh + [MenuItem.pady](https://docs.python.org/3/library/functions.html#float "builtins.float")

        for item in [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
            left \= x0
            bottom \= y0 \- maxh \- [MenuItem.pady](https://docs.python.org/3/library/functions.html#float "builtins.float")

            item.set\_extent(left, bottom, width, height, depth)

            [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.artists.append(item)
            y0 \-= maxh + [MenuItem.pady](https://docs.python.org/3/library/functions.html#float "builtins.float")

        [fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('motion\_notify\_event', self.on\_move)

    def on\_move(self, event):
        if any(item.set\_hover(event) for item in self.[menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
            self.figure.canvas.draw()

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.3)
props \= ItemProperties(labelcolor\='black', bgcolor\='yellow',
                       fontsize\=15, alpha\=0.2)
hoverprops \= ItemProperties(labelcolor\='white', bgcolor\='blue',
                            fontsize\=15, alpha\=0.2)

[menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in ('open', 'close', 'save', 'save as', 'quit'):
    def on\_select(item):
        print(f'you selected {[item.labelstr](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}')
    item \= [MenuItem](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, props\=props, hoverprops\=hoverprops,
                    on\_select\=on\_select)
    [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append(item)

menu \= Menu([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [menuitems](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: menu.ipynb`](https://matplotlib.org/stable/_downloads/7fbe9039d13629f10dcf40d2c3d4986e/menu.ipynb)

[`Download Python source code: menu.py`](https://matplotlib.org/stable/_downloads/1d795d2dbb3742249ef04dbbdc524568/menu.py)

[`Download zipped: menu.zip`](https://matplotlib.org/stable/_downloads/f6930375790ab3ed6a54c5f0d798d9f6/menu.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)