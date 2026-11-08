*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#mdn-search)
    

Using multi-column layouts
==========================

The properties defined in the **CSS multi-column layout module** extend the _block layout mode_, enabling the definition of multiple columns of text. People have trouble reading text if lines are too long. If it takes too long for the eyes to move from the end of one line to the beginning of the next, readers can lose track of which line they were on. To provide for a better user experience when reading text making use of a large screen, you should limit the width of text by using columns of text placed side by side, just as newspapers do.

[Using columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#using_columns)

-------------------------------------------------------------------------------------------------------------

### [Column count and width](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#column_count_and_width)

Two CSS properties control whether and how many columns will appear: [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 and [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
.

The `column-count` property sets the number of columns to a particular number. E.g.,

[Example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#example_1)

-----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#html)

html

    <div id="col">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
      </p>
      <p>
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat.
      </p>
      <p>
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
        eu fugiat nulla pariatur.
      </p>
      <p>
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.
      </p>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#css)

css

    #col {
      column-count: 2;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#result)

The content will be displayed in two columns:

The `column-width` property sets the minimum desired column width. If `column-count` is not also set, then the browser will automatically make as many columns as fit in the available width.

[Example 2](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#example_2)

-----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#html_2)

html

    <div id="wid">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
      cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
      proident, sunt in culpa qui officia deserunt mollit anim id est laborum
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#css_2)

css

    #wid {
      column-width: 100px;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#result_2)

In a multi-column block, content automatically flows from one column into the next as needed. All HTML, CSS, and DOM functionality is supported within columns, as are editing and printing.

### [The columns shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#the_columns_shorthand)

You can use either [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 or [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
. Because values for these properties do not overlap, it is often convenient to use the shorthand [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
.

[Example 3](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#example_3)

-----------------------------------------------------------------------------------------------------

In this example, the CSS declaration `column-width: 12em` is replaced by `columns: 12em`.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#html_3)

html

    <div id="col_short">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
      cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
      proident, sunt in culpa qui officia deserunt mollit anim id est laborum
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#css_3)

css

    #col_short {
      columns: 12em;
    }
    

[Example 4](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#example_4)

-----------------------------------------------------------------------------------------------------

In this example, the CSS declaration `column-count: 4` is replaced by `columns: 4`.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#html_4)

html

    <div id="columns_4">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
      cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
      proident, sunt in culpa qui officia deserunt mollit anim id est laborum
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#css_4)

css

    #columns_4 {
      columns: 4;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#result_3)

[Example 5](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#example_5)

-----------------------------------------------------------------------------------------------------

The two CSS declarations `column-width: 8em` and `column-count: 12` can be replaced by `columns: 12 8em`. The `column-count` portion of the shorthand is the maximum number of columns that will be present. The `column-width` is the minimum width each column should be.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#html_5)

html

    <div id="columns_12">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
      cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
      proident, sunt in culpa qui officia deserunt mollit anim id est laborum
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#css_5)

css

    #columns_12 {
      columns: 12 8em;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#result_4)

Assuming a default `1em` gap between columns, if the container is wider than `103ems` (12 columns \* `8em` width each + 7 `1em` gaps), there will be 12 columns, each with a width of `8ems` or more. If the container is less than `103ems` wide, there will be fewer than 12 columns. If the container is less than `17ems` wide (`8em` column + `8em` column + `1em` gap), the content will be displayed as a single column with no column gap.

### [Height balancing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#height_balancing)

CSS columns require that the column heights must be balanced: that is, the browser automatically sets the maximum column height so that the heights of the content in each column are approximately equal. Firefox does this.

However, in some situations it is also useful to set the maximum height of the columns explicitly, and then lay out content starting at the first column and creating as many columns as necessary, possibly overflowing to the right. Therefore, if the height is constrained, by setting the CSS [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 or [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
 properties on a multi-column block, each column is allowed to grow to that height and no further before adding new column. This mode is also much more efficient for layout.

### [Column Gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#column_gaps)

There is a gap between columns. The recommended default is `1em`. This size can be changed by applying the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 property to the multi-column block:

[Example 6](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#example_6)

-----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#html_6)

html

    <div id="column_gap">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
      cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
      proident, sunt in culpa qui officia deserunt mollit anim id est laborum
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#css_6)

css

    #column_gap {
      column-count: 5;
      column-gap: 2em;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#result_5)

[Conclusion](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using#conclusion)

-------------------------------------------------------------------------------------------------------

CSS columns are a layout primitive that can help make large blocks of text easier to read when responsive content is viewed on wide viewports. Imaginative developers may find many uses for them, especially in conjunction with [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
 and with the automatic height balancing feature.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 15, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/multicol_layout/using/index.md?plain=1 "Folder: en-us/web/css/guides/multicol_layout/using (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMulticol_layout%2FUsing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmulticol_layout%2Fusing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMulticol_layout%2FUsing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmulticol_layout%2Fusing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32bdfdb82cf91ce9942b694286dec62be2cc20aa%0A*+Document+last+modified%3A+2025-12-15T12%3A04%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")