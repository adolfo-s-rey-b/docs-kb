*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#mdn-search)
    

`flex-shrink` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex-shrink`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the flex shrink factor of a flex item. If the size of all flex items is larger than the flex container, the [flex items can shrink](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios#the_flex-shrink_property)
 to fit according to their `flex-shrink` value. Each flex line's [negative free space](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios#positive_and_negative_free_space)
 is distributed between the line's flex items that have a `flex-shrink` value greater than `0`.

**Note:** It is recommended to use the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 shorthand with a keyword value like `auto` or `initial` instead of setting `flex-shrink` on its own. The [keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex#values)
 expand to reliable combinations of [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
, `flex-shrink`, and [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
, which help to achieve the commonly desired flex behaviors.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#try_it)

---------------------------------------------------------------------------------------------------

    flex-shrink: 0;
    

    flex-shrink: 1;
    

    flex-shrink: 2;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">I shrink</div>
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
      flex-basis: 300px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#syntax)

---------------------------------------------------------------------------------------------------

css

    /* <number> values */
    flex-shrink: 2;
    flex-shrink: 0.6;
    
    /* Global values */
    flex-shrink: inherit;
    flex-shrink: initial;
    flex-shrink: revert;
    flex-shrink: revert-layer;
    flex-shrink: unset;
    

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#values)

---------------------------------------------------------------------------------------------------

This property is specified as the following value:

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#number)

See [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. Negative values are invalid. Defaults to 1.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#description)

-------------------------------------------------------------------------------------------------------------

The `flex-shrink` property specifies the flex shrink factor, which determines how much the flex item will shrink relative to the rest of the flex items in the flex container when negative free space is distributed.

This property deals with situations where the browser calculates the flex-basis values of the flex items, and finds that they are too large to fit into the flex container. As long as flex-shrink has a positive value the items will shrink in order that they do not overflow the container.

The `flex-grow` property deals with distributing available positive free space proportional to each item's flex grow factor, with the value of the `flex-grow` property as the only consideration. The `flex-shrink` property manages removing negative free space to make boxes fit into their container without overflowing. Removing space is a bit more complicated than adding space. The flex shrink factor is multiplied by the flex base size; this distributes negative space in proportion to how much the item can shrink. This prevents smaller items from shrinking to `0px` before a larger item is noticeably reduced.

Generally, `flex-shrink` is used alongside the [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 and [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
 properties. Within the `flex` shorthand, the shrink factor is always the second `<number>`. If the shorthand only includes one number value, that value is assumed to be the `flex-grow` value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | flex items, including in-flow pseudo-elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

flex-shrink =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#examples)

-------------------------------------------------------------------------------------------------------

### [Setting flex item shrink factor](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#setting_flex_item_shrink_factor)

This example demonstrates how negative free space is distributed based on the item's shrink factor. It includes five flex items with a `flex-shrink` value greater than 0, which have a combined width greater than their parent flex container's width.

#### HTML

html

    <div id="content">
      <div class="box1">A</div>
      <div class="box2">B</div>
      <div class="box3">C</div>
      <div class="box4">D</div>
      <div class="box5">E</div>
    </div>
    

#### CSS

We give each flex item a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 of `200px`. As the [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
 property defaults to `auto`, each item's flex-basis is `200px`. This gives the flex items a total width of `1000px`, twice the size of the container. We set all flex items to be shrinkable, with `flex-shrink` values greater than `0`. The last two items have greater `flex-shrink` values set so they will shrink more.

css

    #content {
      display: flex;
      width: 500px;
    }
    
    #content div {
      width: 200px;
    }
    
    .box1,
    .box2,
    .box3 {
      flex-shrink: 1;
    }
    
    .box4 {
      flex-shrink: 1.5;
    }
    
    .box5 {
      flex-shrink: 2;
    }
    

    #content {
      margin: 5px;
    }
    div {
      font-family: monospace;
      outline: 1px solid;
      line-height: 4em;
      text-align: center;
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
      background-color: lightsalmon;
    }
    .box5 {
      background-color: lightgreen;
    }
    

#### Result

The flex items don't overflow their container because they can shrink: the `500px` of negative free space is distributed among the five items based on their `flex-shrink` values. The total of all the shrink values for the five items is `1 + 1 + 1 + 1.5 + 2` = `6.5`. As a result, the width of items with `flex-shrink: 1` is reduced by `1/6.5 * 500px` = `76.92px`, the width of items with `flex-shrink: 1.5` is reduced by `1.5/6.5 * 500px` = `115.38px`, and the width of items with `flex-shrink: 2` is reduced by `2/6.5 * 500px` = `153.85px`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-shrink-property](https://drafts.csswg.org/css-flexbox/#flex-shrink-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink#see_also)

-------------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Controlling ratios of flex items along the main axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 31, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-shrink/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-shrink (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-shrink&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-shrink%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-shrink%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-shrink%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fefbef0da1dbe29be125eb7db0b831a4e4bd9220d%0A*+Document+last+modified%3A+2026-08-31T16%3A51%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")