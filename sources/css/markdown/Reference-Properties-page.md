*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#mdn-search)
    

`page` CSS property
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`page`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to specify the named page, a specific type of page defined by the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
.

If there are multiple selectors that are using a named page consecutively then a forced page break using [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
 may be needed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#syntax)

--------------------------------------------------------------------------------------------

css

    /* set a named page */
    page: exampleName;
    page: chapterIntro;
    
    /* Use ancestors named page */
    page: auto; /* default value */
    
    /* Global values */
    page: inherit;
    page: initial;
    page: revert;
    page: revert-layer;
    page: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#auto)

Default value. Use the value of the nearest ancestor with a non-`auto` value. If no ancestor has a named page value set, the used value for auto is the empty string.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

Case-sensitive name defined in a [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 at-rule.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#formal_definition)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block-level elements in the normal flow of the root element. User agents may also apply it to other elements like `table-row` elements. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#formal_syntax)

----------------------------------------------------------------------------------------------------------

page =   
  auto            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#examples)

------------------------------------------------------------------------------------------------

### [Named page example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#named_page_example)

In this example, there are two parts to this HTML; print controls and the content to be printed. The print controls allow the user to select how the `section`s in the `article` will be printed.

html

    <!-- print options in a fieldset -->
    <fieldset id="printStyle">
      <legend>How would you like to print</legend>
      <label for="single">
        <input type="radio" id="single" name="type" value="single" checked />
        No Pages
      </label>
      <label for="grouped">
        <input type="radio" id="grouped" name="type" value="grouped" />Pages with
        Grouped Chapters
      </label>
      <label for="paged">
        <input type="radio" id="paged" name="type" value="paged" />
        Chapters Paged
      </label>
      <button id="print">Print</button>
    </fieldset>
    
    <!-- Content to be printed -->
    <article id="print-area" data-print="single">
      <section id="toc">
        <h2>Table of contents</h2>
        <ul>
          <li>Foreword</li>
          <li>Introduction</li>
          <li>Chapter One - named pages</li>
          <li>Chapter Two - page orientation</li>
          <li>Chapter Three - page margins</li>
          <li>Conclusion</li>
        </ul>
      </section>
      <section id="foreword">
        <h2>Foreword</h2>
        <p>
          This book is all about how the CSS <code>@page</code> at-rule can help
          with printing HTML books.
        </p>
      </section>
      <section id="introduction">
        <h2>Introduction</h2>
        <p>
          This book is a concept to show how an <em>HTML</em> document can easily be
          printed out in pages.
        </p>
      </section>
      <section id="chapter1" class="chapter">
        <h2>Named pages</h2>
        <p>Lorem ipsum</p>
      </section>
      <section id="chapter2" class="chapter">
        <h2>Page Orientation</h2>
        <p>Lorem ipsum</p>
      </section>
      <section id="chapter3" class="chapter">
        <h2>Page Margins</h2>
        <p>There are 16 page margins that can be set:</p>
        <ul>
          <li>@top-left-corner</li>
          <li>@top-left</li>
          <li>@top-center</li>
          <li>@top-right</li>
          <li>@top-right-corner</li>
          <li>@left-top</li>
          <li>@left-middle</li>
          <li>@left-bottom</li>
          <li>@right-top</li>
          <li>@right-middle</li>
          <li>@right-bottom</li>
          <li>@bottom-left-corner</li>
          <li>@bottom-left</li>
          <li>@bottom-center</li>
          <li>@bottom-right</li>
          <li>@bottom-right-corner</li>
        </ul>
        <p>They can be used to show what appears in these parts of the margin</p>
      </section>
      <section id="conclusion">
        <h2>Conclusion</h2>
        <p>Now go ahead and write books.</p>
      </section>
    </article>
    

The first part of the CSS sets up the **named** pages, these include the size and orientation and also some content to go in the [`@top-center` margin](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page#margin_at-rules)
 of the printed pages.

css

    @page toc {
      size: a4 portrait;
      @top-center {
        content: "Table of contents";
      }
    }
    
    @page foreword {
      size: a4 portrait;
      @top-center {
        content: "Foreword";
      }
    }
    
    @page introduction {
      size: a4 portrait;
      @top-center {
        content: "Introduction";
      }
    }
    
    @page conclusion {
      size: a4 portrait;
      @top-center {
        content: "Conclusion";
      }
    }
    
    @page chapter {
      size: a4 landscape;
      @top-center {
        content: "Chapter";
      }
    }
    

    fieldset {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      gap: 1rem;
      width: fit-content;
    }
    body {
      font: 1.1em sans-serif;
    }
    

The next part of the CSS uses [attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
 to apply the print dimensions, orientation, and margins defined in the named `@page` rules defined in the previous CSS section to elements using the `page` property. The sections with `class="chapter"` are concurrent and appear as one page. The `break-after: page;` is used to split them up, which splits each chapter into a separately printed page.

css

    @media print {
      fieldset {
        display: none;
      }
      section {
        font-size: 2rem;
        font-family: "Roboto", sans-serif;
      }
      .chapter {
        border: tomato 2px solid;
      }
      [data-print="grouped"] > #toc,
      [data-print="paged"] > #toc {
        page: toc;
        font-family: "Courier New";
      }
      [data-print="grouped"] > #foreword,
      [data-print="paged"] > #foreword {
        page: foreword;
        font-family: "Courier New";
      }
      [data-print="grouped"] > #introduction,
      [data-print="paged"] > #introduction {
        page: introduction;
        font-family: "Courier New";
      }
      [data-print="grouped"] > #conclusion,
      [data-print="paged"] > #conclusion {
        page: conclusion;
        font-family: "Courier New";
      }
      [data-print="grouped"] > .chapter,
      [data-print="paged"] > .chapter {
        page: chapter;
      }
      [data-print="paged"] > .chapter {
        border: none;
        break-after: page;
      }
      .chapter > ul {
        columns: 2;
      }
    }
    

The JavaScript updates the value of the `data-print` attribute, which is the attribute on which the named page is applied, when you select a different printing option:

js

    const printArea = document.querySelector("#print-area");
    const printButton = document.querySelector("#print");
    const printOption = document.querySelector("#printStyle");
    
    printOption.addEventListener("change", (event) => {
      if (event.target.value === "single") {
        printArea.dataset.print = "single";
      } else if (event.target.value === "grouped") {
        printArea.dataset.print = "grouped";
      } else {
        printArea.dataset.print = "paged";
      }
    });
    
    printButton.addEventListener("click", () => {
      window.print();
    });
    

What is printed, and what is shown in the print preview dialog, will change depending on which print style radio button is selected:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3  <br>\# propdef-page](https://drafts.csswg.org/css-page/#propdef-page) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/page/index.md?plain=1 "Folder: en-us/web/css/reference/properties/page (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")