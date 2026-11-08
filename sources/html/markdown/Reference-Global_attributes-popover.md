*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#mdn-search)
    

`popover` HTML global attribute
===============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2024.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`popover`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is used to designate an element as a popover element.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#value)

-----------------------------------------------------------------------------------------------------

The `popover` attribute can take one of the following values:

[`"auto"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#auto)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#auto_state_and_light_dismiss)
 popovers can be "light dismissed" — this means that you can hide the popover by clicking outside it or pressing the Esc key. Showing an `auto` popover will generally close other `auto` popovers that are already displayed, unless they are nested.

**Note:** Setting an empty value for `popover` — `popover` or `popover=""` — is equivalent to setting `popover="auto"`.

[`"hint"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#hint)

[`hint`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#using_hint_popover_state)
 popovers do not close `auto` popovers when they are displayed, but will close other hint popovers that are not its ancestors in the [hint stack](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_openclose_interaction_rules)
. They can be light dismissed and will respond to close requests.

[`"manual"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#manual)

[`manual`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#using_manual_popover_state)
 popovers cannot be "light dismissed" and are not automatically closed. Popovers must explicitly be displayed and closed using declarative show/hide/toggle buttons or JavaScript. Multiple independent `manual` popovers can be shown simultaneously.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#description)

-----------------------------------------------------------------------------------------------------------------

Popover elements are hidden via `display: none` until opened via an invoking/control element (i.e., a `<button>` or `<input type="button">` with a [`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
 attribute) or a [`HTMLElement.showPopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover)
 call.

When open, popover elements will appear above all other elements in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
, and won't be influenced by parent elements' [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 or [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 styling.

Popovers that have the [`auto`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#auto_state_and_light_dismiss)
 state can be shown and hidden using associated controls (designated by the [`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
 attribute) and "light dismissed" by clicking outside the popover area, opening another popover, or pressing browser-specific mechanisms such as the Esc key.

Generally only one `auto` popover can be displayed on-screen at a time — showing a second popover when one is already shown will hide the first one. The exception to this rule is when you have nested auto popovers. See [Nested popovers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#nested_popovers)
 for more details.

They can also be controlled using JavaScript, for example the [`HTMLElement.togglePopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/togglePopover)
 method can be used to toggle a popover between shown and hidden.

By contrast, [`manual`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#using_manual_popover_state)
 popovers must be manually shown and hidden — they don't automatically close other popovers when they are displayed and they can't be light dismissed. This allows for use cases where you want to show multiple popovers at the same time.

[`hint`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#using_hint_popover_state)
 popovers do not close `auto` popovers when they are displayed, but will close other hint popovers that are not its ancestors in the hint stack. They can be light dismissed and will respond to close requests.

Usually `hint` popovers are shown and hidden in response to non-click JavaScript events such as [`mouseover`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event)
/[`mouseout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseout_event)
 and [`focus`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event)
/[`blur`](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event)
. Clicking a button to open a `hint` popover would cause an open `auto` popover to light-dismiss.

For detailed information on usage, see the [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
 landing page.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#examples)

-----------------------------------------------------------------------------------------------------------

### [Making an element a popover](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#making_an_element_a_popover)

The following code renders a button that, when activated, will open a popover element. This behavior can be achieved using HTML alone.

html

    <button popovertarget="my-popover">Open Popover</button>
    
    <div popover id="my-popover">Greetings, one and all!</div>
    

### [Nesting popovers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#nesting_popovers)

In this example, a button opens a popover that contains additional nested popovers. The nested popovers can be opened without closing the original menu popover.

#### HTML

In the first part of the HTML, we create a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 that will open the main popover, which is a menu containing a few options.

html

    <header>
      <button popovertarget="menu">Open Menu</button>
    </header>
    <main>
      <!--  Page content goes here  -->
    </main>
    

In the second part of the HTML, we create the menu popover that is opened by the button we created in the previous code block. This menu popover contains an unordered list of menu items, each with an info button that opens a nested popover. The menu popover uses `popover="auto"`, which means it will not be closed when the nested popovers are opened.

html

    <!-- menu popover -->
    <div id="menu" popover="auto">
      <ul>
        <li>
          <a href="#">New thing</a><button popovertarget="new-info">ⓘ</button>
        </li>
        <li>
          <a href="#">Open thing</a><button popovertarget="open-info">ⓘ</button>
        </li>
        <li>
          <a href="#">Save thing</a><button popovertarget="save-info">ⓘ</button>
        </li>
        <li>
          <a href="#">Close thing</a><button popovertarget="close-info">ⓘ</button>
        </li>
      </ul>
    </div>
    

In the final part of the HTML, we create the info popovers for each menu item. Each popover includes `popover="hint"`, which means it will not close the original menu popover but will close the other open info popovers.

html

    <!-- info popovers -->
    <div id="new-info" class="info-popover" popover="hint">
      This is some information about <strong>creating a new</strong> thing.
    </div>
    <div id="open-info" class="info-popover" popover="hint">
      This is some information about <strong>opening an existing</strong> thing.
    </div>
    <div id="save-info" class="info-popover" popover="hint">
      This is some information about <strong>saving the current</strong> thing.
    </div>
    <div id="close-info" class="info-popover" popover="hint">
      This is some information about <strong>closing the current</strong> thing.
    </div>
    

#### CSS

    header {
      display: flex;
      justify-content: center;
    }
    header button {
      margin: 0.4rem auto;
    }
    

We've used [anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 to position the menu popover below the `<button>` and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 to lay out the menu items and info buttons.

css

    #menu {
      margin: 0;
      margin-top: 0.4rem;
      inset: auto;
      position-area: bottom;
    }
    #menu ul {
      display: grid;
      grid-template-columns: max-content 1fr;
      gap: 0.4rem;
      padding: 0.4rem;
    }
    #menu li {
      grid-column: span 2;
      display: grid;
      grid: inherit;
      grid-template-columns: subgrid;
      gap: 1.4rem;
    }
    li [popovertarget] {
      cursor: pointer;
      font-size: 1.2rem;
    }
    li button {
      border: none;
      padding: 0;
      background-color: inherit;
    }
    

Here, we've used anchor positioning to make the info popovers appear to the right of their respective info buttons.

css

    div.info-popover {
      margin: 2rem;
      inset: auto;
      max-width: 300px;
      position-area: right;
    }
    

#### Result

Click the _Open Menu_ button, then click the info icons (ⓘ) next to the menu options to open the info popovers.

**Note:** See our [Popover API examples landing page](https://mdn.github.io/dom-examples/popover-api/ "External link (opens in new tab)")
 to access the full collection of MDN popover examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-popover-attribute](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
    
*   [`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
     HTML attribute
*   [`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction)
     HTML attribute
*   [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
     CSS pseudo-element
*   [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
     CSS pseudo-class

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/popover/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/popover (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fpopover&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fpopover%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fpopover%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fpopover%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F58290795d9f78c91933e092053bb6439bde56651%0A*+Document+last+modified%3A+2026-07-03T00%3A59%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")