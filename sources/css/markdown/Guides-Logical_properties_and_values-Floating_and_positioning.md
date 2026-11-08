*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#mdn-search)
    

Logical properties for floating and positioning
===============================================

The [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module contains logical mappings for the physical values of [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
 and [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
, and also for the positioning properties used with [positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
. This guide takes a look at how to use these.

[Mapped properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#mapped_properties_and_values)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The table below details the [logical properties](https://developer.mozilla.org/en-US/docs/Glossary/Logical_properties)
 and values discussed in this guide along with their [physical properties](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
 and values mappings. They assume a horizontal [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, with a left-to-right direction.

| Logical property or value | Physical property or value |
| --- | --- |
| [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)<br>: inline-start | [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)<br>: left |
| [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)<br>: inline-end | [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)<br>: right |
| [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)<br>: inline-start | [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)<br>: left |
| [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)<br>: inline-end | [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)<br>: right |
| [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start) | [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left) |
| [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end) | [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right) |
| [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start) | [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top) |
| [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end) | [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom) |
| [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)<br>: start | [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)<br>: left |
| [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)<br>: end | [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)<br>: right |

In addition to these mapped properties, there are some additional shorthand properties made possible by being able to address block and inline dimensions. These have no mapping to physical properties, aside from the [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
 property.

| Logical property | Purpose |
| --- | --- |
| [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline) | Sets both of the above inset values for the inline dimension simultaneously. |
| [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block) | Sets both of the above inset values for the block dimension simultaneously. |
| [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset) | Sets all four inset values simultaneously with physical mapping of multi-value. |

[Float and clear example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#float_and_clear_example)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

The physical values used with the [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
 and [`clear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
 properties are `left`, `right` and `both`. The CSS logical properties and values module defines the values `inline-start` and `inline-end` as mappings for `left` and `right`.

In the example below, the first box is floated with `float: left`, and the second with `float: inline-start`. If you apply `direction: rtl` to the `.inner` selector, the left-floated box always stays on the left, whereas the `inline-start`\-floated item follows the `direction` of the text. You can combine this with `writing-mode: vertical-rl` to see the difference of block layout in combination with `direction` values.

html

    <div class="container">
      <div class="inner">
        <div class="physical box"></div>
        Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
        kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus winter
        purslane kale.
      </div>
      <div class="inner">
        <div class="logical box"></div>
        Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
        kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus winter
        purslane kale.
      </div>
    </div>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .container {
      display: flex;
    }
    
    .box {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      padding: 10px;
      margin: 10px;
      width: 100px;
      height: 100px;
    }
    

css

    .inner {
      /* direction: rtl; */
      /* writing-mode: vertical-rl; */
    }
    
    .physical {
      float: left;
    }
    
    .logical {
      float: inline-start;
    }
    

[Example: Inset properties for positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#example_inset_properties_for_positioned_layout)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CSS positioning generally allows us to position an element in a manner relative to its containing block — we essentially inset the item relative to where it would fall based on normal flow. To position an element relative to the viewport, use the physical properties [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
, [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
, [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
 and [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
. When you want the positioning to relate to the flow of text in your writing mode, use [`inset-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
, [`inset-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
, [`inset-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
 and [`inset-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
 instead.

These properties take a length or a percentage as a value, and relate to the user's screen dimensions.

In the below example, the `inset-block-start` and `inset-inline-end` properties are used to position the blue box using absolute positioning inside the area with the gray dotted border, which has `position: relative`. Change the `writing-mode` property to `vertical-rl`, or add `direction: rtl`, and see how the flow relative box stays with the text direction.

html

    <div class="container">
      <div class="inner">
        <div class="physical box"></div>
      </div>
      <div class="inner">
        <div class="logical box"></div>
      </div>
    </div>
    

    .container {
      display: flex;
    }
    
    .inner {
      width: 200px;
      height: 200px;
      position: relative;
      border: 2px dotted grey;
    }
    
    .box {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      padding: 10px;
      width: 100px;
      height: 100px;
    }
    

css

    .inner {
      writing-mode: horizontal-tb;
    }
    
    .physical {
      position: absolute;
      top: 20px;
      right: 0;
    }
    
    .logical {
      position: absolute;
      inset-block-start: 20px;
      inset-inline-end: 0;
    }
    

[New two- and four-value shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#new_two-_and_four-value_shorthands)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As with other properties in the module, we have shorthand properties which give the ability to set two or four values at once.

*   [`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
     — sets all four sides together with physical mapping.
*   [`inset-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
     — sets both logical inline insets.
*   [`inset-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
     — sets both logical block insets.

[Example: Logical values for text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning#example_logical_values_for_text-align)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 property has logical values that relate to text direction — rather than using `left` and `right` you can use `start` and `end`. In the below example, `text-align: right` is set in the first block and `text-align: end` in the second.

If you change the value of `direction` to `rtl`, you will see that the alignment stays to the right for the first block, but goes to the logical end on the left in the second.

html

    <div class="container">
      <div class="inner physical">Aligned text</div>
      <div class="inner logical">Aligned text</div>
    </div>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      display: flex;
    }
    
    .inner {
      width: 200px;
      border: 2px dotted grey;
      padding: 10px;
    }
    

css

    .inner {
      direction: ltr;
    }
    
    .physical {
      text-align: right;
    }
    
    .logical {
      text-align: end;
    }
    

This works more consistently when using box alignment that uses start and end rather than physical directions for alignment.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Floating_and_positioning/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/logical_properties_and_values/floating_and_positioning/index.md?plain=1 "Folder: en-us/web/css/guides/logical_properties_and_values/floating_and_positioning (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FFloating_and_positioning&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Ffloating_and_positioning%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FFloating_and_positioning%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Ffloating_and_positioning%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")