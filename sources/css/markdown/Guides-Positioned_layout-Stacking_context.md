*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#mdn-search)
    

Stacking context
================

**Stacking context** is a three-dimensional conceptualization of HTML elements along an imaginary z-axis relative to the user, who is assumed to be facing the viewport or the webpage. The stacking context determines how elements are layered on top of one another along the z-axis (think of it as the "depth" dimension on your screen). Stacking context determines the visual order of how overlapping content is rendered.

Elements within a stacking context are stacked independently from elements outside of that stacking context, ensuring elements in one stacking context don't interfere with the stacking order of elements in another. Each stacking context is completely independent of its siblings: only descendant elements are considered when stacking is processed.

Each stacking context is self-contained. After an element's contents are stacked, the entire element is considered as a single unit in the stacking order of its parent stacking context.

Within a stacking context, child elements are stacked according to the `z-index` values of all the siblings. The stacking contexts of these nested elements only have meaning in this parent. Stacking contexts are treated atomically as a single unit in the parent stacking context. Stacking contexts can be contained in other stacking contexts, and together create a hierarchy of stacking contexts.

The hierarchy of stacking contexts is a subset of the hierarchy of HTML elements because only certain elements create stacking contexts. Elements that don't create their own stacking contexts are _assimilated_ by the parent stacking context.

[Features creating stacking contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#features_creating_stacking_contexts)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

A stacking context is formed, anywhere in the document, by any element in the following scenarios:

*   Root element of the document (`<html>`).
    
*   Element with a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     value `absolute` or `relative` and [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
     value other than `auto`.
    
*   Element with a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     value `fixed` or `sticky`.
    
*   Element with a [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
     value `size` or `inline-size` set (See [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    ).
    
*   Element that is a [flex item](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
     with a [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
     value other than `auto`.
    
*   Element that is a [grid item](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts#layering_items_with_z-index)
     with [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
     value other than `auto`.
    
*   Element with an [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
     value less than `1`.
    
*   Element with a [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
     value other than `normal`.
    
*   Element with any of the following properties with a value other than `none`:
    
    *   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
        
    *   [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
        
    *   [`perspective`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
        
    *   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
        
    *   [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
         / [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
         / [`mask-border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
        
*   Element with the [`isolation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation)
     value `isolate`.
    
*   Element with a [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
     value specifying any property that would create a stacking context on non-initial value.
    
*   Element with a [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
     value of `layout` or `paint`, or a composite value that includes either of these values (i.e., `contain: strict`, `contain: content`).
    
*   Element placed into the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
     and its corresponding [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
    . Examples include [fullscreen](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
     and [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
     elements.
    
*   Element that has had stacking context-creating properties (such as `opacity`) animated using [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
    , with [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
     set to [`forwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#forwards)
    .
    

[Nested stacking contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#nested_stacking_contexts)

------------------------------------------------------------------------------------------------------------------------------------------------

Stacking contexts can be contained in other stacking contexts, and they can together create a hierarchy of stacking contexts.

The root element of a document is a stacking context which, in most cases, contains nested stacking contexts, many of which will contain additional stacking contexts. Within each stacking context, child elements are stacked according to the same rules explained in [Using `z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index)
. Importantly, the `z-index` values of its child stacking contexts only have meaning within its parent's stacking context. Stacking contexts are treated atomically as a single unit in the parent stacking context.

To figure out the _rendering order_ of stacked elements along the z-axis, think of each index value as a "version number" of sorts, where child elements represent minor version numbers underneath their parent's major version number.

To demonstrate how the stacking order of each element participates in the stacking order of their ancestor stacking contexts, let's look at an example page with six container elements. There are three sibling [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 elements. The last `<article>` contains three sibling [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements, with the [<h1>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 and [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
 of that third article appearing between the first and second sibling `<section>` elements.

Every container element has an [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 of less than `1` (which creates a stacking context), and a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 of either `relative` or `absolute` (which creates a stacking context when the element also has a `z-index` value other than `auto`).

The CSS properties for colors, fonts, alignment, and [box-model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
 have been hidden for brevity.

The hierarchy of stacking contexts in the above example is as follows:

Root
│
├── ARTICLE #1
├── ARTICLE #2
└── ARTICLE #3
  │
  ├── SECTION #4
  ├── SECTION #5
  └── SECTION #6

The three `<section>` elements are children of ARTICLE #3. Therefore, the stacking of the section elements is completely resolved within ARTICLE #3. Once stacking and rendering within ARTICLE #3 is completed, the whole ARTICLE #3 element is passed for stacking in the root element with respect to its sibling `<article>` elements.

By comparing the `z-index` as "version numbers", we can see how an element with a `z-index` of `1` (SECTION #5) is stacked above an element with a `z-index` of `2` (ARTICLE #2), and how an element with a `z-index` of `6` (SECTION #4) is stacked below an element with a `z-index` of `5` (ARTICLE #1). SECTION #4 is rendered under ARTICLE #1 because ARTICLE #1's z-index (`5`) is valid within the stacking context of the root element, while SECTION #4's z-index (`6`) is valid within the stacking context of ARTICLE #3 (`z-index: 4`). So SECTION #4 is under ARTICLE #1 because SECTION #4 belongs to ARTICLE #3, which has a lower z-index value (`4-6` is less than `5-0`).

For the same reason, ARTICLE #2 (`z-index: 2`) is rendered under SECTION #5 (`z-index`: 1) because SECTION #5 belongs to ARTICLE #3 (`z-index: 4`), which has a higher z-index value (`2-0` is less than `4-1`).

ARTICLE #3's z-index is `4`, but this value is independent of the `z-index` of three sections nested inside it because they belong to a different stacking context.

In our example (sorted according to the final rendering order):

*   Root
    *   ARTICLE #2: (`z-index`: 2), which results in a rendering order of `2-0`
        
    *   ARTICLE #3: (`z-index`: 4), which results in a rendering order of `4-0`
        
        *   SECTION #5: (`z-index`: 1), stacked under an element (`z-index`: 4), which results in a rendering order of `4-1`
        *   SECTION #6: (`z-index`: 3), stacked under an element (`z-index`: 4), which results in a rendering order of `4-3`
        *   SECTION #4: (`z-index`: 6), stacked under an element (`z-index`: 4), which results in a rendering order of `4-6`
    *   ARTICLE #1: (`z-index`: 5), which results in a rendering order of `5-0`
        

[Additional examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#additional_examples)

--------------------------------------------------------------------------------------------------------------------------------------

Additional examples include a [2-level hierarchy with `z-index` on the last level](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1)
, a [2-level HTML hierarchy, `z-index` on all levels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_2)
, and a [3-level HTML hierarchy, `z-index` on the second level](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Understanding z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Understanding_z-index)
    
*   [Stacking without the `z-index` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)
    
*   [Stacking floating elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements)
    
*   [Using z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index)
    
*   [Top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/positioned_layout/stacking_context/index.md?plain=1 "Folder: en-us/web/css/guides/positioned_layout/stacking_context (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_context&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_context%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_context%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_context%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F15e1155ab8a0587405601cc4753bb789cd6ac47c%0A*+Document+last+modified%3A+2026-09-28T19%3A28%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")