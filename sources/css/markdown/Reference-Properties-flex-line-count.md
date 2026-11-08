*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#mdn-search)
    

`flex-line-count` CSS property
==============================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#browser_compatibility)
 carefully before using this in production.

The **`flex-line-count`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the minimum number of flex lines that flex items will be balanced over in cases where a flex container's [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 or [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 property includes the `balance` keyword.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#try_it)

-------------------------------------------------------------------------------------------------------

    flex-line-count: 1;
    

    flex-line-count: 3;
    

    flex-line-count: 4;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <div>Item One</div>
        <div>Item Two</div>
        <div>Item Three</div>
        <div>Item Four</div>
        <div>Item Five</div>
        <div>Item Six</div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      width: 80%;
      display: flex;
      flex-wrap: wrap balance;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      width: 60px;
      margin: 10px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Integer values */
    flex-line-count: 1;
    flex-line-count: 3;
    flex-line-count: 12;
    
    /* Global values */
    flex-line-count: inherit;
    flex-line-count: initial;
    flex-line-count: revert;
    flex-line-count: revert-layer;
    flex-line-count: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#values)

This property is specified as the following value:

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

A positive integer setting the minimum number of flex lines that balanced, wrapped flex items will be distributed over. The default value is `1`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#description)

-----------------------------------------------------------------------------------------------------------------

