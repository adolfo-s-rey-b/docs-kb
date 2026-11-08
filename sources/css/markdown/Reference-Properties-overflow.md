*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#mdn-search)
    

`overflow` CSS property
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the desired behavior when content does not fit in the element's padding box (overflows) in the horizontal and/or vertical direction.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#try_it)

------------------------------------------------------------------------------------------------

    overflow: visible;
    

    overflow: hidden;
    

    overflow: clip;
    

    overflow: scroll;
    

    overflow: auto;
    

    <section class="default-example" id="default-example">
      <p id="example-element">
        Michaelmas term lately over, and the Lord Chancellor sitting in Lincoln's
        Inn Hall. Implacable November weather. As much mud in the streets as if the
        waters had but newly retired from the face of the earth.
      </p>
    </section>
    

    #example-element {
      width: 15em;
      height: 9em;
      border: medium dotted;
      padding: 0.75em;
      text-align: left;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    
*   [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#syntax)

------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    overflow: visible;
    overflow: hidden;
    overflow: clip;
    overflow: scroll;
    overflow: auto;
    
    /* Two-value syntax: horizontal | vertical */
    overflow: hidden visible;
    
    /* Global values */
    overflow: inherit;
    overflow: initial;
    overflow: revert;
    overflow: revert-layer;
    overflow: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#values)

This property is specified as one or two space-separated [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
 keyword values:

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#visible)

Overflow content is not clipped and may be visible outside the element's padding box. The element box is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. This is the default value.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#hidden)

Overflow content is clipped at the element's padding box, hiding the clipped content. When overflowing, the element box is a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 with no scroll bars; scrolling is still possible via other methods including tabbing to hidden focusable elements, properties such as [`scrollLeft`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollLeft "scrollLeft")
 property, and methods like [`scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo "scrollTo()")
.

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#clip)

Overflow content is clipped at the element's _overflow clip edge_ defined by the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property. The element box is not a scroll container, clipped content is not visible, and programmatic scrolling is not supported.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#scroll)

Overflow content is clipped at the element's padding box. Whether overflowing or not, the element box is always a scroll container displaying scroll bars.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#auto)

Overflow content is clipped at the element's padding box. When overflowing, the element box is a scroll container displaying scroll bars.

#### Non-standard values

Some non-standard values are also supported in some browsers:

[`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#overlay)

A legacy alias for `auto`, defined in the specification for web compatibility. Originally implemented as a non-standard value to render scrollbars on top of content rather than taking up space. Its use in new code is discouraged.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#description)

----------------------------------------------------------------------------------------------------------

By default, block-level elements grow to fit their content. If the size of a container is constrained, the content will overflow. The `overflow` property determines how a container handles content that overflows its edges.

The `overflow` property is shorthand for the horizontal [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 and vertical [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 properties. If only one keyword is specified, both `overflow-x` and `overflow-y` are set to the same value. If two keywords are specified, the first value applies to `overflow-x` in the horizontal direction and the second one applies to `overflow-y` in the vertical direction.

Overflow options include hiding overflow content, enabling scroll bars to view overflow content or displaying the content flowing out of an element box into the surrounding area, and combinations there of.

All values, except `visible` and `clip`, create a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
. The new block formatting context is necessary for scroll containers because if a float were to intersect with a scrolling element, it would forcibly rewrap the content after each scroll step, leading to a slow scrolling experience.

### [What creates overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#what_creates_overflow)

Overflow occurs when a block-level element has content that overflows its constrained space. The allotted space may be constrained by a height ([`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 or [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
) for vertical overflow, a width ([`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 or [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
) for horizontal overflow, a block-size ([`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
 or [`max-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
) for block direction overflow, or an inline-size ([`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
, [`max-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
, or [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 set to `nowrap`) for inline direction overflow.

The following CSS limits the size of the container, defining [box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
 property values that limit the container's size. A background color, clipped to the `content-box`, is also added to help demonstrate how overflowing content overflows the content box in the explanations that follow.

css

    div {
      height: 10em;
      width: 15em;
      border: 3px solid;
      padding: 10px;
    
      background-color: #ededed;
      background-clip: content-box;
    }
    

### [Understanding overflow values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#understanding_overflow_values)

The different `overflow` values define whether an element has scrollbars, whether it is user and programmatically scrollable, and whether it is a scroll container (which creates a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
) when that element's contents overflow and, in the case of `scroll`, even when they don't.

#### The `visible` value

The default value is `visible`. By default, if content overflows a container's constraints, the contents are not contained to the container. An element that defaults or is explicitly set to `visible` doesn't have scrollbars, is not user or programmatically scrollable, and is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. This value does not create a new block formatting context.

css

    div {
      overflow: visible;
    }
    

    <div>
      <h2>overflow: visible;</h2>
    </div>
    <div>
      <p>
        The <code>overflow</code> property in this example is set to
        <code>visible</code>. No scroll container is created; the content just
        overflows the container.
      </p>
    </div>
    

With `visible`, no clipping occurs, so the overflowing content is visible outside the element's padding box, potentially overlapping adjacent content.

#### The `scroll` value

With `scroll`, content is clipped at the element's padding box and can be scrolled into view. User agents display scroll bars in both directions, whether or not any content is overflowing, which prevents scroll bars from appearing and disappearing as content changes. Printers may still print overflow content.

The element is always a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 — even when there is no overflowing content — and is both user-scrollable and programmatically scrollable.

css

    div {
      overflow: scroll;
    }
    

    <div>
      <h2>overflow: scroll;</h2>
    </div>
    <div>
      <p>
        The <code>overflow</code> property in this example is set to
        <code>scroll</code>. A scroll container is created; a scrollbar is always
        visible, even if not needed.
      </p>
    </div>
    

In the first example, even though the content is not overflowing, a scroll container is still created. In the second example, the content is clipped to the padding box, with a scroll bar enabling scrolling to the overflowing content.

#### The `auto` value

With `auto`, whether the element has scrollbars and is a scroll container depends on whether the element has overflowing content. When the element contains overflowing content, it behaves like `scroll`: the overflowing content is clipped at the element's padding box, and overflow content can be scrolled into view using scroll bars. Unlike `scroll`, user agents display scroll bars _only if_ the content is overflowing. If content fits inside the element's padding box, it looks the same as with `visible`, but still establishes a new formatting context. The element box is a scroll container only when there is overflowing content.

css

    div {
      overflow: auto;
    }
    

    <div>
      <h2>overflow: auto;</h2>
    </div>
    <div>
      <p>
        The <code>overflow</code> property in this example is set to
        <code>auto</code>. Because there is overflowing content, a scroll container
        is created. The content is clipped to the padding box and a scroll bar
        enables scrolling to the overflowing content.
      </p>
    </div>
    

When using the two value syntax, if one value is set to `visible`, that `visible` overflow direction will behave as `auto` if the other value is not `visible` or `clip`.

#### The `hidden` value

With `hidden`, overflowing content is clipped at the element's padding box. There are no scroll bars and the clipped content is not visible (i.e., it's "hidden").

If there is overflowing content, the element is a scroll container. While there are no scroll bars and the user cannot view the content outside the clipped region by actions such as dragging on a touch screen or using the scroll wheel on a mouse, the hidden overflow content can be scrolled into view.

If the content contains focusable elements, tabbing brings the currently focused element into view. Content can also be scrolled to programmatically. Setting a value for the [`scrollLeft`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollLeft "scrollLeft")
 or [`scrollTop`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop "scrollTop")
 property scrolls that distance from the left or top edge, respectively. You can also scroll using the [`scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo "scrollTo()")
 method.

css

    div {
      overflow: hidden;
    }
    

    <div>
      <h2>overflow: hidden;</h2>
    </div>
    <div>
      <p>
        The <code>overflow</code> property in this example is set to
        <code>hidden</code>. While hidden,
        <a
          href="https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content"
          >interactive content</a
        >
        can be scrolled into view when focused. Because content overflows, the
        element is a scroll container, even though no scroll bars are present.
        Tabbing will give this
        <input aria-label="input" placeholder="input" /> focus and scroll it into
        view. This content is also programmatically scrollable.
      </p>
    </div>
    

The first example does not have overflowing content and is not a scroll container. The second example has overflowing content that is clipped to the padding box. Even though there is no scroll bar enabling scrolling to the overflowing content, the content can be scrolled into view, such as by tabbing to the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 in the hidden content. The second example is a scroll container.

#### The `clip` value

With `clip`, content that overflows is by default hidden, there are no scroll bars, and programmatic scrolling is not possible. The element is not a scroll container and no new [formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 is created. If the clipped content includes interactive content, hidden focusable content still receives keyboard focus, but that content will not scroll into view, making it inaccessible to keyboard users.

With `clip`, overflow content is clipped at the element's _overflow clip edge_ that is defined using the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property. The clipped content overflows the element's padding box by the [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value of `overflow-clip-margin`, which defaults to `0px`.

css

    div {
      overflow: clip;
    }
    

    <div>
      <h2>overflow: clip;</h2>
    </div>
    <div>
      <p>
        The <code>overflow</code> property in this example is set to
        <code>clip</code>. When hidden,
        <a
          href="https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content"
          >interactive content</a
        >
        can NOT be scrolled into view when focused. Overflowing content is clipped
        to the container. No scroll container is created. Tabbing will give this
        <input aria-label="input" placeholder="input" /> focus but will not scroll
        it into view. Keyboard users will not be able to reach this content. This
        content is also not programmatically scrollable.
      </p>
    </div>
    <fieldset>
      <legend>Select a <code>overflow-clip-margin</code> value</legend>
      <ul>
        <li>
          <label
            ><input type="radio" name="overflow" value="0" /> overflow-clip-margin:
            0;</label
          >
        </li>
        <li>
          <label
            ><input type="radio" name="overflow" value="3em" />
            overflow-clip-margin: 3em;</label
          >
        </li>
      </ul>
    </fieldset>
    

The second example's overflowing content is clipped. Tabbing to the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 in the hidden content gives the element focus, but does not scroll it into view, making that content inaccessible to keyboard users.

When using the two value syntax, if one value is set to `clip`, that `clip` overflow direction will behave as `hidden` if the other value is not set to `visible` or `clip`.

    ul {
      list-style-type: none;
    }
    label {
      font-family: monospace;
    }
    :has([value="0"]:checked) div {
      overflow-clip-margin: 0;
    }
    :has([value="3em"]:checked) div {
      overflow-clip-margin: 3em;
    }
    
    @supports not (overflow-clip-margin: 0) {
      body::before {
        content: "Your browser doesn't support overflow-clip-margin yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
    
        width: 100%;
      }
    }
    

#### With scroll-driven animations

When creating [scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
 using the [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 function, consider using `clip` instead of `hidden` if there is no interactive content within the clipped area, unless you explicitly want to create a scroll container.

With both `hidden` and `clip`, the overflow gets clipped, but `overflow: clip` doesn't create a scroll container, so clipped elements are skipped when the user agent goes up the DOM tree looking for the nearest ancestor scroll container.

Because `overflow: hidden` creates a scroll container when there is overflowing content, you might accidentally create a scrolling-ancestor that doesn't scroll. But only use `clip` if you are certain you won't clip any interactive content.

    div {
      height: 10em;
      width: 15em;
      border: 3px solid;
      padding: 10px;
      background-color: #ededed;
      background-clip: content-box;
    }
    p {
      font-size: 1.5rem;
      line-height: 1.6;
      font-family: sans-serif;
    }
    h2 {
      font-family: monospace;
    }
    body {
      height: 98vh;
      overflow: clip;
      display: flex;
      flex-flow: row wrap;
      gap: 3em;
    }
    

### [Overflowing replaced elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#overflowing_replaced_elements)

Setting `overflow` on images and other [replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
 works as expected in browsers that support CSS Overflow Module Level 4; in previous versions of the specification, replaced elements were always clipped to the bounding container.

See the [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#browser_compatibility)
 chart for current browser support information.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `visible` |
| Applies to | Block-containers, flex containers, and grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br>    : as specified, except with `visible`/`clip` computing to `auto`/`hidden` respectively if one of [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br>     or [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br>     is neither `visible` nor clip<br>*   [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br>    : as specified, except with `visible`/`clip` computing to `auto`/`hidden` respectively if one of [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br>     or [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br>     is neither `visible` nor clip |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#formal_syntax)

--------------------------------------------------------------------------------------------------------------

overflow =   
  [<'overflow-block'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<overflow-block>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
 =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  clip     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto       

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#accessibility)

--------------------------------------------------------------------------------------------------------------

In some browsers, scrolling content areas are not keyboard-focusable, so they cannot be scrolled by a keyboard-only user. To ensure all keyboard-only users can scroll the container, enable the element to receive focus by setting [`tabindex="0"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
 on the container. To give screen reader users context when the container receives focus, set an appropriate [WAI-ARIA role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles)
 on the container, such as `role="region"`, and an accessible name using the [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 or [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
 attribute.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#examples)

----------------------------------------------------------------------------------------------------

### [Demonstrating results of various overflow keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#demonstrating_results_of_various_overflow_keywords)

#### HTML

html

    <div>
      <code>visible</code>
      <p class="visible">
        Maya Angelou: "I've learned that people will forget what you said, people
        will forget what you did, but people will never forget how you made them
        feel."
      </p>
    </div>
    
    <div>
      <code>hidden</code>
      <p class="hidden">
        Maya Angelou: "I've learned that people will forget what you said, people
        will forget what you did, but people will never forget how you made them
        feel."
      </p>
    </div>
    
    <div>
      <code>clip</code>
      <p class="clip">
        Maya Angelou: "I've learned that people will forget what you said, people
        will forget what you did, but people will never forget how you made them
        feel."
      </p>
    </div>
    
    <div>
      <code>scroll</code>
      <p class="scroll">
        Maya Angelou: "I've learned that people will forget what you said, people
        will forget what you did, but people will never forget how you made them
        feel."
      </p>
    </div>
    
    <div>
      <code>auto</code>
      <p class="auto">
        Maya Angelou: "I've learned that people will forget what you said, people
        will forget what you did, but people will never forget how you made them
        feel."
      </p>
    </div>
    

#### CSS

    body {
      display: flex;
      flex-wrap: wrap;
      justify-content: start;
    }
    
    div {
      margin: 2em;
      font-size: 1.2em;
    }
    
    p {
      width: 5em;
      height: 5em;
      border: dotted;
      margin-top: 0.5em;
    }
    
    div:nth-of-type(5),
    div:nth-of-type(6) {
      margin-top: 200px;
    }
    

css

    p.visible {
      overflow: visible;
    }
    
    p.hidden {
      overflow: hidden;
    }
    
    p.clip {
      overflow: clip;
      overflow-clip-margin: 1em;
    }
    
    p.scroll {
      overflow: scroll;
    }
    
    p.auto {
      overflow: auto;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# propdef-overflow](https://drafts.csswg.org/css-overflow/#propdef-overflow) |
| [Scalable Vector Graphics (SVG) 2  <br>\# OverflowAndClipProperties](https://w3c.github.io/svgwg/svg2-draft/render.html#OverflowAndClipProperties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#see_also)

----------------------------------------------------------------------------------------------------

*   [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    , [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    
*   [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
    , [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
    , [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
    
*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    , [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    , [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   SVG [`overflow`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/overflow)
     attribute
*   [Scroll progress timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [Keyboard-only scrolling areas](https://adrianroselli.com/2022/06/keyboard-only-scrolling-areas.html "External link (opens in new tab)")
     on adrianroselli.com (2022)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")