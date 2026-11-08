*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#mdn-search)
    

`::backdrop` CSS pseudo-element
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::backdrop`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 is a box the size of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
, which is rendered immediately beneath any element being presented in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#try_it)

-------------------------------------------------------------------------------------------------

    button {
      font-size: 1.2rem;
      padding: 5px 15px;
    }
    
    dialog::backdrop {
      background-color: salmon;
    }
    

    <button id="showDialogBtn">Show a dialog</button>
    
    <dialog id="favDialog">
      <form method="dialog">
        <p>The background shown outside of this dialog is a backdrop.</p>
        <button id="confirmBtn">Close the dialog</button>
      </form>
    </dialog>
    

    const showDialogBtn = document.getElementById("showDialogBtn");
    const favDialog = document.getElementById("favDialog");
    
    showDialogBtn.addEventListener("click", () => favDialog.showModal());
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#syntax)

-------------------------------------------------------------------------------------------------

css

    ::backdrop {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#description)

-----------------------------------------------------------------------------------------------------------

Backdrops appear in the following instances:

*   Elements which have been placed in fullscreen mode using the [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
     [`Element.requestFullscreen()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestFullscreen)
     method.
*   [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     elements that have been shown in the top layer via a [`HTMLDialogElement.showModal()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal)
     call.
*   [Popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover")
     elements that have been shown in the top layer via a [`HTMLElement.showPopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover)
     call.

When multiple elements have been placed into the top layer, each one has its own `::backdrop` pseudo-element.

css

    /* Backdrop is only displayed when dialog is opened with dialog.showModal() */
    dialog::backdrop {
      background: rgb(255 0 0 / 25%);
    }
    

Elements are placed in a last-in/first out (LIFO) stack in the top layer. The `::backdrop` pseudo-element makes it possible to obscure, style, or completely hide everything located below a top layer element.

`::backdrop` neither inherits from nor is inherited by any other elements. No restrictions are made on what properties apply to this pseudo-element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#examples)

-----------------------------------------------------------------------------------------------------

### [Styling a modal dialog's backdrop](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#styling_a_modal_dialogs_backdrop)

In this example, we use the `::backdrop` pseudo-element to style the backdrop that is used when a modal [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 is open.

#### HTML

We include a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 that, when clicked, will open the included `<dialog>`. When the `<dialog>` is opened, we give focus to the button that closes the dialog:

html

    <dialog>
      <button autofocus>Close</button>
      <p>This modal dialog has a beautiful backdrop!</p>
    </dialog>
    <button>Show the dialog</button>
    

#### CSS

We add a background to the backdrop, creating a colorful donut using [CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
:

css

    ::backdrop {
      background-image:
        radial-gradient(
          circle,
          white 0 5vw,
          transparent 5vw 20vw,
          white 20vw 22.5vw,
          #eeeeee 22.5vw
        ),
        conic-gradient(
          #272b66 0 50grad,
          #2d559f 50grad 100grad,
          #9ac147 100grad 150grad,
          #639b47 150grad 200grad,
          #e1e23b 200grad 250grad,
          #f7941e 250grad 300grad,
          #662a6c 300grad 350grad,
          #9a1d34 350grad 400grad,
          #43a1cd 100grad 150grad,
          #ba3e2e
        );
    }
    

#### JavaScript

The dialog is opened modally using the [`.showModal()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal)
 method and closed using the [`.close()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close)
 method.

js

    const dialog = document.querySelector("dialog");
    const showButton = document.querySelector("dialog + button");
    const closeButton = document.querySelector("dialog button");
    
    // "Show the dialog" button opens the dialog modally
    showButton.addEventListener("click", () => {
      dialog.showModal();
    });
    
    // "Close" button closes the dialog
    closeButton.addEventListener("click", () => {
      dialog.close();
    });
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Positioned Layout Module Level 4  <br>\# backdrop](https://drafts.csswg.org/css-position-4/#backdrop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop#see_also)

-----------------------------------------------------------------------------------------------------

*   [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    
*   [`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module
*   [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module
*   [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
    
*   [`popover`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
     HTML global attribute
*   [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_backdrop/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_backdrop (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Abackdrop&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_backdrop%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Abackdrop%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_backdrop%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8fa3309a76fe8dc4cf5e8eed97ef596a91513fbd%0A*+Document+last+modified%3A+2026-05-21T11%3A07%3A20.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")