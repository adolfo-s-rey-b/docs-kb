*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#mdn-search)
    

Basic concepts of multi-column layouts
======================================

Multi-column layout, usually referred to as multicol layout, is a specification for laying out content into a set of column boxes much like columns in a newspaper. This guide explains how the specification works with some common use case examples.

[Key properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#key_properties)

------------------------------------------------------------------------------------------------------------------------

Multicol layout is unlike any of the other layout methods in CSS; it fragments the content, including all descendant elements, into columns. This happens in the same way that content is fragmented into pages when we work with [CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
 by creating a print stylesheet.

In this and subsequent guides, we will be discussing the following properties defined in the [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 module:

*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    
*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    
*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
     shorthand
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`column-span`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span)
    
*   [`column-fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill)
    
*   [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    
*   [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
    
*   [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
    
*   [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
    

[Defining columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#defining_columns)

----------------------------------------------------------------------------------------------------------------------------

By adding the `column-count` or the `column-width` property to an element, or using the `columns` shorthand, the element becomes a _multi-column container_ or _multicol container_ for short. The columns are anonymous boxes; they're described as _column boxes_ in the specification.

### [Specifying the number of columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#specifying_the_number_of_columns)

The `column-count` property specifies the number of columns that you would like the content to be displayed as. The browser will then assign the correct amount of space to each column box to create the requested number of columns.

In the below example, we use the `column-count` property to create three columns on the `.container` element. The content, including the children of `.container`, is then split between the three columns.

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
    }
    

In the above example, the content is wrapped within the paragraph `<p>` tags with the default styling. Therefore, there is a margin above each paragraph. You can see how this margin causes the first line of text to be pushed down. This is because a multicol container creates a [block formatting context (BFC)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 because of which margins on child elements do not collapse with any margin on the container.

### [Specifying the width of columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#specifying_the_width_of_columns)

The `column-width` property is used to set the optimal width for every column box. If you declare a column width, the browser will work out how many columns of that width will fit into the multicol container and distribute any extra space equally between the columns. Therefore, the column width should be seen as minimum width because the column boxes are likely to be wider due to the additional space.

In the case of a single column with less width available than the value of `column-width`, the column box will shrink to be smaller than the declared column width.

In the example below, the `column-width` property is set to `200px`. We get as many 200-pixel columns as will fit the container, with the extra space shared equally.

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
      column-width: 200px;
    }
    

### [Specifying both number and width of columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#specifying_both_number_and_width_of_columns)

If you specify both the properties on a multicol container, then `column-count` will act as a maximum number of columns. Therefore, the behavior as described for `column-width` will happen, until the number of columns in `column-count` is reached. After this point, no more columns will be drawn, and the extra space is distributed evenly between the existing columns, even if there is enough room for more columns of the specified `column-width` size.

When using both properties together, you may get fewer columns than specified in the value for `column-count`.

In this next example, we use `column-width` of `200px` and `column-count` of `2`. Even if there is space for more than two columns, we get two. If there is not enough space for two columns of at least 200 pixels each, we get one.

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
        carrot soko. .
      </p>
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      column-count: 2;
      column-width: 200px;
    }
    

### [Shorthand for column properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#shorthand_for_column_properties)

You can use the `columns` shorthand to set the `column-count` and `column-width` values. If you specify a length unit, the value will be used for `column-width`, and if you specify an integer, the value will be used for `column-count`. You can set both the properties, separating the two values with a space.

This CSS would give the same result as [the first example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#specifying_the_number_of_columns)
, with `column-count` set to `3`.

css

    .container {
      columns: 3;
    }
    

This CSS would give the same result as [the second example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#specifying_the_width_of_columns)
, with `column-width` of `200px`.

css

    .container {
      columns: 200px;
    }
    

This CSS would give the same result as [the third example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#specifying_both_number_and_width_of_columns)
, with both `column-count` and `column-width` set.

css

    .container {
      columns: 2 200px;
    }
    

[Next steps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts#next_steps)

----------------------------------------------------------------------------------------------------------------

In this guide, we've learned the basic use of multi-column layout. In the next guide, we will look at how much we can [style the columns themselves](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns)
.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/multicol_layout/basic_concepts/index.md?plain=1 "Folder: en-us/web/css/guides/multicol_layout/basic_concepts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMulticol_layout%2FBasic_concepts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmulticol_layout%2Fbasic_concepts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMulticol_layout%2FBasic_concepts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmulticol_layout%2Fbasic_concepts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")