*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#mdn-search)
    

`:nth-last-child()` CSS pseudo-class
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:nth-last-child()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements based on their position among a group of siblings, counting from the end.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#try_it)

------------------------------------------------------------------------------------------------------

    p {
      font-weight: bold;
    }
    
    li:nth-last-child(-n + 3) {
      border: 2px solid orange;
      margin-top: 1px;
    }
    
    li:nth-last-child(even) {
      background-color: lightyellow;
    }
    

    <p>Eight deadliest wildfires:</p>
    <ol reversed>
      <li>Matheson Fire</li>
      <li>Miramichi Fire</li>
      <li>1997 Indonesian fires</li>
      <li>Thumb Fire</li>
      <li>Great Hinckley Fire</li>
      <li>Cloquet Fire</li>
      <li>Kursha-2 Fire</li>
      <li>Peshtigo Fire</li>
    </ol>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#syntax)

------------------------------------------------------------------------------------------------------

css

    :nth-last-child(<nth> [of <complex-selector-list>]?) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#parameters)

The `:nth-last-child()` pseudo-class is specified with a single argument, which represents the pattern for matching elements, counting from the end.

#### Keyword values

[`odd`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#odd)

Represents elements whose numeric position in a series of siblings is odd: 1, 3, 5, etc., counting from the end.

[`even`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#even)

Represents elements whose numeric position in a series of siblings is even: 2, 4, 6, etc., counting from the end.

#### Functional notation

[`<An+B>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#anb)

Represents elements whose numeric position in a series of siblings matches the pattern `An+B`, for every positive integer or zero value of `n`, where:

*   `A` is an integer step size,
*   `B` is an integer offset,
*   `n` is all non-negative integers, starting from 0.

It can be read as the `An+B`\-th element of a list. The index of the first element, counting from the end, is `1`. The `A` and `B` must both have [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 values.

#### The `of <selector>` syntax

By passing a selector argument, we can select the **nth-last** element that matches that selector. For example, the following selector matches the last three _important_ list items, which are assigned with `class="important"`.

css

    :nth-last-child(-n + 3 of li.important) {
    }
    

**Note:** This is different from moving the selector outside of the function, like:

css

    li.important:nth-last-child(-n + 3) {
    }
    

This selector applies a style to list items if they are also within the last three children.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#examples)

----------------------------------------------------------------------------------------------------------

### [Example selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#example_selectors)

[`tr:nth-last-child(odd)` or `tr:nth-last-child(2n+1)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#trnth-last-childodd)

Represents the odd rows of an HTML table: 1, 3, 5, etc., counting from the end.

[`tr:nth-last-child(even)` or `tr:nth-last-child(2n)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#trnth-last-childeven)

Represents the even rows of an HTML table: 2, 4, 6, etc., counting from the end.

[`:nth-last-child(7)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#nth-last-child7)

Represents the seventh element, counting from the end.

[`:nth-last-child(5n)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#nth-last-child5n)

Represents elements 5, 10, 15, etc., counting from the end.

[`:nth-last-child(3n+4)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#nth-last-child3n4)

Represents elements 4, 7, 10, 13, etc., counting from the end.

[`:nth-last-child(-n+3)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#nth-last-child-n3)

Represents the last three elements among a group of siblings.

[`p:nth-last-child(n)` or `p:nth-last-child(n+1)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#pnth-last-childn)

Represents every `<p>` element among a group of siblings. This is the same as a simple `p` selector. (Since `n` starts at zero, while the last element begins at one, `n` and `n+1` will both select the same elements.)

[`p:nth-last-child(1)` or `p:nth-last-child(0n+1)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#pnth-last-child1)

Represents every `<p>` that is the first element among a group of siblings, counting from the end. This is the same as the [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
 selector.

### [Table example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#table_example)

#### HTML

html

    <table>
      <tbody>
        <tr>
          <td>First line</td>
        </tr>
        <tr>
          <td>Second line</td>
        </tr>
        <tr>
          <td>Third line</td>
        </tr>
        <tr>
          <td>Fourth line</td>
        </tr>
        <tr>
          <td>Fifth line</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    table {
      border: 1px solid blue;
    }
    
    /* Selects the last three elements */
    tr:nth-last-child(-n + 3) {
      background-color: pink;
    }
    
    /* Selects every element starting from the second to last item */
    tr:nth-last-child(n + 2) {
      color: blue;
    }
    
    /* Select only the last second element */
    tr:nth-last-child(2) {
      font-weight: 600;
    }
    

#### Result

### [Quantity query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#quantity_query)

A _quantity query_ styles elements depending on how many of them there are. In this example, list items turn red when there are at least three of them in a given list. This is accomplished by combining the capabilities of the `nth-last-child` pseudo-class and the [subsequent-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator)
.

#### HTML

html

    <h4>A list of four items (styled):</h4>
    <ol>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
    </ol>
    
    <h4>A list of two items (unstyled):</h4>
    <ol>
      <li>One</li>
      <li>Two</li>
    </ol>
    

#### CSS

css

    /* If there are at least three list items,
       style them all */
    li:nth-last-child(n + 3),
    li:nth-last-child(3) ~ li {
      color: red;
    }
    

#### Result

### [`of <selector>` syntax example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#of_selector_syntax_example)

In this example, there is an unordered list of names. Some items have a `noted` class applied and are then highlighted with a thick bottom border.

#### HTML

html

    <ul>
      <li class="noted">Diego</li>
      <li>Shilpa</li>
      <li class="noted">Caterina</li>
      <li>Jayla</li>
      <li>Tyrone</li>
      <li>Ricardo</li>
      <li class="noted">Gila</li>
      <li>Sienna</li>
      <li>Titilayo</li>
      <li class="noted">Lexi</li>
      <li>Aylin</li>
      <li>Leo</li>
      <li>Leyla</li>
      <li class="noted">Bruce</li>
      <li>Aisha</li>
      <li>Veronica</li>
      <li class="noted">Kyouko</li>
      <li>Shireen</li>
      <li>Tanya</li>
      <li class="noted">Marlene</li>
    </ul>
    

#### CSS

css

    * {
      font-family: sans-serif;
    }
    
    ul {
      display: flex;
      flex-wrap: wrap;
      list-style: none;
      font-size: 1.2rem;
      padding-left: 0;
    }
    
    li {
      margin: 0.125rem;
      padding: 0.25rem;
      border: 1px solid tomato;
    }
    
    .noted {
      border-bottom: 5px solid tomato;
    }
    

In the following CSS we are targeting the **odd** list items that are marked with `class="noted"`.

css

    li:nth-last-child(odd of .noted) {
      background-color: tomato;
      border-bottom-color: seagreen;
    }
    

#### Result

Items with `class="noted"` have a thick bottom border and items 1, 7, 14, and 20 have a solid background as they are the _odd_ list items with `class="noted"`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# nth-last-child-pseudo](https://drafts.csswg.org/selectors/#nth-last-child-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child#see_also)

----------------------------------------------------------------------------------------------------------

*   [`:nth-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    
*   [`:nth-last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
    
*   [Quantity Queries for CSS](https://alistapart.com/article/quantity-queries-for-css/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_nth-last-child/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_nth-last-child (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Anth-last-child&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_nth-last-child%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Anth-last-child%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_nth-last-child%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0c62b082755017d0773ecaaee7e74efd5e066d0b%0A*+Document+last+modified%3A+2026-07-17T12%3A50%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")