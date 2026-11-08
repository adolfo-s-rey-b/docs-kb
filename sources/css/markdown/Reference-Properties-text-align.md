*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#mdn-search)
    

`text-align` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-align`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the horizontal alignment of the inline-level content inside a block element or table-cell box. This means it works like [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 but in the horizontal direction.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#try_it)

--------------------------------------------------------------------------------------------------

    text-align: start;
    

    text-align: end;
    

    text-align: center;
    

    text-align: justify;
    

    <section id="default-example">
      <div id="example-element">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
          veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
          velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
          cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
          est laborum.
        </p>
      </div>
    </section>
    

    section {
      font-size: 1.5em;
    }
    
    #default-example > div {
      width: 250px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-align: start;
    text-align: end;
    text-align: left;
    text-align: right;
    text-align: center;
    text-align: justify;
    text-align: match-parent;
    
    /* Block alignment values (Non-standard syntax) */
    text-align: -moz-center;
    text-align: -webkit-center;
    
    /* Global values */
    text-align: inherit;
    text-align: initial;
    text-align: revert;
    text-align: revert-layer;
    text-align: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#values)

This property is specified as one of the following keyword values:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#start)

The same as `left` if direction is left-to-right and `right` if direction is right-to-left.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#end)

The same as `right` if direction is left-to-right and `left` if direction is right-to-left.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#left)

The inline contents are aligned to the left edge of the line box.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#right)

The inline contents are aligned to the right edge of the line box.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#center)

The inline contents are centered within the line box.

[`justify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#justify)

The inline contents are justified. Spaces out the content to line up its left and right edges to the left and right edges of the line box, except for the last line.

[`match-parent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#match-parent)

Similar to `inherit`, but the values `start` and `end` are calculated according to the parent's [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 and are replaced by the appropriate `left` or `right` value.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#accessibility)

----------------------------------------------------------------------------------------------------------------

The inconsistent spacing between words created by justified text can be problematic for people with cognitive concerns such as Dyslexia.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.8 | Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `start`, or a nameless value that acts as `left` if [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)<br> is `ltr`, `right` if [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)<br> is `rtl` if `start` is not supported by the browser. |
| Applies to | block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, except for the `match-parent` value which is calculated against its parent's `direction` value and results in a computed value of either `left` or `right` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#formal_syntax)

----------------------------------------------------------------------------------------------------------------

text-align =   
  start         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  justify       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  match-parent  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  justify-all     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#examples)

------------------------------------------------------------------------------------------------------

### [Start alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#start_alignment)

#### HTML

html

    <p class="example">
      Integer elementum massa at nulla placerat varius. Suspendisse in libero risus,
      in interdum massa. Vestibulum ac leo vitae metus faucibus gravida ac in neque.
      Nullam est eros, suscipit sed dictum quis, accumsan a ligula.
    </p>
    

#### CSS

css

    .example {
      text-align: start;
      border: solid;
    }
    

#### Result

### [Centered text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#centered_text)

#### HTML

html

    <p class="example">
      Integer elementum massa at nulla placerat varius. Suspendisse in libero risus,
      in interdum massa. Vestibulum ac leo vitae metus faucibus gravida ac in neque.
      Nullam est eros, suscipit sed dictum quis, accumsan a ligula.
    </p>
    

#### CSS

css

    .example {
      text-align: center;
      border: solid;
    }
    

#### Result

### [Example using "justify"](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#example_using_justify)

#### HTML

html

    <p class="example">
      Integer elementum massa at nulla placerat varius. Suspendisse in libero risus,
      in interdum massa. Vestibulum ac leo vitae metus faucibus gravida ac in neque.
      Nullam est eros, suscipit sed dictum quis, accumsan a ligula.
    </p>
    

#### CSS

css

    .example {
      text-align: justify;
      border: solid;
    }
    

#### Result

### [Table alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#table_alignment)

This example demonstrates the use of `text-align` on [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 elements:

*   The [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
     is set to right-aligned.
*   The first two [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
     elements inherit the left alignment from the `text-align: left` set on the [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , while the third is set to right-aligned.
*   Inside the [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
     element, the first row is set to right-aligned, the second is set to center-aligned, and the third uses the default (left) alignment.
*   Within each row, some cells (c12, c31) are set to override the alignment of the row.

#### HTML

html

    <table>
      <caption>
        Example table
      </caption>
      <thead>
        <tr>
          <th>Col 1</th>
          <th>Col 2</th>
          <th class="right">Col 3</th>
        </tr>
      </thead>
      <tbody>
        <tr class="right">
          <td>11</td>
          <td class="center">12</td>
          <td>13</td>
        </tr>
        <tr class="center">
          <td>21</td>
          <td>22</td>
          <td>23</td>
        </tr>
        <tr id="r3">
          <td class="right">31</td>
          <td>32</td>
          <td>33</td>
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
    
    thead {
      text-align: left;
    }
    
    td,
    th {
      border: solid 1px black;
    }
    
    .center {
      text-align: center;
    }
    
    .right,
    caption {
      text-align: right;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# text-align](https://drafts.csswg.org/css-logical/#text-align) |
| [CSS Text Module Level 3  <br>\# text-align-property](https://drafts.csswg.org/css-text/#text-align-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align#see_also)

------------------------------------------------------------------------------------------------------

*   [`margin: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    , [`margin-left: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    , [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-align/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-align (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-align&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-align%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-align%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-align%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")