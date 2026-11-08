*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#mdn-search)
    

`:empty` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:empty`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any element that has no children. Children can be either element nodes or text (including whitespace). Comments, processing instructions, and CSS [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 do not affect whether an element is considered empty.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#try_it)

---------------------------------------------------------------------------------------------

    div:empty {
      outline: 2px solid deeppink;
      height: 1em;
    }
    

    <p>Element with no content:</p>
    <div></div>
    
    <p>Element with comment:</p>
    <div><!-- A comment --></div>
    
    <p>Element with nested empty element:</p>
    <div><p></p></div>
    

**Note:** In [Selectors Level 4](https://drafts.csswg.org/selectors-4/#the-empty-pseudo "External link (opens in new tab)")
, the `:empty` pseudo-class was changed to act like [`:-moz-only-whitespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace)
, but no browser currently supports this yet.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#syntax)

---------------------------------------------------------------------------------------------

css

    :empty {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#accessibility)

-----------------------------------------------------------------------------------------------------------

Assistive technology such as screen readers cannot parse interactive content that is empty. All interactive content must have an accessible name, which is created by providing a text value for the interactive control's parent element ([anchors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, etc.). Accessible names expose the interactive control to the [accessibility tree](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility#accessibility_apis)
, an API that communicates information useful for assistive technologies.

The text that provides the interactive control's accessible name can be hidden using [a combination of properties](https://gomakethings.com/articles/hidden-content-for-better-a11y/#hiding-the-link "External link (opens in new tab)")
 that remove it visually from the screen but keep it parsable by assistive technology. This is commonly used for buttons that rely solely on an icon to convey purpose.

*   [What is an accessible name? | Vispero](https://vispero.com/resources/what-is-an-accessible-name/ "External link (opens in new tab)")
    
*   [Hidden content for better a11y | Go Make Things](https://gomakethings.com/articles/hidden-content-for-better-a11y/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 2.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.4_%e2%80%94_navigable_provide_ways_to_help_users_navigate_find_content_and_determine_where_they_are)
    
*   [Understanding Success Criterion 2.4.4 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-refs.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#examples)

-------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#html)

html

    <div class="box"><!-- I will be lime. --></div>
    <div class="box">I will be pink.</div>
    <div class="box">
      <!-- I will be pink in older browsers because of the whitespace around this comment. -->
    </div>
    <div class="box">
      <p>
        <!-- I will be pink in all browsers because of the non-collapsible whitespace and elements around this comment. -->
      </p>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#css)

    body {
      display: flex;
      justify-content: space-around;
    }
    

css

    .box {
      background: pink;
      height: 80px;
      width: 80px;
    }
    
    .box:empty {
      background: lime;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# the-empty-pseudo](https://drafts.csswg.org/selectors/#the-empty-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty#see_also)

-------------------------------------------------------------------------------------------------

*   [`:-moz-only-whitespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace)
     – The [prefixed](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)
     implementation of the changes in [Selectors Level 4](https://drafts.csswg.org/selectors-4/#the-empty-pseudo "External link (opens in new tab)")
    
*   [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_empty/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_empty (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aempty&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_empty%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aempty%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_empty%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fafcdfa050626bb7eb05ee693df8997020db9ff2e%0A*+Document+last+modified%3A+2026-07-08T23%3A28%3A09.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")