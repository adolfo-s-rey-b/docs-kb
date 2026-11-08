*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#mdn-search)
    

`:active-view-transition-type()` CSS pseudo-class
=================================================

Baseline 2026

Newly available

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The functional **`:active-view-transition-type()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements when a view transition with one or more specific types is in progress (is _active_) and stops matching once the view transition has completed.

css

    html:active-view-transition-type(forwards, backwards) {
      /* ... */
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#syntax)

-------------------------------------------------------------------------------------------------------------------

css

    :active-view-transition-type(<custom-ident>#) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#parameters)

[`<custom-ident>#`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#custom-ident)

One or more comma-separated [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values representing the choice of types that can be applied to the active view transition for this selector to match.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#description)

-----------------------------------------------------------------------------------------------------------------------------

[View transition types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)
 provide a mechanism by which different **types** can be specified for active view transitions. Types can be set on view transitions in multiple ways:

*   For same-document (SPA) view transitions, specify types in the [`types`](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition#types)
     option of the [`startViewTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition "startViewTransition()")
     method.
*   For cross-document view transitions, specify types in the [`types`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#types)
     descriptor of the [`@view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)
     at-rule.
*   You can also modify the active view transition's types on-the-fly via the [`types`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/types "types")
     property of the corresponding `ViewTransition` object:
    *   For same-document view transitions, this is the `ViewTransition` object returned by the `startViewTransition()` method.
    *   For cross-document view transitions, the `ViewTransition` object is available in the [`viewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/PageSwapEvent/viewTransition "viewTransition")
         property of the [`pageswap`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageswap_event "pageswap")
         event object in the case of the outgoing page, and the [`viewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/PageRevealEvent/viewTransition "viewTransition")
         property of the [`pagereveal`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pagereveal_event "pagereveal")
         event object in the case of the incoming page.
    *   You can also access the active `ViewTransition` via the [`Document.activeViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/Document/activeViewTransition)
         property. This provides a consistent way to access the active view transition in any context.

Once the active view transition has one or more types set on it, the `:active-view-transition-type()` pseudo-class can be applied to the document root element to set custom styles for each type. The pseudo-class takes a comma-separated list of types as its argument to specify the types that can be set on the active view transition for the selector to be matched.

For example, you might want to apply different transition animations to an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element in an image gallery app as the displayed image changes, depending on whether you are moving forward or backward in the sequence, deleting an image, or adding an image into the sequence.

### [OR versus AND behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#or_versus_and_behavior)

It is important to note that the comma-separated list of types specified inside the `:active-view-transition-type()` pseudo-class provides OR behavior — if one or more of these types are set on the active view transition, the selector will match.

For example, in this case, the selector will match if the active view transition has a type of `forwards`, `backwards`, or both:

css

    html:active-view-transition-type(forwards, backwards) {
      /* ... */
    }
    

If you want to specify AND behavior — that is, all the types must be set for the selector to match — you can do so by chaining multiple `:active-view-transition-type()` pseudo-classes together. In the following case, the selector will only match if the active view transition has types of `slide` _and_ `forwards`:

css

    html:active-view-transition-type(slide):active-view-transition-type(forwards) {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#examples)

-----------------------------------------------------------------------------------------------------------------------

See also [Using view transition types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)
 for multiple complete examples.

### [Basic `:active-view-transition-type()` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#basic_active-view-transition-type_usage)

This example includes a basic document that transitions between two different pieces of content via two different buttons, "Backwards" and "Forwards". We demonstrate how view transition types can be used to animate the transition differently depending on which button was pressed.

#### HTML

The markup includes a single [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element to contain the content and two [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements to trigger the view transitions.

html

    <p>This is my first piece of content. I hope you like it!</p>
    <div>
      <button id="backwards">Backwards</button>
      <button id="forwards">Forwards</button>
    </div>
    

#### JavaScript

In our script, we create references to both buttons and the content paragraph, and then store our two different pieces of content in two constants.

js

    const backBtn = document.getElementById("backwards");
    const fwdBtn = document.getElementById("forwards");
    const content = document.querySelector("p");
    
    const first = "This is my first piece of content. I hope you like it!";
    const second =
      "This is my second piece of content. Is it better than the first?";
    

Next, we add `click` event listeners to the backwards and forwards buttons; when they are clicked, the `changeContent()` function is run.

js

    backBtn.addEventListener("click", changeContent);
    fwdBtn.addEventListener("click", changeContent);
    

Finally, we define the `changeContent()` function. We start by declaring a `type` value that will hold our view transition type value. If the event target is the "Backwards" button, we set `type` to `backwards`. If not, we set `type` to `forwards`. We then invoke the [`startViewTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/startViewTransition "startViewTransition()")
 method to update the content and start the transition:

*   The `update` callback checks whether the paragraph `textContent` is equal to the `first` string. If so, we set it to the `second` string. If not, we set it to the `first` string.
*   The `types` array is given one element: the `type` value we declared earlier.

js

    function changeContent(e) {
      const type = e.target === backBtn ? "backwards" : "forwards";
      document.startViewTransition({
        update() {
          content.textContent === first
            ? (content.textContent = second)
            : (content.textContent = first);
        },
        types: [type],
      });
    }
    

#### CSS

In our styles, we start off by creating a set of nested rules using the `:active-view-transition` pseudo-class. These styles will be applied whenever a view transition is active, regardless of the their types. We apply a [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 of `none` to the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
, as we don't want any elements captured and animated on transition except for the `<p>` element, which is given a `view-transition-name` of `slide`.

    html,
    body {
      height: 100%;
    }
    
    body {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    
    div {
      display: flex;
      width: 60%;
      justify-content: space-between;
    }
    
    p {
      font-size: 1.7em;
      width: 60%;
      color: blue;
      margin-top: 0;
    }
    

css

    html:active-view-transition {
      :root {
        view-transition-name: none;
      }
      p {
        view-transition-name: slide;
      }
    }
    

Next, we use the `:active-view-transition-type()` pseudo-class to create two blocks of nested styles, the first of which is only applied when the active view transition has a type of `forwards`, and the second of which is only applied when the active view transition has a type of `backwards`. In each block, we use the [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
 and [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
 pseudo-elements to apply custom [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 values to the `slide` capture group's outgoing and incoming views.

As a result:

*   When the transition type is `forwards`, the old content view slides out to the left, and the new content view slides in from the right.
*   When the transition type is `backwards`, the old content view slides out to the right, and the new content view slides in from the left.

css

    html:active-view-transition-type(forwards) {
      &::view-transition-old(slide) {
        animation-name: slide-out-to-left;
      }
      &::view-transition-new(slide) {
        animation-name: slide-in-from-right;
      }
    }
    
    html:active-view-transition-type(backwards) {
      &::view-transition-old(slide) {
        animation-name: slide-out-to-right;
      }
      &::view-transition-new(slide) {
        animation-name: slide-in-from-left;
      }
    }
    

Finally, we use [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animation blocks to define the animations referenced previously.

css

    @keyframes slide-in-from-left {
      from {
        translate: -100vw 0;
      }
    }
    @keyframes slide-in-from-right {
      from {
        translate: 100vw 0;
      }
    }
    @keyframes slide-out-to-left {
      to {
        translate: -100vw 0;
      }
    }
    @keyframes slide-out-to-right {
      to {
        translate: 100vw 0;
      }
    }
    

#### Result

The example is rendered like so:

Try clicking the "Backwards" and "Forwards" buttons, and note how, even though the same code is used to trigger the content update and view transition in each case, a different animation is used for the transition. This is because a different transition type is set depending on which button is pressed.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 2  <br>\# the-active-view-transition-type-pseudo](https://drafts.csswg.org/css-view-transitions-2/#the-active-view-transition-type-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`Document.activeViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/Document/activeViewTransition)
    
*   [`:active-view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)
     pseudo-class
*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Using the View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)
    
*   [Using view transition types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_active-view-transition-type/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_active-view-transition-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aactive-view-transition-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_active-view-transition-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aactive-view-transition-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_active-view-transition-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")