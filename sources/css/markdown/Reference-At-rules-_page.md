*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#mdn-search)
    

`@page` CSS at-rule
===================

Baseline 2024

Newly available

\*

Since December 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@page`** at-rule is a CSS at-rule used to modify different aspects of printed pages. It targets and modifies the page's dimensions, orientation, and margins. The `@page` at-rule can be used to target all pages in a print-out or a subset using its various pseudo-classes.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#syntax)

-------------------------------------------------------------------------------------------

css

    /* Targets all the pages */
    @page {
      size: 8.5in 9in;
      margin-top: 4in;
    }
    
    /* Targets all even-numbered pages */
    @page :left {
      margin-top: 4in;
    }
    
    /* Targets all odd-numbered pages */
    @page :right {
      size: 11in;
      margin-top: 4in;
    }
    
    /* Targets all selectors with `page: wide;` set */
    @page wide {
      size: a4 landscape;
    }
    
    @page {
      /* margin box at top right showing page number */
      @top-right {
        content: "Page " counter(pageNumber);
      }
    }
    

### [Page properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#page_properties)

The `@page` at-rule can contain only page descriptors and [margin at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#margin_at-rules)
. The following descriptors have been implemented by at least one browser:

[`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)

Specifies the page margins. Individual margin properties [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
, [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
, [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
, and [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
 can also be used.

[`page-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation)

Specifies the orientation of the page. This does not affect the layout of the page; the rotation is applied after the layout in the output medium.

[`size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size)

Specifies the target size and orientation of the page box's containing block. In the general case, where one page box is rendered onto one page sheet, it also indicates the size of the destination page sheet.

The specification mentions following CSS properties to be applicable to page boxes via @page at-rule. But these have _not been supported_ by any user agent yet.

Remaining page properties

| Feature | CSS properties |
| --- | --- |
| bidi properties | direction |
| background properties | background-color |
|     | background-image |
|     | background-repeat |
|     | background-attachment |
|     | background-position |
|     | background |
| border properties | border-top-width |
|     | border-right-width |
|     | border-bottom-width |
|     | border-left-width |
|     | border-width |
|     | border-top-color |
|     | border-right-color |
|     | border-bottom-color |
|     | border-left-color |
|     | border-color |
|     | border-top-style |
|     | border-right-style |
|     | border-bottom-style |
|     | border-left-style |
|     | border-short-style |
|     | border-top |
|     | border-right |
|     | border-bottom |
|     | border-left |
|     | border |
| counter properties | counter-reset |
|     | counter-increment |
| color | color |
| font properties | font-family |
|     | font-size |
|     | font-style |
|     | font-variant |
|     | font-weight |
|     | font |
| height properties | height |
|     | min-height |
|     | max-height |
| line height | line-height |
| margin properties | margin-top |
|     | margin-right |
|     | margin-bottom |
|     | margin-left |
|     | margin |
| outline properties | outline-width |
|     | outline-style |
|     | outline-color |
|     | outline |
| padding properties | padding-top |
|     | padding-right |
|     | padding-bottom |
|     | padding-left |
|     | padding |
| quotes | quotes |
| text properties | letter-spacing |
|     | text-align |
|     | text-decoration |
|     | text-indent |
|     | text-transform |
|     | white-space |
|     | word-spacing |
| visibility | visibility |
| width properties | width |
|     | min-width |
|     | max-width |

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#description)

-----------------------------------------------------------------------------------------------------

The @page rule defines properties of the page box. The `@page` at-rule can be accessed via the CSS object model interface [`CSSPageRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPageRule)
.

**Note:** The W3C is discussing how to handle viewport-related [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 units, `vh`, `vw`, `vmin`, and `vmax`. Meanwhile do not use them within a `@page` at-rule.

### [Related properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#related_properties)

The `@page` at-rule, allows the user to assign a name to the rule, which is then called in a declaration using the `page` property.

[`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page)

Allows a selector to use a user-defined **named page**

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#formal_syntax)

---------------------------------------------------------------------------------------------------------

@page =   
  @page <page-selector-list>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 { <declaration-rule-list> }    
  
<page-selector-list> =   
  <page-selector>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<page-selector> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <ident-token>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <pseudo-page>[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
!    
  
<pseudo-page> =   
  : [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 first [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 blank [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

Where the `<page-body>` includes:

*   page-properties
*   page-margin properties

and `<pseudo-page>` represents these pseudo-classes:

*   [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
    
*   [`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
    
*   [`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
    
*   [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    

[Margin at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#margin_at-rules)

-------------------------------------------------------------------------------------------------------------

The margin at-rules are used inside of the `@page` at-rule. They each target a different section of the document printed page, styling the area of the printed page based on the property values set in the style block:

css

    @page {
      @top-left {
        /* page-margin-properties */
      }
    }
    

**`@top-left`** targets the top-left of the document and applies the changes based on the page-margin-properties set.

Other margin-at rules include:

css

    @top-left-corner
    @top-left
    @top-center
    @top-right
    @top-right-corner
    @bottom-left-corner
    @bottom-left
    @bottom-center
    @bottom-right
    @bottom-right-corner
    @left-top
    @left-middle
    @left-bottom
    @right-top
    @right-middle
    @right-bottom
    

### [Page-margin properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#page-margin_properties)

The page-margin properties are the set of CSS properties can be set in any individual margin at-rule. They include:

Page-margin properties

| Feature | CSS properties |
| --- | --- |
| bidi properties | direction |
| background properties | background-color |
|     | background-image |
|     | background-repeat |
|     | background-attachment |
|     | background-position |
|     | background |
| border properties | border-top-width |
|     | border-right-width |
|     | border-bottom-width |
|     | border-left-width |
|     | border-width |
|     | border-top-color |
|     | border-right-color |
|     | border-bottom-color |
|     | border-left-color |
|     | border-color |
|     | border-top-style |
|     | border-right-style |
|     | border-bottom-style |
|     | border-left-style |
|     | border-short-style |
|     | border-top |
|     | border-right |
|     | border-bottom |
|     | border-left |
|     | border |
| counter properties | counter-reset |
|     | counter-increment |
| content | content |
| color | color |
| font properties | font-family |
|     | font-size |
|     | font-style |
|     | font-variant |
|     | font-weight |
|     | font |
| height properties | height |
|     | min-height |
|     | max-height |
| line height | line-height |
| margin properties | margin-top |
|     | margin-right |
|     | margin-bottom |
|     | margin-left |
|     | margin |
| outline properties | outline-width |
|     | outline-style |
|     | outline-color |
|     | outline |
| padding properties | padding-top |
|     | padding-right |
|     | padding-bottom |
|     | padding-left |
|     | padding |
| quotes | quotes |
| text properties | letter-spacing |
|     | text-align |
|     | text-decoration |
|     | text-indent |
|     | text-transform |
|     | white-space |
|     | word-spacing |
| vertical alignment | vertical-align |
| visibility | visibility |
| width properties | width |
|     | min-width |
|     | max-width |
| z-index | z-index |

[Named pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#named_pages)

-----------------------------------------------------------------------------------------------------

Named pages enable performing per-page layout and adding [page-breaks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fragmentation)
 in a declarative manner when printing.

Named pages can be applied using the [`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page)
 property. This allows the user to create different page configurations for use in print layouts.

An example of this can be found on the [`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#examples)
 examples.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#examples)

-----------------------------------------------------------------------------------------------

### [Using the size property to change the page orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#using_the_size_property_to_change_the_page_orientation)

This example shows how to split the `<section>`s into individual pages in `landscape` format with each page having a 20% margin when printed. Clicking the print button will launch a print dialog with the HTML sections split into individual pages.

html

    <button>Print page</button>
    <article>
      <section>
        <h2>Header one</h2>
        <p>Paragraph one.</p>
      </section>
      <section>
        <h2>Header two</h2>
        <p>Paragraph two.</p>
      </section>
      <section>
        <h2>Header three</h2>
        <p>Paragraph three.</p>
      </section>
    </article>
    

js

    const button = document.querySelector("button");
    
    button.addEventListener("click", () => {
      window.print();
    });
    

css

    @page {
      size: landscape;
      margin: 2cm;
    }
    
    section {
      page-break-after: always;
      break-after: page;
    }
    
    @media print {
      button {
        display: none;
      }
    }
    

    body {
      font-family: "Helvetica", sans-serif;
      background-color: silver;
    }
    
    article {
      width: 100%;
    }
    
    section {
      display: grid;
      background-color: white;
      border-radius: 0.6rem;
      justify-items: center;
      padding: 1rem;
      width: 50%;
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
      margin: 0 auto;
      margin-block-end: 1rem;
      border: 1px dashed;
    }
    

### [@page pseudo-class examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#page_pseudo-class_examples)

See the various [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 of `@page` for examples.

*   [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
    
*   [`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
    
*   [`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
    
*   [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3  <br>\# at-page-rule](https://drafts.csswg.org/css-page/#at-page-rule) |
| [CSS Logical Properties and Values Module Level 1  <br>\# page](https://drafts.csswg.org/css-logical/#page) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#see_also)

-----------------------------------------------------------------------------------------------

*   The [`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page)
     property
*   The `@page` [`size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size)
     descriptor
*   [CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
     module
*   [\[META\] CSS Paged Media Module Level 3](https://bugzil.la/286443 "External link (opens in new tab)")
     Bugzilla for tracking progress on the subject (page-based counters, etc.)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@page/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@page (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40page&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40page%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40page%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40page%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd571e753a6e1aa3f37c775f0308690bc738cdbe6%0A*+Document+last+modified%3A+2026-09-12T19%3A13%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")