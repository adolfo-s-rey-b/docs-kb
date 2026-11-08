[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

Reusing JupyterLab UI[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#reusing-jupyterlab-ui "Link to this heading")

================================================================================================================================================

The [`ui-components`](https://jupyterlab.readthedocs.io/en/stable/api/modules/ui-components.html)
 package provides UI elements that are widely used in JupyterLab core, and that can be reused in your own extensions.

For example, all of the icons in JupyterLab core can be reused via [`LabIcon`](https://jupyterlab.readthedocs.io/en/stable/api/classes/ui-components.LabIcon-1.html)
. You can also use `LabIcon` to create your own custom icons that will be able to automatically change color to match the current JupyterLab theme.

[`LabIcon` - set up and render icons](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#id1)
[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#labicon-set-up-and-render-icons "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`LabIcon`](https://jupyterlab.readthedocs.io/en/stable/api/classes/ui-components.LabIcon-1.html)
 is the icon class used by JupyterLab, and is part of the new system introduced in JupyterLab v2.0.

### How JupyterLab handles icons[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#how-jupyterlab-handles-icons "Link to this heading")

The @jupyterlab/ui-components package provides icons to the rest of JupyterLab, in the form of a set of `LabIcon` instances (currently about 80). All of the icons in the core JupyterLab packages are rendered using one of these `LabIcon` instances.

### Using the icons in your own code[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#using-the-icons-in-your-own-code "Link to this heading")

You can use any of JupyterLab icons in your own code via an `import` statement. For example, to use `jupyterIcon` you would first do:

import { jupyterIcon } from '@jupyterlab/ui-components';

Copy to clipboard

### How to render an icon into a DOM node[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#how-to-render-an-icon-into-a-dom-node "Link to this heading")

Icons can be added as children to any `div` or `span` nodes using the `icon.element(...)` method (where `icon` is any instance of `LabIcon`). For example, to render the Jupyter icon you could do:

jupyterIcon.element({
  container: elem,
  height: '16px',
  width: '16px',
  marginLeft: '2px'
});

Copy to clipboard

where `elem` is any `HTMLElement` with a `div` or `span` tag. As shown in the above example, the icon can be styled by passing CSS parameters into `.element(...)`. Any valid CSS parameter can be used (one catch: snake case params do have to be converted to camel case: instead of `foo-bar: '8px'`, you’d need to use `fooBar: '8px'`.

### How to render an icon as a React component[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#how-to-render-an-icon-as-a-react-component "Link to this heading")

Icons can also be rendered using React. The `icon.react` parameter holds a standard React component that will display the icon on render. Like any React component, `icon.react` can be used in various ways.

For example, here is how you would add the Jupyter icon to the render tree of another React component:

public render() {
  return (
    <div className\="outer"\>
      <div className\="inner"\>
        <jupyterIcon.react tag\="span" right\="7px" top\="5px" />
        "and here's a text node"
      </div\>
    </div\>
  );
}

Copy to clipboard

Alternatively, you can just render the icon directly into any existing DOM node `elem` by using the `ReactDOM` module:

ReactDOM.render(jupyterIcon.react, elem);

Copy to clipboard

If do you use `ReactDOM` to render, and if the `elem` node is ever removed from the DOM, you’ll first need to clean it up:

ReactDOM.unmountComponentAtNode(elem);

Copy to clipboard

This cleanup step is not a special property of `LabIcon`, but is instead needed for any React component that is rendered directly at the top level by `ReactDOM`: failure to call `unmountComponentAtNode` can result in a memory leak.

### How to create your own custom `LabIcon`[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#how-to-create-your-own-custom-labicon "Link to this heading")

You can create your own custom icon by constructing a new instance of `LabIcon`:

export const fooIcon \= new LabIcon({
  name: 'barpkg:foo',
  svgstr: '<svg>...</svg>'
});

Copy to clipboard

where `name` should be of the form “your-pkg:icon-name”, and `svgstr` is the raw contents of your icon’s svg file.

### How to create a new `LabIcon` from an external svg file[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#how-to-create-a-new-labicon-from-an-external-svg-file "Link to this heading")

Although you can copy-and-paste an svg directly into the `LabIcon` constructor, the best practice is to keep the svg for each of your icons in its own separate svg file. You will need to have an `svg.d.ts` file at the root of your project’s `src` folder:

// svg.d.ts

declare module '\*.svg' {
  const value: string;
  export default value;
}

Copy to clipboard

You can then `import` the contents of an svg file:

import fooSvgstr from 'path-to-your/foo.svg';

export const fooIcon \= new LabIcon({
  name: 'barpkg:foo',
  svgstr: fooSvgstr
});

Copy to clipboard

### Sync icon color to JupyterLab theme[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#sync-icon-color-to-jupyterlab-theme "Link to this heading")

_Example svgs with class annotation can be found in [ui-components/style/icons](https://github.com/jupyterlab/jupyterlab/tree/f0153e0258b32674c9aec106383ddf7b618cebab/packages/ui-components/style/icons)
_

You can ensure that the colors of your custom

`LabIcon`

sync up to the colors of the current JupyterLab theme by adding appropriate

`class`

annotations to each colored element of your icon’s svg.

In other words, each element of your svg that a

`fill="..."`

or a

`stroke="..."`

property should also have a

`class="jp-icon<whatever>"`

property.

#### Available icon classes[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#available-icon-classes "Link to this heading")

_Icon-related CSS classes are defined in [ui-components/style/icons.css](https://github.com/jupyterlab/jupyterlab/blob/f0153e0258b32674c9aec106383ddf7b618cebab/packages/ui-components/style/icons.css)
_

All colors shown are for the standard light/dark theme, mouse over for hex values.

##### `jp-iconX`: contrast to theme background[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#jp-iconx-contrast-to-theme-background "Link to this heading")

*   jp-icon0: #111 / #fff
*   jp-icon1: #212121 / #fff
*   jp-icon2: #424242 / #eee
*   jp-icon3: #616161 / #bdbdbd
*   jp-icon4: #757575 / #757575

Most one-color icons in JupyterLab (including the sidebar and toolbar icons) are colored using the `jp-icon3` class.

For light/dark themes, `jp-icon0` corresponds to the darkest/lightest background color, while `jp-icon1` is somewhat lighter/darker, and so forth.

##### `jp-icon-accentX`: match to theme background[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#jp-icon-accentx-match-to-theme-background "Link to this heading")

*   jp-icon-accent0: #fff / #111
*   jp-icon-accent1: #fff / #212121
*   jp-icon-accent2: #eee / #424242
*   jp-icon-accent3: #bdbdbd / #616161
*   jp-icon-accent4: #757575 / #757575

For light/dark themes, `jp-icon-accent0` corresponds to the lightest/darkest background color, while `jp-icon-accent1` is somewhat darker/lighter, and so forth.

#### Adding classes to a one-color icon[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#adding-classes-to-a-one-color-icon "Link to this heading")

For most simple, one-color icons, it is desirable for the icon’s color to strongly contrast with that of the application’s background. You can achieve this using one of the `jp-iconX` classes.

**Example: check icon**

_svg source:_

<svg xmlns\="http://www.w3.org/2000/svg" width\="100" viewBox\="0 0 24 24"\>
  <path
    class\="jp-icon3"
    fill\="#616161"
    d\="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"
  />
</svg\>

Copy to clipboard

_rendered icon:_

#### Adding classes to a multi-colored icon[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#adding-classes-to-a-multi-colored-icon "Link to this heading")

For more complex icons, each element that needs to match the background should be annotated with a `jp-icon-accentX` class, while each element that needs to contrast with the background should be annotated with a `jp-iconX` class.

**Example: close-circle icon**

_svg source:_

<svg xmlns\="http://www.w3.org/2000/svg" width\="100" viewBox\="0 0 24 24"\>
  <circle class\="jp-icon3" fill\="#616161" cx\="12" cy\="12" r\="11" />
  <rect
    class\="jp-icon-accent0"
    fill\="#fff"
    height\="18"
    width\="2"
    x\="11"
    y\="3"
    transform\="rotate(315, 12, 12)"
  />
  <rect
    class\="jp-icon-accent0"
    fill\="#fff"
    height\="18"
    width\="2"
    x\="11"
    y\="3"
    transform\="rotate(45, 12, 12)"
  />
</svg\>

Copy to clipboard

_rendered icon:_

### Background[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#background "Link to this heading")

#### Icon handling in JupyterLab[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#icon-handling-in-jupyterlab "Link to this heading")

Pre JupyterLab 2.0, most icons were created using the icons-as-css-background pattern:

*   Set up the icon’s svg as a `background-image` in CSS:
    
    /\* CSS \*/
    
    .jp-FooIcon {
      background-image: url('path-to-your/foo.svg');
    }
    
    Copy to clipboard
    
*   Add the icon to the DOM by constructing an otherwise empty DOM node with the appropriate class:
    
    // typescript
    
    const e \= document.createElement('div');
    e.className \= 'jp-FooIcon';
    document.body.append(e);
    
    Copy to clipboard
    

What you end up with is a single DOM node that has the “foo” icon as a background image.

Post JupyterLab 2.0, nearly all icons in core are now created using [LabIcon](https://github.com/jupyterlab/jupyterlab/blob/f0153e0258b32674c9aec106383ddf7b618cebab/packages/ui-components/src/icon/labicon.tsx)
 and the icons-as-inline-svg pattern:

*   Construct a new instance of LabIcon from the icon’s name and svg:
    
    // typescript
    
    // svgstr is the raw contents of an icon's svg file
    export const fooIcon \= new LabIcon({
      name: 'barpkg:foo',
      svgstr: '<svg>...</svg>'
    });
    
    Copy to clipboard
    
*   Add the icon to the DOM using the appropriate property of your LabIcon instance (either LabIcon.element() to directly create a DOM node, or LabIcon.react to get the icon as a react component):
    
    // typescript
    
    const e \= fooIcon.element();
    document.body.append(e);
    
    Copy to clipboard
    

What you end up with is a DOM node (by default a ‘div’) that has an inline svg node as a child.

#### `background-image` vs inline svg[#](https://jupyterlab.readthedocs.io/en/stable/extension/ui_components.html#background-image-vs-inline-svg "Link to this heading")

The big limitation of the old icon-as-css-background pattern is that svg images rendered as `background-image` are invisible to CSS. On the other hand, an icon rendered as an inline svg node is fully exposed to the CSS. This allows us to dynamically change icon styling as needed simply by modifying our CSS. Most importantly, this allows us to recolor icons according to JupyterLab’s current theme.

On this page

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/ui_components.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/ui_components.md.txt)