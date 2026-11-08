*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#mdn-search)
    

`-webkit-text-stroke-width` CSS property
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`-webkit-text-stroke-width`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the width of the stroke for text.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    -webkit-text-stroke-width: thin;
    -webkit-text-stroke-width: medium;
    -webkit-text-stroke-width: thick;
    
    /* <length> values */
    -webkit-text-stroke-width: 2px;
    -webkit-text-stroke-width: 0.1em;
    -webkit-text-stroke-width: 1mm;
    -webkit-text-stroke-width: 5pt;
    
    /* Global values */
    -webkit-text-stroke-width: inherit;
    -webkit-text-stroke-width: initial;
    -webkit-text-stroke-width: revert;
    -webkit-text-stroke-width: revert-layer;
    -webkit-text-stroke-width: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#values)

This property is specified as the following value:

[`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#line-width)

The width of the stroke.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length) |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

\-webkit-text-stroke-width =   
  <line-width>    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#examples)

---------------------------------------------------------------------------------------------------------------------

### [Varying stroke widths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#varying_stroke_widths)

#### CSS

css

    p {
      margin: 0;
      font-size: 4em;
      -webkit-text-stroke-color: red;
    }
    
    #thin {
      -webkit-text-stroke-width: thin;
    }
    
    #medium {
      -webkit-text-stroke-width: 3px;
    }
    
    #thick {
      -webkit-text-stroke-width: 1.5mm;
    }
    

#### HTML

html

    <p id="thin">Thin stroke</p>
    <p id="medium">Medium stroke</p>
    <p id="thick">Thick stroke</p>
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compatibility  <br>\# the-webkit-text-stroke-width](https://compat.spec.whatwg.org/#the-webkit-text-stroke-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Introducing Text-Stroke](https://webkit.org/blog/85/introducing-text-stroke/ "External link (opens in new tab)")
     on webkit.org (2006)
*   [CSS-Tricks article explaining this feature](https://css-tricks.com/adding-stroke-to-web-text/ "External link (opens in new tab)")
    
*   [`-webkit-text-stroke-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-color)
    
*   [`-webkit-text-stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke)
    
*   [`-webkit-text-fill-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-fill-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-webkit-text-stroke-width/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-webkit-text-stroke-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-text-stroke-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-text-stroke-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-text-stroke-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-text-stroke-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")