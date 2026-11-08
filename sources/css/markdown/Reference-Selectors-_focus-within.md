*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#mdn-search)
    

`:focus-within` CSS pseudo-class
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:focus-within`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches an element if the element or any of its descendants are focused. In other words, it represents an element that is itself matched by the [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 pseudo-class or has a descendant that is matched by `:focus`. (This includes descendants in [shadow trees](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
.)

This selector is useful, to take a common example, for highlighting an entire [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 container when the user focuses on one of its [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 fields.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#try_it)

----------------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    label:focus-within {
      font-weight: bold;
    }
    

    <p>Which flavor would you like to order?</p>
    <label>Full Name: <input name="firstName" type="text" /></label>
    <label
      >Flavor:
      <select name="flavor">
        <option>Cherry</option>
        <option>Green Tea</option>
        <option>Moose Tracks</option>
        <option>Mint Chip</option>
      </select>
    </label>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#syntax)

----------------------------------------------------------------------------------------------------

css

    :focus-within {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#examples)

--------------------------------------------------------------------------------------------------------

In this example, the container will receive special coloring styles when either text input receives focus.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#html)

html

    <ul class="group">
      <li>
        <label for="given-name">Given Name:</label>
        <input id="given-name" type="text" />
      </li>
      <li>
        <label for="family-name">Family Name:</label>
        <input id="family-name" type="text" />
      </li>
    </ul>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#css)

css

    .group {
      list-style: none;
      border: 1px solid;
      color: gray;
      padding: 4px;
    }
    
    .group:focus-within {
      background: #ffff88;
      color: black;
    }
    
    input {
      margin: 4px;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#result)

Try typing in the text fields.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# the-focus-within-pseudo](https://drafts.csswg.org/selectors/#the-focus-within-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within#see_also)

--------------------------------------------------------------------------------------------------------

*   [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
    
*   [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
    
*   [Grab your user's attention with the focus-within selector](https://dev.to/vtrpldn/grab-your-user-s-attention-with-the-focus-within-css-selector-4d4 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_focus-within/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_focus-within (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afocus-within&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_focus-within%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afocus-within%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_focus-within%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")