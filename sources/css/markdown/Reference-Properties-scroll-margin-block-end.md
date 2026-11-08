*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#mdn-search)
    

`scroll-margin-block-end` CSS property
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `scroll-margin-block-end` property defines the margin of the scroll snap area at the end of the block dimension that is used for snapping this box to the [snapport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snapport)
. The scroll snap area is determined by taking the transformed border box, finding its rectangular bounding box (axis-aligned in the scroll container's coordinate space), then adding the specified outsets.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#try_it)

---------------------------------------------------------------------------------------------------------------

    scroll-margin-block-end: 0;
    

    scroll-margin-block-end: 20px;
    

    scroll-margin-block-end: 2em;
    

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
      scroll-snap-align: end;
    }
    
    .scroller > div:nth-child(even) {
      background-color: white;
      color: rebeccapurple;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    scroll-margin-block-end: 10px;
    scroll-margin-block-end: 1em;
    
    /* Global values */
    scroll-margin-block-end: inherit;
    scroll-margin-block-end: initial;
    scroll-margin-block-end: revert;
    scroll-margin-block-end: revert-layer;
    scroll-margin-block-end: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

An outset from the block end edge of the scroll container.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

scroll-margin-block-end =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# margin-longhands-logical](https://drafts.csswg.org/css-scroll-snap/#margin-longhands-logical) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-margin-block-end/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-margin-block-end (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-margin-block-end&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-margin-block-end%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-margin-block-end%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-margin-block-end%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")