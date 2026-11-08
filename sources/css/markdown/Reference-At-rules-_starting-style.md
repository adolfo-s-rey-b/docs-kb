*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#mdn-search)
    

`@starting-style` CSS at-rule
=============================

Baseline 2024

Newly available

Since August 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@starting-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 is used to define starting values for properties set on an element that you want to transition from when the element receives its first style update, i.e., when an element is first displayed on a previously loaded page.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#syntax)

-----------------------------------------------------------------------------------------------------

The `@starting-style` at rule can be used in two ways:

1.  As a standalone block, in which case it contains one or more rulesets defining starting style declarations and selecting the elements they apply to:
    
    css
    
        @starting-style {
          /* rulesets */
        }
        
    
2.  Nested within an existing ruleset, in which case it contains one or more declarations defining starting property values for the elements already selected by that ruleset:
    
    css
    
        selector {
          /* existing ruleset */
          /* ... */
        
          @starting-style {
            /* declarations */
          }
        }
        
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#description)

---------------------------------------------------------------------------------------------------------------

To avoid unexpected behavior, [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 are by default not triggered on an element's initial style update, or when its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 type changes from `none` to another value. To enable first-style transitions, `@starting-style` rules are needed. They provide starting styles for elements that do not have a previous state, defining the property values to transition from.

`@starting-style` is especially useful when creating entry and exit transitions for elements displayed in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
 (such as [popovers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 and modal [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
s), elements that are changing to and from `display: none`, and elements when first added to or removed from the DOM.

**Note:** `@starting-style` is only relevant to CSS transitions. When using [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 to implement such effects, `@starting-style` is not needed. See [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
 for an example.

There are two ways to use `@starting-style`: as a standalone rule or nested within a ruleset.

Let's consider a scenario where we want to animate a [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 when shown (that is, when added to the top layer). The "original rule" specifying the styles for the open popover could look something like this (see the [popover example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#animating_a_popover)
 below):

css

    [popover]:popover-open {
      opacity: 1;
      transform: scaleX(1);
    }
    

To specify the starting values of the popover's properties that will be animated using the first method, you include a standalone `@starting-style` block in your CSS:

css

    @starting-style {
      [popover]:popover-open {
        opacity: 0;
        transform: scaleX(0);
      }
    }
    

**Note:** The `@starting-style` at-rule and the "original rule" have the same [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
. To ensure that starting styles get applied, include the `@starting-style` at-rule _after_ the "original rule". If you specify the `@starting-style` at-rule before the "original rule", the original styles will override the starting styles.

To specify the starting style for the popover using the nested method, you can nest the `@starting-style` block inside the "original rule":

css

    [popover]:popover-open {
      opacity: 1;
      transform: scaleX(1);
    
      @starting-style {
        opacity: 0;
        transform: scaleX(0);
      }
    }
    

### [When exactly are starting styles used?](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#when_exactly_are_starting_styles_used)

It is important to understand that an element will transition from its `@starting-style` styles when it is first rendered in the DOM, or when it transitions from [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to a visible value. When it transitions back from its initial visible state, it will no longer use the `@starting-style` styles as it is now visible in the DOM. Instead, it will transition back to whatever styles exist for that element's default state.

In effect, there are three style states to manage in these situations — starting-style state, transitioned state, and default state. It is possible for the "to" and "from" transitions to be different in such cases. You can see a proof of this in our [Demonstration of when starting styles are used](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#demonstration_of_when_starting_styles_are_used)
 example, below.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

@starting-style =   
  @starting-style { [<rule-list>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list)
 }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#examples)

---------------------------------------------------------------------------------------------------------

### [Basic @starting-style usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#basic_starting-style_usage)

Transition an element's [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 from transparent to green when it is initially rendered:

css

    #target {
      transition: background-color 1.5s;
      background-color: green;
    }
    
    @starting-style {
      #target {
        background-color: transparent;
      }
    }
    

Transition the [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 of an element when it changes its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value to or from `none`:

css

    #target {
      transition-property: opacity, display;
      transition-duration: 0.5s;
      display: block;
      opacity: 1;
      @starting-style {
        opacity: 0;
      }
    }
    
    #target.hidden {
      display: none;
      opacity: 0;
    }
    

### [Demonstration of when starting styles are used](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#demonstration_of_when_starting_styles_are_used)

In this example, a button is pressed to create a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element, give it a `class` of `showing`, and add it to the DOM.

`showing` is given a `@starting-style` of `background-color: red` and a style of `background-color: blue` to transition to. The default `div` ruleset contains `background-color: yellow`, and is also where the `transition` is set.

When the `<div>` is first added to the DOM, you'll see the background transition from red to blue. After a timeout, we remove the `showing` class from the `<div>` via JavaScript. At that point it transitions from blue back to yellow, not red. This proves that the starting styles are only used when the element is first rendered in the DOM. Once it has appeared, the element transitions back to the default style set on it.

After another timeout, we then remove the `<div>` from the DOM altogether, resetting the initial state of the example so it can be run again.

#### HTML

html

    <button>Display <code>&lt;div&gt;</code></button>
    

#### CSS

    div {
      width: 200px;
      height: 100px;
      border: 1px solid black;
      margin-top: 10px;
    }
    
    div::after {
      content: "class: " attr(class);
      position: relative;
      top: 3px;
      left: 3px;
    }
    

css

    div {
      background-color: yellow;
      transition: background-color 3s;
    }
    
    div.showing {
      background-color: skyblue;
    }
    
    @starting-style {
      div.showing {
        background-color: red;
      }
    }
    

#### JavaScript

js

    const btn = document.querySelector("button");
    
    btn.addEventListener("click", () => {
      btn.disabled = true;
      const divElem = document.createElement("div");
      divElem.classList.add("showing");
      document.body.append(divElem);
    
      setTimeout(() => {
        divElem.classList.remove("showing");
    
        setTimeout(() => {
          divElem.remove();
          btn.disabled = false;
        }, 3000);
      }, 3000);
    });
    

#### Result

The code renders as follows:

### [Animating a popover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#animating_a_popover)

In this example, a [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 is animated using [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
. Basic entry and exit animations are provided using the [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 property.

#### HTML

The HTML contains a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element declared as a popover using the [popover](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute and a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element designated as the popover's display control using its [popovertarget](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
 attribute.

html

    <button popovertarget="mypopover">Show the popover</button>
    <div popover="auto" id="mypopover">I'm a Popover! I should animate.</div>
    

#### CSS

In this example, we want to animate two properties, [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 and [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 (specifically, a horizontally scaling transform), to make the popover fade in and out as well as grow and shrink horizontally.

css

    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    [popover]:popover-open {
      opacity: 1;
      transform: scaleX(1);
    }
    
    [popover] {
      font-size: 1.2rem;
      padding: 10px;
    
      /* Final state of the exit animation */
      opacity: 0;
      transform: scaleX(0);
    
      transition:
        opacity 0.7s,
        transform 0.7s,
        overlay 0.7s allow-discrete,
        display 0.7s allow-discrete;
      /* Equivalent to
      transition: all 0.7s allow-discrete; */
    }
    
    /* Include after the [popover]:popover-open rule */
    @starting-style {
      [popover]:popover-open {
        opacity: 0;
        transform: scaleX(0);
      }
    }
    
    /* Transition for the popover's backdrop */
    [popover]::backdrop {
      background-color: transparent;
      transition:
        display 0.7s allow-discrete,
        overlay 0.7s allow-discrete,
        background-color 0.7s;
      /* Equivalent to
      transition: all 0.7s allow-discrete; */
    }
    
    [popover]:popover-open::backdrop {
      background-color: rgb(0 0 0 / 25%);
    }
    
    /* Nesting (&) is not supported for pseudo-elements
    so specify a standalone starting-style block. */
    @starting-style {
      [popover]:popover-open::backdrop {
        background-color: transparent;
      }
    }
    

To achieve this, we have set a starting state for these properties on the default hidden state of the popover element (selected via `[popover]`), and an ending state on the open state of the popover (selected via the [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
 pseudo-class).

We then set a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 property to animate between the two states. A starting state for the animation is included inside a `@starting-style` at-rule to enable the entry animation.

Because the animated element is being promoted to the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
 when shown and removed from the top layer when hidden (with [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
), some extra steps are required to ensure the animation works in both directions:

*   `display` is added to the list of transitioned elements to ensure the animated element is visible (set to `display: block` or another visible `display` value) throughout both the entry and exit animations. Without this, the exit animation would not be visible; in effect, the popover would just disappear. Note that the [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
     value is also set in the shorthand to activate the animation.
*   [`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay)
     is added to the list of transitioned elements to ensure that the removal of the element from the top layer is deferred until the animation ends. This doesn't make a huge difference for animations such as this one, but in more complex cases, not doing this can result in the element being removed from the overlay too quickly, meaning the animation is not smooth or effective. Again, `transition-behavior: allow-discrete` is required in this case for the animation to occur.

**Note:** We've also included a transition on the [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
 that appears behind the popover when it opens, to provide a nice darkening animation. `[popover]:popover-open::backdrop` is used to select the backdrop when the popover is open.

#### Result

The code renders as follows:

**Note:** Because popovers change from `display: none` to `display: block` each time they are shown, the popover transitions from its `@starting-style` styles to its `[popover]:popover-open` styles every time the entry transition occurs. When the popover closes, it transitions from its `[popover]:popover-open` state to the default `[popover]` state.

**Note:** You can find an example that demonstrates transitioning a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element and its backdrop as it is shown and hidden on the `<dialog>` reference page — see [Transitioning dialog elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog#transitioning_dialog_elements)
.

### [Transitioning elements on DOM addition and removal](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#transitioning_elements_on_dom_addition_and_removal)

This example contains a button which, when pressed, appends new elements to a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 container. Each element, in turn, contains a nested button, which when pressed, removes the element. This example demonstrates how to use transitions to animate elements when they are added to or removed from the DOM.

#### HTML

html

    <button>Create new column</button>
    <section></section>
    

#### JavaScript

JavaScript enables the addition and removal of elements:

js

    const btn = document.querySelector("button");
    const sectionElem = document.querySelector("section");
    
    btn.addEventListener("click", createColumn);
    
    function randomBackground() {
      function randomNum() {
        return Math.floor(Math.random() * 255);
      }
      const baseColor = `${randomNum()} ${randomNum()} ${randomNum()}`;
    
      return `linear-gradient(to right, rgb(${baseColor} / 0), rgb(${baseColor} / 0.5))`;
    }
    
    function createColumn() {
      const divElem = document.createElement("div");
      divElem.style.background = randomBackground();
    
      const closeBtn = document.createElement("button");
      closeBtn.textContent = "✖";
      closeBtn.setAttribute("aria-label", "close");
      divElem.append(closeBtn);
      sectionElem.append(divElem);
    
      closeBtn.addEventListener("click", () => {
        divElem.classList.add("fade-out");
    
        setTimeout(() => {
          divElem.remove();
        }, 1000);
      });
    }
    

When the "Create new column" button is clicked, the `createColumn()` function is called. This creates a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element with a randomly generated background color and a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element to close the `<div>`. It then appends the `<button>` to the `<div>` and the `<div>` to the `<section>` container.

We then add an event listener to the close button via [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener "addEventListener()")
. Clicking the close button does two things:

*   Adds the `fade-out` class to the `<div>`. Adding the class triggers the exit animation set on that class.
*   Removes the `<div>` after a 1000ms delay. The [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
     delays removal of the `<div>` from the DOM (via [`Element.remove()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove)
    ) until after the animation ends.

#### CSS

We include a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 that animates the [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 and [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
 of each column as they are added and removed:

    html * {
      box-sizing: border-box;
      font-family: sans-serif;
    }
    
    body {
      margin: 0;
      display: flex;
      flex-direction: column;
      height: 100vh;
      gap: 10px;
    }
    
    body > button {
      margin: 10px 10px 0 10px;
    }
    
    section {
      display: flex;
      flex: 1;
      gap: 10px;
      margin: 10px;
    }
    

css

    div {
      flex: 1;
      border: 1px solid gray;
      position: relative;
      opacity: 1;
      scale: 1 1;
    
      transition:
        opacity 0.7s,
        scale 0.7s,
        display 0.7s allow-discrete,
        all 0.7s allow-discrete;
      /* Equivalent to
      transition: all 0.7s allow-discrete; */
    }
    
    /* Include after the `div` rule */
    @starting-style {
      div {
        opacity: 0;
        scale: 1 0;
      }
    }
    
    .fade-out {
      opacity: 0;
      display: none;
      scale: 1 0;
    }
    
    div > button {
      font-size: 1.6rem;
      background: none;
      border: 0;
      text-shadow: 2px 1px 1px white;
      border-radius: 15px;
      position: absolute;
      top: 1px;
      right: 1px;
      cursor: pointer;
    }
    

To animate the [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 and [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
 of each `<div>` as it is added to the DOM and then reverse the animation as it is removed from the DOM, we:

*   Specify the ending state of the properties we want to transition on the `div { ... }` rule.
*   Specify the starting state from which to transition the properties inside a `@starting-style` block.
*   Specify the exit animation inside the `.fade-out` rule — this is the class that the JavaScript assigns to the `<div>` elements when their close buttons are pressed. Besides setting the `opacity` and `scale` ending states, we also set [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
     on the `<div>`s — we want them to become immediately unavailable when removed from the UI.
*   Specify the [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
     list inside the `div { ... }` rule to animate `opacity`, `scale`, and `display`. Note that for `display`, the [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
     value is also set in the shorthand so that it will animate.

#### Result

The final result looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 2  <br>\# defining-before-change-style](https://drafts.csswg.org/css-transitions-2/#defining-before-change-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#see_also)

---------------------------------------------------------------------------------------------------------

*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
*   [`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay)
    
*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [`CSSStartingStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStartingStyleRule)
    
*   [Four new CSS features for smooth entry and exit animations](https://developer.chrome.com/blog/entry-exit-animations/ "External link (opens in new tab)")
     on developer.chrome.com (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@starting-style/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@starting-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40starting-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40starting-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40starting-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40starting-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")