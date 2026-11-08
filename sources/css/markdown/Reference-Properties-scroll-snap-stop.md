*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#mdn-search)
    

`scroll-snap-stop` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-snap-stop`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines whether or not the scroll container is allowed to "pass over" possible snap positions.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#try_it)

--------------------------------------------------------------------------------------------------------

    scroll-snap-stop: normal;
    

    scroll-snap-stop: always;
    

    <section class="default-example" id="default-example">
      <p class="explanation">
        The effect of this property can be noticed on devices with a touchpad. Try
        to scroll through all items with a single swing. Value
        <b class="keyword">'normal'</b> should pass through all pages, while
        <b class="keyword">'always'</b> will stop at the second page.
      </p>
      <div class="snap-container">
        <div>1</div>
        <div id="example-element">2</div>
        <div>3</div>
      </div>
      <div class="info">Scroll »</div>
    </section>
    

    .default-example {
      flex-direction: column;
    }
    
    .explanation {
      margin-top: 0;
    }
    
    .keyword {
      color: darkorange;
    }
    
    .default-example .info {
      width: 100%;
      padding: 0.5em 0;
      font-size: 90%;
    }
    
    .snap-container {
      text-align: left;
      width: 250px;
      height: 250px;
      overflow-x: scroll;
      display: flex;
      box-sizing: border-box;
      border: 1px solid black;
      scroll-snap-type: x mandatory;
    }
    
    .snap-container > div {
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
    
    .snap-container > div:nth-child(even) {
      background-color: white;
      color: rebeccapurple;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    scroll-snap-stop: normal;
    scroll-snap-stop: always;
    
    /* Global values */
    scroll-snap-stop: inherit;
    scroll-snap-stop: initial;
    scroll-snap-stop: revert;
    scroll-snap-stop: revert-layer;
    scroll-snap-stop: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#normal)

When the visual [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 of this element's scroll container is scrolled, it may "pass over" possible snap positions.

[`always`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#always)

The scroll container must not "pass over" a possible snap position; and must snap to the first of this elements' snap positions.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

scroll-snap-stop =   
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  always    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#examples)

------------------------------------------------------------------------------------------------------------

### [Setting different snap stops](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#setting_different_snap_stops)

The example below demonstrates the contrast between the `always` and `normal` values of `scroll-snap-stop`. The difference in the two `scroll-snap-stop` values is more noticeable when the `scroll-snap-type` property is set to `mandatory`, which is what is used in this example.

#### HTML

html

    <p>scroll-snap-stop: always (X Mandatory)</p>
    <div class="x mandatory-scroll-snapping always-stop">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </div>
    
    <p>scroll-snap-stop: always (X Mandatory) on odd child elements</p>
    <div class="x mandatory-scroll-snapping always-stop-odd">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </div>
    
    <p>scroll-snap-stop: always (X Mandatory) on even child elements</p>
    <div class="x mandatory-scroll-snapping always-stop-even">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </div>
    
    <p>scroll-snap-stop: normal (X Mandatory)</p>
    <div class="x mandatory-scroll-snapping normal-stop">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </div>
    
    <p>scroll-snap-stop: always (Y Mandatory)</p>
    <div class="y mandatory-scroll-snapping always-stop">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </div>
    
    <p>scroll-snap-stop: normal (Y Mandatory)</p>
    <div class="y mandatory-scroll-snapping normal-stop">
      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
    </div>
    

#### CSS

    /* setup */
    body {
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-flow: column nowrap;
      font-family: monospace;
      text-align: center;
    }
    
    div[class] {
      font-size: 3rem;
      display: flex;
      overflow: auto;
      flex: none;
    }
    
    .x {
      width: 50%;
      min-width: 15rem;
      height: 6rem;
      flex-flow: row nowrap;
    }
    
    .y {
      width: 30%;
      min-width: 12rem;
      height: 12rem;
      flex-flow: column nowrap;
    }
    
    div > div {
      flex: none;
      outline: 1px solid #333333;
    }
    
    .x > div {
      width: 90%;
      height: 100%;
    }
    
    .y > div {
      width: 100%;
      height: 80%;
    }
    
    /* coloration */
    div > div:nth-child(even) {
      background-color: #87ea87;
    }
    
    div > div:nth-child(odd) {
      background-color: #87ccea;
    }
    

css

    /* setting up mandatory scroll-snap on parent */
    .x.mandatory-scroll-snapping {
      scroll-snap-type: x mandatory;
    }
    
    .y.mandatory-scroll-snapping {
      scroll-snap-type: y mandatory;
    }
    
    /* defining scroll-snap alignment on children */
    div > div {
      scroll-snap-align: center;
    }
    
    /* defining scroll-snap stop on children */
    .always-stop > div {
      scroll-snap-stop: always;
    }
    
    .always-stop-odd > div:nth-of-type(odd) {
      scroll-snap-stop: always;
    }
    
    .always-stop-even > div:nth-of-type(even) {
      scroll-snap-stop: always;
    }
    
    .normal-stop > div {
      scroll-snap-stop: normal;
    }
    

#### Result

Scroll from left to right and from top to bottom in the X and Y boxes below, respectively. In the X and Y boxes where the `scroll-snap-stop` property is set to `always`, the scrolling is forced to stop at the snap point even when you scroll fast. However, in the boxes where the `scroll-snap-stop` property is set to `normal`, the snap points are skipped when you scroll fast.

If required, you can be selective about the items that are `always` stopped at inside the scroll container. This is demonstrated in the example below by targeting odd and even items; you can choose a different strategy based on your requirement. In the example below, scrolling does not "pass over" odd and even items in the second and third boxes, respectively.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scroll Snap Module Level 1  <br>\# scroll-snap-stop](https://drafts.csswg.org/css-scroll-snap/#scroll-snap-stop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop#see_also)

------------------------------------------------------------------------------------------------------------

*   [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
    
*   [`scroll-initial-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target)
    
*   [CSS scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
     module
*   [Well-controlled scrolling with CSS scroll snap](https://web.dev/articles/css-scroll-snap "External link (opens in new tab)")
     on web.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-snap-stop/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-snap-stop (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-snap-stop&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-snap-stop%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-snap-stop%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-snap-stop%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")