*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#mdn-search)
    

`:only-child` CSS pseudo-class
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:only-child`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element without any siblings. This is the same as `:first-child:last-child` or `:nth-child(1):nth-last-child(1)`, but with a lower specificity.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#try_it)

--------------------------------------------------------------------------------------------------

    li:only-child {
      color: fuchsia;
    }
    
    b:only-child {
      text-decoration: underline;
    }
    

    <p>Stars expected to attend:</p>
    <ol>
      <li>Robert Downey, Jr.</li>
    </ol>
    
    <p>Stars yet to confirm:</p>
    <ol>
      <li>Scarlett Johansson</li>
      <li>Samuel L. Jackson</li>
      <li>Chris Pratt</li>
    </ol>
    
    <p>The ceremony is going to be held in <b>The Dolby Theatre</b>.</p>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#syntax)

--------------------------------------------------------------------------------------------------

css

    :only-child {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#examples)

------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#basic_example)

#### HTML

html

    <div>
      <div>I am an only child.</div>
    </div>
    
    <div>
      <div>I am the 1st sibling.</div>
      <div>I am the 2nd sibling.</div>
      <div>
        I am the 3rd sibling,
        <div>but this is an only child.</div>
      </div>
    </div>
    

#### CSS

css

    div:only-child {
      color: red;
    }
    
    div {
      display: inline-block;
      margin: 6px;
      outline: 1px solid;
    }
    

#### Result

### [A list example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#a_list_example)

#### HTML

html

    <ol>
      <li>
        First
        <ul>
          <li>This list has just one element.</li>
        </ul>
      </li>
      <li>
        Second
        <ul>
          <li>This list has three elements.</li>
          <li>This list has three elements.</li>
          <li>This list has three elements.</li>
        </ul>
      </li>
    </ol>
    

#### CSS

css

    li li {
      list-style-type: disc;
    }
    
    li:only-child {
      color: red;
      list-style-type: square;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# only-child-pseudo](https://drafts.csswg.org/selectors/#only-child-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child#see_also)

------------------------------------------------------------------------------------------------------

*   [`:only-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type)
    
*   [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
    
*   [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    
*   [`:nth-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_only-child/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_only-child (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aonly-child&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_only-child%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aonly-child%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_only-child%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")