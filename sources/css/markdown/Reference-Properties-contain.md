*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#mdn-search)
    

`contain` CSS property
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contain`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property indicates that an element and its contents are, as much as possible, independent from the rest of the document tree. Containment enables isolating a subsection of the DOM, providing performance benefits by limiting calculations of layout, style, paint, size, or any combination to a DOM subtree rather than the entire page. Containment can also be used to scope CSS counters and quotes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#try_it)

-----------------------------------------------------------------------------------------------

    contain: none;
    

    contain: size;
    

    contain: layout;
    

    contain: paint;
    

    contain: strict;
    

    <section class="default-example" id="default-example">
      <div class="card" id="example-element">
        <h2>Element with '<code>contain</code>'</h2>
        <p>
          The Goldfish is a species of domestic fish best known for its bright
          colors and patterns.
        </p>
        <div class="fixed"><p>Fixed right 4px</p></div>
      </div>
    </section>
    

    h2 {
      margin-top: 0;
    }
    
    #default-example {
      text-align: left;
      padding: 4px;
      font-size: 16px;
    }
    
    .card {
      text-align: left;
      border: 3px dotted;
      padding: 20px;
      margin: 10px;
      width: 85%;
      min-height: 150px;
    }
    
    .fixed {
      position: fixed;
      border: 3px dotted;
      right: 4px;
      padding: 4px;
      margin: 4px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Keyword values */
    contain: none;
    contain: strict;
    contain: content;
    contain: size;
    contain: inline-size;
    contain: layout;
    contain: style;
    contain: paint;
    
    /* Multiple keywords */
    contain: size paint;
    contain: size layout paint;
    contain: inline-size layout;
    
    /* Global values */
    contain: inherit;
    contain: initial;
    contain: revert;
    contain: revert-layer;
    contain: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#values)

This property is specified as a single value (`none`, `strict`, or `content`) or as a space-separated list of one or more of `size` (or `inline-size`), `layout`, `style`, and `paint`, in any order:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#none)

The element renders as normal, with no containment applied.

[`strict`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#strict)

All containment rules are applied to the element. This is equivalent to `contain: size layout paint style`.

[`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#content)

All containment rules except `size` are applied to the element. This is equivalent to `contain: layout paint style`.

