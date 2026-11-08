*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#mdn-search)
    

`:active-view-transition` CSS pseudo-class
==========================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:active-view-transition`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches the root element of a document when a [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API#concepts_and_usage)
 is in progress (_active_) and stops matching once the transition has completed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#syntax)

--------------------------------------------------------------------------------------------------------------

css

    :root:active-view-transition ... {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#examples)

------------------------------------------------------------------------------------------------------------------

### [Styling an active view transition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#styling_an_active_view_transition)

This example extends the [Basic view transition example](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition#basic_usage)
 on the `startViewTransition` page.

html

    <main>
      <section class="color">
        <h2>Color is changing!</h2>
      </section>
      <button id="change-color">Change Color</button>
    </main>
    

A `<h2>` element initially has a `display: none` style, and this is overwritten using the `:active-view-transition` pseudo-class setting the `<h2>` style to `display: block`. The button is hidden using `visibility: hidden`, when the view transition is in progress:

    html {
      --bg: indigo;
    }
    main {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    section {
      background-color: var(--bg);
      height: 60px;
      border-radius: 5px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    ::view-transition-group(root) {
      animation-duration: 2s;
    }
    

css

    h2 {
      display: none;
      color: white;
    }
    :root:active-view-transition h2 {
      display: block;
    }
    :root:active-view-transition button {
      visibility: hidden;
    }
    

    const colors = ["darkred", "darkslateblue", "darkgreen"];
    const colBlock = document.querySelector(".color");
    let count = 0;
    const updateColor = () => {
      colBlock.style = `--bg: ${colors[count]}`;
      count = count !== colors.length - 1 ? ++count : 0;
    };
    const changeColor = () => {
      if (!document.startViewTransition) {
        updateColor();
        return;
      }
      const transition = document.startViewTransition(() => {
        updateColor();
      });
    };
    const changeColorButton = document.querySelector("#change-color");
    changeColorButton.addEventListener("click", changeColor);
    changeColorButton.addEventListener("keypress", changeColor);
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 2  <br>\# the-active-view-transition-pseudo](https://drafts.csswg.org/css-view-transitions-2/#the-active-view-transition-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`:active-view-transition-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type)
     pseudo-class
*   [`startViewTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition)
     method
*   [`Document.activeViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/Document/activeViewTransition)
    
*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Using the View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)
    
*   [Using view transition types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_active-view-transition/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_active-view-transition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aactive-view-transition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_active-view-transition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aactive-view-transition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_active-view-transition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3064cbe8212ea919874fb21120a89657afccba25%0A*+Document+last+modified%3A+2026-09-11T17%3A16%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")