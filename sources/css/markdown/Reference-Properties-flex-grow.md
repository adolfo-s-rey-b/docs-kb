*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#mdn-search)
    

`flex-grow` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex-grow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the flex grow factor, which specifies how much of the flex container's [**positive free space**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios)
, if any, should be assigned to the flex item's [main size](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox#the_flex_model)
.

When the flex-container's main size is larger than the combined main sizes of its flex items, this positive free space can be distributed among the flex items, with each item's growth being their growth factor value as a proportion of the sum total of all the flex items' flex grow factors.

**Note:** It is recommended to use the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 shorthand with a keyword value like `auto` or `initial` instead of setting `flex-grow` on its own. The [keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#values)
 expand to reliable combinations of `flex-grow`, [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
, and [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
, which help to achieve the commonly desired flex behaviors.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#try_it)

-------------------------------------------------------------------------------------------------

    flex-grow: 1;
    

    flex-grow: 2;
    

    flex-grow: 3;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">I grow</div>
      <div>Item Two</div>
      <div>Item Three</div>
    </section>
    

    .default-example {
      border: 1px solid #c5c5c5;
      width: auto;
      max-height: 300px;
      display: flex;
    }
    
    .default-example > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      margin: 10px;
      flex-grow: 1;
      flex-shrink: 1;
      flex-basis: 0;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#syntax)

-------------------------------------------------------------------------------------------------

css

    /* <number> values */
    flex-grow: 3;
    flex-grow: 0.6;
    
    /* Global values */
    flex-grow: inherit;
    flex-grow: initial;
    flex-grow: revert;
    flex-grow: revert-layer;
    flex-grow: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#values)

This property is specified as the following value:

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#number)

See [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. Negative values are invalid. Defaults to 0, which prevents the flex item from growing.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#description)

-----------------------------------------------------------------------------------------------------------

This property specifies how much of the remaining space in the flex container should be assigned to the item (the flex grow factor).

The [main size](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox#the_flex_model)
 is either the width or height of the item, depending on the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 value.

The remaining space, or positive free space, is the size of the flex container minus the size of all flex items' sizes together. If all sibling items have the same flex grow factor, then all items will receive the same share of remaining space. The common practice is to set `flex-grow: 1`, but setting the flex grow factor for all the flex items to `88`, `100`, `1.2`, or any other value greater than `0` will produce the same result: the value is a ratio.

If the `flex-grow` values differ, the positive free space is distributed according to the ratio defined by the different flex grow factors. The `flex-grow` factor values of all the sibling flex items are added together. The flex container's positive free space, if any, is then divided by that total. The main size of each flex item with a `flex-grow` value greater than `0` will grow by this quotient multiplied by its own growth factor.

For example, if four `100px` flex items are in a `700px` container and the flex items have `flex-grow` factors of `0`, `1`, `2`, and `3`, respectively, the total main size of the four items is `400px`, meaning there is `300px` of positive free space to be distributed. The sum of the four grow factors (`0 + 1 + 2 + 3 = 6`) is equal to six. Therefore, each grow factor is equal to `50px` (`300px / 6`). Each flex item is given 50px of free space multiplied by its `flex-grow` factor — so `0`, `50px`, `100px`, and `150px` respectively. The total flex item sizes become `100px`, `150px`, `200px`, and `250px`, respectively.

`flex-grow` is generally used alongside the other [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 shorthand properties, [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
 and [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
. Using the `flex` shorthand property is recommended to ensure all values are set.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | flex items, including in-flow pseudo-elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#formal_syntax)

---------------------------------------------------------------------------------------------------------------

flex-grow =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#examples)

-----------------------------------------------------------------------------------------------------

### [Setting flex item grow factor](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#setting_flex_item_grow_factor)

In this example, the sum of six flex-grow factors is equal to eight, meaning each growth-factor value is `12.5%` of the remaining space.

#### HTML

html

    <h1>This is a <code>flex-grow</code> example</h1>
    <p>
      A, B, C, and F have <code>flex-grow: 1</code> set. D and E have
      <code>flex-grow: 2</code> set.
    </p>
    <div id="content">
      <div class="box1">A</div>
      <div class="box2">B</div>
      <div class="box3">C</div>
      <div class="box4">D</div>
      <div class="box5">E</div>
      <div class="box6">F</div>
    </div>
    

#### CSS

css

    #content {
      display: flex;
    }
    
    div > div {
      border: 3px solid rgb(0 0 0 / 20%);
    }
    
    .box1,
    .box2,
    .box3,
    .box6 {
      flex-grow: 1;
    }
    
    .box4,
    .box5 {
      flex-grow: 2;
      border: 3px solid rgb(0 0 0 / 20%);
    }
    
    .box1 {
      background-color: red;
    }
    .box2 {
      background-color: lightblue;
    }
    .box3 {
      background-color: yellow;
    }
    .box4 {
      background-color: brown;
    }
    .box5 {
      background-color: lightgreen;
    }
    .box6 {
      background-color: brown;
    }
    

#### Result

When the six flex items are distributed along the container's main axis, if the sum of the main content of those flex items is less than the size of the container's main axis, the extra space is distributed among the size flex items, with `A`, `B`, `C`, and `F`, each getting `12.5%` of the remaining space and `D` and `E` each getting `25%` of the extra space.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-grow-property](https://drafts.csswg.org/css-flexbox/#flex-grow-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow#see_also)

-----------------------------------------------------------------------------------------------------

*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
     shorthand
*   [Basic Concepts of Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Controlling Ratios of flex items along the main axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [`flex-grow` is weird. Or is it?](https://css-tricks.com/flex-grow-is-weird/ "External link (opens in new tab)")
     via CSS-Tricks (2017)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-grow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-grow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-grow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-grow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-grow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-grow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")