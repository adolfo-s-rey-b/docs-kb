*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#mdn-search)
    

`scroll-margin-inline-start` CSS property
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `scroll-margin-inline-start` property defines the margin of the scroll snap area at the start of the inline dimension that is used for snapping this box to the [snapport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snapport)
. The scroll snap area is determined by taking the transformed border box, finding its rectangular bounding box (axis-aligned in the scroll container's coordinate space), then adding the specified outsets.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#try_it)

------------------------------------------------------------------------------------------------------------------

    scroll-margin-inline-start: 0;
    

    scroll-margin-inline-start: 20px;
    

    scroll-margin-inline-start: 2em;
    

    <section class="default-example" id="default-example">
      <div class="scroller">
        <div>1</div>
        <div id="example-element">2</div>
        <div>3</div>
      </div>
      <div class="info">Scroll »</div>
    </section>
    

    .default-example {
      flex-wrap: wrap;
    }
    
    .default-example .info {
      width: 100%;
      padding: 0.5em 0;
      font-size: 90%;
    }
    
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
    
    .scroller > div:nth-child(even) {
      background-color: white;
      color: rebeccapurple;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#syntax)

------------------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    scroll-margin-inline-start: 10px;
    scroll-margin-inline-start: 1em;
    
    /* Global values */
    scroll-margin-inline-start: inherit;
    scroll-margin-inline-start: initial;
    scroll-margin-inline-start: revert;
    scroll-margin-inline-start: revert-layer;
    scroll-margin-inline-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

An outset from the inline start edge of the scroll container.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------------

scroll-margin-inline-start =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#examples)

----------------------------------------------------------------------------------------------------------------------

### [Basic demonstration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#basic_demonstration)

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
      scroll-margin-inline-start: 1rem;
    }
    
    .scroller > div:nth-child(3) {
      scroll-margin-inline-start: 2rem;
    }
    

This means that when scrolling past the middle child elements, the scrolling will snap to `1rem` outside the inline start edge of the second `<div>`, and `2rems` outside the inline start edge of the third `<div>`.

#### Result

Try it for yourself:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# margin-longhands-logical](https://drafts.csswg.org/css-scroll-snap/#margin-longhands-logical) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-margin-inline-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-margin-inline-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-margin-inline-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-margin-inline-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-margin-inline-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-margin-inline-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")