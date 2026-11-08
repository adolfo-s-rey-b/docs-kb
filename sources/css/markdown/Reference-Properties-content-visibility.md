*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#mdn-search)
    

`content-visibility` CSS property
=================================

Baseline 2024

Newly available

\*

Since September 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`content-visibility`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls whether or not an element renders its contents at all, along with forcing a strong set of containments, allowing user agents to potentially omit large swathes of layout and rendering work until it becomes needed. It enables the user agent to skip an element's rendering work (including layout and painting) until it is needed — which makes the initial page load much faster.

**Note:** The [`contentvisibilityautostatechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event "contentvisibilityautostatechange")
 event fires on any element with `content-visibility: auto` set on it when its rendering work starts or stops being skipped. This provides a convenient way for an app's code to start or stop rendering processes (e.g., drawing on a [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
) when they are not needed, thereby conserving processing power.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#try_it)

----------------------------------------------------------------------------------------------------------

    content-visibility: visible;
    

    content-visibility: hidden;
    

    <section class="default-example" id="default-example">
      <div class="container" id="example-element">
        <div class="child">
          <span>This is an inner div</span>
        </div>
      </div>
    </section>
    

    .container {
      width: 140px;
      height: 140px;
      border: 3px solid rgb(64 28 163);
      background-color: rgb(135 136 184);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    .child {
      border: 3px solid rgb(64 28 163);
      background-color: wheat;
      color: black;
      width: 80%;
      height: 80%;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    content-visibility: visible;
    content-visibility: hidden;
    content-visibility: auto;
    
    /* Global values */
    content-visibility: inherit;
    content-visibility: initial;
    content-visibility: revert;
    content-visibility: revert-layer;
    content-visibility: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#values)

This property is specified as one of the following keyword values:

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#visible)

No effect. The element's contents are laid out and rendered as normal. This is the default value.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#hidden)

The element [skips its contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents)
. The skipped contents must not be accessible to user-agent features, such as find-in-page, tab-order navigation, etc., nor be selectable or focusable. This is similar to giving the contents `display: none`.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#auto)

The element turns on layout containment, style containment, and paint containment. If the element is not [relevant to the user](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#relevant_to_the_user)
, it also skips its contents. Unlike hidden, the skipped contents must still be available as normal to user-agent features such as find-in-page, tab order navigation, etc., and must be focusable and selectable as normal.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#description)

--------------------------------------------------------------------------------------------------------------------

### [Animating and transitioning content-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#animating_and_transitioning_content-visibility)

[Supporting browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#browser_compatibility)
 animate/transition `content-visibility` with a variation on the [discrete animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)
.

Discrete animation generally means that the property will flip between two values 50% of the way through the animation. In the case of `content-visibility`, however, the browser will flip between the two values to show the animated content for the entire animation duration. So, for example:

*   When animating `content-visibility` from `hidden` to `visible`, the value will flip to `visible` at `0%` of the animation duration so it is visible throughout.
*   When animating `content-visibility` from `visible` to `hidden`, the value will flip to `hidden` at `100%` of the animation duration so it is visible throughout.

This behavior is useful for creating entry/exit animations where you want to, for example, remove some content from the DOM with `content-visibility: hidden`, but you want a smooth transition (such as a fade-out) rather than it disappearing immediately.

When animating `content-visibility` with [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
, [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
 needs to be set on `content-visibility`. This effectively enables `content-visibility` transitions.

**Note:** When transitioning an element's `content-visibility` value, you don't need to provide a set of starting values for transitioned properties using a [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
 block, like you do when [transitioning `display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#animating_display)
. This is because `content-visibility` doesn't hide an element from the DOM like `display` does: it just skips rendering the element's content.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `visible` |
| Applies to | elements for which size containment can apply |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Discrete behavior except when animating to or from `hidden` is visible for the entire duration |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

content-visibility =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden     

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#accessibility)

------------------------------------------------------------------------------------------------------------------------

Off-screen content within a `content-visibility: auto` property remains in the document object model and the accessibility tree. This allows improving page performance with `content-visibility: auto` without negatively impacting accessibility.

Since styles for off-screen content are not rendered, elements intentionally hidden with `display: none` or `visibility: hidden` _will still appear in the accessibility tree_. If you don't want an element to appear in the accessibility tree, use `aria-hidden="true"`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#examples)

--------------------------------------------------------------------------------------------------------------

### [Using auto to reduce rendering cost of long pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#using_auto_to_reduce_rendering_cost_of_long_pages)

The following example shows the use of `content-visibility: auto` to skip painting and rendering of off-screen sections. When a `section` is out of the viewport then the painting of the content is skipped until the section comes close to the viewport, this helps with both load and interactions on the page.

#### HTML

html

    <section>
      <!-- Content for each section… -->
    </section>
    <section>
      <!-- Content for each section… -->
    </section>
    <section>
      <!-- Content for each section… -->
    </section>
    <!-- … -->
    

#### CSS

The `contain-intrinsic-size` property adds a default size of 500px to the height and width of each `section` element. After a section is rendered, it will retain its rendered intrinsic size, even when it is scrolled out of the viewport.

css

    section {
      content-visibility: auto;
      contain-intrinsic-size: auto 500px;
    }
    

### [Using hidden to manage visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#using_hidden_to_manage_visibility)

The following example shows how to manage content visibility with JavaScript. Using `content-visibility: hidden;` instead of `display: none;` preserves the rendering state of content when hidden and rendering is faster.

#### HTML

html

    <div class="hidden">
      <button class="toggle">Show</button>
      <p>
        This content is initially hidden and can be shown by clicking the button.
      </p>
    </div>
    <div class="visible">
      <button class="toggle">Hide</button>
      <p>
        This content is initially visible and can be hidden by clicking the button.
      </p>
    </div>
    

#### CSS

The `content-visibility` property is set on paragraphs that are direct children of elements with the `visible` and `hidden` classes. In our example, we can show and hide content in paragraphs depending on the CSS class of parent div elements.

The `contain-intrinsic-size` property is included to represent the content size. This helps to reduce layout shift when content is hidden.

css

    p {
      contain-intrinsic-size: 0 1.1em;
      border: dotted 2px;
    }
    
    .hidden > p {
      content-visibility: hidden;
    }
    
    .visible > p {
      content-visibility: visible;
    }
    

#### JavaScript

js

    const handleClick = (event) => {
      const button = event.target;
      const div = button.parentElement;
      button.textContent = div.classList.contains("visible") ? "Show" : "Hide";
      div.classList.toggle("hidden");
      div.classList.toggle("visible");
    };
    
    document.querySelectorAll("button.toggle").forEach((button) => {
      button.addEventListener("click", handleClick);
    });
    

#### Result

### [Animating content-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#animating_content-visibility)

In this example, we have a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element, the content of which can be toggled between shown and hidden by clicking or pressing any key.

#### HTML

html

    <p>
      Click anywhere on the screen or press any key to toggle the
      <code>&lt;div&gt;</code> content between hidden and showing.
    </p>
    
    <div>
      This is a <code>&lt;div&gt;</code> element that animates between
      <code>content-visibility: hidden;</code>and
      <code>content-visibility: visible;</code>. We've also animated the text color
      to create a smooth animation effect.
    </div>
    

#### CSS

In the CSS we initially set `content-visibility: hidden;` on the `<div>` to hide its content. We then set up `@keyframes` animations and attach them to classes to show and hide the `<div>`, animating `content-visibility` and [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 so that you get a smooth animation effect as the content is shown/hidden.

css

    div {
      font-size: 1.6rem;
      padding: 20px;
      border: 3px solid red;
      border-radius: 20px;
      width: 480px;
    
      content-visibility: hidden;
    }
    
    /* Animation classes */
    
    .show {
      animation: show 0.7s ease-in forwards;
    }
    
    .hide {
      animation: hide 0.7s ease-out forwards;
    }
    
    /* Animation keyframes */
    
    @keyframes show {
      0% {
        content-visibility: hidden;
        color: transparent;
      }
    
      100% {
        content-visibility: visible;
        color: black;
      }
    }
    
    @keyframes hide {
      0% {
        content-visibility: visible;
        color: black;
      }
    
      100% {
        content-visibility: hidden;
        color: transparent;
      }
    }
    

#### JavaScript

Finally, we use JavaScript to apply the `.show` and `.hide` classes to the `<div>` as appropriate to apply the animations as it is toggled between shown and hidden states.

js

    const divElem = document.querySelector("div");
    const htmlElem = document.querySelector(":root");
    
    htmlElem.addEventListener("click", showHide);
    document.addEventListener("keydown", showHide);
    
    function showHide() {
      if (divElem.classList.contains("show")) {
        divElem.classList.remove("show");
        divElem.classList.add("hide");
      } else {
        divElem.classList.remove("hide");
        divElem.classList.add("show");
      }
    }
    

#### Result

The rendered result looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Containment Module Level 2  <br>\# content-visibility](https://drafts.csswg.org/css-contain/#content-visibility) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility#see_also)

--------------------------------------------------------------------------------------------------------------

*   [CSS Containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
    
*   [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
    
*   [`contentvisibilityautostatechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event "contentvisibilityautostatechange")
    
*   [content-visibility: the new CSS property that boosts your rendering performance](https://web.dev/articles/content-visibility "External link (opens in new tab)")
     (web.dev)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/content-visibility/index.md?plain=1 "Folder: en-us/web/css/reference/properties/content-visibility (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontent-visibility&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontent-visibility%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontent-visibility%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontent-visibility%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")