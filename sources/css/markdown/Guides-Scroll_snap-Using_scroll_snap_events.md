*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#mdn-search)
    

Using scroll snap events
========================

The [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
 module defines two **scroll snap events**: [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
 and [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
. These enable running JavaScript in response to the browser determining that new [scroll snap targets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts)
 are pending and selected, respectively.

This guide provides an overview of these events, along with complete examples.

[Events overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#events_overview)

--------------------------------------------------------------------------------------------------------------------------------

Scroll snap events are set on a [scrolling container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 that contains potential scroll snap targets:

*   The [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
     event is fired when the browser determines that a new scroll snap target will be selected when the current scroll gesture ends. This is the _pending_ scroll snap target. Specifically, this event fires during a scrolling gesture, each time the user moves over potential new snap targets. While the `scrollsnapchanging` event may fire multiple times for each scrolling gesture, it does not fire on all potential snap targets for a scrolling gesture that moves over multiple snap targets. Rather, it fires just for the last target that the snapping will potentially rest on.
    
*   The [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
     event is fired at the end of a scrolling operation when a new scroll snap target is selected. Specifically, this event fires when a scrolling gesture is completed, but only if a new snap target is selected. This event fires just before the [`scrollend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollend_event "scrollend")
     event fires.
    

Let's look at an example that shows the two events in action (you'll see how this is built later on in the article):

Have a go at scrolling up and down the list of boxes:

*   Try slowly scrolling the container up and down without releasing the scrolling gesture. For example, drag your finger(s) over the scrolling area on a touchscreen device or trackpad, or hold down the mouse button on the scroll bar and move the mouse. The boxes you move over should turn a darker gray color as you move over them, and then return to normal as you move away from them again. This is the `scrollsnapchanging` event in action.
*   Now try releasing the scrolling gesture; the nearest box to your scrolling position should animate to a purple color, with white text. The animation occurs when the `scrollsnapchange` event fires.
*   Finally, try scrolling fast. For example, flick your finger hard on the screen, to scroll past several potential targets before starting to come to rest near a target further down the scroll container. You should only see one `scrollsnapchanging` event fire as the scrolling starts to slow, before the `scrollsnapchange` event fires and the selected snap target turns purple.

[The `SnapEvent` event object](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#the_snapevent_event_object)

--------------------------------------------------------------------------------------------------------------------------------------------------------

Both of the above events share the [`SnapEvent`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent)
 event object. This has two properties that are key to how scroll snap events work:

*   [`snapTargetBlock`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetBlock "snapTargetBlock")
     returns a reference to the element snapped to in the [block direction](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values#block_direction)
     when the event fired, or `null` if scroll snapping only occurs in the inline direction so no element is snapped to in the block direction.
*   [`snapTargetInline`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetInline "snapTargetInline")
     returns a reference to the element snapped to in the [inline direction](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values#inline_direction)
     when the event fired, or `null` if scroll snapping only occurs in the block direction so no element is snapped to in the inline direction.

These properties enable event handler functions to report the element that has been snapped to (in the case of `scrollsnapchange`) or the element that _would be snapped to_ if the scrolling gesture were to be finished now (in the case of `scrollsnapchanging`) — in one- and two-dimensions. You can then manipulate these elements in any way you want, for example by directly setting styles on them via their [`style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style "style")
 properties, setting classes on them that have styles defined for them in a stylesheet, etc.

### [Relationship with CSS `scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#relationship_with_css_scroll-snap-type)

The property values available on `SnapEvent` correspond directly to the value of the [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 CSS property set on the scroll container:

*   If the snap axis is specified as `block` (or a physical axis value that equates to `block` in the current writing mode), only `snapTargetBlock` returns an element reference.
*   If the snap axis is specified as `inline` (or a physical axis value that equates to `inline` in the current writing mode), only `snapTargetInline` returns an element reference.
*   If the snap axis is specified as `both`, `snapTargetBlock` and `snapTargetInline` return an element reference.

### [Handling one-dimensional scrollers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#handling_one-dimensional_scrollers)

If you are dealing with a horizontal scroller, only the event object's `snapTargetInline` property will change as the snapped element changes if the content has a horizontal [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, or the `snapTargetBlock` property if the content has a vertical `writing-mode`.

Conversely, if you are dealing with a vertical scroller, only the `snapTargetBlock` property will change as the snapped element changes if the content has a horizontal `writing-mode`, or the `snapTargetInline` property if the content has a vertical `writing-mode`.

In both cases, the non-changing property of the two returns `null`.

Let's look at an example snippet to show a typical one-dimensional scroll snap event handler function:

js

    scrollingElem.addEventListener("scrollsnapchange", (event) => {
      event.snapTargetBlock.className = "select-section";
    });
    

In this snippet, a `scrollsnapchange` handler function is set on a block-direction scrolling container element that snap targets appear inside. When the event fires, we set a `select-section` class on the `snapTargetBlock` element, which could be used to style a newly-selected snap target to look like it has been selected (for example, with an animation).

### [Handling two-dimensional scrollers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#handling_two-dimensional_scrollers)

If you are dealing with a horizontal _and_ vertical scroller, the code gets more complex. This is because the `snapTargetBlock` property _and_ the `snapTargetInline` property values both return an element reference (neither returns `null`), and one or the other will change value depending on which direction you scroll in and the `writing-mode` of the content:

*   If the scroller is scrolled horizontally, the `snapTargetInline` property will change as the snapped element changes if the content has a horizontal [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , or the `snapTargetBlock` property if the content has a vertical `writing-mode`.
*   If the scroller is scrolled vertically, the `snapTargetBlock` property will change as the snapped element changes if the content has a horizontal `writing-mode`, or the `snapTargetInline` property if the content has a vertical `writing-mode`.

To handle this, you will likely need to keep track of whether it was the `snapTargetBlock` or the `snapTargetInline` element that changed. Let's look at an example:

js

    const prevState = {
      snapTargetInline: "s1",
      snapTargetBlock: "s1",
    };
    
    scrollingElem.addEventListener("scrollsnapchange", (event) => {
      if (!(prevState.snapTargetBlock === event.snapTargetBlock.id)) {
        console.log(
          `The container was scrolled in the block direction to element ${event.snapTargetBlock.id}`,
        );
      }
    
      if (!(prevState.snapTargetInline === event.snapTargetInline.id)) {
        console.log(
          `The container was scrolled in the block direction to element ${event.snapTargetBlock.id}`,
        );
      }
    
      prevState.snapTargetBlock = event.snapTargetBlock.id;
      prevState.snapTargetInline = event.snapTargetInline.id;
    });
    

In this snippet, we first define an object (`prevState`) that stores the ID of the previous `snapTargetBlock` and `snapTargetInline` elements.

In the event handler function, we use `if` statements to test whether:

*   The `prevState.snapTargetBlock` ID is equal to the ID of the current `event.snapTargetBlock` element.
*   The `prevState.snapTargetInline` ID is equal to the ID of the current `event.snapTargetInline` element.

If the values are different, it means that the scroller has been scrolled in that direction (block or inline), and we log a message to console to indicate this. In a real example, you'd likely style the snapped element in some way to indicate that it has been snapped to.

We then update the values of `prevState.snapTargetBlock` and `prevState.snapTargetInline` ready for when the event handler next runs.

For the remainder of this article, we'll look at a couple of complete scroll snap event examples, which you can play with in the live rendered versions at the end of each section.

[One-dimensional scroller example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#one-dimensional_scroller_example)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

This example features a vertically-scrolling [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 element containing multiple light gray [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements, which are all scroll snap targets. When a new snap target is pending, it will turn a darker shade of gray. When a new snap target is selected, it will smoothly animate to purple with white text. If a different snap target was previously selected, it will smoothly animate back to gray with black text.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#html)

The HTML for the example is a single `<main>` element. We will add the `<section>` elements dynamically with JavaScript later on, to save on page space.

html

    <main></main>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#css)

    * {
      box-sizing: border-box;
    }
    
    html {
      height: 100%;
    }
    
    body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: inherit;
    }
    
    h2 {
      font-size: 1rem;
      letter-spacing: 1px;
    }
    
    section {
      font-family: "Helvetica", "Arial", sans-serif;
      border-radius: 5px;
      background: #eeeeee;
      box-shadow:
        inset 1px 1px 4px rgb(255 255 255 / 0.5),
        inset -1px -1px 4px rgb(0 0 0 / 0.5);
      width: 150px;
      height: 150px;
    
      display: flex;
      align-items: center;
      justify-content: center;
    }
    

In the CSS, we start off by giving the `<main>` element a chunky black [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 and a fixed [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
. We set its [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 value to `scroll` so overflowing content will be hidden and can be scrolled to, and set [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 to `block mandatory` so that snap targets in the block direction only will always be snapped to.

css

    main {
      border: 3px solid black;
      width: 250px;
      height: 450px;
      overflow: scroll;
      scroll-snap-type: block mandatory;
    }
    

Each `<section>` element is given a [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 of `50px` to separate out the `<section>` elements and make the scroll snapping behavior more apparent. We then set [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 to `center`, to specify that we want to snap to the center of each snap target. Finally, we apply a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 to smoothly animate to and from the style changes applied when a snap target selection has been made or is pending.

css

    section {
      margin: 50px auto;
      scroll-snap-align: center;
      transition: 0.5s ease;
    }
    

The style changes mentioned above will be applied through classes applied to the `<section>` elements via JavaScript. The `select-section` class will be applied to signify a selection — this set a purple background and white text color. The `pending` class will be applied to signify a pending snap target selection — this colors the target selection's background a darker gray.

css

    .pending {
      background-color: #cccccc;
    }
    
    .select-section {
      background: purple;
      color: white;
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#javascript)

In the JavaScript, we start by grabbing a reference to the `<main>` element and defining the number of `<section>` elements to generate (in this case, 21) and a variable to begin counting from. We then use a [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 loop to generate the `<section>` elements, giving each one a child [`h2`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 with text that reads `Section` plus the current value of `n`.

js

    const mainElem = document.querySelector("main");
    const sectionCount = 21;
    let n = 1;
    
    while (n <= sectionCount) {
      mainElem.innerHTML += `
        <section>
          <h2>Section ${n}</h2>
        </section>
      `;
      n++;
    }
    

Now on to the [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
 event handler function. When a child of the `<main>` element (i.e., any `<section>` element) becomes a pending snap target selection, we:

1.  Check to see if an element previously had the `pending` class applied and, if so, remove it. This is so that only the current pending target is given the `pending` class and colored darker gray. We don't want previously-pending targets that are no longer pending to keep the styling.
2.  Give the element referenced by the [`snapTargetBlock`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetBlock "snapTargetBlock")
     property (which will be one of the `<section>` elements) the `pending` class so it turns a darker gray.

js

    mainElem.addEventListener("scrollsnapchanging", (event) => {
      const previousPending = document.querySelector(".pending");
      if (previousPending) {
        previousPending.classList.remove("pending");
      }
    
      event.snapTargetBlock.classList.add("pending");
    });
    

**Note:** We don't need to worry about the `snapTargetInline` event object property for this demo — we are only scrolling vertically and the demo is using a horizontal writing mode, therefore only the `snapTargetBlock` value will change. In this case, `snapTargetInline` will always return `null`.

When a scrolling gesture ends, and a `<section>` element is actually selected as a snap target, the [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
 event handler function fires. This:

1.  Checks to see if a snap target was previously selected — i.e., if a `select-section` class was previously applied to an element. If so, we remove it.
2.  Applies the `select-section` class to the `<section>` element referenced in the `snapTargetBlock` property so that the snap target that was just selected will have the selection animation applied to it.

js

    mainElem.addEventListener("scrollsnapchange", (event) => {
      const currentlySnapped = document.querySelector(".select-section");
      if (currentlySnapped) {
        currentlySnapped.classList.remove("select-section");
      }
    
      event.snapTargetBlock.classList.add("select-section");
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#result)

Try scrolling up and down the scroll container and observing the behavior described above:

[Two-dimensional scroller example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#two-dimensional_scroller_example)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

This example is similar to the previous one, except that it features a horizontally- _and_ vertically-scrolling [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 element containing multiple light gray [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements, which are all snap targets.

The HTML for the example is the same as for the previous example — a single `<main>` element.

    <main></main>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#css_2)

    * {
      box-sizing: border-box;
    }
    
    html {
      height: 100%;
    }
    
    body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: inherit;
    }
    
    section {
      font-family: "Helvetica", "Arial", sans-serif;
      border-radius: 5px;
      background: #eeeeee;
      box-shadow:
        inset 1px 1px 4px rgb(255 255 255 / 0.5),
        inset -1px -1px 4px rgb(0 0 0 / 0.5);
      width: 150px;
      height: 150px;
    
      display: flex;
      align-items: center;
      justify-content: center;
    
      scroll-snap-align: center;
    }
    
    h2 {
      font-size: 1rem;
      letter-spacing: 1px;
    }
    

The CSS for this example is similar to the CSS in the previous example. The most significant differences are as follows.

First let's look at the `<main>` element styling. We want the `<section>` elements to be laid out as a grid, so we use [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 to specify that we want them displayed in seven columns, using a [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 value of `repeat(7, 1fr)`. We also specify the space around the `<section>` elements by setting `padding` and [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 on the `<main>` element rather than `margin` on the `<section>` elements.

Finally, since we are scrolling in both directions in this example, we set [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 to `both mandatory` so that snap targets in the block direction _and_ inline direction will always be snapped to.

css

    main {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      padding: 100px;
      gap: 50px;
      overflow: scroll;
      border: 3px solid black;
      width: 350px;
      height: 350px;
    
      scroll-snap-type: both mandatory;
    }
    

Next, we are going to use CSS animations in this example instead of transitions. This results in more complex code, but enables more fine-grained control over the animations applied.

We first define the classes that will be applied to signal that a snap target selection has been made or is pending. The `select-section` and `deselect-section` classes will apply keyframe animations to signify a selection or deselection. The `pending` class will be applied to signify a pending snap target selection (it applies a darker gray background to the selection, as in the previous example).

The [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animate from a gray background and black (default) text color to a purple background and white text color, and back again, respectively. The latter animation is somewhat different from the first one — it also uses [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 to create a fade out/fade in effect.

css

    .select-section {
      animation: select 0.8s ease forwards;
    }
    
    .deselect-section {
      animation: deselect 0.8s ease forwards;
    }
    
    .pending {
      background-color: #cccccc;
    }
    
    @keyframes select {
      from {
        background: #eeeeee;
        color: black;
      }
    
      to {
        background: purple;
        color: white;
      }
    }
    
    @keyframes deselect {
      0% {
        background: purple;
        color: white;
        opacity: 1;
      }
    
      80% {
        background: #eeeeee;
        color: black;
        opacity: 0.1;
      }
    
      100% {
        background: #eeeeee;
        color: black;
        opacity: 1;
      }
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#javascript_2)

In the JavaScript, we start off in the same way as with the previous example, except that this time we generate 49 `<section>` elements, and we give each one an ID of `s` plus the current value of `n` to help track them later on. With the CSS grid layout we specified above, we have seven columns of seven `<section>` elements.

js

    const mainElem = document.querySelector("main");
    const sectionCount = 49;
    let n = 1;
    
    while (n <= sectionCount) {
      mainElem.innerHTML += `
        <section id="s${n}">
          <h2>Section ${n}</h2>
        </section>
      `;
      n++;
    }
    

Next we specify an object called `prevState`, which allows us to keep track of the previously-selected snap target at any point — its properties store the previous inline and block snap targets' IDs. This is important for figuring out if we need to style the new block target or the new inline target each time an event handler fires.

js

    const prevState = {
      snapTargetInline: "s1",
      snapTargetBlock: "s1",
    };
    

For example, let's say the scroll container is scrolled so that the ID of the new [`SnapEvent.snapTargetBlock`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetBlock)
 element has changed (it doesn't equal the ID stored in `prevState.snapTargetBlock`), but the ID of the new [`SnapEvent.snapTargetInline`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetInline)
 element is still the same as the ID stored in `prevState.snapTargetInline`. This means that we've moved to a new snap target in the block direction, so we should style `SnapEvent.snapTargetBlock`, but we've not moved to a new snap target in the inline direction, so we shouldn't style `SnapEvent.snapTargetInline`.

This time around, we'll explain the [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
 event handler function first. In this function, we:

1.  Start by making sure that a previously-selected `<section>` element snap target (as signified by the presence of the `select-section` class) has the `deselect-section` class applied so it shows the deselection animation. If no snap target was previously selected, we apply the `select-section` class to the first `<section>` in the DOM so it shows up as selected when the page first loads.
2.  Compare the previously-selected snap target ID to the newly-selected snap target ID, for both the block _and_ inline selections. If they are different, it indicates that the selection has changed, so we apply the `select-section` class to the appropriate snap target to visually indicate this.
3.  Update `prevState.snapTargetBlock` and `prevState.snapTargetInline` to be equal to the IDs of the scroll snap targets that were just selected, so that when the event next fires, they will be the previous selections.

js

    mainElem.addEventListener("scrollsnapchange", (event) => {
      if (document.querySelector(".select-section")) {
        document.querySelector(".select-section").className = "deselect-section";
      } else {
        document.querySelector("section").className = "select-section";
      }
    
      if (!(prevState.snapTargetBlock === event.snapTargetBlock.id)) {
        event.snapTargetBlock.className = "select-section";
      }
    
      if (!(prevState.snapTargetInline === event.snapTargetInline.id)) {
        event.snapTargetInline.className = "select-section";
      }
    
      prevState.snapTargetBlock = event.snapTargetBlock.id;
      prevState.snapTargetInline = event.snapTargetInline.id;
    });
    

When the [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
 event handler function fires, we:

1.  Remove the `pending` class from the element that previously had it applied so that only the current pending target is given the `pending` class and colored darker gray.
2.  Give the current pending element the `pending` class so it turns a darker gray, but only if it has not already got the `select-section` class applied — we want a previously selected target to keep the purple selection styling until a new target is actually selected. We also include an extra check in the `if` statements to make sure we style only the inline or block pending snap target, depending on which one has changed. Again, we compare the previous snap target to the current snap target in each case.

js

    mainElem.addEventListener("scrollsnapchanging", (event) => {
      const previousPending = document.querySelector(".pending");
      if (previousPending) {
        previousPending.className = "";
      }
    
      if (
        !(event.snapTargetBlock.className === "select-section") &&
        !(prevState.snapTargetBlock === event.snapTargetBlock.id)
      ) {
        event.snapTargetBlock.className = "pending";
      }
    
      if (
        !(event.snapTargetInline.className === "select-section") &&
        !(prevState.snapTargetInline === event.snapTargetInline.id)
      ) {
        event.snapTargetInline.className = "pending";
      }
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#result_2)

Try scrolling horizontally and vertically around the scroll container and observing the behavior described above:

[Scroll snap events on `Document` and `Window`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#scroll_snap_events_on_document_and_window)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this article, we've covered the scroll snap events that fire on the [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
 interface, but the same events also fire on the [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document)
 and [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 objects. See:

*   `Document` [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Document/scrollsnapchange_event "scrollsnapchange")
     and [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Document/scrollsnapchanging_event "scrollsnapchanging")
     event references.
*   `Window` [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollsnapchange_event "scrollsnapchange")
     and [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollsnapchanging_event "scrollsnapchanging")
     event references.

These work in much the same way as the `Element` versions, except that the overall HTML document has to be set as the scroll snap container (i.e., [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 is set on the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 element).

For example, if we took a similar example to the ones we've looked at above, where we've got a `<main>` element containing significant content:

html

    <main>
      <!-- Significant content -->
    </main>
    

The `<main>` element could be turned into a scroll container using a combination of CSS properties, for example:

css

    main {
      width: 250px;
      height: 450px;
      overflow: scroll;
    }
    

You could then implement scroll snapping behavior on the scrolling content by specifying the [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 property on the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 element:

css

    html {
      scroll-snap-type: block mandatory;
    }
    

The following JavaScript snippet would cause the `scrollsnapchange` event to fire on the HTML document when a child of the `<main>` element becomes a newly-selected snap target. In the handler function, we set a `selected` class on the child referenced by the [`SnapEvent.snapTargetBlock`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent/snapTargetBlock)
, which could be used to style it to look like it has been selected (for example, with an animation) when the event fires.

js

    document.addEventListener("scrollsnapchange", (event) => {
      event.snapTargetBlock.classList.add("selected");
    });
    

We could fire the event on `Window` instead, to achieve the same functionality:

js

    window.addEventListener("scrollsnapchange", (event) => {
      event.snapTargetBlock.classList.add("selected");
    });
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event "scrollsnapchanging")
     event
*   [`scrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event "scrollsnapchange")
     event
*   [`SnapEvent`](https://developer.mozilla.org/en-US/docs/Web/API/SnapEvent)
    
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Scroll Snap Events](https://developer.chrome.com/blog/scroll-snap-events "External link (opens in new tab)")
     on developer.chrome.com (2024)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/scroll_snap/using_scroll_snap_events/index.md?plain=1 "Folder: en-us/web/css/guides/scroll_snap/using_scroll_snap_events (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_snap%2FUsing_scroll_snap_events&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fscroll_snap%2Fusing_scroll_snap_events%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FScroll_snap%2FUsing_scroll_snap_events%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fscroll_snap%2Fusing_scroll_snap_events%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")