[`size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#size)

Size containment is applied to the element in both the inline and block directions. The size of the element can be computed in isolation, ignoring the child elements. This value cannot be combined with `inline-size`.

[`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#inline-size)

Inline size containment is applied to the element. The inline size of the element can be computed in isolation, ignoring the child elements. This value cannot be combined with `size`.

[`layout`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#layout)

The internal layout of the element is isolated from the rest of the page. This means nothing outside the element affects its internal layout, and vice versa.

[`style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#style)

For properties that can affect more than just an element and its descendants, the effects don't escape the containing element. Counters and quotes are scoped to the element and its contents.

[`paint`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#paint)

Descendants of the element don't display outside its bounds. If the containing box is offscreen, the browser does not need to paint its contained elements — these must also be offscreen as they are contained completely by that box. If a descendant overflows the containing element's bounds, then that descendant will be clipped to the containing element's overflow clip edge. By default, this edge corresponds to the padding-box for non-replaced elements.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#description)

---------------------------------------------------------------------------------------------------------

There are four types of CSS containment: size, layout, style, and paint, which are set on the container. The property is a space-separated list of a subset of the five standard values or one of the two shorthand values. Changes to the contained properties within the container are not propagated outside of the contained element to the rest of the page. The main benefit of containment is that the browser does not have to re-render the DOM or page layout as often, leading to small performance benefits during the rendering of static pages and greater performance benefits in more dynamic applications.

Using the `contain` property is useful on pages with groups of elements that are supposed to be independent, as it can prevent element internals from having side effects outside of its bounding-box.

**Note:** Using `layout`, `paint`, `strict` or `content` values for this property creates:

1.  A new [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
     (for the descendants whose [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     property is `absolute` or `fixed`).
2.  A new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    .
3.  A new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    .

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#formal_syntax)

-------------------------------------------------------------------------------------------------------------

contain =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  strict                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  content                                             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 size [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-size [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 layout [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 style [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 paint [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#examples)

---------------------------------------------------------------------------------------------------

### [Paint containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#paint_containment)

The following example shows how to use `contain: paint` to prevent an element's descendants from painting outside of its bounds.

css

    div {
      width: 100px;
      height: 100px;
      background: red;
      margin: 10px;
      font-size: 20px;
    }
    
    .contain-paint {
      contain: paint;
    }
    

html

    <div class="contain-paint">
      <p>This text will be clipped to the bounds of the box.</p>
    </div>
    <div>
      <p>This text will not be clipped to the bounds of the box.</p>
    </div>
    

### [Layout containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#layout_containment)

Consider the example below which shows how elements behave with and without layout containment applied:

html

    <div class="card contain-layout">
      <h2>Card 1</h2>
      <div class="fixed"><p>Fixed box 1</p></div>
      <div class="float"><p>Float box 1</p></div>
    </div>
    <div class="card">
      <h2>Card 2</h2>
      <div class="fixed"><p>Fixed box 2</p></div>
      <div class="float"><p>Float box 2</p></div>
    </div>
    <div class="card">
      <h2>Card 3</h2>
      <!-- ... -->
    </div>
    

    p {
      margin: 4px;
      padding: 4px;
    }
    
    h2 {
      margin-bottom: 4px;
      padding: 10px;
    }
    
    div {
      border-radius: 4px;
      box-shadow: 0 2px 4px 0 gray;
      padding: 6px;
      margin: 6px;
    }
    

css

    .card {
      width: 70%;
      height: 90px;
    }
    
    .fixed {
      position: fixed;
      right: 10px;
      top: 10px;
      background: coral;
    }
    
    .float {
      float: left;
      height: 40px;
      margin: 10px;
      background: aquamarine;
    }
    
    .contain-layout {
      contain: layout;
    }
    

The first card has layout containment applied, and its layout is isolated from the rest of the page. We can reuse this card in other places on the page without worrying about layout recalculation of the other elements. If floats overlap the card bounds, elements on the rest of the page are not affected. When the browser recalculates the containing element's subtree, only that element is recalculated. Nothing outside of the contained element needs to be recalculated. Additionally, the fixed box uses the card as a layout container to position itself.

The second and third cards have no containment. The layout context for the fixed box in the second card is the root element so the fixed box is positioned in the top right corner of the page. A float overlaps the second card's bounds causing the third card to have unexpected layout shift that's visible in the positioning of the `<h2>` element. When recalculation occurs, it is not limited to a container. This impacts performance and interferes with the rest of the page layout.

### [Style containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#style_containment)

Style containment scopes [counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
 and [quotes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
 to the contained element. For CSS counters, the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 and [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 properties are scoped to the element as if the element is at the root of the document.

#### Containment and counters

The example below takes a look at how counters work when style containment is applied:

html

    <ul>
      <li>Item A</li>
      <li>Item B</li>
      <li class="container">Item C</li>
      <li>Item D</li>
      <li>Item E</li>
    </ul>
    

css

    body {
      counter-reset: list-items;
    }
    
    li::before {
      counter-increment: list-items;
      content: counter(list-items) ": ";
    }
    
    .container {
      contain: style;
    }
    

Without containment, the counter would increment from 1 to 5 for each list item. Style containment causes the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 property to be scoped to the element's subtree and the counter begins again at 1:

#### Containment and quotes

CSS quotes are similarly affected in that the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 values relating to quotes are scoped to the element:

html

    <!-- With style containment -->
    <span class="open-quote">
      outer
      <span class="contain-style">
        <span class="open-quote">inner</span>
      </span>
    </span>
    <span class="close-quote">close</span>
    <br />
    <!-- Without containment -->
    <span class="open-quote">
      outer
      <span>
        <span class="open-quote">inner</span>
      </span>
    </span>
    <span class="close-quote">close</span>
    

css

    body {
      quotes: "[" "]" "‹" "›";
    }
    .open-quote::before {
      content: open-quote;
    }
    
    .close-quote::after {
      content: close-quote;
    }
    
    .contain-style {
      contain: style;
    }
    

Because of containment, the first closing quote ignores the inner span and uses the outer span's closing quote instead:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Containment Module Level 2  <br>\# contain-property](https://drafts.csswg.org/css-contain/#contain-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#see_also)

---------------------------------------------------------------------------------------------------

*   [CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
    
*   [CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   CSS [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
     property
*   CSS [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/contain/index.md?plain=1 "Folder: en-us/web/css/reference/properties/contain (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F316367d0a304cf967691602672795825c05f835a%0A*+Document+last+modified%3A+2026-09-07T10%3A53%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")