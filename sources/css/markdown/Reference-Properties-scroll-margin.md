*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#mdn-search)
    

`scroll-margin` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-margin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets all of the scroll margins of an element at once, assigning values much like the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 property does for margins of an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#try_it)

-----------------------------------------------------------------------------------------------------

    scroll-margin: 0;
    

    scroll-margin: 20px;
    

    scroll-margin: 2em;
    

    <section class="default-example" id="default-example">
      <div class="scroller">
        <div>1</div>
        <div id="example-element">2</div>
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
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`scroll-margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-bottom)
    
*   [`scroll-margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-left)
    
*   [`scroll-margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-right)
    
*   [`scroll-margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-top)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* <length> values */
    scroll-margin: 10px;
    scroll-margin: 1em 0.5em 1em 1em;
    
    /* Global values */
    scroll-margin: inherit;
    scroll-margin: initial;
    scroll-margin: revert;
    scroll-margin: revert-layer;
    scroll-margin: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

An outset from the corresponding edge of the scroll container.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#description)

---------------------------------------------------------------------------------------------------------------

You can see the effect of `scroll-margin` by scrolling to a point partway between two of the "pages" of the example's content. The value specified for `scroll-margin` determines how much of the page that's primarily outside the [snapport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snapport)
 should remain visible.

Thus, the `scroll-margin` values represent outsets defining the scroll snap area that is used for snapping this box to the snapport. The scroll snap area is determined by taking the transformed border box, finding its rectangular bounding box (axis-aligned in the scroll container's coordinate space), then adding the specified outsets.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`scroll-margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-bottom)<br>    : `0`<br>*   [`scroll-margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-left)<br>    : `0`<br>*   [`scroll-margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-right)<br>    : `0`<br>*   [`scroll-margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-top)<br>    : `0` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`scroll-margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-bottom)<br>    : as specified<br>*   [`scroll-margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-left)<br>    : as specified<br>*   [`scroll-margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-right)<br>    : as specified<br>*   [`scroll-margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-top)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

scroll-margin =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#examples)

---------------------------------------------------------------------------------------------------------

### [Basic demonstration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#basic_demonstration)

This example implements something very similar to the interactive example above, except that here we'll explain to you how it's implemented.

The aim here is to create four horizontally-scrolling blocks, the second and third of which snap into place, near but not quite at the left of each block.

#### HTML

The HTML includes a scroller with four children:

html

    <div class="scroller">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
    </div>
    

#### CSS

Let's walk through the CSS. The outer container is styled like this:

css

    .scroller {
      text-align: left;
      width: 250px;
      height: 250px;
      overflow-x: scroll;
      display: flex;
      box-sizing: border-box;
      border: 1px solid black;
      scroll-snap-type: x mandatory;
    }
    

The main parts relevant to the scroll snapping are `overflow-x: scroll`, which makes sure the contents will scroll and not be hidden, and `scroll-snap-type: x mandatory`, which dictates that scroll snapping must occur along the horizontal axis, and the scrolling will always come to rest on a snap point.

The child elements are styled as follows:

css

    .scroller > div {
      flex: 0 0 250px;
      width: 250px;
      background-color: rebeccapurple;
      color: white;
      font-size: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      scroll-snap-align: start;
    }
    
    .scroller > div:nth-child(2n) {
      background-color: white;
      color: rebeccapurple;
    }
    

The most relevant part here is `scroll-snap-align: start`, which specifies that the left-hand edges (the "starts" along the x axis, in our case) are the designated snap points.

Last of all we specify the scroll margin-values, a different one for the second and third child elements:

css

    .scroller > div:nth-child(2) {
      scroll-margin: 1rem;
    }
    
    .scroller > div:nth-child(3) {
      scroll-margin: 2rem;
    }
    

This means that when scrolling past the middle child elements, the scrolling will snap to `1rem` outside the left edge of the second `<div>`, and `2rems` outside the left edge of the third `<div>`.

**Note:** Here we are setting `scroll-margin` on all sides at once, but only the start edge is really relevant. It would work just as well here to only set a scroll margin on that one edge, for example with `scroll-margin-inline-start: 1rem`, or `scroll-margin: 0 0 0 1rem`.

#### Result

Try it for yourself:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# scroll-margin](https://drafts.csswg.org/css-scroll-snap/#scroll-margin) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin#see_also)

---------------------------------------------------------------------------------------------------------

*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-margin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-margin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-margin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-margin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-margin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-margin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")