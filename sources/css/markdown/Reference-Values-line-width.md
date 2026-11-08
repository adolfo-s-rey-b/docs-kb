*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#mdn-search)
    

`<line-width>` CSS type
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<line-width>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value type represents the length or keyword value that defines the width of a line, or the lack of a line. The `<line-width>` keyword values are used in the following longhand and shorthand properties:

*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    , [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    
*   [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
    , [`border-block-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-width)
    
*   [`border-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end)
    , [`border-block-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-width)
    
*   [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
    , [`border-block-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)
    
*   [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
    
*   [`border-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline)
    , [`border-inline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)
    
*   [`border-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end)
    , [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)
    
*   [`border-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start)
    , [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)
    
*   [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
    , [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)
    
*   [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
    , [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)
    
*   [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
    , [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    , [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
    , [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
    , [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    , [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#syntax)

----------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#values)

The `<line-width>` type is specified using either `<length>` or a keyword:

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#length)

A non-negative [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
.

[`hairline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#hairline)

Represents a "just visible" line that is less than or equal to `1px`.

[`thin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#thin)

Same as `1px`.

[`medium`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#medium)

Same as `3px`.

[`thick`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#thick)

Same as `5px`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#formal_syntax)

------------------------------------------------------------------------------------------------------------

<line-width> =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#examples)

--------------------------------------------------------------------------------------------------

### [Defining a line width](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#defining_a_line_width)

This example demonstrates all the `<line-width>` keyword values, along with a `<length>` value.

#### HTML

We include five boxes within a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element.

html

    <section>
      <div data-width="hairline">hairline</div>
      <div data-width="thin">thin</div>
      <div data-width="medium">medium</div>
      <div data-width="thick">thick</div>
      <div data-width="10px">10px</div>
    </section>
    

#### CSS

We style all the elements to be identical, then set the [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 based on the element's `data-width` attribute.

css

    section {
      display: flex;
      gap: 10px;
    }
    div {
      flex: 0 0 15%;
      border-style: solid;
      border-color: purple;
      text-align: center;
    }
    [data-width="hairline"] {
      border-width: hairline;
    }
    
    [data-width="thin"] {
      border-width: thin;
    }
    
    [data-width="medium"] {
      border-width: medium;
    }
    
    [data-width="thick"] {
      border-width: thick;
    }
    
    [data-width="10px"] {
      border-width: 10px;
    }
    

    @supports not (border-width: hairline) {
      body::before {
        content: "Your browser does not support the 'hairline' value.";
        color: black;
        background-color: #ffcd33;
        display: block;
        width: 100%;
        text-align: center;
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# typedef-line-width](https://drafts.csswg.org/css-backgrounds/#typedef-line-width) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width#see_also)

--------------------------------------------------------------------------------------------------

*   [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
     data type
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/line-width/index.md?plain=1 "Folder: en-us/web/css/reference/values/line-width (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fline-width&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fline-width%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fline-width%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fline-width%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa9dc3374034d357cbfea717fd5d641605359e3c7%0A*+Document+last+modified%3A+2026-07-25T06%3A18%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")