*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#mdn-search)
    

`interactivity` CSS property
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/305)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#browser_compatibility)
 carefully before using this in production.

The **`interactivity`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether an element and its descendant nodes are set to be [inert](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    interactivity: auto;
    interactivity: inert;
    
    /* Global values */
    interactivity: inherit;
    interactivity: initial;
    interactivity: revert;
    interactivity: revert-layer;
    interactivity: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#auto)

Selected elements are in their default state in terms of inertness. This usually means that they are interactive, but this is [not always the case](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#default_inertness)
. This is the default value.

[`inert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#inert)

Selected elements and their descendants are inert.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

interactivity =   
  auto   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inert    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#description)

---------------------------------------------------------------------------------------------------------------

The `interactivity` property can be used to set whether an element and its descendants are inert. See the HTML [`inert`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert)
 attribute reference page for a detailed description of the inert state.

A typical use case for `interactivity: inert` is in paginated content, like carousels, when you only want the currently-visible page's content and controls to be interacted with. In such cases, unexpectedly focusing on an off-screen link or button could spoil the experience.

If an element's inert state is specified both by HTML (the `inert` attribute, or an automatic browser setting) and CSS (the `interactive` property) at the same time, the CSS will have no effect — it cannot override the HTML's inertness.

For example, the following HTML element will be inert:

html

    <button inert>You can't press me</button>
    

Setting `interactive: auto` on it will have no effect.

### [Default inertness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#default_inertness)

Most elements are interactive by default, but this is not always the case:

*   An element's ancestor may be set to an inert state, via the `interactive` property or the `inert` attribute.
*   While a modal [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     is displayed, the rest of the page is set to an inert state automatically.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#examples)

---------------------------------------------------------------------------------------------------------

### [Basic `interactivity` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#basic_interactivity_usage)

In this example we have two [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements. The second one has `interactivity: inert` set on it via a class, and therefore is not focusable or editable in supporting browsers.

html

    <p>
      <label>
        This input is interactive:
        <input type="text" name="one" value="editable" />
      </label>
    </p>
    <p>
      <label>
        This input is not interactive:
        <input type="text" name="two" value="Not editable" class="inert" />
      </label>
    </p>
    

css

    .inert {
      interactivity: inert;
      background-color: lightpink;
    }
    

#### Result

The output looks like this:

### [Exploring the effects of inertness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#exploring_the_effects_of_inertness)

In this example we explore the effects of the `interactivity` property.

#### HTML

The markup features two [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements, each of which contain a link. The second paragraph also has a class of `inert` set on it, and a child [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element with [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 set on it to make it editable.

html

    <p>
      This paragraph is not
      <a
        href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert"
        >inert</a
      >. You should be able to select the text content, search for it using
      in-browser search features, and focus and click the link. There is a
      <code>click</code> event handler set on the paragraph that changes the border
      color for a second when it is clicked anywhere.
      <span contenteditable>This sentence has <code>contenteditable</code> set on
      it, so it is editable</span>.
    </p>
    
    <p class="inert">
      This paragraph is
      <a
        href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert"
        >inert</a
      >. You won't be able to select the text content, search for it using
      in-browser search features, focus and click the link, or issue
      <code>click</code> events on it (the border color won't change when it is
      clicked).
      <span contenteditable
        >This sentence has <code>contenteditable</code> set on it, but it is not
        editable because it is inert</span
      >.
    </p>
    

#### CSS

We set the `interactivity` property on the second paragraph to a value of `inert`, making it inert. This means that you should be able to edit the `contenteditable` text in the first paragraph, but not in the second, and you shouldn't be able to search for text, select text, or interact with the link within the second paragraph.

css

    .inert {
      interactivity: inert;
    }
    
    [contenteditable] {
      outline: 1px dashed lightblue;
    }
    
    .borderChanged {
      border-color: orange;
    }
    

    body {
      font: 1.2em / 1.5 system-ui;
    }
    
    p {
      border: 5px solid black;
      padding: 10px;
      width: 90%;
      margin: 20px auto;
    }
    

#### JavaScript

We set an event handler on each paragraph that toggles a class name when clicked, adding the classname then removing the class after two seconds.

js

    const paras = document.querySelectorAll("p");
    
    function tempBorderChange(e) {
      const targetPara = e.currentTarget;
      targetPara.classList.add("borderChanged");
      setTimeout(() => {
        targetPara.classList.remove("borderChanged");
      }, 2000);
    }
    
    for (para of paras) {
      para.addEventListener("click", tempBorderChange);
    }
    

#### Result

Note how the second paragraph is inert; it therefore does not behave like the first paragraph. For example, the link cannot be clicked or focused, the text cannot be selected or searched, the `contenteditable` `<span>` is not editable, and `click` events do not register on it.

### [Setting off-screen elements to inert using a view timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#setting_off-screen_elements_to_inert_using_a_view_timeline)

This example shows horizontally-scrolling paginated content, with each page snapped to using [CSS Scroll Snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
, and the inertness controlled via a [scroll-driven animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
 that uses a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
. Content displayed in the [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 is interactive; it becomes inert when it moves out into the overflowing content.

#### HTML

The HTML consists of a top-level [heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 and an [unordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 with four [list items](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
, each containing the content for a separate page.

html

    <h1>Pagination interactivity demo</h1>
    <ul>
      <li>
        <h2>Page 1</h2>
        <p>This is the first page of content.</p>
        <p><a href="#">A demo link</a>.</p>
        <p><button>Press me</button></p>
      </li>
      <li>
        <h2>Page 2</h2>
        <p>This is the second page of content.</p>
        <p><a href="#">A demo link</a>.</p>
        <p><button>Press me</button></p>
      </li>
      <li>
        <h2>Page 3</h2>
        <p>This is the third page of content.</p>
        <p><a href="#">A demo link</a>.</p>
        <p><button>Press me</button></p>
      </li>
      <li>
        <h2>Page 4</h2>
        <p>This is the fourth page of content.</p>
        <p><a href="#">A demo link</a>.</p>
        <p><button>Press me</button></p>
      </li>
    </ul>
    

#### CSS

A [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 of `100vw` is set on the unordered list to make it as wide as the viewport. We add a fixed [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, some [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, and an [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 value of `scroll` so overflowing content will scroll. Its child list items are laid out horizontally with [`display: flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
. This flex container is given a [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 value of `x mandatory` to make it into a [scroll snap container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#scroll_snap_container)
. The `x` keyword causes the container's [snap targets](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_target)
 to be snapped horizontally. The `mandatory` keyword means that the container will always snap to a snap target at the end of a scrolling action.

    * {
      box-sizing: border-box;
    }
    
    body {
      margin: 0;
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    h1 {
      text-align: center;
      margin: 0;
    }
    
    button {
      background-color: white;
    }
    

css

    ul {
      width: 100vw;
      height: 250px;
      padding: 1vw;
      overflow-x: scroll;
      display: flex;
      gap: 1vw;
      scroll-snap-type: x mandatory;
    }
    

Each list item has the following styles applied:

*   A [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
     value of `0 0 98vw`, forcing each item to be as big as the scroll container minus the [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
     set on the list (see the `gap` declaration in the `ul` rule shown earlier). This also has the effect of centering each page inside the scroll container.
*   A [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
     value of `center`, to cause the scroll container to snap to the center of each snap target.
*   A [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
     value of `--inner-change inline`, to declare the element as the subject of the `--inner-change` view progress timeline, and set that timeline to progress in the inline direction as it moves through its ancestor scroll container.
*   An [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
     value with the same name as the [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    , as defined in the `view-timeline` shorthand, which means that the named view progress timeline will be used to control the progress of animations applied to the element.
*   An [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
     and [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
     defining the animation applied to this element and its fill mode. The `both` value is required because you want the starting animation state to apply to the element before the animation starts, and the end animation state to apply to the element after the animation finishes. If the animation isn't persisted, the `interactivity: inert` declaration applied via the animation won't apply to list items when they are outside the scroll container.

css

    li {
      list-style-type: none;
      background-color: #eeeeee;
      border: 1px solid #dddddd;
      padding: 20px;
    
      flex: 0 0 98vw;
    
      scroll-snap-align: center;
    
      view-timeline: --inner-change inline;
      animation-timeline: --inner-change;
      animation-name: inert-change;
      animation-fill-mode: both;
    }
    

Finally, the animation [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 are defined. `interactivity: inert` is set at positions `entry 0%` and `exit 100%` of the view timeline. Combined with the `animation-fill-mode: both` value, this means that the list items will be inert before the start and after the end of the view timeline, that is, when they are outside the scroll container. Between positions `entry 1%` and `exit 99%`, `interactivity: auto` is set on the list items, meaning they can be interacted with normally when they are inside the scroll container.

css

    @keyframes inert-change {
      entry 0%,
      exit 100% {
        interactivity: inert;
      }
    
      entry 1%,
      exit 99% {
        interactivity: auto;
      }
    }
    

See the [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 reference page for an explanation of the position values.

#### Result

Scroll the unordered list horizontally to see the pagination effect — each page snaps into view. Try tabbing between the links and the buttons; you'll find that only the ones on-screen are interactive and can be tabbed to.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#accessibility_concerns)

-------------------------------------------------------------------------------------------------------------------------------------

Consider accessibility carefully when making elements inert. By default, there is no visual way to tell whether or not an element or its subtree is inert. As a web developer, it is your responsibility to clearly indicate the content parts that are active and those that are inert.

While providing visual and non-visual cues about content inertness, also remember that the visual viewport may contain only sections of content. Users may be zoomed in to a small section of content, or users may not be able to view the content at all. Inert sections not being obviously inert can lead to frustration and bad user experience.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-interactivity](https://drafts.csswg.org/css-ui-4/#propdef-interactivity) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity#see_also)

---------------------------------------------------------------------------------------------------------

*   HTML [`inert`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert)
     attribute
*   [`HTMLElement.inert`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/inert)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/interactivity/index.md?plain=1 "Folder: en-us/web/css/reference/properties/interactivity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finteractivity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finteractivity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finteractivity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finteractivity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")