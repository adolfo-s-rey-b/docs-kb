*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#mdn-search)
    

`scroll-padding` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-padding`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets scroll padding on all sides of an element at once. It specifies offsets that define the optimal viewing region of a scrollport within a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#try_it)

------------------------------------------------------------------------------------------------------

    scroll-padding: 0;
    

    scroll-padding: 20px;
    

    scroll-padding: 20%;
    

    <section class="default-example" id="default-example">
      <div class="scroller" id="example-element">
        <div>1</div>
        <div>2</div>
        <div>3</div>
      </div>
      <div class="info">Scroll »</div>
    </section>
    

    .default-example .info {
      inline-size: 100%;
      padding: 0.5em 0;
      font-size: 90%;
      writing-mode: vertical-rl;
    }
    
    .scroller {
      text-align: left;
      height: 250px;
      width: 270px;
      overflow-y: scroll;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
      border: 1px solid black;
      scroll-snap-type: y mandatory;
    }
    
    .scroller > div {
      flex: 0 0 250px;
      background-color: rebeccapurple;
      color: white;
      font-size: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      scroll-snap-align: start;
    }
    
    .scroller > div:nth-child(even) {
      background-color: white;
      color: rebeccapurple;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`scroll-padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)
    
*   [`scroll-padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)
    
*   [`scroll-padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)
    
*   [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    scroll-padding: auto;
    
    /* <length> values */
    scroll-padding: 10px;
    scroll-padding: 1em 0.5em 1em 1em;
    scroll-padding: 10%;
    
    /* Global values */
    scroll-padding: inherit;
    scroll-padding: initial;
    scroll-padding: revert;
    scroll-padding: revert-layer;
    scroll-padding: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

An inwards offset from the corresponding edge of the scrollport, as a valid [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#auto)

The offset is determined by the user agent. This will generally be `0px`, but the user agent is free to detect and do something else if a non-zero value is more appropriate.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#description)

----------------------------------------------------------------------------------------------------------------

The `scroll-padding` property is a shorthand that sets [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)
, [`scroll-padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)
, [`scroll-padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)
, and [`scroll-padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)
, in that order, setting the top, right, bottom, and left scroll padding of a scroll container, respectively.

Useful when creating scroll-snap containers, the `scroll-padding` property enables defining offsets for the _optimal viewing region_ of the scrollport: the region used as the target region for placing elements in view of the user. This allows you to create insets in the scrollport to make room for objects that might obscure the content, such as fixed-positioned toolbars or sidebars, or to put more breathing room between a targeted element and the edges of the scrollport.

While defined in the [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
 module, this property applies to all scroll containers, no matter the value of the [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`scroll-padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)<br>    : `auto`<br>*   [`scroll-padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)<br>    : `auto`<br>*   [`scroll-padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)<br>    : `auto`<br>*   [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)<br>    : `auto` |
| Applies to | scroll containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | relative to the scroll container's scrollport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`scroll-padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)<br>    : as specified<br>*   [`scroll-padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)<br>    : as specified<br>*   [`scroll-padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)<br>    : as specified<br>*   [`scroll-padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

scroll-padding =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage \[0,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#examples)

----------------------------------------------------------------------------------------------------------

### [Preventing content from being hidden by a fixed header](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#preventing_content_from_being_hidden_by_a_fixed_header)

A common use case for `scroll-padding` is to prevent scrolling content from being hidden by a fixed-position header. This example demonstrates how to use `scroll-padding` for this purpose.

#### HTML

The header contains links to three sections on the page.

html

    <header>
      <nav>
        <a href="#section-1">Section 1</a>
        <a href="#section-2">Section 2</a>
        <a href="#section-3">Section 3</a>
      </nav>
    </header>
    <main>
      <section id="section-1">
        <h2>Section 1</h2>
        <p>Use the links in the header to jump to another section.</p>
      </section>
      <section id="section-2">
        <h2>Section 2</h2>
        <p>This heading remains visible below the fixed header.</p>
      </section>
      <section id="section-3">
        <h2>Section 3</h2>
        <p>This heading also remains visible below the fixed header.</p>
      </section>
    </main>
    

#### CSS

    header {
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #eeeeee;
    }
    
    nav {
      display: flex;
      gap: 1rem;
    }
    
    section {
      box-sizing: border-box;
      padding: 1rem;
      min-height: 60vh;
    }
    
    h2 {
      margin-top: 0;
    }
    

The header is fixed to the top of the viewport and is `60px` tall. We set `scroll-padding` on the root element to reserve `60px` at the top of the viewport when scrolling to a section, with no offset on the other sides.

css

    html {
      --navbar-height: 60px;
    
      scroll-padding: var(--navbar-height) 0 0;
      scroll-behavior: smooth;
    }
    
    header {
      position: fixed;
      top: 0;
      height: var(--navbar-height);
      width: 100%;
    }
    

We add padding to the main content so the first section starts below the header on initial load.

css

    main {
      padding-top: var(--navbar-height);
    }
    

#### Result

Click the links in the header to jump between sections. Each section appears below the header, keeping its heading visible. Open this example in the playground, remove the `scroll-padding` line, and click the links again to see the header obscure the headings.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# scroll-padding](https://drafts.csswg.org/css-scroll-snap/#scroll-padding) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding#see_also)

----------------------------------------------------------------------------------------------------------

*   [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
    
*   [Basic concepts of scroll-snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts)
    
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-padding/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-padding (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-padding&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-padding%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-padding%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-padding%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")