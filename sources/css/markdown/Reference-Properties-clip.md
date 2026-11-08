*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#mdn-search)
    

`clip` CSS property
===================

Deprecated

Avoid using this feature in new projects. The CSS Masking specification deprecated the `clip` property. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [clip-path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path "The clip-path CSS property and SVG attribute set the visible area of an element. Everything outside the area will be hidden.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** Authors are encouraged to use the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property instead.

The **`clip`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines a visible portion of an element. The `clip` property applies only to absolutely positioned elements — that is, elements with [`position:absolute`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 or [`position:fixed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#syntax)

--------------------------------------------------------------------------------------------

css

    /* Keyword value */
    clip: auto;
    
    /* <shape> values */
    clip: rect(1px, 10em, 3rem, 2ch);
    
    /* Global values */
    clip: inherit;
    clip: initial;
    clip: revert;
    clip: revert-layer;
    clip: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#values)

This property is specified as a single value from the following list:

[`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#rect)

A rectangle defined using a `rect()` function of the form `rect(<top>, <right>, <bottom>, <left>)`. The `<top>` and `<bottom>` values are offsets from the _inside top border edge_ of the box, while `<right>` and `<left>` are offsets from the _inside left border edge_ of the box — that is, the extent of the padding box.

The `<top>`, `<right>`, `<bottom>`, and `<left>` values may be either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or `auto`. If any side's value is `auto`, the element is clipped to that side's _inside border edge_.

**Note:** The `rect()` [`<shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape)
 function used in the deprecated `clip` property is different from the CSS [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 function used to define a CSS [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#auto)

The element does not clip (default). This is different from `rect(auto, auto, auto, auto)`, which clips to the element's inside border edges.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#formal_definition)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | absolutely positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `auto` if specified as `auto`, otherwise a rectangle with four values, each of which is `auto` if specified as `auto` or the computed length otherwise |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [rectangle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#interpolation "Values of the <shape> CSS data type which are rectangles are interpolated over their top, right, bottom and left component, each treated as a real, floating-point number.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#formal_syntax)

----------------------------------------------------------------------------------------------------------

clip =   
  <rect()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto        
  
[<rect()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 =   
  rect( <top> , <right> , <bottom> , <left> )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#examples)

------------------------------------------------------------------------------------------------

### [Clipping an image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#clipping_an_image)

html

    <p class="dotted-border">
      <img src="macarons.png" alt="Original graphic" />
      <img id="top-left" src="macarons.png" alt="Graphic clipped to upper left" />
      <img id="middle" src="macarons.png" alt="Graphic clipped towards middle" />
      <img
        id="bottom-right"
        src="macarons.png"
        alt="Graphic clipped to bottom right" />
    </p>
    

css

    .dotted-border {
      border: dotted;
      position: relative;
      width: 390px;
      height: 400px;
    }
    
    #top-left,
    #middle,
    #bottom-right {
      position: absolute;
      top: 0;
    }
    
    #top-left {
      left: 400px;
      clip: rect(0, 130px, 90px, 0);
    }
    
    #middle {
      left: 270px;
      clip: rect(100px, 260px, 190px, 130px);
    }
    
    #bottom-right {
      left: 140px;
      clip: rect(200px, 390px, 290px, 260px);
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# propdef-clip](https://drafts.csswg.org/css-masking/#propdef-clip) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip#see_also)

------------------------------------------------------------------------------------------------

*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
    
*   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   [`shape-image-threshold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold)
    
*   [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/clip/index.md?plain=1 "Folder: en-us/web/css/reference/properties/clip (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclip&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclip%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclip%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclip%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")