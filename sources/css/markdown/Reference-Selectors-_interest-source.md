*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#mdn-search)
    

`:interest-source` CSS pseudo-class
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/464)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#browser_compatibility)
 carefully before using this in production.

The **`:interest-source`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an [interest invoker](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 element when interest is shown on it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#syntax)

-------------------------------------------------------------------------------------------------------

css

    :interest-source {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#examples)

-----------------------------------------------------------------------------------------------------------

### [Selecting an interest invoker element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#selecting_an_interest_invoker_element)

In this example, we demonstrate how `:interest-source` can be used to apply styles to an interest invoker element when interest is shown on it.

#### HTML

The markup includes a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 and a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
. We specify the `<button>` as an interest invoker by giving it the `interestfor` attribute whose value matches the `id` of the `<p>` element, making the paragraph the target element. The paragraph is turned into a popover by giving it the [`popover`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute, which hides it initially.

html

    <button interestfor="mypopover">Button</button>
    <p id="mypopover" popover>A hover tooltip</p>
    

#### CSS

In the CSS, we specify a rule with an `:interest-source` selector to apply a specific combination of [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 to the `<button>` when interest is shown on it. We also apply some other styles to the `<button>`, which are hidden for brevity.

    button {
      margin: 10px;
      padding: 5px 10px;
      border: 1px solid #dddddd;
      border-radius: 5px;
      font-size: 1.5em;
      background-color: #eeeeee;
    
      cursor: pointer;
    }
    

css

    button:interest-source {
      background-color: hotpink;
      color: purple;
    }
    

#### Result

This renders as follows:

Try showing interest in the button (for example, by hovering or focusing it), and note how the `hotpink` and `purple` color combination is applied only when interest is shown.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 5  <br>\# selectordef-interest-source](https://drafts.csswg.org/selectors-5/#selectordef-interest-source) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`:interest-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    
*   [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_interest-source/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_interest-source (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ainterest-source&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_interest-source%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ainterest-source%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_interest-source%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")