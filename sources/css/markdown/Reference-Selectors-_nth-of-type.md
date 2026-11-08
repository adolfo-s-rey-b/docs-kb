*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#mdn-search)
    

`:nth-of-type()` CSS pseudo-class
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:nth-of-type()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements based on their position among siblings of the same type (tag name).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#try_it)

---------------------------------------------------------------------------------------------------

    dt {
      font-weight: bold;
    }
    
    dd {
      margin: 3px;
    }
    
    dd:nth-of-type(even) {
      border: 2px solid orange;
    }
    

    <dl>
      <dt>Vegetables:</dt>
      <dd>1. Tomatoes</dd>
      <dd>2. Cucumbers</dd>
      <dd>3. Mushrooms</dd>
      <dt>Fruits:</dt>
      <dd>4. Apples</dd>
      <dd>5. Mangos</dd>
      <dd>6. Pears</dd>
      <dd>7. Oranges</dd>
    </dl>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#syntax)

---------------------------------------------------------------------------------------------------

css

    :nth-of-type(<An+B> | even | odd) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#parameters)

The `:nth-of-type()` pseudo-class is specified with a single argument, which represents the pattern for matching elements.

See [`:nth-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
 for a more detailed explanation of its syntax.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#examples)

-------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#basic_example)

#### HTML

html

    <div>
      <div>This element isn't counted.</div>
      <p>1st paragraph.</p>
      <p class="fancy">2nd paragraph.</p>
      <div>This element isn't counted.</div>
      <p class="fancy">3rd paragraph.</p>
      <p>4th paragraph.</p>
    </div>
    

#### CSS

css

    /* Odd paragraphs */
    p:nth-of-type(2n + 1) {
      color: red;
    }
    
    /* Even paragraphs */
    p:nth-of-type(2n) {
      color: blue;
    }
    
    /* First paragraph */
    p:nth-of-type(1) {
      font-weight: bold;
    }
    
    /* This will match the 3rd paragraph as it will match elements which are 2n+1 AND have a class of fancy.
    The second paragraph has a class of fancy but is not matched as it is not :nth-of-type(2n+1) */
    p.fancy:nth-of-type(2n + 1) {
      text-decoration: underline;
    }
    

#### Result

**Note:** There is no way to select the "nth-of-class" using this selector. The `:nth-of-type` selector looks at the type only when creating the list of matches. You can however use the [`:nth-of-child` selector `of` syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child#the_of_selector_syntax)
 to achieve an "nth-of-class" behavior. You can also apply CSS to an element based on `:nth-of-type` location **and** a class, as shown in the previous example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# nth-of-type-pseudo](https://drafts.csswg.org/selectors/#nth-of-type-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type#see_also)

-------------------------------------------------------------------------------------------------------

*   [`:nth-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    , [`:nth-last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_nth-of-type/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_nth-of-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Anth-of-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_nth-of-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Anth-of-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_nth-of-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe620c4f06bca1cbecc4412084e43ddc12e88fe56%0A*+Document+last+modified%3A+2026-05-11T08%3A21%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")