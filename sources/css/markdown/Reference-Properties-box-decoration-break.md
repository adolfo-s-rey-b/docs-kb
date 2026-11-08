*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#mdn-search)
    

`box-decoration-break` CSS property
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/41)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`box-decoration-break`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies how an element's [fragments](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation)
 should be rendered when broken across multiple lines, columns, or pages.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#try_it)

------------------------------------------------------------------------------------------------------------

    -webkit-box-decoration-break: slice;
    box-decoration-break: slice;
    

    -webkit-box-decoration-break: clone;
    box-decoration-break: clone;
    

    <section id="default-example">
      <div id="example-container">
        <span id="example-element">This text breaks across multiple lines.</span>
      </div>
    </section>
    

    #example-container {
      width: 14rem;
    }
    
    #example-element {
      background: linear-gradient(to bottom right, #6f6f6f, black);
      color: white;
      box-shadow:
        8px 8px 10px 0 #ff1492,
        -5px -5px 5px 0 blue,
        5px 5px 15px 0 yellow;
      padding: 0 1em;
      border-radius: 16px;
      border-style: solid;
      margin-left: 10px;
      font: 24px sans-serif;
      line-height: 2;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    box-decoration-break: slice;
    box-decoration-break: clone;
    
    /* Global values */
    box-decoration-break: inherit;
    box-decoration-break: initial;
    box-decoration-break: revert;
    box-decoration-break: revert-layer;
    box-decoration-break: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#values)

This property is specified as one of the following keyword values:

[`slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#slice)

The element is initially rendered as if its box were not fragmented, after which the rendering for this hypothetical box is sliced into pieces for each line/column/page. Note that the hypothetical box can be different for each fragment since it uses its own height if the break occurs in the inline direction, and its own width if the break occurs in the block direction. See the CSS specification for details.

[`clone`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#clone)

Each box fragment is rendered independently with the specified border, padding, and margin wrapping each fragment. The [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
, and [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 are applied to each fragment independently. The background is also drawn independently for each fragment, which means that a background image with [`background-repeat: no-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 may nevertheless repeat multiple times.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#description)

----------------------------------------------------------------------------------------------------------------------

The specified value will impact the appearance of the following properties:

*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    
*   [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    
*   [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `slice` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

box-decoration-break =   
  slice  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  clone    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#examples)

----------------------------------------------------------------------------------------------------------------

### [Inline box fragments](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#inline_box_fragments)

An inline element with a box decoration may have unexpected appearance when it contains line breaks due to the initial `slice` value. The following example shows the effect of adding `box-decoration-break: clone` to a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 that contains [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
 tags:

    body {
      display: flex;
      background-color: grey;
      justify-content: space-around;
    }
    
    span {
      padding: 0em 1em;
      border-radius: 1rem;
      border-style: solid;
      margin: 1rem;
      font: 22px sans-serif;
      line-height: 2;
    }
    

css

    span {
      background: linear-gradient(to bottom right, yellow, green);
      box-shadow:
        8px 8px 10px 0px deeppink,
        -5px -5px 5px 0px blue,
        5px 5px 15px 0px yellow;
    }
    
    #clone {
      -webkit-box-decoration-break: clone;
      box-decoration-break: clone;
    }
    

html

    <p>
      <span>The<br />quick<br />orange fox</span>
    </p>
    <p>
      <span id="clone">The<br />quick<br />orange fox</span>
    </p>
    

### [Block box fragments](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#block_box_fragments)

The following example shows how block elements with box decoration look when they contain line breaks in a [multi-column layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Multiple-column_Layout)
. Notice how the result of `box-decoration-break: slice` would be the equivalent of the first [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 if stacked vertically.

    body {
      background-color: grey;
    }
    span {
      padding: 0em 2em;
      border-radius: 250px;
      border-style: solid;
      margin-left: 1em;
      font: 20px sans-serif;
      line-height: 1.5;
    }
    

css

    span {
      display: block;
      background: linear-gradient(to bottom right, yellow, green);
      box-shadow:
        inset 8px 8px 10px 0px deeppink,
        inset -5px -5px 5px 0px blue,
        inset 5px 5px 15px 0px yellow;
    }
    #base {
      width: 33%;
    }
    .columns {
      columns: 3;
    }
    
    .clone {
      -webkit-box-decoration-break: clone;
      box-decoration-break: clone;
    }
    

html

    <div id="base">
      <span>The<br />quick<br />orange fox</span>
    </div>
    <br />
    
    <h2>'box-decoration-break: slice'</h2>
    <div class="columns">
      <span>The<br />quick<br />orange fox</span>
    </div>
    
    <h2>'box-decoration-break: clone'</h2>
    <div class="columns">
      <span class="clone">The<br />quick<br />orange fox</span>
    </div>
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fragmentation Module Level 3  <br>\# break-decoration](https://drafts.csswg.org/css-break/#break-decoration) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
    , [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
    , [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-decoration-break/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-decoration-break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-decoration-break&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-decoration-break%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-decoration-break%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-decoration-break%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")