*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#mdn-search)
    

`position` CSS property
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how an element is positioned in a document. The [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
, [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
, and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 physical properties and the [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
, [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
, [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
, and [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
 flow-relative logical properties can be used to determine the final location of positioned elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#try_it)

------------------------------------------------------------------------------------------------

    position: static;
    

    position: relative;
    top: 40px;
    left: 40px;
    

    position: absolute;
    inset-inline-start: 40px;
    inset-block-start: 40px;
    

    position: sticky;
    top: 20px;
    

    <section class="default-example" id="default-example">
      <div id="example-element-container">
        <p>
          In this demo you can control the <code>position</code> property for the
          yellow box.
        </p>
        <div class="box"></div>
        <div class="box" id="example-element"></div>
        <div class="box"></div>
        <p class="clear">
          To see the effect of <code>sticky</code> positioning, select the
          <code>position: sticky</code> option and scroll this container.
        </p>
        <p>
          The element will scroll along with its container, until it is at the top
          of the container (or reaches the offset specified in <code>top</code>),
          and will then stop scrolling, so it stays visible.
        </p>
        <p>
          The rest of this text is only supplied to make sure the container
          overflows, so as to enable you to scroll it and see the effect.
        </p>
        <hr />
        <p>
          Far out in the uncharted backwaters of the unfashionable end of the
          western spiral arm of the Galaxy lies a small unregarded yellow sun.
          Orbiting this at a distance of roughly ninety-two million miles is an
          utterly insignificant little blue green planet whose ape-descended life
          forms are so amazingly primitive that they still think digital watches are
          a pretty neat idea.
        </p>
      </div>
    </section>
    

    section {
      align-items: flex-start;
      overflow: auto;
    }
    
    .box {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      float: left;
      width: 65px;
      height: 65px;
    }
    
    .box + .box {
      margin-left: 10px;
    }
    
    .clear {
      clear: both;
      padding-top: 1em;
    }
    
    #example-element-container {
      position: relative;
      text-align: left;
    }
    
    #example-element {
      background-color: yellow;
      border: 3px solid red;
      z-index: 1;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#syntax)

------------------------------------------------------------------------------------------------

css

    position: static;
    position: relative;
    position: absolute;
    position: fixed;
    position: sticky;
    
    /* Global values */
    position: inherit;
    position: initial;
    position: revert;
    position: revert-layer;
    position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#values)

This property is specified as one of the following keyword values:

[`static`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#static)

The element is positioned according to the [Normal Flow](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction#normal_layout_flow)
 of the document. The [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
, [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
, [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
, and [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
 properties have _no effect_. This is the default value.

[`relative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#relative)

The element is positioned according to the normal flow of the document, and then offset _relative to itself_ based on the values of `top`, `right`, `bottom`, and `left`. The offset does not affect the position of any other elements; thus, the space given for the element in the page layout is the same as if position were `static`.

This value creates a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
 when the value of `z-index` is not `auto`. Its effect on `table-*-group`, `table-row`, `table-column`, `table-cell`, and `table-caption` elements is undefined.

[`absolute`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#absolute)

The element is removed from the normal document flow, and no space is created for the element in the page layout. The element is positioned relative to its closest positioned ancestor (if any) or to the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#identifying_the_containing_block)
. Its final position is determined by the values of `top`, `right`, `bottom`, and `left`.

This value creates a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
 when the value of `z-index` is not `auto`. The margins of absolutely positioned boxes do not [collapse](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
 with other margins.

[`fixed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#fixed)

The element is removed from the normal document flow, and no space is created for the element in the page layout. The element is positioned relative to its initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#identifying_the_containing_block)
, which is the viewport in the case of visual media. Its final position is determined by the values of `top`, `right`, `bottom`, and `left`.

This value always creates a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
. In printed documents, the element is placed in the same position on _every page_.

[`sticky`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#sticky)

The element is positioned according to the normal flow of the document, and then offset relative to its _nearest scrolling ancestor_ and [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 (nearest block-level ancestor), including table-related elements, based on the values of `top`, `right`, `bottom`, and `left`. The offset does not affect the position of any other elements.

This value always creates a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
. Note that a sticky element "sticks" to its nearest ancestor that has a "scrolling mechanism" (created when `overflow` is `hidden`, `scroll`, `auto`, or `overlay`), even if that ancestor isn't the nearest actually scrolling ancestor.

**Note:** At least one [inset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
 property ([`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
, [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
, etc.) needs to be set to a non-`auto` value for the axis on which the element needs to be made sticky. If both `inset` properties for an axis are set to `auto`, on that axis the `sticky` value will behave as `relative`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#description)

----------------------------------------------------------------------------------------------------------

### [Types of positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#types_of_positioning)

*   A **positioned element** is an element whose [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     `position` value is either `relative`, `absolute`, `fixed`, or `sticky`. (In other words, it's anything except `static`.)
*   A **relatively positioned element** is an element whose [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     `position` value is `relative`. The [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
     and [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
     properties specify the vertical offset from its normal position; the [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
     and [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
     properties specify the horizontal offset.
*   An **absolutely positioned element** is an element whose [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     `position` value is `absolute` or `fixed`. The [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    , [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    , [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    , and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
     properties specify offsets from the edges of the element's [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
    . (The containing block is the ancestor relative to which the element is positioned.) If the element has margins, they are added to the offset. The element establishes a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
     (BFC) for its contents.
*   A **stickily positioned element** is an element whose [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     `position` value is `sticky`. It's treated as relatively positioned until its [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
     crosses a specified threshold (such as setting [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
     to value other than auto) within its flow root (or the container it scrolls within), at which point it is treated as "stuck" until meeting the opposite edge of its [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
    .

Most of the time, absolutely positioned elements that have [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 and [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 set to `auto` are sized so as to fit their contents. However, non-[replaced](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, absolutely positioned elements can be made to fill the available vertical space by specifying both [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 and [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
 and leaving [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 unspecified (that is, `auto`). They can likewise be made to fill the available horizontal space by specifying both [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 and [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
 and leaving [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 as `auto`.

Except for the case just described (of absolutely positioned elements filling the available space):

*   If both `top` and `bottom` are specified (technically, not `auto`), `top` wins.
*   If both `left` and `right` are specified, `left` wins when [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
     is `ltr` (English, horizontal Japanese, etc.) and `right` wins when [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
     is `rtl` (Persian, Arabic, Hebrew, etc.).

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#accessibility)

--------------------------------------------------------------------------------------------------------------

Ensure that elements positioned with an `absolute` or `fixed` value do not obscure other content when the page is zoomed to increase text size.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Visual Presentation: Understanding SC 1.4.8 | Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-visual-presentation.html "External link (opens in new tab)")
    

### [Performance & Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#performance_accessibility)

Scrolling elements containing `fixed` or `sticky` content can cause performance and accessibility issues. As a user scrolls, the browser must repaint the sticky or fixed content in a new location. Depending on the content needing to be repainted, the browser performance, and the device's processing speed, the browser may not be able to manage repaints at 60 fps. Such a scenario can lead to [jank](https://developer.mozilla.org/en-US/docs/Glossary/Jank)
 and, more importantly, accessibility concerns for people with sensitivities. One solution is to add [`will-change: transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
 to the positioned elements to render the element in its own layer, improving repaint speed and therefore improving performance and accessibility.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `static` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#formal_syntax)

--------------------------------------------------------------------------------------------------------------

position =   
  static       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  relative     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  absolute     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sticky       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <running()>    
  
<running()> =   
  running( [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#examples)

----------------------------------------------------------------------------------------------------

### [Relative positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#relative_positioning)

Relatively positioned elements are offset a given amount from their normal position within the document, but without the offset affecting other elements. In the example below, note how the other elements are placed as if "Two" were taking up the space of its normal location.

#### HTML

html

    <div class="box" id="one">One</div>
    <div class="box" id="two">Two</div>
    <div class="box" id="three">Three</div>
    <div class="box" id="four">Four</div>
    

#### CSS

css

    * {
      box-sizing: border-box;
    }
    
    .box {
      display: inline-block;
      width: 100px;
      height: 100px;
      background: red;
      color: white;
    }
    
    #two {
      position: relative;
      top: 20px;
      left: 20px;
      background: blue;
    }
    

### [Absolute positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#absolute_positioning)

Elements that are relatively positioned remain in the normal flow of the document. In contrast, an element that is absolutely positioned is taken out of the flow; thus, other elements are positioned as if it did not exist. The absolutely positioned element is positioned relative to its _nearest positioned ancestor_ (i.e., the nearest ancestor that is not `static`). If a positioned ancestor doesn't exist, it is positioned relative to the ICB ([initial containing block](https://drafts.csswg.org/css-display/#initial-containing-block "External link (opens in new tab)")
), which is the containing block of the document's root element.

#### HTML

html

    <h1>Absolute positioning</h1>
    
    <p>
      I am a basic block level element. My adjacent block level elements sit on new
      lines below me.
    </p>
    
    <p class="positioned">
      By default we span 100% of the width of our parent element, and we are as tall
      as our child content. Our total width and height is our content + padding +
      border width/height.
    </p>
    
    <p>
      We are separated by our margins. Because of margin collapsing, we are
      separated by the width of one of our margins, not both.
    </p>
    
    <p>
      inline elements <span>like this one</span> and <span>this one</span> sit on
      the same line as one another, and adjacent text nodes, if there is space on
      the same line. Overflowing inline elements
      <span>wrap onto a new line if possible — like this one containing text</span>,
      or just go on to a new line if not, much like this image will do:
      <img src="https://mdn.github.io/shared-assets/images/examples/long.jpg" />
    </p>
    

#### CSS

css

    * {
      box-sizing: border-box;
    }
    
    body {
      width: 500px;
      margin: 0 auto;
    }
    
    p {
      background: aqua;
      border: 3px solid blue;
      padding: 10px;
      margin: 10px;
    }
    
    span {
      background: red;
      border: 1px solid black;
    }
    
    .positioned {
      position: absolute;
      background: yellow;
      inset-block-start: 30px;
      inset-inline-start: 30px;
    }
    

#### Result

### [Fixed positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#fixed_positioning)

Fixed positioning is similar to absolute positioning, with the exception that the element's [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 is the initial containing block established by the _viewport_, unless any ancestor has `transform`, `perspective`, or `filter` property set to something other than `none` (see [fixed positioning containing block](https://drafts.csswg.org/css-position/#fixed-positioning-containing-block "External link (opens in new tab)")
), which then causes that ancestor to take the place of the elements [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
. This can be used to create a "floating" element that stays in the same position regardless of scrolling. In the example below, box "One" is fixed at 80 pixels from the top of the page and 10 pixels from the left. Even after scrolling, it remains in the same place relative to the viewport. Also, when the [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
 property is set to `transform`, a new containing block is established.

#### HTML

html

    <div class="outer">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam congue tortor
        eget pulvinar lobortis. Vestibulum ante ipsum primis in faucibus orci luctus
        et ultrices posuere cubilia Curae; Nam ac dolor augue. Pellentesque mi mi,
        laoreet et dolor sit amet, ultrices varius risus. Nam vitae iaculis elit.
        Aliquam mollis interdum libero. Sed sodales placerat egestas. Vestibulum ut
        arcu aliquam purus viverra dictum vel sit amet mi. Duis nisl mauris, aliquam
        sit amet luctus eget, dapibus in enim. Sed velit augue, pretium a sem
        aliquam, congue porttitor tortor. Sed tempor nisl a lorem consequat, id
        maximus erat aliquet. Sed sagittis porta libero sed condimentum. Aliquam
        finibus lectus nec ante congue rutrum. Curabitur quam quam, accumsan id
        ultrices ultrices, tempor et tellus.
      </p>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam congue tortor
        eget pulvinar lobortis. Vestibulum ante ipsum primis in faucibus orci luctus
        et ultrices posuere cubilia Curae; Nam ac dolor augue. Pellentesque mi mi,
        laoreet et dolor sit amet, ultrices varius risus. Nam vitae iaculis elit.
        Aliquam mollis interdum libero. Sed sodales placerat egestas. Vestibulum ut
        arcu aliquam purus viverra dictum vel sit amet mi. Duis nisl mauris, aliquam
        sit amet luctus eget, dapibus in enim. Sed velit augue, pretium a sem
        aliquam, congue porttitor tortor. Sed tempor nisl a lorem consequat, id
        maximus erat aliquet. Sed sagittis porta libero sed condimentum. Aliquam
        finibus lectus nec ante congue rutrum. Curabitur quam quam, accumsan id
        ultrices ultrices, tempor et tellus.
      </p>
      <div class="box" id="one">One</div>
    </div>
    

#### CSS

css

    * {
      box-sizing: border-box;
    }
    
    .box {
      width: 100px;
      height: 100px;
      background: red;
      color: white;
    }
    
    #one {
      position: fixed;
      top: 80px;
      left: 10px;
      background: blue;
    }
    
    .outer {
      width: 500px;
      height: 300px;
      overflow: scroll;
      padding-left: 150px;
    }
    

#### Result

### [Sticky positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#sticky_positioning)

The following CSS rule positions the element with id `one` relatively until the viewport is scrolled such that the element is 10 pixels from the top. Beyond that threshold, the element is fixed to 10 pixels from the top.

css

    #one {
      position: sticky;
      top: 10px;
    }
    

#### List with sticky headings

A common use for sticky positioning is for the headings in an alphabetized list. The "B" heading will appear just below the items that begin with "A" until they are scrolled offscreen. Rather than sliding offscreen with the rest of the content, the "B" heading will then remain fixed to the top of the viewport until all the "B" items have scrolled offscreen, at which point it will be covered up by the "C" heading, and so on.

You must specify a threshold with at least one of `top`, `right`, `bottom`, or `left` for sticky positioning to behave as expected. Otherwise, it will be indistinguishable from relative positioning.

##### HTML

html

    <dl>
      <div>
        <dt>A</dt>
        <dd>Andrew W.K.</dd>
        <dd>Apparat</dd>
        <dd>Arcade Fire</dd>
        <dd>At The Drive-In</dd>
        <dd>Aziz Ansari</dd>
      </div>
      <div>
        <dt>C</dt>
        <dd>Chromeo</dd>
        <dd>Common</dd>
        <dd>Converge</dd>
        <dd>Crystal Castles</dd>
        <dd>Cursive</dd>
      </div>
      <div>
        <dt>E</dt>
        <dd>Explosions In The Sky</dd>
      </div>
      <div>
        <dt>T</dt>
        <dd>Ted Leo &amp; The Pharmacists</dd>
        <dd>T-Pain</dd>
        <dd>Thrice</dd>
        <dd>TV On The Radio</dd>
        <dd>Two Gallants</dd>
      </div>
    </dl>
    

##### CSS

css

    * {
      box-sizing: border-box;
    }
    
    dl > div {
      background: white;
      padding-top: 24px;
    }
    
    dt {
      background: #b8c1c8;
      border-bottom: 1px solid #989ea4;
      border-top: 1px solid #717d85;
      color: white;
      font:
        bold 18px/21px "Helvetica",
        "Arial",
        sans-serif;
      margin: 0;
      padding: 2px 0 0 12px;
      position: -webkit-sticky;
      position: sticky;
      top: -1px;
    }
    
    dd {
      font:
        bold 20px/45px "Helvetica",
        "Arial",
        sans-serif;
      margin: 0;
      padding-left: 12px;
      white-space: nowrap;
    }
    
    dd + dd {
      border-top: 1px solid #cccccc;
    }
    

##### Result

#### Sticky position with all the inset boundaries set

The following example demonstrates an element's behavior when all inset boundaries are set. Here, we have two light bulb emojis in a paragraph. The light bulbs use sticky positioning, and the inset boundaries are specified as 50px from the top and bottom, and 100px from the left and right. A gray background on the parent div element marks the inset area.

##### HTML

html

    Use scrollbars to put the light bulbs(💡) in the right place in the following
    text:
    <div>
      <p>
        The representation of an idea by a light bulb(<span class="bulb">💡</span>)
        is a commonly used metaphor that symbolizes the moment of inspiration or the
        birth of a new idea. The association between a light bulb and an idea can be
        traced back to the invention of the incandescent light bulb(<span
          class="bulb"
          >💡</span
        >) by Thomas Edison in the late 19th century. The light bulb is a powerful
        symbol because it represents illumination, clarity, and the sudden
        brightening of one's thoughts or understanding. When someone has an idea, it
        is often described as a light bulb turning on in their mind, signifying a
        moment of insight or creativity. The image of a light bulb also suggests the
        idea of energy, power, and the potential for growth and development.
      </p>
    </div>
    

##### CSS

    div {
      width: 400px;
      height: 200px;
      overflow: scroll;
      scrollbar-width: thin;
      font-size: 16px;
      font-family: "Verdana";
      border: 1px solid;
    }
    
    p {
      width: 600px;
      user-select: none;
      margin: 0;
      border: 110px solid transparent;
    }
    

css

    .bulb {
      position: sticky;
      inset: 50px 100px;
    }
    
    div {
      /* mark area defined by the inset boundaries using gray color */
      background: linear-gradient(#99999999, #99999999) 100px 50px / 192px 100px
        no-repeat;
    }
    

##### Result

When you put both bulbs in their proper place, you'll notice that they are relatively positioned inside the inset area. When you move them out of the inset area, they are fixed (sticky) to the inset boundary in that direction.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Positioned Layout Module Level 3  <br>\# position-property](https://drafts.csswg.org/css-position/#position-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#see_also)

----------------------------------------------------------------------------------------------------

*   [Inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
    
*   [Learn CSS: Positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)
    
*   [Inset properties for positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#example_inset_properties_for_positioned_layout)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     modules

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")