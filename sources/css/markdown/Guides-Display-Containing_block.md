*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#mdn-search)
    

Layout and the containing block
===============================

The size and position of an element are often impacted by its **containing block**. Most often, the containing block is the [content area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content_area)
 of an element's nearest [block-level](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
 ancestor, but this is not always the case. In this article, we examine the factors that determine an element's containing block.

When a user agent (such as your browser) lays out a document, it generates a box for every element. Each box is divided into four areas:

1.  Content area
2.  Padding area
3.  Border area
4.  Margin area

![Diagram of the box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block/box-model.png)

Many developers believe that the containing block of an element is always the content area of its parent, but that isn't necessarily true. Let's investigate the factors that determine what an element's containing block is.

[Effects of the containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#effects_of_the_containing_block)

----------------------------------------------------------------------------------------------------------------------------------------------------

Before learning what determines the containing block of an element, it's useful to know why it matters in the first place.

The size and position of an element are often impacted by its containing block. Percentage values that are applied to the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, and offset properties of an absolutely positioned element (i.e., which has its [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 set to `absolute` or `fixed`) are computed from the element's containing block.

[Identifying the containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#identifying_the_containing_block)

------------------------------------------------------------------------------------------------------------------------------------------------------

The process for identifying the containing block depends entirely on the value of the element's [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 property:

1.  If the `position` property is **`static`**, **`relative`**, or **`sticky`**, the containing block is formed by the edge of the _content box_ of the nearest ancestor element that is either **a block container** (such as an inline-block, block, or list-item element) or **establishes a formatting context** (such as a table container, flex container, grid container, or the block container itself).
2.  If the `position` property is **`absolute`**, the containing block is formed by the edge of the _padding box_ of the nearest ancestor element that has a `position` value other than `static` (`fixed`, `absolute`, `relative`, or `sticky`).
3.  If the `position` property is **`fixed`**, the containing block is established by the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
     (in the case of continuous media) or the page area (in the case of paged media).
4.  If the `position` property is **`absolute`** or **`fixed`**, the containing block may also be formed by the edge of the _padding box_ of the nearest ancestor element that has any of the following:
    *   A [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
        , [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
        , [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
        , [`perspective`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
        , [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        , [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        , or [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
         value other than `none`.
    *   A [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
         value of `layout`, `paint`, `strict` or `content` (e.g., `contain: paint;`).
    *   A [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
         value containing a property for which a non-initial value would form a containing block (e.g., `filter` or `transform`).
    *   A [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
         value of `auto`.

**Note:** The containing block in which the root element ([`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
) resides is a rectangle called the **initial containing block**. It has the dimensions of the viewport (for continuous media) or the page area (for paged media).

**Note:** There are browser inconsistencies with `perspective` and `filter` contributing to containing block formation.

[Calculating percentage values from the containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#calculating_percentage_values_from_the_containing_block)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As noted above, when certain properties are given a percentage value, the computed value depends on the element's containing block. The properties that work this way are **box model properties** and **offset properties**:

1.  The [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    , [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    , and [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
     properties compute percentage values from the `height` of the containing block.
2.  The [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    , [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    , [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    , [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    , and [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
     properties compute percentage values from the `width` of the containing block.

**Note:** A **block container** (such as an inline-block, block, or list-item element) either contains only inline-level boxes participating in an inline formatting context, or only block-level boxes participating in a block formatting context. An element is a block container only if it contains block-level or inline-level boxes.

[Some examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#some_examples)

----------------------------------------------------------------------------------------------------------------

The HTML code for all our examples is:

html

    <body>
      <section>
        <p>This is a paragraph!</p>
      </section>
    </body>
    

Only the CSS is altered in each instance below.

### [Example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#example_1)

In this example, the paragraph is statically positioned, so its containing block is [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 because it's the nearest ancestor that is a block container (because of `display: block`).

    <body>
      <section>
        <p>This is a paragraph!</p>
      </section>
    </body>
    

css

    body {
      background: beige;
    }
    
    section {
      display: block;
      width: 400px;
      height: 160px;
      background: lightgray;
    }
    
    p {
      width: 50%; /* == 400px * .5 = 200px */
      height: 25%; /* == 160px * .25 = 40px */
      margin: 5%; /* == 400px * .05 = 20px */
      padding: 5%; /* == 400px * .05 = 20px */
      background: cyan;
    }
    

### [Example 2](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#example_2)

In this example, the paragraph's containing block is the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element, because `<section>` is not a block container (because of `display: inline`) and doesn't establish a formatting context.

    <body>
      <section>
        <p>This is a paragraph!</p>
      </section>
    </body>
    

css

    body {
      background: beige;
    }
    
    section {
      display: inline;
      background: lightgray;
    }
    
    p {
      width: 50%; /* == half the body's width */
      height: 200px; /* Note: a percentage would be 0 */
      background: cyan;
    }
    

### [Example 3](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#example_3)

In this example, the paragraph's containing block is `<section>` because the latter's `position` is `absolute`. The paragraph's percentage values are affected by the `padding` of its containing block, though if the containing block's [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
 value were `border-box` this would not be the case.

    <body>
      <section>
        <p>This is a paragraph!</p>
      </section>
    </body>
    

css

    body {
      background: beige;
    }
    
    section {
      position: absolute;
      left: 30px;
      top: 30px;
      width: 400px;
      height: 160px;
      padding: 30px 20px;
      background: lightgray;
    }
    
    p {
      position: absolute;
      width: 50%; /* == (400px + 20px + 20px) * .5 = 220px */
      height: 25%; /* == (160px + 30px + 30px) * .25 = 55px */
      margin: 5%; /* == (400px + 20px + 20px) * .05 = 22px */
      padding: 5%; /* == (400px + 20px + 20px) * .05 = 22px */
      background: cyan;
    }
    

### [Example 4](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#example_4)

In this example, the paragraph's `position` is `fixed`, so its containing block is the initial containing block (on screens, the viewport). Thus, the paragraph's dimensions change based on the size of the browser window.

    <body>
      <section>
        <p>This is a paragraph!</p>
      </section>
    </body>
    

css

    body {
      background: beige;
    }
    
    section {
      width: 400px;
      height: 480px;
      margin: 30px;
      padding: 15px;
      background: lightgray;
    }
    
    p {
      position: fixed;
      width: 50%; /* == (50vw - (width of vertical scrollbar)) */
      height: 50%; /* == (50vh - (height of horizontal scrollbar)) */
      margin: 5%; /* == (5vw - (width of vertical scrollbar)) */
      padding: 5%; /* == (5vw - (width of vertical scrollbar)) */
      background: cyan;
    }
    

### [Example 5](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#example_5)

In this example, the paragraph's `position` is `absolute`, so its containing block is `<section>`, which is the nearest ancestor with a [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 property that isn't `none`.

    <body>
      <section>
        <p>This is a paragraph!</p>
      </section>
    </body>
    

css

    body {
      background: beige;
    }
    
    section {
      transform: rotate(0deg);
      width: 400px;
      height: 160px;
      background: lightgray;
    }
    
    p {
      position: absolute;
      left: 80px;
      top: 30px;
      width: 50%; /* == 200px */
      height: 25%; /* == 40px */
      margin: 5%; /* == 20px */
      padding: 5%; /* == 20px */
      background: cyan;
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#see_also)

------------------------------------------------------------------------------------------------------

*   [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
     property
*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
     property
*   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
     property
*   [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
     property
*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
     and [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
     size values
*   [Learn: sizing items in CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Sizing)
    
*   [Box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module
*   [Layout modes](https://developer.mozilla.org/en-US/docs/Glossary/Layout_mode)
    
*   [Visual formatting models](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
    
*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    
*   [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
    
*   [Initial](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    , [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    , [used](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    , and [actual](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
     values
*   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
    
*   [Intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 30, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/display/containing_block/index.md?plain=1 "Folder: en-us/web/css/guides/display/containing_block (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FContaining_block&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fcontaining_block%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FContaining_block%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fcontaining_block%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F19497692665c3551b4097af5cd9f52f84564cefd%0A*+Document+last+modified%3A+2026-04-30T08%3A06%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")