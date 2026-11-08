*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#mdn-search)
    

`:modal` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:modal`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches an element that is in a state in which it excludes all interaction with elements outside it until the interaction has been dismissed. Multiple elements can be selected by the `:modal` pseudo-class at the same time, but only one of them will be active and able to receive input.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#try_it)

---------------------------------------------------------------------------------------------

    button {
      display: block;
      margin: auto;
      width: 10rem;
      height: 2rem;
    }
    
    :modal {
      background-color: beige;
      border: 2px solid burlywood;
      border-radius: 5px;
    }
    
    p {
      color: black;
    }
    

    <p>Would you like to see a new random number?</p>
    <button id="showNumber">Show me</button>
    
    <dialog id="favDialog">
      <form method="dialog">
        <p>Lucky number is: <strong id="number"></strong></p>
        <button>Close dialog</button>
      </form>
    </dialog>
    

    const showNumber = document.getElementById("showNumber");
    const favDialog = document.getElementById("favDialog");
    const number = document.getElementById("number");
    
    showNumber.addEventListener("click", () => {
      number.innerText = Math.floor(Math.random() * 1000);
      favDialog.showModal();
    });
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#syntax)

---------------------------------------------------------------------------------------------

css

    :modal {
      /* ... */
    }
    

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#usage_notes)

-------------------------------------------------------------------------------------------------------

Examples of elements that will prevent user interaction with the rest of the page and will be selected by the `:modal` pseudo-class include:

*   The [`dialog`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     element opened with the `showModal()` API.
*   The element selected by the [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
     pseudo-class when opened with the `requestFullscreen()` API.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#examples)

-------------------------------------------------------------------------------------------------

### [Styling a modal dialog](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#styling_a_modal_dialog)

This example styles a modal dialog that opens when the "Show the dialog" button is activated. This example is adapted from the [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element [example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog#handling_the_return_value_from_the_dialog)
.

    <!-- A modal dialog containing a form -->
    <dialog id="favDialog">
      <form method="dialog">
        <p>
          <label>
            Favorite animal:
            <select>
              <option>Choose…</option>
              <option>Brine shrimp</option>
              <option>Red panda</option>
              <option>Spider monkey</option>
            </select>
          </label>
        </p>
        <div>
          <button>Cancel</button>
          <button>Confirm</button>
        </div>
      </form>
    </dialog>
    <p>
      <button id="showDialog">Show the dialog</button>
    </p>
    

#### CSS

The `:modal` pseudo-class selects the dialog opened with `showModal()`, giving it a red border, a yellow background, and a box shadow.

css

    :modal {
      border: 5px solid red;
      background-color: yellow;
      box-shadow: 3px 3px 10px rgb(0 0 0 / 50%);
    }
    

    const showButton = document.getElementById("showDialog");
    const favDialog = document.getElementById("favDialog");
    
    showButton.addEventListener("click", () => {
      favDialog.showModal();
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-modal](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-modal) |
| [Selectors Level 4  <br>\# selectordef-modal](https://drafts.csswg.org/selectors/#selectordef-modal) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal#see_also)

-------------------------------------------------------------------------------------------------

*   [`dialog`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     element
*   Other element display state pseudo-classes: [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
     and [`:picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
    
*   Complete list of [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_modal/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_modal (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Amodal&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_modal%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Amodal%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_modal%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F31e1fcaa50ff25bb27d7093758fa7a7088fff1e0%0A*+Document+last+modified%3A+2026-10-02T18%3A21%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")