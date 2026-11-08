*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#mdn-search)
    

`::scroll-button()` CSS pseudo-element
======================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/316)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#browser_compatibility)
 carefully before using this in production.

The **`::scroll-button()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents a button for controlling the scrolling of a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. They are generated on scroll containers when their [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 value is not `none`. The direction of the scrolling is determined by the parameter value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#syntax)

------------------------------------------------------------------------------------------------------

css

    ::scroll-button(<scroll-button-direction>) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#parameters)

[`<scroll-button-direction>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#scroll-button-direction)

A value representing which direction of scroll button you want to select. The following values are available:

[`*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#sect)

Selects all the originating element's scroll buttons, allowing styles to be applied to each of them in a single rule.

[`down`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#down)

Selects the button that will scroll the content downward.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#left)

Selects the button that will scroll the content left.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#right)

Selects the button that will scroll the content right.

[`up`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#up)

Selects the button that will scroll the content upward.

[`block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#block-end)

Selects the button that will scroll the content in the block-end direction.

[`block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#block-start)

Selects the button that will scroll the content in the block-start direction.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#inline-end)

Selects the button that will scroll the content in the inline-end direction.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#inline-start)

Selects the button that will scroll the content in the inline-start direction.

The specification also defines two other values — `next` and `prev` — but these are not currently supported in any browser.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#description)

----------------------------------------------------------------------------------------------------------------

The `::scroll-button()` pseudo-elements are generated inside a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 only when their [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 properties are set to a value other than `none`. They are generated as siblings of the scroll container's child DOM elements, immediately preceding them and any [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
 generated on the container.

You can generate up to four scroll buttons per scroll container, which will scroll the content towards the start and end of the block and inline axes. The selector's argument specifies which scrolling direction is selected. You can also specify a value of `*` to target all of the `::scroll-button()` pseudo-elements, providing styles to all the buttons in a single rule.

The generated buttons behave just like regular [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements, including sharing their default browser styles. They are focusable, accessible, and can be activated like regular buttons. When a scroll button is pressed, the scroll container's content is scrolled in the specified direction by one "page," or approximately the dimension of the scroll container, similar to pressing PgUp and PgDn keys.

The recommendation is to set up [CSS scroll snapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
 on the scroll container and set each separate item of content you want to scroll to as a [snap target](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_target)
. This being the case, activating a scroll button will scroll the content to the snap target that is one "page" away. While the scroll buttons will work without scroll snapping, you might not get the desired effect.

When it is not possible to scroll any further in a particular scroll button's scrolling direction, the button is automatically disabled, otherwise it is enabled. You can style the scroll buttons in their enabled and disabled states using the [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
 and [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
 pseudo-classes.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#examples)

----------------------------------------------------------------------------------------------------------

See [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
 for more carousel examples.

### [Creating scroll buttons](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#creating_scroll_buttons)

In this example, we demonstrate how to create scroll buttons on a CSS carousel.

#### HTML

We have a basic HTML [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 list with several [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 list items.

html

    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
      <li>Item 4</li>
      <li>Item 5</li>
      <li>Item 6</li>
      <li>Item 7</li>
      <li>Item 8</li>
    </ul>
    

#### CSS

##### Styling the carousel

We convert our `<ul>` into a carousel by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`, creating a single, non-wrapping row of `<li>` elements. The [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 property is set to `auto`, meaning if the items overflow their container on the x-axis, the content will scroll horizontally. We then convert the `<ul>` into a [scroll-snap container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#scroll_snap_container)
, ensuring that items always snap into place when the container is scrolled with a [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 value of `mandatory`.

css

    ul {
      display: flex;
      gap: 4vw;
      padding-left: 0;
      overflow-x: auto;
      overscroll-behavior-x: contain;
      scroll-snap-type: x mandatory;
    }
    

Next, we style the `<li>` elements, using the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 property to make them 100% of the width of the container. The [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 value of `start` causes the left-hand side of the left-most visible item to snap to the left edge of the container when the content is scrolled.

css

    li {
      list-style-type: none;
      background-color: #eeeeee;
      flex: 0 0 100%;
      height: 100px;
      padding-top: 20px;
      scroll-snap-align: start;
      text-align: center;
    }
    

##### Creating the scroll buttons

First, all scroll buttons are targeted with some rudimentary styles, as well as styling based on different states. It is important to set [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 styles for keyboard users. Also, as scroll buttons are automatically set to [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)
 when no more scrolling can occur in that direction, we use the [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
 pseudo-class to target this state.

css

    ul::scroll-button(*) {
      border: 0;
      font-size: 2rem;
      background: none;
      color: black;
      opacity: 0.7;
      cursor: pointer;
    }
    
    ul::scroll-button(*):hover,
    ul::scroll-button(*):focus {
      opacity: 1;
    }
    
    ul::scroll-button(*):active {
      translate: 1px 1px;
    }
    
    ul::scroll-button(*):disabled {
      opacity: 0.2;
      cursor: unset;
    }
    

**Note:** We also set a [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
 value of `pointer` on the scroll buttons to make it more obvious that they can be interacted with (an improvement for both general [UX](https://developer.mozilla.org/en-US/docs/Glossary/UX)
 and [cognitive accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Cognitive_accessibility)
), unsetting it when the scroll buttons are `:disabled`.

Next, an appropriate icon is set on the left and right scroll buttons via the `content` property, which is also what causes the scroll buttons to be generated:

css

    ul::scroll-button(left) {
      content: "◄";
    }
    
    ul::scroll-button(right) {
      content: "►";
    }
    

We don't need to set [alternative text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#alternative_text_string_counter_attr)
 for the icons on the `content` as the browser takes care of providing appropriate [accessible names](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)
 automatically.

#### Result

Note how the scroll buttons are created at the bottom left on the carousel. Try pressing them to see how they cause the content to be scrolled.

### [Positioning the scroll buttons](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#positioning_the_scroll_buttons)

The previous example works, but the buttons are not ideally placed. In this section, we will add some CSS to position them using [anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
.

#### CSS

First of all, a reference [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 is set on the `<ul>` to define it as a named anchor. Next, each scroll button has its [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 set to `absolute` and its [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property set to the list's `anchor-name`, to [associate the two together](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#associating_anchor_and_positioned_elements)
.

css

    ul {
      anchor-name: --my-carousel;
    }
    
    ul::scroll-button(*) {
      position: absolute;
      position-anchor: --my-carousel;
    }
    

To actually position each scroll button, we first set an [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 value of `anchor-center` on both of them, to center them vertically on the carousel:

css

    ul::scroll-button(*) {
      align-self: anchor-center;
    }
    

We then set values on their [inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 to handle the horizontal positioning. We use [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 functions to position the specified sides of the buttons relative to the sides of the carousel. In each case, the [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 function is used to add some space between the button edge and the carousel edge. For example, the right-hand edge of the left scroll button is positioned 45 pixels to the right of the carousel's left-hand edge.

css

    ul::scroll-button(left) {
      right: calc(anchor(left) - 45px);
    }
    
    ul::scroll-button(right) {
      left: calc(anchor(right) - 45px);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 5  <br>\# scroll-buttons](https://drafts.csswg.org/css-overflow-5/#scroll-buttons) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button#see_also)

----------------------------------------------------------------------------------------------------------

*   [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [CSS Carousel Gallery](https://chrome.dev/carousel/ "External link (opens in new tab)")
     via chrome.dev (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_scroll-button/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_scroll-button (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ascroll-button&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_scroll-button%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ascroll-button%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_scroll-button%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")