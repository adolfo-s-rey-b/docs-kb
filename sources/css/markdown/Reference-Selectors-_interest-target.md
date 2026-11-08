*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#mdn-search)
    

`:interest-target` CSS pseudo-class
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/464)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#browser_compatibility)
 carefully before using this in production.

The **`:interest-target`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents the target element associated with an [interest invoker](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 when interest is shown on that invoker.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#syntax)

-------------------------------------------------------------------------------------------------------

css

    :interest-target {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#examples)

-----------------------------------------------------------------------------------------------------------

### [Selecting the target element associated with an interest invoker](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#selecting_the_target_element_associated_with_an_interest_invoker)

In this example, we demonstrate how `:interest-target` can be used to apply styles to an interest invoker element's target element when interest is shown on the invoker.

#### HTML

The markup includes a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 and a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
. We specify the `<button>` as an interest invoker by giving it the `interestfor` attribute whose value matches the `id` of the `<p>` element, making the paragraph the target element.

html

    <button interestfor="mytarget">Button</button>
    <p id="mytarget">A paragraph</p>
    

#### CSS

In the CSS, we specify a rule with an `:interest-target` selector, which will apply a specific set of styles to the `<p>` element when interest is shown in the `<button>`. We also apply some other styles to the `<button>`, which we've hidden for brevity.

    body {
      margin: 10px;
    }
    
    button {
      padding: 5px 10px;
      border: 1px solid #dddddd;
      border-radius: 5px;
      background-color: #eeeeee;
    
      cursor: pointer;
    }
    

css

    p:interest-target {
      font-size: 1.5em;
      font-family: sans-serif;
      padding: 10px;
      background-color: hotpink;
      color: purple;
    }
    

#### Result

This renders as follows:

Try showing interest in the button (for example, by hovering or focusing it), and note how this results in the styles shown earlier being applied to the paragraph.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 5  <br>\# selectordef-interest-target](https://drafts.csswg.org/selectors-5/#selectordef-interest-target) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`:interest-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    
*   [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_interest-target/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_interest-target (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ainterest-target&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_interest-target%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ainterest-target%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_interest-target%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")