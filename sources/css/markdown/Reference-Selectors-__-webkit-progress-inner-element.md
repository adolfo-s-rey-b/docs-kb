*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#mdn-search)
    

`::-webkit-progress-inner-element` CSS pseudo-element
=====================================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`::-webkit-progress-inner-element`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the outermost container of the [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
 element. It is the parent of the [`::-webkit-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-bar)
 pseudo-element.

**Note:** In order to let `::-webkit-progress-value` take effect, [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 needs to be set to `none` on the `<progress>` element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#syntax)

-----------------------------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#examples)

---------------------------------------------------------------------------------------------------------------------------

These examples work only on Blink and WebKit.

### [Adding a black border around the progress bar](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#adding_a_black_border_around_the_progress_bar)

In this example, a 2px black border is added around the progress bar.

#### HTML

#### CSS

#### Result

#### Result screenshot

If you're not using a Blink or WebKit browser, the above code results in a progress bar looking like this:

![Progressbar is a long green and gray box with a black border. The left 20% of the box is green. The right 80% is gray.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element/-webkit-progress-inner-element_example.png)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   The pseudo-elements used by WebKit/Blink to style other parts of a [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
     element:
    
    *   [`::-webkit-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-bar)
        
    *   [`::-webkit-progress-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-value)
        
*   [`::-moz-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-progress-bar)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_-webkit-progress-inner-element/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_-webkit-progress-inner-element (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-webkit-progress-inner-element&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-webkit-progress-inner-element%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-webkit-progress-inner-element%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-webkit-progress-inner-element%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")