The `flex-line-count` property sets the minimum number of flex lines that flex items will be distributed over in wrapping, balanced flex containers — in other words, flex containers that include a [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 or [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 property with the `balance` keyword set in addition to the `wrap` or `wrap-reverse` keyword.

A key use case for `flex-line-count` is creating a balanced set of two (or more) columns, regardless of the number of items in a list. In such cases, setting an explicit [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 or [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
 won't work as you don't know how much content you will have, and may end up with fewer or more columns than desired. See [Creating balanced columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#creating_balanced_columns)
 for an example implementation.

If `balance` is not set, or if flex items are not set to wrap onto multiple flex lines, the `flex-line-count` property has no effect.

If the `flex-line-count` value is equal to or greater than the number of flex items, there will be one flex item per flex line.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | multi-line flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

flex-line-count =   
  <integer \[1,∞\]>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#examples)

-----------------------------------------------------------------------------------------------------------

### [Effect of different `flex-line-count` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#effect_of_different_flex-line-count_values)

This example demonstrates the effects of different values of `flex-line-count` on four boxes.

#### HTML

We include four container [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
s, each with a `class` of `box` and ten child `<div>`s; each container `<div>` has a different `id` value.

html

    <div class="box" id="box-no-balance">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
      <div>Eight</div>
      <div>Nine</div>
      <div>Ten</div>
    </div>
    
    <div class="box" id="box1">...</div>
    <div class="box" id="box2">...</div>
    <div class="box" id="box3">...</div>
    

    <p>No <code>balance</code></p>
    
    <div class="box" id="box-no-balance">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
      <div>Eight</div>
      <div>Nine</div>
      <div>Ten</div>
    </div>
    
    <p><code>flex-line-count: 3</code></p>
    
    <div class="box" id="box1">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
      <div>Eight</div>
      <div>Nine</div>
      <div>Ten</div>
    </div>
    
    <p><code>flex-line-count: 4</code></p>
    
    <div class="box" id="box2">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
      <div>Eight</div>
      <div>Nine</div>
      <div>Ten</div>
    </div>
    
    <p><code>flex-line-count: 5</code></p>
    
    <div class="box" id="box3">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
      <div>Eight</div>
      <div>Nine</div>
      <div>Ten</div>
    </div>
    

#### CSS

    * {
      box-sizing: border-box;
    }
    
    .box {
      width: 100%;
      border: 2px dotted gray;
      margin-bottom: 20px;
      gap: 10px;
    }
    
    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: lightgray;
    }
    

We apply `display: flex` to all the boxes to make them flex containers, then give them a `flex-wrap` value of `wrap balance` to make all their flex children wrap onto multiple, balanced lines.

css

    .box {
      display: flex;
      flex-wrap: wrap balance;
    }
    

We also set a [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 value of `1 1 150px` on the flex children, so they have a base width of `150px` and will distribute any excess space evenly across the items in each flex line.

css

    .box > * {
      flex: 1 1 150px;
    }
    

For the `#box-no-balance` flex container, we remove the balancing, thereby nullifying the line count, by overriding the original `flex-wrap: wrap balance` value with `wrap`. We apply different `flex-line-count` values to each flex container, incrementing them so their children are laid out over a progressively greater number of flex lines.

css

    #box-no-balance {
      flex-line-count: 6;
      flex-wrap: wrap;
    }
    
    #box1 {
      flex-line-count: 3;
    }
    
    #box2 {
      flex-line-count: 4;
    }
    
    #box3 {
      flex-line-count: 5;
    }
    

We've hidden the rest of the CSS for brevity.

#### Results

Note the following:

*   As the first flex container doesn't have the `balance` keyword set in its `flex-wrap` value, its children are not given a balanced distribution and its `flex-line-count` value is ignored.
*   The second flex container's `flex-line-count: 3` declaration doesn't affect the layout of the flex children; as the flex items are by default distributed over four flex lines, any value of `4` or less has no effect.

### [Creating balanced columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#creating_balanced_columns)

This example demonstrates how `flex-line-count` can be used to create a balanced set of two columns.

#### HTML

We include an [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 element containing ten [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements.

html

    <ol>
      <li>
        <a href="#">The Silent Cartographer</a>, published by Meridian House,
        released March 12, 2014.
      </li>
      <li>
        <a href="#">Echoes of the Fallow Field</a>, published by Northbridge Press,
        released July 4, 2009.
      </li>
    
      ...
    </ol>
    

    <ol>
      <li>
        <a href="#">The Silent Cartographer</a>, published by Meridian House,
        released March 12, 2014.
      </li>
      <li>
        <a href="#">Echoes of the Fallow Field</a>, published by Northbridge Press,
        released July 4, 2009.
      </li>
      <li>
        <a href="#">A Ledger of Small Regrets</a>, published by Ashwood & Kline,
        released November 21, 2017.
      </li>
      <li>
        <a href="#">The Clockmaker's Daughter's Shadow</a>, published by Hollow Pine
        Publishing, released February 8, 2011.
      </li>
      <li>
        <a href="#">Salt and Signal</a>, published by Redcliffe Editions, released
        September 30, 2019.
      </li>
      <li>
        <a href="#">Under a Borrowed Sky</a>, published by Fenwick & Marsh, released
        May 16, 2006.
      </li>
      <li>
        <a href="#">The Last Cartel of Winter</a>, published by Graywolf Bindery,
        released January 2, 2021.
      </li>
      <li>
        <a href="#">Notes from an Unfinished Atlas</a>, published by Coastline
        Books, released June 27, 2013.
      </li>
      <li>
        <a href="#">The Weight of Empty Rooms</a>, published by Draymoor House,
        released October 15, 2008.
      </li>
      <li>
        <a href="#">A Brief History of Almost Everyone</a>, published by Ferngate
        Press, released April 9, 2022.
      </li>
    </ol>
    

#### CSS

We set the list's [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`. We set a [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 value of `column` and a [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 value of `balance` using the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 shorthand so that the flex lines are arranged in columns and will balance when wrapped. The [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 value `10px 40px` specifies a gap of `10px` between flex items within each column and `40px` between flex lines.

Finally, we set a `flex-line-count` value of `2`, meaning that, even though no fixed height is set on the list, its content will always be wrapped over two balanced columns, regardless of how much content is included.

css

    ol {
      display: flex;
      gap: 10px 40px;
      flex-flow: column balance;
      flex-line-count: 2;
    }
    

    * {
      box-sizing: border-box;
    }
    
    body {
      padding: 10px 30px;
    }
    
    @supports not (flex-line-count: 3) {
      body::before {
        content: "Your browser does not support the flex-line-count property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

We've hidden the rest of the CSS for brevity.

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 2  <br>\# flex-line-count-property](https://drafts.csswg.org/css-flexbox-2/#flex-line-count-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
    
*   [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
     shorthand
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Mastering wrapping of flex items > Balanced wrapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Wrapping_items#balanced_wrapping)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-line-count/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-line-count (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-line-count&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-line-count%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-line-count%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-line-count%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")