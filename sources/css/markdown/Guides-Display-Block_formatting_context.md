*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#mdn-search)
    

Block formatting context
========================

A **block formatting context** (BFC) is a part of a visual CSS rendering of a web page. It's the region in which the layout of block boxes occurs and in which floats interact with other elements.

A block formatting context is created by at least one of the following:

*   The root element of the document (`<html>`).
*   Floats (elements where [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
     isn't `none`).
*   Absolutely positioned elements (elements where [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     is `absolute` or `fixed`).
*   Inline-blocks (elements with [`display: inline-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    ). This is the default display type for [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
     and button [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements.
*   Table cells (elements with [`display: table-cell`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , which is the default for HTML table cells).
*   Table captions (elements with [`display: table-caption`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , which is the default for HTML table captions).
*   Anonymous table cells implicitly created by the elements with [`display: table`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , `table-row`, `table-row-group`, `table-header-group`, `table-footer-group` (which is the default for HTML tables, table rows, table bodies, table headers, and table footers, respectively), or `inline-table`.
*   Elements with [`display: flow-root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    .
*   Flex items (direct children of the element with [`display: flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
     or `inline-flex`) if they are neither [flex](https://developer.mozilla.org/en-US/docs/Glossary/Flex_Container)
     nor [grid](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Container)
     nor [table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     containers themselves.
*   Grid items (direct children of the element with [`display: grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
     or `inline-grid`) if they are neither [flex](https://developer.mozilla.org/en-US/docs/Glossary/Flex_Container)
     nor [grid](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Container)
     nor [table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     containers themselves.
*   Block elements where [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
     has a value other than `visible` and `clip`.
*   Elements with [`contain: layout`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    , `content`, or `paint`.
*   Query containers (elements where [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
     isn't `normal`).
*   Multicol containers (elements where [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
     or [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
     isn't `auto`, including elements with `column-count: 1`).
*   [`column-span: all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span)
    , even when the `column-span: all` element isn't contained by a multicol container.

Formatting contexts affect layout because an element that establishes a new block formatting context will:

*   contain internal floats.
*   exclude external floats.
*   suppress [margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
    .

Flex and grid containers, defined by setting an element's [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`, `grid`, `inline-flex`, or `inline-grid`, establishes a new flex or grid formatting context. These are similar to block formatting context except there are no floating children available inside a flex or grid container, but these formatting contexts do exclude external floats and suppress margin collapsing.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#examples)

--------------------------------------------------------------------------------------------------------------

Let's have a look at a couple of these in order to see the effect creating a new BFC.

### [Contain internal floats](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#contain_internal_floats)

In the following example, we have float content that is the same height as the content alongside it. We have a floated element inside a `<div>` with a `border` applied. The content of that `<div>` has floated alongside the floated element. As the content of the float is taller than the content alongside it, the border of the `<div>` now runs through the float. As explained in the [guide to in flow and out of flow elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow)
, the float has been taken out of flow so the `background` and `border` of the `<div>` only contain the content and not the float.

**using `overflow: auto`**

Setting `overflow: auto` or set other values than the initial value of `overflow: visible` created a new BFC containing the float. Our `<div>` now becomes a mini-layout inside our layout. Any child element will be contained inside it.

The problem with using `overflow` to create a new BFC is that the `overflow` property is meant for telling the browser how you want to deal with overflowing content. There are some occasions in which you will find you get unwanted scrollbars or clipped shadows when you use this property purely to create a BFC. In addition, it is potentially not readable for a future developer, as it might not be obvious why you used `overflow` for this purpose. If you use `overflow`, it is a good idea to comment the code to explain.

**using `display: flow-root`**

The `display: flow-root` value lets us create a new BFC without any other potentially problematic side-effects. Using `display: flow-root` on the containing block creates a new BFC.

With `display: flow-root;` on the `<div>`, everything inside that container participates in the block formatting context of that container, and floats will not poke out of the bottom of the element.

The value name of `flow-root` makes sense when you understand you are creating something that acts like the `root` element (`<html>` element in browser) in terms of how it creates a new context for the flow layout inside it.

#### HTML

html

    <section>
      <div class="box1">
        <div class="float">I am a floated box!</div>
        <p>I am content inside the container.</p>
      </div>
    </section>
    <section>
      <div class="box2">
        <div class="float">I am a floated box!</div>
        <p>I am content inside the <code>overflow:auto</code> container.</p>
      </div>
    </section>
    <section>
      <div class="box3">
        <div class="float">I am a floated box!</div>
        <p>I am content inside the <code>display:flow-root</code> container.</p>
      </div>
    </section>
    

#### CSS

css

    section {
      height: 150px;
    }
    .box1 {
      background-color: rgb(224 206 247);
      border: 5px solid rebeccapurple;
    }
    .box2,
    .box3 {
      background-color: aliceblue;
      border: 5px solid steelblue;
    }
    .box2 {
      overflow: auto;
    }
    .box3 {
      display: flow-root;
    }
    .float {
      float: left;
      width: 200px;
      height: 100px;
      background-color: rgb(255 255 255 / 50%);
      border: 1px solid black;
      padding: 10px;
    }
    

### [Exclude external floats](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#exclude_external_floats)

In the following example, we are using `display: flow-root` and floats, creating two side-by-side boxes demonstrating that an element in the normal flow establishes a new BFC and does not overlap the margin box of any floats in the same block formatting context as the element itself.

#### HTML

html

    <section>
      <div class="float">Try to resize this outer float</div>
      <div class="box"><p>Normal</p></div>
    </section>
    <section>
      <div class="float">Try to resize this outer float</div>
      <div class="box2">
        <p><code>display:flow-root</code></p>
      </div>
    </section>
    

#### CSS

css

    section {
      height: 150px;
    }
    .box {
      background-color: rgb(224 206 247);
      border: 5px solid rebeccapurple;
    }
    .box2 {
      background-color: aliceblue;
      border: 5px solid steelblue;
      display: flow-root;
    }
    .float {
      float: left;
      overflow: hidden; /* required by resize:both */
      resize: both;
      margin-right: 25px;
      width: 200px;
      height: 100px;
      background-color: rgb(255 255 255 / 75%);
      border: 1px solid black;
      padding: 10px;
    }
    

### [Prevent margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#prevent_margin_collapsing)

You can create a new BFC to avoid [margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
 between two neighbor elements.

#### Margin collapsing example

In this example we have two adjacent [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, which each have a vertical margin of `10px`. Because of margin collapsing, the vertical gap between them is `10px`, not the `20px` we might expect.

html

    <div class="blue"></div>
    <div class="red"></div>
    

css

    .blue,
    .red {
      height: 50px;
      margin: 10px 0;
    }
    
    .blue {
      background: blue;
    }
    
    .red {
      background: red;
    }
    

#### Preventing margin collapsing

In this example, we wrap the second `<div>` in an outer `<div>`, and create a new BFC by using `overflow: hidden` on the outer `<div>`. This new BFC prevents the margins of the nested `<div>` from collapsing with those of the outer `<div>`.

html

    <div class="blue"></div>
    <div class="outer">
      <div class="red"></div>
    </div>
    

css

    .blue,
    .red {
      height: 50px;
      margin: 10px 0;
    }
    
    .blue {
      background: blue;
    }
    
    .red {
      background: red;
    }
    
    .outer {
      overflow: hidden;
      background: transparent;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# block-formatting-context](https://drafts.csswg.org/css-display/#block-formatting-context) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context#see_also)

--------------------------------------------------------------------------------------------------------------

*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    
*   [Box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    
*   [Layout modes](https://developer.mozilla.org/en-US/docs/Glossary/Layout_mode)
    
*   [Visual formatting models](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
    
*   [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
    
*   [Initial](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    , [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    , [used values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    , and [actual](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
     values
*   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
    
*   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/display/block_formatting_context/index.md?plain=1 "Folder: en-us/web/css/guides/display/block_formatting_context (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FBlock_formatting_context&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fblock_formatting_context%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FBlock_formatting_context%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fblock_formatting_context%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")