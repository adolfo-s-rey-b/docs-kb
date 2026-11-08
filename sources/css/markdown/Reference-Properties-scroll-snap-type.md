*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#mdn-search)
    

`scroll-snap-type` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-snap-type`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is set on a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
, opting it into scroll snapping by setting the direction and strictness of snap point enforcement within the [snap port](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snapport)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#try_it)

--------------------------------------------------------------------------------------------------------

    scroll-snap-type: none;
    

    scroll-snap-type: x mandatory;
    

    scroll-snap-type: x proximity;
    

    <section class="default-example" id="default-example">
      <div id="example-element">
        <div>1</div>
        <div>2</div>
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
    
    #example-element {
      text-align: left;
      width: 250px;
      height: 250px;
      overflow-x: scroll;
      display: flex;
      box-sizing: border-box;
      border: 1px solid black;
    }
    
    #example-element > div {
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
    
    #example-element > div:nth-child(even) {
      background-color: white;
      color: rebeccapurple;
    }
    

If the content in the scroll port changes — for example, if content is added, moved, deleted, or resized — the scroll container will re-snap to the previously snapped content if that content is still present.

If the value of a scroll snap-related property, such as `scroll-snap-type` or [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
, is changed, the scroll container will re-snap based on the current value of `scroll-snap-type`.

Specifying any precise animations or physics used to enforce those snap points is not covered by this property but instead left up to the user agent.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* No snapping */
    scroll-snap-type: none;
    
    /* Keyword values for snap axes */
    scroll-snap-type: x;
    scroll-snap-type: y;
    scroll-snap-type: block;
    scroll-snap-type: inline;
    scroll-snap-type: both;
    
    /* Optional keyword values for snap strictness */
    /* mandatory | proximity */
    scroll-snap-type: x mandatory;
    scroll-snap-type: y proximity;
    scroll-snap-type: both mandatory;
    
    /* Global values */
    scroll-snap-type: inherit;
    scroll-snap-type: initial;
    scroll-snap-type: revert;
    scroll-snap-type: revert-layer;
    scroll-snap-type: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#values)

This property is specified as one or two of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#none)

When the visual [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 of this scroll container is scrolled, it must ignore snap points.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#x)

The scroll container snaps to snap positions in its horizontal axis only.

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#y)

The scroll container snaps to snap positions in its vertical axis only.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#block)

The scroll container snaps to snap positions in its block axis only.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#inline)

The scroll container snaps to snap positions in its inline axis only.

[`both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#both)

The scroll container snaps to snap positions in both of its axes independently (potentially snapping to different elements in each axis).

[`mandatory`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#mandatory)

The visual viewport of this scroll container must snap to a snap position if it isn't currently scrolled.

[`proximity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#proximity)

The visual viewport of this scroll container may snap to a snap position if it isn't currently scrolled. The user agent decides if it snaps or not based on scroll parameters. This is the default snap strictness if any snap axis is specified.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

scroll-snap-type =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 x [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 block [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 both [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 pair [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 mandatory [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 proximity [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#examples)

------------------------------------------------------------------------------------------------------------

### [Snapping in different axes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#snapping_in_different_axes)

#### HTML

html

    <main>
      <section class="x mandatory-scroll-snapping" dir="ltr">
        <div>X Mand. LTR</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="x proximity-scroll-snapping" dir="ltr">
        <div>X Prox. LTR</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="y mandatory-scroll-snapping" dir="ltr">
        <div>Y Mand. LTR</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="y proximity-scroll-snapping" dir="ltr">
        <div>Y Prox. LTR</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="x mandatory-scroll-snapping" dir="rtl">
        <div>X Mand. RTL</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="x proximity-scroll-snapping" dir="rtl">
        <div>X Prox. RTL</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="y mandatory-scroll-snapping" dir="rtl">
        <div>Y Mand. RTL</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
      <section class="y proximity-scroll-snapping" dir="rtl">
        <div>Y Prox. RTL</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div>5</div>
      </section>
    </main>
    

#### CSS

    main {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-flow: column nowrap;
      font-family: monospace;
    }
    section {
      display: flex;
      margin: 1em auto;
      outline: 1px dashed lightgray;
      flex: none;
      overflow: auto;
    }
    .x {
      width: 100%;
      height: 128px;
      flex-flow: row nowrap;
      overflow-y: hidden;
    }
    .y {
      width: 256px;
      height: 256px;
      flex-flow: column nowrap;
      overflow-x: hidden;
    }
    

css

    /* scroll-snap */
    .x.mandatory-scroll-snapping {
      scroll-snap-type: x mandatory;
    }
    .x.proximity-scroll-snapping {
      scroll-snap-type: x proximity;
    }
    .y.mandatory-scroll-snapping {
      scroll-snap-type: y mandatory;
    }
    .y.proximity-scroll-snapping {
      scroll-snap-type: y proximity;
    }
    
    div {
      text-align: center;
      scroll-snap-align: center;
      flex: none;
    }
    

    .x div {
      line-height: 128px;
      font-size: 64px;
      width: 100%;
      height: 128px;
    }
    .y div {
      line-height: 256px;
      font-size: 128px;
      width: 256px;
      height: 100%;
    }
    
    /* appearance fixes */
    .y div:first-child {
      line-height: 1.3;
      font-size: 64px;
    }
    
    /* coloration */
    div:nth-child(even) {
      background-color: #87ea87;
    }
    div:nth-child(odd) {
      background-color: #87ccea;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# scroll-snap-type](https://drafts.csswg.org/css-scroll-snap/#scroll-snap-type) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type#see_also)

------------------------------------------------------------------------------------------------------------

*   Other scroll port properties: [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
    , [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
    
*   Scroll-child properties: [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
    , [`scroll-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
    , [`scroll-snap-stop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
    
*   [Basic concepts of CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Basic_concepts)
    
*   [Using scroll snap events](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap/Using_scroll_snap_events)
    
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-snap-type/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-snap-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-snap-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-snap-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-snap-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-snap-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")