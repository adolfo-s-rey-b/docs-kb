*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#mdn-search)
    

`scroll-target-group` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/475)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#browser_compatibility)
 carefully before using this in production.

The **`scroll-target-group`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether an element is a scroll marker group container.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    scroll-target-group: none;
    scroll-target-group: auto;
    
    /* Global values */
    scroll-target-group: inherit;
    scroll-target-group: initial;
    scroll-target-group: revert;
    scroll-target-group: revert-layer;
    scroll-target-group: unset;
    

The `scroll-target-group` property is specified as one of the following keyword values:

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#none)

The element is not a scroll marker group container.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#auto)

The element is a scroll marker group container.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#description)

---------------------------------------------------------------------------------------------------------------------

Setting `scroll-target-group: auto` on an element denotes it as a **scroll marker group container**. This groups together a set of navigation items that allow users to navigate between elements on a page (such as carousel items or article sections) and highlight which element is currently in view.

Any [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements with fragment identifiers inside the container are automatically set as scroll markers. The anchor element whose scroll target is currently in view can be styled via the [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
 pseudo-class.

### [Differences between `scroll-target-group` and `scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#differences_between_scroll-target-group_and_scroll-marker-group)

Scroll marker group containers created using `scroll-target-group` behave in a very similar way to those created using the [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 property, with some differences:

*   With `scroll-target-group`, you have to create your own markup to represent the scroll marker group container and scroll markers, whereas `scroll-marker-group` automatically creates a set of pseudo-elements to represent the container ([`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    ) and the markers (one or more instances of [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    ). These automatically have the expected navigation associations with the [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
     they are generated on. Using `scroll-marker-group` provides a quicker setup because you don't need to use your own markup. However, creating your own markup and setting it as a scroll marker group container via `scroll-target-group` provides more control and flexibility.
*   Links denoted as scroll markers via `scroll-target-group` have no special navigation behavior, whereas markers generated via `scroll-marker-group` automatically have [`tablist`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)
    /[`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)
     semantics applied to them, meaning they behave like a single item in the tab order, and users can move between scroll markers with the arrow keys. Again, `scroll-marker-group` provides useful default behavior, but you have the flexibility of providing alternative semantics and behavior for markers specified using `scroll-target-group`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

scroll-target-group =   
  none  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic `scroll-target-group` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#basic_scroll-target-group_usage)

This example shows a page with a table of contents linking to different sections.

#### HTML

Our markup has a series of [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements containing content, and a table of contents created using an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
/[`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
) and [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements.

html

    <nav id="toc">
      <ol>
        <li><a href="#intro">Introduction</a></li>
        <li><a href="#ch1">Chapter 1</a></li>
        <li><a href="#ch2">Chapter 2</a></li>
        <li><a href="#ch3">Chapter 3</a></li>
        <li><a href="#ch4">Chapter 4</a></li>
      </ol>
    </nav>
    <section id="intro" class="chapter">
      <h1>Prose of the century</h1>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
        aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
        pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
        ultricies tellus laoreet sit amet.
      </p>
    </section>
    <section id="ch1" class="chapter">
      <h2>Chapter 1</h2>
    
      <!-- ... -->
    </section>
    <section id="ch2" class="chapter">
      <h2>Chapter 2</h2>
    
      <!-- ... -->
    </section>
    
    <!-- ... -->
    

    <nav id="toc">
      <ol>
        <li><a href="#intro">Introduction</a></li>
        <li><a href="#ch1">Chapter 1</a></li>
        <li><a href="#ch2">Chapter 2</a></li>
        <li><a href="#ch3">Chapter 3</a></li>
        <li><a href="#ch4">Chapter 4</a></li>
      </ol>
    </nav>
    <section id="intro" class="chapter">
      <h1>My story</h1>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
        aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
        pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
        ultricies tellus laoreet sit amet.
      </p>
    </section>
    <section id="ch1" class="chapter">
      <h2>Chapter 1</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
        aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
        pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
        ultricies tellus laoreet sit amet.
      </p>
      <p>
        Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet
        orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare
        ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat.
        Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra
        congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec lacus
        varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.
      </p>
      <p>
        Nam vulputate diam nec tempor bibendum. Donec luctus augue eget malesuada
        ultrices. Phasellus turpis est, posuere sit amet dapibus ut, facilisis sed
        est. Nam id risus quis ante semper consectetur eget aliquam lorem. Vivamus
        tristique elit dolor, sed pretium metus suscipit vel. Mauris ultricies
        lectus sed lobortis finibus. Vivamus eu urna eget velit cursus viverra quis
        vestibulum sem. Aliquam tincidunt eget purus in interdum. Cum sociis natoque
        penatibus et magnis dis parturient montes, nascetur ridiculus mus.
      </p>
    </section>
    <section id="ch2" class="chapter">
      <h2>Chapter 2</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
        aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
        pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
        ultricies tellus laoreet sit amet.
      </p>
      <p>
        Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet
        orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare
        ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat.
        Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra
        congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec lacus
        varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.
      </p>
    </section>
    <section id="ch3" class="chapter">
      <h2>Chapter 3</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
        aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
        pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
        ultricies tellus laoreet sit amet.
      </p>
      <p>
        Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet
        orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare
        ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat.
        Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra
        congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec lacus
        varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.
      </p>
    </section>
    <section id="ch4" class="chapter">
      <h2>Chapter 4</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla luctus
        aliquam dolor, eu lacinia lorem placerat vulputate. Duis felis orci,
        pulvinar id metus ut, rutrum luctus orci. Cras porttitor imperdiet nunc, at
        ultricies tellus laoreet sit amet.
      </p>
      <p>
        Sed auctor cursus massa at porta. Integer ligula ipsum, tristique sit amet
        orci vel, viverra egestas ligula. Curabitur vehicula tellus neque, ac ornare
        ex malesuada et. In vitae convallis lacus. Aliquam erat volutpat.
        Suspendisse ac imperdiet turpis. Aenean finibus sollicitudin eros pharetra
        congue. Duis ornare egestas augue ut luctus. Proin blandit quam nec lacus
        varius commodo et a urna. Ut id ornare felis, eget fermentum sapien.
      </p>
    </section>
    

#### CSS

We've hidden most of the styling for brevity. Most pertinent to this example, we've set `scroll-target-group: auto` on the `<ol>` to turn it into a scroll marker group container and trigger the browser's algorithm for calculating which `<a>` element is the `:target-current` at any given time (that is, which link's target is currently in view). We then style the `:target-current` pseudo-class with a `red` [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 so that it stands out clearly.

    body {
      font: 1.2em / 1.5 system-ui;
      width: 50%;
      max-width: 700px;
      margin: 0 auto;
    }
    
    nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      display: flex;
      justify-content: center;
    }
    
    section {
      padding-top: 60px;
    }
    
    a {
      color: black;
      text-decoration: none;
    }
    
    a:hover,
    a:focus {
      text-decoration: underline;
    }
    
    ol {
      display: flex;
      width: 100%;
      justify-content: space-around;
      list-style-type: none;
      padding: 20px 0;
      margin: 0;
      background: white;
    }
    

css

    ol {
      scroll-target-group: auto;
    }
    
    :target-current {
      color: red;
    }
    

#### Result

Try navigating by activating the links and by scrolling. You'll see that in each case, the red highlight moves between the links to match the section currently being shown.

### [CSS carousel with `scroll-target-group` scroll markers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#css_carousel_with_scroll-target-group_scroll_markers)

This example shows how to create [CSS carousel](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
 scroll markers using `scroll-target-group`. The code for this example is similar to our [Carousel with single pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels#carousel_with_single_pages)
 example; we'll just explain the differences below.

#### HTML

The markup has IDs set on the list items that define each page, and an ordered list added that we'll turn into a scroll marker group container using CSS.

html

    <h1>CSS carousel single item per page</h1>
    <ul>
      <li id="page1">
        <h2>Page 1</h2>
      </li>
      <li id="page2">
        <h2>Page 2</h2>
      </li>
      <li id="page3">
        <h2>Page 3</h2>
      </li>
      <li id="page4">
        <h2>Page 4</h2>
      </li>
    </ul>
    <ol>
      <li><a href="#page1">1</a></li>
      <li><a href="#page2">2</a></li>
      <li><a href="#page3">3</a></li>
      <li><a href="#page4">4</a></li>
    </ol>
    

#### CSS

We create the scroll marker group container and scroll markers by setting `scroll-target-group` on the `<ol>` element. The rest of the code for styling these is very similar, except that we are targeting elements of our own choosing (`<ol>` and `<a>`) rather than the [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
 and [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-elements.

We complete the code by setting some styles on the `:target-current`, `a:hover`, and `a:focus` states to indicate which page is currently being shown and which links are being hovered/focused.

    /* General styles */
    
    * {
      box-sizing: border-box;
    }
    
    body {
      margin: 0;
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    h1 {
      text-align: center;
    }
    
    button {
      background-color: white;
    }
    
    /* General styling of list as scrolling carousel */
    
    ul {
      width: 100%;
      height: 400px;
      padding: 20px;
      gap: 4%;
      display: grid;
      grid-auto-flow: column;
      grid-auto-columns: 100%;
      overflow-x: scroll;
      scroll-snap-type: x mandatory;
    }
    
    ul li {
      list-style-type: none;
      background-color: #eeeeee;
      border: 1px solid #dddddd;
      padding: 20px;
    
      scroll-snap-align: center;
    }
    
    /* CSS scroll buttons */
    
    /* Style the scroll buttons */
    
    ul::scroll-button(*) {
      border: 0;
      font-size: 2rem;
      background: none;
      color: rgb(0 0 0 / 0.7);
      cursor: pointer;
    }
    
    ul::scroll-button(*):hover,
    ul::scroll-button(*):focus {
      color: black;
    }
    
    ul::scroll-button(*):active {
      translate: 1px 1px;
    }
    
    ul::scroll-button(*):disabled {
      color: rgb(0 0 0 / 0.2);
    }
    
    ul::scroll-button(left) {
      content: "◄";
    }
    
    ul::scroll-button(right) {
      content: "►";
    }
    
    /* Position the scroll buttons */
    
    ul {
      anchor-name: --my-carousel;
    }
    
    ul::scroll-button(*) {
      position: absolute;
      position-anchor: --my-carousel;
    }
    
    ul::scroll-button(left) {
      right: calc(anchor(left) - 70px);
      top: calc(anchor(bottom) - 80px);
    }
    
    ul::scroll-button(right) {
      left: calc(anchor(right) - 70px);
      top: calc(anchor(bottom) - 80px);
    }
    

css

    ol {
      position: absolute;
      position-anchor: --my-carousel;
      top: calc(anchor(bottom) - 90px);
      justify-self: anchor-center;
      display: flex;
      justify-content: center;
      gap: 20px;
    
      list-style-type: none;
      padding: 0;
      scroll-target-group: auto;
    }
    
    ol a {
      width: 28px;
      height: 28px;
      display: inline-block;
      text-align: center;
      text-decoration: none;
      padding-top: 4px;
      color: black;
      background-color: transparent;
      border: 2px solid black;
      border-radius: 50%;
    }
    
    ol a:hover,
    ol a:focus,
    :target-current {
      background-color: black;
      color: white;
    }
    

#### Result

Try navigating in each of these three ways: by activating the scroll marker links, by horizontal scrolling, or by pressing the scroll buttons on either side. You'll see that in each case, the highlight moves between the links to match the section currently being shown.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 5  <br>\# scroll-target-group](https://drafts.csswg.org/css-overflow-5/#scroll-target-group) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
     and [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
     pseudo-elements
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    , [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    , and [`:target-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after)
     pseudo-classes
*   [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow/Carousels)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-target-group/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-target-group (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-target-group&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-target-group%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-target-group%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-target-group%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")