*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#mdn-search)
    

Logical properties for sizing
=============================

In this guide, we will explain the flow-relative mappings between physical dimension properties and logical properties used for sizing elements on our pages.

When specifying the size of an item, the [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module gives you the ability to indicate sizing as it relates to the flow of text (inline and block) rather than physical sizing which relates to the physical dimensions of horizontal and vertical (e.g., left and right). While these flow relative mappings may well become the default for many of us, in a design you may well use both physical and logical sizing. You might want some features to always relate to the physical dimensions whatever the writing mode.

[Mappings for dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#mappings_for_dimensions)

------------------------------------------------------------------------------------------------------------------------------------------------

The table below provides mappings between logical and physical properties. These mappings assume that you are in a `horizontal-tb` writing mode, such as English or Arabic, in which case [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 would be mapped to [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
.

If you were in a vertical writing mode then [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 would be mapped to [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
.

| Logical Property | Physical Property |
| --- | --- |
| [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size) | [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width) |
| [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size) | [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height) |
| [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size) | [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width) |
| [`min-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-block-size) | [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height) |
| [`max-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size) | [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width) |
| [`max-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size) | [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height) |

[Width and height example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#width_and_height_example)

--------------------------------------------------------------------------------------------------------------------------------------------------

The logical mappings for [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 are [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
, which sets the length in the inline dimension and [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
, which sets the length in the block dimension. When working in English, replacing `width` with `inline-size` and `height` with `block-size` will give the same layout.

In the live example below, the `writing-mode` is set to `horizontal-tb`. Change it to `vertical-rl` and you will see that the first example — which uses `width` and `height` — remains the same size in each dimension, despite the text becoming vertical. The second example — which uses `inline-size` and `block-size` — will follow the text direction as if the entire block has rotated.

[Min-width and min-height example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#min-width_and_min-height_example)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are also mappings for [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
 and [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
 — these are [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
 and [`min-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-block-size)
. These work in the same way as the `inline-size` and `block-size` properties, but setting a minimum rather than a fixed size.

Try changing the example below to `vertical-rl`, as with the first example, to see the effect it has. I am using `min-height` in the first example and `min-block-size` in the second.

html

    <div class="container">
      <div class="physical box">
        I have a width of 200px and a min-height of 5em.
      </div>
    
      <div class="logical box">
        I have an inline-size of 200px and a min-block-size of 5em.
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
    }
    

css

    .box {
      writing-mode: horizontal-tb;
    }
    
    .physical {
      width: 200px;
      min-height: 5em;
    }
    
    .logical {
      inline-size: 200px;
      min-block-size: 5em;
    }
    

[Max-width and max-height example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#max-width_and_max-height_example)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally you can use [`max-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
 and [`max-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
 as logical replacements for [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 and [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
. Try playing with the below example in the same way as before.

html

    <div class="container">
      <div class="physical box">I have a max-width of 200px.</div>
    
      <div class="logical box">I have a max-inline-size of 200px.</div>
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
    }
    

css

    .box {
      writing-mode: horizontal-tb;
    }
    
    .physical {
      max-width: 200px;
    }
    
    .logical {
      max-inline-size: 200px;
    }
    

[Logical keywords for resize](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing#logical_keywords_for_resize)

--------------------------------------------------------------------------------------------------------------------------------------------------------

The [`resize`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize)
 property sets whether or not an item can be resized and has physical values of `horizontal` and `vertical`. The `resize` property also has logical keyword values. Using `resize: inline` allows resizing in the inline dimension and `resize: block` allow resizing in the block dimension.

The keyword value of `both` for the resize property works whether you are thinking physically or logically. It sets both dimensions at once. Try playing with the below example.

html

    <div class="container">
      <div class="physical box">
        I have a width of 200px and a height of 100px. I can be resized
        horizontally.
      </div>
    
      <div class="logical box">
        I have an inline-size of 200px and a block-size of 100px. I can be resized
        in the inline direction.
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
    }
    

css

    .box {
      writing-mode: horizontal-tb;
      overflow: scroll;
    }
    
    .physical {
      width: 200px;
      height: 100px;
      resize: horizontal;
    }
    
    .logical {
      inline-size: 200px;
      block-size: 100px;
      resize: inline;
    }
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Sizing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/logical_properties_and_values/sizing/index.md?plain=1 "Folder: en-us/web/css/guides/logical_properties_and_values/sizing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FSizing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Fsizing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FSizing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Fsizing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")