*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#mdn-search)
    

`:fullscreen` CSS pseudo-class
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/93)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:fullscreen`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches every element that is currently in fullscreen mode. If multiple elements have been put into fullscreen mode, this selects them all.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#syntax)

--------------------------------------------------------------------------------------------------

css

    :fullscreen {
      /* ... */
    }
    

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#usage_notes)

------------------------------------------------------------------------------------------------------------

The `:fullscreen` pseudo-class lets you configure your stylesheets to automatically adjust the size, style, or layout of content when elements switch back and forth between fullscreen and traditional presentations.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#examples)

------------------------------------------------------------------------------------------------------

### [Styling a fullscreen element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#styling_a_fullscreen_element)

This example applies a different background color to a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element, depending on whether or not it is in fullscreen mode. It includes a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 to toggle fullscreen on and off.

html

    <div class="element">
      <h1><code>:fullscreen</code> pseudo-class demo</h1>
    
      <p>
        This demo uses the <code>:fullscreen</code> pseudo-class to automatically
        change the background color of the <code>.element</code> div.
      </p>
    
      <p>
        Normally, the background is light yellow. In fullscreen mode, the background
        is light pink.
      </p>
    
      <button class="toggle">Toggle Fullscreen</button>
    </div>
    

The `:fullscreen` pseudo-class is used to override the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 of the `<div>` when it is in fullscreen mode.

css

    .element {
      background-color: lightyellow;
    }
    
    .element:fullscreen {
      background-color: lightpink;
    }
    

The following JavaScript provides an event handler function that toggles fullscreen when the `<button>` is clicked.

js

    document.querySelector(".toggle").addEventListener("click", (event) => {
      if (document.fullscreenElement) {
        // If there is a fullscreen element, exit full screen.
        document.exitFullscreen();
        return;
      }
      // Make the .element div fullscreen.
      document.querySelector(".element").requestFullscreen();
    });
    

    .element {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-family: sans-serif;
      padding: 1.2em;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# selectordef-fullscreen](https://drafts.csswg.org/selectors/#selectordef-fullscreen) |
| [Fullscreen API  <br>\# css-pc-fullscreen](https://fullscreen.spec.whatwg.org/#css-pc-fullscreen) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen#see_also)

------------------------------------------------------------------------------------------------------

*   [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
    
*   [`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [Guide to the Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API/Guide)
    
*   [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
    
*   DOM API: [`Element.requestFullscreen()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestFullscreen)
    , [`Document.exitFullscreen()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/exitFullscreen)
    , [`Document.fullscreenElement`](https://developer.mozilla.org/en-US/docs/Web/API/Document/fullscreenElement)
    
*   [`allowfullscreen`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#allowfullscreen)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_fullscreen/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_fullscreen (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afullscreen&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_fullscreen%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afullscreen%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_fullscreen%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8fa3309a76fe8dc4cf5e8eed97ef596a91513fbd%0A*+Document+last+modified%3A+2026-05-21T11%3A07%3A20.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")