*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#mdn-search)
    

`path-length` CSS property
==========================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#browser_compatibility)
 carefully before using this in production.

The **`path-length`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a total path length, in user units. All path computations are then scaled using the ratio `path-length` / _(computed value of path length)_ — this includes text paths, animation paths, and various stroke operations.

The `path-length` property only applies to [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)
, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)
, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
.

**Note:** If present, the `path-length` CSS property overrides an SVG element's [`pathLength`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/pathLength)
 attribute. This property doesn't apply to SVG, HTML, or pseudo-elements other than those listed above.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    path-length: none;
    
    /* <length> values */
    path-length: 0;
    path-length: 70px;
    path-length: 500px;
    
    /* Global values */
    path-length: inherit;
    path-length: initial;
    path-length: revert;
    path-length: revert-layer;
    path-length: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#none)

No author path length is specified and the user agent's own computed path length is used for all path-related calculations.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#length)

A non-negative [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing an author-defined total path length.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | The SVG [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)<br>, [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br>, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br>, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)<br>, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)<br>, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)<br>, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | The keyword `none` or an absolute length. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

path-length =   
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#basic_usage)

This example defines a path and shows how to apply a path length to it using the `path-length` CSS property.

#### SVG

Our SVG defines a single curved [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 element with a colored [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
. It includes a [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-dasharray)
 attribute that defines a regular dashed pattern for the stroke.

html

    <svg viewBox="0 0 600 200">
      <path
        d="M 30 100 C 150 20, 250 180, 380 100 S 520 20, 570 100"
        fill="none"
        stroke="#D85A30"
        stroke-width="4"
        stroke-dasharray="24 24"></path>
    </svg>
    

#### CSS

We set a `path-length` value on the `<path>`:

css

    path {
      path-length: 500px;
    }
    

#### Results

Setting a large `path-length` value results in the dashes becoming smaller and more frequent.

### [Animating `path-length`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#animating_path-length)

One major advantage of making `path-length` available as a CSS property is that you can apply standard CSS functionality such as [animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 and [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 to it. This example builds on the previous one, showing how to animate a `path-length` with a CSS animation.

#### HTML and SVG

This example includes the same SVG `<path>` as the previous one. In addition, it includes an [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 element that can be used to change the value of `path-length` applied to the `<path>` at runtime. We also include an [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
 element to display the current slider value.

html

    <div>
      <label for="path-slider">Adjust path-length</label>
      <input type="range" id="path-slider" min="0" max="800" value="200" />
      <output>200</output>
    </div>
    

#### CSS

On the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 element, we define a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 called `--path-length` and give it an initial value of `200px`. We then set the `<path>` element's `path-length` value to the `--path-length` property, and set an [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 on it that runs an infinite number of times and alternates between forwards and backwards.

css

    :root {
      --path-length: 200px;
    }
    
    path {
      path-length: var(--path-length);
      animation: path-length-anim 2s alternate infinite ease-in-out;
    }
    

    div {
      position: fixed;
      bottom: 0;
      left: 0;
      display: flex;
      align-items: center;
    }
    

Next, we define the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 block for the animation — it animates the `path-length` property between the `--path-length` value and the `--path-length` value multiplied by `1.5`.

css

    @keyframes path-length-anim {
      from {
        path-length: var(--path-length);
      }
    
      to {
        path-length: calc(var(--path-length) * 1.5);
      }
    }
    

#### JavaScript

We start our script by grabbing references to the `<input type="range">`, `<output>`, and `:root` elements.

js

    const slider = document.querySelector("input");
    const output = document.querySelector("output");
    const rootElem = document.querySelector(":root");
    

Next, we add an `input` event handler to the range slider so that, when its value is changed, the `<output>` element's `textContent` and the value of the `--path-length` custom property are set to equal the slider's new value.

js

    slider.addEventListener("input", () => {
      output.textContent = `${slider.value}px`;
      rootElem.style.setProperty("--path-length", `${slider.value}px`);
    });
    

#### Results

Adjust the slider, and note how larger values result in a smaller dash size.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# PathLengthProperty](https://w3c.github.io/svgwg/svg2-draft/paths.html#PathLengthProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length#see_also)

-------------------------------------------------------------------------------------------------------

*   SVG [`pathLength`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/pathLength)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/path-length/index.md?plain=1 "Folder: en-us/web/css/reference/properties/path-length (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpath-length&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpath-length%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpath-length%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpath-length%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7e9f482c51817d3a885e26092f8219fd0d9d278%0A*+Document+last+modified%3A+2026-09-28T21%3A00%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")