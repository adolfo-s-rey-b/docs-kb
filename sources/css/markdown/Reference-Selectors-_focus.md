*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#mdn-search)
    

`:focus` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:focus`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element (such as a form input) that has received focus. It is generally triggered when the user clicks or taps on an element or selects it with the keyboard's Tab key.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#try_it)

---------------------------------------------------------------------------------------------

    label {
      display: block;
      margin-top: 1em;
    }
    
    input:focus {
      background-color: lightblue;
    }
    
    select:focus {
      background-color: ivory;
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
    

**Note:** This pseudo-class applies only to the focused element itself. Use [`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
 if you want to select an element that _contains_ a focused element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#syntax)

---------------------------------------------------------------------------------------------

css

    :focus {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#accessibility)

-----------------------------------------------------------------------------------------------------------

Make sure the visual focus indicator can be seen by people with low vision. This will also benefit anyone use a screen in a brightly lit space (like outside in the sun). [WCAG 2.1 SC 1.4.11 Non-Text Contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html "External link (opens in new tab)")
 requires that the visual focus indicator be at least 3 to 1.

*   Accessible Visual Focus Indicators: [Give Your Site Some Focus! Tips for Designing Useful and Usable Focus Indicators](https://www.deque.com/blog/give-site-focus-tips-designing-usable-focus-indicators/ "External link (opens in new tab)")
    

### [`:focus { outline: none; }`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#focus_outline_none)

Never just remove the focus outline (visible focus indicator) without replacing it with a focus outline that will pass [WCAG 2.1 SC 1.4.11 Non-Text Contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html "External link (opens in new tab)")
.

*   Quick Tip: [Never remove CSS outlines](https://www.a11yproject.com/posts/never-remove-css-outlines/ "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#examples)

-------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#html)

html

    <div><input class="red-input" value="I'll be red when focused." /></div>
    <div><input class="blue-input" value="I'll be blue when focused." /></div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#css)

css

    .red-input:focus {
      background: yellow;
      color: red;
    }
    
    .blue-input:focus {
      background: yellow;
      color: blue;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-focus](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-focus) |
| [Selectors Level 4  <br>\# focus-pseudo](https://drafts.csswg.org/selectors/#focus-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus#see_also)

-------------------------------------------------------------------------------------------------

*   [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
    
*   [`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_focus/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_focus (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afocus&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_focus%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afocus%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_focus%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")