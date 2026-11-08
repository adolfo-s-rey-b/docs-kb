*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#mdn-search)
    

`white-space` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`white-space`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets how [white space](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
 inside an element is handled.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#try_it)

---------------------------------------------------------------------------------------------------

    white-space: normal;
    

    white-space: pre;
    

    white-space: pre-wrap;
    

    white-space: pre-line;
    

    white-space: wrap;
    

    white-space: collapse;
    

    white-space: preserve nowrap;
    

    <section class="default-example" id="default-example">
      <div id="example-element">
        <p>
          But ere she from the church-door stepped She smiled and told us why: 'It
          was a wicked woman's curse,' Quoth she, 'and what care I?' She smiled, and
          smiled, and passed it off Ere from the door she stept—
        </p>
      </div>
    </section>
    

    #example-element {
      width: 16rem;
    }
    
    #example-element p {
      border: 1px solid #c5c5c5;
      padding: 0.75rem;
      text-align: left;
    }
    

The property specifies two things:

*   Whether and how white space is [collapsed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Whitespace#collapsing_and_transformation)
    .
*   Whether and how lines wrap.

**Note:** To make words break _within themselves_, use [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
, [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
, or [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
 instead.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#constituent_properties)

-----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`white-space-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
    
*   [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
    

**Note:** The spec defines a third constituent property: `white-space-trim`, which is not implemented in any browser yet.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Single keyword values */
    white-space: normal;
    white-space: pre;
    white-space: pre-wrap;
    white-space: pre-line;
    
    /* white-space-collapse and text-wrap-mode shorthand values */
    white-space: nowrap;
    white-space: wrap;
    white-space: break-spaces;
    white-space: collapse;
    white-space: preserve nowrap;
    
    /* Global values */
    white-space: inherit;
    white-space: initial;
    white-space: revert;
    white-space: revert-layer;
    white-space: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#values)

The `white-space` property values can be specified as one or two keywords representing the values for the [`white-space-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
 and [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
 properties, or the following special keywords:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#normal)

Sequences of white space are [collapsed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Whitespace#collapsing_and_transformation)
. Newline characters in the source are handled the same as other white spaces. Lines are broken as necessary to fill line boxes. Equivalent to `collapse wrap`.

[`pre`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#pre)

Sequences of white space are preserved. Lines are only broken at newline characters in the source and at [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
 elements. Equivalent to `preserve nowrap`.

[`pre-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#pre-wrap)

Sequences of white space are preserved. Lines are broken at newline characters, at [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
, and as necessary to fill line boxes. Equivalent to `preserve wrap`.

[`pre-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#pre-line)

Sequences of white space are [collapsed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Whitespace#collapsing_and_transformation)
. Lines are broken at newline characters, at [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
, and as necessary to fill line boxes. Equivalent to `preserve-breaks wrap`.

**Note:** The `white-space` property as a shorthand is a relatively new feature (see [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#browser_compatibility)
). Originally, it had six keyword values; now, the value `nowrap` is instead interpreted as a value for [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
, while the value `break-spaces` is interpreted as a value for [`white-space-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
. The above four keywords are still specific to `white-space`, but they have longhand equivalents. The change to make `white-space` a shorthand expands acceptable values to even more keywords and combinations, such as `wrap` and `collapse`.

The following table summarizes the behavior of these four `white-space` keyword values:

|     | New lines | Spaces and tabs | Text wrapping | End-of-line spaces | End-of-line other space separators |
| --- | --- | --- | --- | --- | --- |
| `normal` | Collapse | Collapse | Wrap | Remove | Hang |
| `pre` | Preserve | Preserve | No wrap | Preserve | No wrap |
| `pre-wrap` | Preserve | Preserve | Wrap | Hang | Hang |
| `pre-line` | Preserve | Collapse | Wrap | Remove | Hang |

A tab defaults to 8 spaces and can be configured using the [`tab-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size)
 property. In the case of `normal`, `nowrap`, and `pre-line` values, every tab is converted to a space (U+0020) character.

**Note:** There is a distinction made between **spaces** and **other space separators**. These are defined as follows:

[spaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#spaces)

Spaces (U+0020), tabs (U+0009), and segment breaks (such as newlines).

[other space separators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#other_space_separators)

All other space separators defined in Unicode, other than those already defined as spaces.

Where white space is said to _hang_, this can affect the size of the box when measured for intrinsic sizing.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

white-space =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pre                                                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pre-wrap                                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pre-line                                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'white-space-collapse'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [<'text-wrap-mode'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 <'white-space-trim'>    
  
[<white-space-collapse>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
 =   
  collapse         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  discard          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve-breaks  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve-spaces  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  break-spaces       
  
[<text-wrap-mode>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
 =   
  wrap    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nowrap    
  
<white-space-trim> =   
  none                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  discard-before [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 discard-after [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 discard-inner    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#examples)

-------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#basic_example)

css

    code {
      white-space: pre;
    }
    

### [Line breaks inside <pre> elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#line_breaks_inside_pre_elements)

css

    pre {
      white-space: pre-wrap;
    }
    

### [In action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#in_action)

    <div id="css-code" class="box">
      p { white-space:
      <select>
        <option>normal</option>
        <option>nowrap</option>
        <option>pre</option>
        <option>pre-wrap</option>
        <option>pre-line</option>
        <option>break-spaces</option>
      </select>
      }
    </div>
    <div id="results" class="box">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
        non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </div>
    

    .box {
      width: 350px;
      padding: 16px;
    }
    
    #css-code {
      background-color: gainsboro;
      font-size: 16px;
      font-family: monospace;
    }
    
    #css-code select {
      font-family: inherit;
      width: 100px;
    }
    
    #results {
      background-color: rgb(230 230 230);
      overflow-x: scroll;
      white-space: normal;
      font-size: 14px;
    }
    

    const select = document.querySelector("#css-code select");
    const results = document.querySelector("#results p");
    select.addEventListener("change", (e) => {
      results.style.setProperty("white-space", e.target.value);
    });
    

### [Controlling line wrapping in tables](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#controlling_line_wrapping_in_tables)

#### HTML

html

    <table>
      <tbody>
        <tr>
          <td></td>
          <td>Very long content that splits</td>
          <td class="nw">Very long content that don't split</td>
        </tr>
        <tr>
          <td class="nw">white-space:</td>
          <td>normal</td>
          <td>nowrap</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    table {
      border-collapse: collapse;
      border: solid black 1px;
      width: 250px;
      height: 150px;
    }
    td {
      border: solid 1px black;
      text-align: center;
    }
    .nw {
      white-space: nowrap;
    }
    

#### Result

### [Multiple lines in SVG text element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#multiple_lines_in_svg_text_element)

The `white-space` CSS property can be used to create multiple lines in a [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 element, which does not wrap by default.

#### HTML

The text inside the `<text>` element needs to be split into multiple lines for the new lines to be detected. After the first line the rest need to have their whitespace removed.

html

    <svg viewBox="0 0 320 150">
      <text y="20" x="10">Here is an English paragraph
    that is broken into multiple lines
    in the source code so that it can
    be more easily read and edited
    in a text editor.
      </text>
    </svg>
    

#### CSS

css

    text {
      white-space: break-spaces;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# white-space-property](https://drafts.csswg.org/css-text-4/#white-space-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# TextWhiteSpace](https://w3c.github.io/svgwg/svg2-draft/text.html#TextWhiteSpace) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#see_also)

-------------------------------------------------------------------------------------------------------

*   Properties that define how words break _within themselves_: [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    , [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    , [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`tab-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size)
    
*   [Handling whitespace in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Whitespace)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/white-space/index.md?plain=1 "Folder: en-us/web/css/reference/properties/white-space (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwhite-space&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwhite-space%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwhite-space%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwhite-space%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")