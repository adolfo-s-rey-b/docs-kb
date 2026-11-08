*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#mdn-search)
    

`view-transition-scope` CSS property
====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/496)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#browser_compatibility)
 carefully before using this in production.

The **`view-transition-scope`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables the discoverability of elements with [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 values set on them (and therefore the creation of view transition [snapshots](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#an_aside_on_snapshots)
) to be isolated to a specific element subtree.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    view-transition-scope: none;
    view-transition-scope: all;
    
    /* Global values */
    view-transition-scope: inherit;
    view-transition-scope: initial;
    view-transition-scope: revert;
    view-transition-scope: revert-layer;
    view-transition-scope: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#none)

The initial value. Discoverability of elements to snapshot during a view transition is not limited to any specific subtree.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#all)

Limits the discoverability of elements to snapshot during a view transition to the subtree of the element on which this property is set. Only elements with a non-`none` [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 are considered.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#description)

-----------------------------------------------------------------------------------------------------------------------

During [the view transition process](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_process)
, the browser captures snapshots of elements that have a non-`none` [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 set on them. These snapshots are then animated via CSS animations.

One issue that can arise during this process is naming collisions between elements involved in a view transition. You can't have the same [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 set on multiple elements — if you do, the browser throws an `InvalidStateError` when the [`Element.startViewTransition()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/startViewTransition)
 method is called to start the transition.

You could solve this problem by setting a `view-transition-name` of [`match-element`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#match-element)
 on the elements to let the browser auto-assign internal unique names. However, this won't work if you are including multiple components from different sources that you don't control. A naming collision might still occur.

The `view-transition-scope` property allows view transitions to be self-contained. When `view-transition-scope: all` is set on an element, it limits the transition scope to that element and its descendants, which can be used to solve the above problem.

Whenever an [element-scoped view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_element-scoped)
 is triggered, the browser automatically sets `view-transition-scope: all` on the transition root element, ensuring that only elements inside the transition scope are snapshotted and animated.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

view-transition-scope =   
  none  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using `view-transition-scope` to isolate snapshots](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#using_view-transition-scope_to_isolate_snapshots)

This example demonstrates how to use `view-transition-scope` to isolate the scope of document-scoped view transitions, enabling the same `view-transition-name` to be used on multiple elements.

#### HTML

The HTML includes a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element to control updating the DOM, plus several components with the class `change-me`, some of which are nested, all wrapped in a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element.

html

    <button>Update DOM</button>
    <section>
      <div class="change-me"><span>I can change</span></div>
      <div class="change-me">
        <span>I can change</span>
        <div class="change-me"><span>I can change</span></div>
      </div>
      <div class="change-me"><span>I can change</span></div>
    </section>
    

#### CSS

We start by setting the same `view-transition-name` on all components. We then set `view-transition-scope: all` on all of them, to isolate the view transition process for each one. Next, we set a longer [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
 on all view transitions with this `view-transition-name` via the [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
 pseudo-element.

    body {
      font: 1.2em / 1.5 sans-serif;
      width: 50%;
      max-width: 700px;
      margin: 0 auto;
    }
    
    section,
    .change-me {
      border: 2px solid #666666;
      padding: 10px;
    }
    
    section {
      background-color: orange;
    }
    

css

    .change-me {
      background-color: white;
      view-transition-name: para-change;
      view-transition-scope: all;
    }
    
    ::view-transition-group(para-change) {
      animation-duration: 1s;
    }
    

#### JavaScript

The script starts by grabbing references to the button and the `<div>` elements (our components).

js

    const btn = document.querySelector("button");
    const divs = document.querySelectorAll("div");
    

Next, we define a function called `updateDivs()`, which toggles the text content of each component's nested [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element between two values, and also toggles the component's foreground and background colors between two values.

js

    function updateDivs() {
      divs.forEach((div) => {
        if (div.firstElementChild.textContent === "I can change") {
          div.firstElementChild.textContent = "I have changed";
          div.style.color = "white";
          div.style.backgroundColor = "black";
        } else {
          div.firstElementChild.textContent = "I can change";
          div.style.color = "black";
          div.style.backgroundColor = "white";
        }
      });
    }
    

Finally, we add a `click` event listener to the `<button>` element. When the button is clicked, we first check whether `startViewTransition()` exists on the `document` object — if it does not, we run `updateDivs()` and then `return` out of the function. This first part allows browsers that don't support view transitions to still update the DOM without error. Next, we run `updateDivs()` inside a `startViewTransition()` callback to trigger the view transition as the DOM updates.

js

    btn.addEventListener("click", handleClick);
    
    function handleClick(e) {
      if (!document.startViewTransition) {
        updateDivs();
        return;
      }
      document.startViewTransition(() => {
        updateDivs();
      });
    }
    

#### Result

Click the "Update DOM" button to see the view transition. Now try the following:

1.  Inspect one of the `<div>` elements.
2.  In the Styles panel in your browser's developer tools, uncheck the `view-transition-scope: all;` declaration to disable it.
3.  Now switch to the JavaScript Console.
4.  Click the "Update DOM" button again.

You should see that the view transition animation is not applied when the DOM changes, and an `InvalidStateError` is reported in the console.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 2  <br>\# view-transition-scope-prop](https://drafts.csswg.org/css-view-transitions-2/#view-transition-scope-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
    
*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Using the View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)
     guide
*   [Using element-scoped view transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_element-scoped)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/view-transition-scope/index.md?plain=1 "Folder: en-us/web/css/reference/properties/view-transition-scope (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-transition-scope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-transition-scope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-transition-scope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-transition-scope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb6de98eb9cd52ce7e37f22a340352f0af4c9d597%0A*+Document+last+modified%3A+2026-08-14T17%3A15%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")