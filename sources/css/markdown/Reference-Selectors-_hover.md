*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#mdn-search)
    

`:hover` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:hover`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches an element when a user interacts with it using a pointing device. The pseudo-class is generally triggered when the user moves the cursor (mouse pointer) over an element without pressing the mouse button.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#try_it)

---------------------------------------------------------------------------------------------

    .joinBtn {
      width: 10em;
      height: 5ex;
      background-color: gold;
      border: 2px solid firebrick;
      border-radius: 10px;
      font-weight: bold;
      color: black;
      cursor: pointer;
    }
    
    .joinBtn:hover {
      background-color: bisque;
    }
    

    <p>Would you like to join our quest?</p>
    <button class="joinBtn">Confirm</button>
    

Styles defined by the `:hover` pseudo-class will be overridden by any subsequent link-related pseudo-class ([`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
, [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
, or [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
) that has at least equal specificity. To style links appropriately, put the `:hover` rule after the `:link` and `:visited` rules but before the `:active` one, as defined by the _LVHA-order_: `:link` — `:visited` — `:hover` — `:active`.

**Note:** The `:hover` pseudo-class is problematic on touchscreens. Depending on the browser, the `:hover` pseudo-class might never match, match only for a moment after touching an element, or continue to match even after the user has stopped touching and until the user touches another element. Web developers should make sure that content is accessible on devices with limited or non-existent hovering capabilities.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#syntax)

---------------------------------------------------------------------------------------------

css

    :hover {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#examples)

-------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#basic_example)

#### HTML

html

    <a href="#">Try hovering over this link.</a>
    

#### CSS

css

    a {
      background-color: powderblue;
      transition: background-color 0.5s;
    }
    
    a:hover {
      background-color: gold;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-hover](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-hover) |
| [Selectors Level 4  <br>\# hover-pseudo](https://drafts.csswg.org/selectors/#hover-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover#see_also)

-------------------------------------------------------------------------------------------------

*   [Chromium bug #370155: Don't make `:hover` sticky on tap on sites that set a mobile viewport](https://crbug.com/370155 "External link (opens in new tab)")
    
*   [Chromium bug #306581: Immediately show hover and active states on touch when page isn't scrollable.](https://crbug.com/306581 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_hover/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_hover (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahover&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_hover%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ahover%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_hover%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")