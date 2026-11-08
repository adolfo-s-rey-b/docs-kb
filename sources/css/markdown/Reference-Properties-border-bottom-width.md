*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#mdn-search)
    

`border-bottom-width` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-bottom-width`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the width of the bottom border of an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#try_it)

-----------------------------------------------------------------------------------------------------------

    border-bottom-width: thick;
    

    border-bottom-width: 2em;
    

    border-bottom-width: 4px;
    

    border-bottom-width: 2ex;
    

    border-bottom-width: 0;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a border around it.
      </div>
    </section>
    

    #example-element {
      background-color: palegreen;
      color: black;
      border: 0 solid crimson;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    border-bottom-width: thin;
    border-bottom-width: medium;
    border-bottom-width: thick;
    
    /* <length> values */
    border-bottom-width: 10em;
    border-bottom-width: 3vmax;
    border-bottom-width: 6px;
    
    /* Global keywords */
    border-bottom-width: inherit;
    border-bottom-width: initial;
    border-bottom-width: revert;
    border-bottom-width: revert-layer;
    border-bottom-width: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#values)

[`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)

Defines the width of the border, either as an explicit non-negative [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or the keywords: `thin`, `medium`, or `thick`. The default is `medium`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `medium` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>, snapped as a line width |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

border-bottom-width =   
  <line-width>    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#examples)

---------------------------------------------------------------------------------------------------------------

### [Comparing bottom border widths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#comparing_bottom_border_widths)

#### HTML

html

    <div>Element 1</div>
    <div>Element 2</div>
    

#### CSS

css

    div {
      border: 1px solid red;
      margin: 1em 0;
    }
    
    div:nth-child(1) {
      border-bottom-width: thick;
    }
    div:nth-child(2) {
      border-bottom-width: 2em;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-width](https://drafts.csswg.org/css-backgrounds/#border-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width#see_also)

---------------------------------------------------------------------------------------------------------------

*   The other border-width-related CSS properties: [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)
    , [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)
    , [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
    , and [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    .
*   The other border-bottom-related CSS properties: [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    , [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    , and [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-bottom-width/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-bottom-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-bottom-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-bottom-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-bottom-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-bottom-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9c03ba87f9ff4123150d8f7dc457bd546bdab83%0A*+Document+last+modified%3A+2026-07-24T10%3A23%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")