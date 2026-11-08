*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns#mdn-search)
    

Styling columns
===============

As column boxes created inside multi-column (_multicol_) containers are anonymous boxes, styling individual columns is not possible, but we can style the gaps between the columns and the container in general. This guide explains how to change the gap and style rules between columns.

[Column gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns#column_gaps)

-------------------------------------------------------------------------------------------------------------------

The gap between columns is controlled using the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 or [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 property. The `column-gap` property is defined in the [multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 module. The `gap` property is defined in the [box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module. This is a unified property to define gaps between boxes in all layouts that support gaps, including [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Box_alignment)
 and [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Wrapping_items)
.

The initial value of `column-gap` is `1em`, which prevents columns from running into each other. In other layout methods, `column-gap` is supported as a synonym for `gap`, but with an initial value of `0`. The keyword value `normal` sets `column-gap` to the initial value.

You can change the gap by using any [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value. In the example below, the `column-gap` is set to `40px`.

html

    <div class="container">
      <p>
        Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi welsh onion
        daikon amaranth tatsoi tomatillo melon azuki bean garlic.
      </p>
      <p>
        Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
        tatsoi pea sprouts fava bean collard greens dandelion okra wakame tomato.
        Dandelion cucumber earthnut pea peanut soko zucchini.
      </p>
      <p>
        Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
        kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus winter
        purslane kale. Celery potato scallion desert raisin horseradish spinach
        carrot soko.
      </p>
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      column-count: 3;
      column-gap: 40px;
    }
    

The allowed value for `column-gap` is a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, meaning percentages are allowed. Percentage values for `column-gap` are calculated as a percentage of the width of the multicol container.

[Column rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns#column_rules)

---------------------------------------------------------------------------------------------------------------------

The specification defines [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
, [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
 and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
, providing a shorthand [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
. These properties work in exactly the same way as the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 properties: any [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 can be used as a `column-rule-style`, just as for valid [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
.

These properties are applied to the element, which is the multicol container, and therefore, all columns will have the same rule. Rules are only drawn between columns and not on the outer edges. Rules are also only drawn between columns that have content.

In this next example, a 5px-dotted rule with a color of `rebeccapurple` has been created using the longhand values.

    <div class="container">
      <p>
        Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi welsh onion
        daikon amaranth tatsoi tomatillo melon azuki bean garlic.
      </p>
      <p>
        Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
        tatsoi pea sprouts fava bean collard greens dandelion okra wakame tomato.
        Dandelion cucumber earthnut pea peanut soko zucchini.
      </p>
      <p>
        Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
        kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus winter
        purslane kale. Celery potato scallion desert raisin horseradish spinach
        carrot soko.
      </p>
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      column-count: 3;
      column-rule-width: 5px;
      column-rule-style: dotted;
      column-rule-color: rebeccapurple;
    }
    

Note that the rule itself does not take up any space: a wide rule will not push the columns apart to make space for the rule. Instead, the rule overlays the gap.

The example below uses a very wide rule of `40px` and a `10px` gap. The rule displays under the column content. To make space on both sides of the rule, the gap would need to be increased to be larger than `40px`.

    <div class="container">
      <p>
        Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi welsh onion
        daikon amaranth tatsoi tomatillo melon azuki bean garlic.
      </p>
      <p>
        Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
        tatsoi pea sprouts fava bean collard greens dandelion okra wakame tomato.
        Dandelion cucumber earthnut pea peanut soko zucchini.
      </p>
      <p>
        Turnip greens yarrow ricebean rutabaga endive cauliflower sea lettuce
        kohlrabi amaranth water spinach avocado daikon napa cabbage asparagus winter
        purslane kale. Celery potato scallion desert raisin horseradish spinach
        carrot soko.
      </p>
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      column-count: 3;
      column-gap: 10px;
      column-rule: 40px solid rebeccapurple;
    }
    

[Next steps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns#next_steps)

-----------------------------------------------------------------------------------------------------------------

This article details all the current ways in which column boxes can be styled. In the next guide, we will take a look at making elements inside a container [span across all columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Spanning_balancing_columns)
.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/multicol_layout/styling_columns/index.md?plain=1 "Folder: en-us/web/css/guides/multicol_layout/styling_columns (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMulticol_layout%2FStyling_columns&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmulticol_layout%2Fstyling_columns%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMulticol_layout%2FStyling_columns%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmulticol_layout%2Fstyling_columns%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")