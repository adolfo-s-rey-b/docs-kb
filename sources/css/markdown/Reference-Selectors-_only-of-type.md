*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#mdn-search)
    

`:only-of-type` CSS pseudo-class
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:only-of-type`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element that has no siblings of the same type (tag name).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#try_it)

----------------------------------------------------------------------------------------------------

    a:only-of-type {
      color: fuchsia;
    }
    
    dd:only-of-type {
      background-color: bisque;
    }
    

    <p>
      To find out more about <b>QUIC</b>, check <a href="#">RFC 9000</a> and
      <a href="#">RFC 9114</a>.
    </p>
    
    <dl>
      <dt>Published</dt>
      <dd>2021</dd>
      <dd>2022</dd>
    </dl>
    
    <p>Details about <b>QPACK</b> can be found in <a href="#">RFC 9204</a>.</p>
    
    <dl>
      <dt>Published</dt>
      <dd>2022</dd>
    </dl>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#syntax)

----------------------------------------------------------------------------------------------------

css

    :only-of-type {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#examples)

--------------------------------------------------------------------------------------------------------

### [Styling elements with no siblings of the same type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#styling_elements_with_no_siblings_of_the_same_type)

#### HTML

html

    <main>
      <div>I am `div` #1.</div>
      <p>I am the only `p` among my siblings.</p>
      <div>I am `div` #2.</div>
      <div>
        I am `div` #3.
        <i>I am the only `i` child.</i>
        <em>I am `em` #1.</em>
        <em>I am `em` #2.</em>
      </div>
    </main>
    

#### CSS

css

    main :only-of-type {
      color: red;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# only-of-type-pseudo](https://drafts.csswg.org/selectors/#only-of-type-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type#see_also)

--------------------------------------------------------------------------------------------------------

*   [`:only-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child)
    
*   [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    
*   [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    
*   [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_only-of-type/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_only-of-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aonly-of-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_only-of-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aonly-of-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_only-of-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")