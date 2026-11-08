*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#mdn-search)
    

`:active` CSS pseudo-class
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:active`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element (such as a button) that is being activated by the user. When using a mouse, "activation" typically starts when the user presses down the primary mouse button.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#try_it)

----------------------------------------------------------------------------------------------

    .joinBtn {
      width: 10em;
      height: 5ex;
      background-image: linear-gradient(135deg, #f34079 40%, #fc894d);
      border: none;
      border-radius: 5px;
      font-weight: bold;
      color: white;
      cursor: pointer;
    }
    
    .joinBtn:active {
      box-shadow: 2px 2px 5px #fc894d;
    }
    

    <p>Would you like to subscribe to our channel?</p>
    <button class="joinBtn">Subscribe</button>
    

The `:active` pseudo-class is commonly used on [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements. Other common targets of this pseudo-class include elements that are _contained in_ an activated element, and form elements that are being activated through their associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
.

Styles defined by the `:active` pseudo-class will be overridden by any subsequent link-related pseudo-class ([`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
, [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
, or [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
) that has at least equal specificity. To style links appropriately, put the `:active` rule after all other link-related rules, as defined by the _LVHA-order_: `:link` — `:visited` — `:hover` — `:active`.

**Note:** On systems with multi-button mice, CSS specifies that the `:active` pseudo-class must only apply to the primary button; on right-handed mice, this is typically the leftmost button.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#syntax)

----------------------------------------------------------------------------------------------

css

    :active {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#examples)

--------------------------------------------------------------------------------------------------

### [Active links](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#active_links)

#### HTML

html

    <p>
      This paragraph contains a link:
      <a href="#">This link will turn red while you click on it.</a>
      The paragraph will get a gray background while you click on it or the link.
    </p>
    

#### CSS

css

    /* Unvisited links */
    a:link {
      color: blue;
    }
    /* Visited links */
    a:visited {
      color: purple;
    }
    /* Hovered links */
    a:hover {
      background: yellow;
    }
    /* Active links */
    a:active {
      color: red;
    }
    
    /* Active paragraphs */
    p:active {
      background: #eeeeee;
    }
    

#### Result

### [Active form elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#active_form_elements)

#### HTML

html

    <form>
      <label for="my-button">My button: </label>
      <button id="my-button" type="button">Try Clicking Me or My Label!</button>
    </form>
    

#### CSS

css

    form :active {
      color: red;
    }
    
    form button {
      background: white;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-active](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-active) |
| [Selectors Level 4  <br>\# active-pseudo](https://drafts.csswg.org/selectors/#active-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active#see_also)

--------------------------------------------------------------------------------------------------

*   Link-related pseudo-classes: [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
    , [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
    , and [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_active/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_active (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aactive&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_active%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aactive%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_active%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")