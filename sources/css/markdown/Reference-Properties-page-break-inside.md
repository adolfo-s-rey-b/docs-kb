*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#mdn-search)
    

`page-break-inside` CSS property
================================

Deprecated

Avoid using this feature in new projects. The `page-break-` alias properties exist only for backwards compatibility with pages that predate the `break-` properties. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Page breaks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation "In printed page layouts, the break-after, break-before, break-inside CSS properties control where printed pages start and end. Also known as pagination or page breaking.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** This property has been replaced by the [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
 property.

The **`page-break-inside`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property adjusts page breaks _inside_ the current element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#try_it)

---------------------------------------------------------------------------------------------------------

    page-break-inside: auto;
    

    page-break-inside: avoid;
    

    <div>
      <p>
        The effect of this property can be noticed when the document is being
        printed or a preview of a print is displayed.
      </p>
      <button id="print-btn">Show Print Preview</button>
      <div class="box-container">
        <div class="box">Content before the property</div>
        <div class="box" id="example-element">Content with 'page-break-inside'</div>
        <div class="box">Content after the property</div>
      </div>
    </div>
    

    .box {
      border: solid #5b6dcd 5px;
      background-color: #5b6dcd;
      margin: 10px 0;
      padding: 5px;
    }
    
    #example-element {
      border: solid 5px #ffc129;
      background-color: #ffc129;
      color: black;
    }
    
    @media print {
      #example-element {
        height: 25cm;
      }
    }
    

    const btn = document.getElementById("print-btn");
    
    btn.addEventListener("click", () => {
      window.print();
    });
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    page-break-inside: auto;
    page-break-inside: avoid;
    
    /* Global values */
    page-break-inside: inherit;
    page-break-inside: initial;
    page-break-inside: revert;
    page-break-inside: revert-layer;
    page-break-inside: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#auto)

Initial value. Automatic page breaks (neither forced nor forbidden).

[`avoid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#avoid)

Avoid page breaks inside the element.

[Page break aliases](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#page_break_aliases)

---------------------------------------------------------------------------------------------------------------------------------

The `page-break-inside` property is now a legacy property, replaced by [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
.

For compatibility reasons, `page-break-inside` should be treated by browsers as an alias of `break-inside`. This ensures that sites using `page-break-inside` continue to work as designed. A subset of values should be aliased as follows:

| page-break-inside | break-inside |
| --- | --- |
| `auto` | `auto` |
| `avoid` | `avoid` |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block-level elements in the normal flow of the root element. User agents may also apply it to other elements like `table-row` elements. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

page-break-inside =   
  avoid    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inherit    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#examples)

-------------------------------------------------------------------------------------------------------------

### [Avoiding page breaks inside elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#avoiding_page_breaks_inside_elements)

#### HTML

html

    <div class="page">
      <p>This is the first paragraph.</p>
      <section class="list">
        <span>A list</span>
        <ol>
          <li>one</li>
          <!-- <li>two</li> -->
        </ol>
      </section>
      <ul>
        <li>one</li>
        <!-- <li>two</li> -->
      </ul>
      <p>This is the second paragraph.</p>
      <p>This is the third paragraph, it contains more text.</p>
      <p>
        This is the fourth paragraph. It has a little bit more text than the third
        one.
      </p>
    </div>
    

#### CSS

css

    .page {
      background-color: #8cffa0;
      height: 90px;
      width: 200px;
      columns: 1;
      column-width: 100px;
    }
    
    .list,
    ol,
    ul,
    p {
      break-inside: avoid;
    }
    
    p {
      background-color: #8ca0ff;
    }
    
    ol,
    ul,
    .list {
      margin: 0.5em 0;
      display: block;
      background-color: orange;
    }
    
    p:first-child {
      margin-top: 0;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fragmentation Module Level 3  <br>\# page-break-properties](https://drafts.csswg.org/css-break/#page-break-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
    , [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
    , [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
    
*   [`page-break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-after)
    , [`page-break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before)
    
*   [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
    , [`widows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/page-break-inside/index.md?plain=1 "Folder: en-us/web/css/reference/properties/page-break-inside (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpage-break-inside&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpage-break-inside%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpage-break-inside%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpage-break-inside%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")