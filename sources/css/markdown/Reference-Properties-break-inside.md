*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#mdn-search)
    

`break-inside` CSS property
===========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2019.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`break-inside`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how page, column, or region breaks should behave inside a generated box. If there is no generated box, the property is ignored.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#try_it)

----------------------------------------------------------------------------------------------------

    break-inside: auto;
    

    break-inside: avoid;
    

    <div>
      <p>
        The effect of this property can be noticed when the document is being
        printed or a preview of a print is displayed.
      </p>
      <button id="print-btn">Show Print Preview</button>
      <div class="box-container">
        <div class="box">Content before the property</div>
        <div class="box" id="example-element">Content with 'break-inside'</div>
        <div class="box">Content after the property</div>
      </div>
    </div>
    

    .box {
      border: solid #5b6dcd 5px;
      background-color: #5b6dcd;
      margin: 10px 0;
      padding: 5px;
    }
    
    #example-element {
      border: solid 5px #ffc129;
      background-color: #ffc129;
      color: black;
    }
    
    @media print {
      #example-element {
        height: 25cm;
      }
    }
    

    const btn = document.getElementById("print-btn");
    
    btn.addEventListener("click", () => {
      window.print();
    });
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    break-inside: auto;
    break-inside: avoid;
    break-inside: avoid-page;
    break-inside: avoid-column;
    break-inside: avoid-region;
    
    /* Global values */
    break-inside: inherit;
    break-inside: initial;
    break-inside: revert;
    break-inside: revert-layer;
    break-inside: unset;
    

Each possible break point (in other words, each element boundary) is affected by three properties: the [`break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
 value of the previous element, the [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
 value of the next element, and the `break-inside` value of the containing element.

To determine if a break must be done, the following rules are applied:

1.  If any of the three concerned values is a _forced break value_ (`always`, `left`, `right`, `page`, `column`, or `region`), it has precedence. If more than one of them are such a break, the value of the element that appears the latest in the flow is used. Thus, the `break-before` value has precedence over the `break-after` value, which in turn has precedence over the `break-inside` value.
2.  If any of the three concerned values is an _avoid break value_ (`avoid`, `avoid-page`, `avoid-region`, or `avoid-column`), no such break will be applied at that point.

Once forced breaks have been applied, soft breaks may be added if needed, but not on element boundaries that resolve in a corresponding `avoid` value.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#auto)

Allows, but does not force, any break (page, column, or region) to be inserted within the principal box.

[`avoid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#avoid)

Avoids any break (page, column, or region) from being inserted within the principal box.

[`avoid-page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#avoid-page)

Avoids any page break within the principal box.

[`avoid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#avoid-column)

Avoids any column break within the principal box.

[`avoid-region`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#avoid-region)

Avoids any region break within the principal box.

[Page break aliases](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#page_break_aliases)

----------------------------------------------------------------------------------------------------------------------------

For compatibility reasons, the legacy [`page-break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside)
 property should be treated by browsers as an alias of `break-inside`. This ensures that sites using `page-break-inside` continue to work as designed. A subset of values should be aliased as follows:

| page-break-inside | break-inside |
| --- | --- |
| `auto` | `auto` |
| `avoid` | `avoid` |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block-level elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#formal_syntax)

------------------------------------------------------------------------------------------------------------------

break-inside =   
  auto          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-page    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-column  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-region    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#examples)

--------------------------------------------------------------------------------------------------------

### [Avoiding breaking inside a figure](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#avoiding_breaking_inside_a_figure)

In the following example we have a container that contains an `<h1>` spanning all columns (achieved using `column-span: all`) and a series of paragraphs laid out in multiple columns using `column-width: 200px`. We also have a `<figure>` containing an image and a caption.

By default, it is possible for you to get a break between the image and its caption, which is not what we want. To avoid this, we have set `break-inside: avoid` on the `<figure>`, which causes them to always stay together.

#### HTML

html

    <article>
      <h1>Main heading</h1>
    
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vitae
        fringilla mauris. Quisque commodo eget nisi sed pretium. Mauris luctus nec
        lacus in ultricies. Mauris vitae hendrerit arcu, ac scelerisque lacus.
        Aliquam lobortis in lacus sit amet posuere. Fusce iaculis urna id neque
        dapibus, eu lacinia lectus dictum.
      </p>
    
      <figure>
        <img
          src="https://mdn.dev/archives/media/attachments/2020/07/29/17350/3b4892b7e820122ac6dd7678891d4507/firefox.png" />
        <figcaption>The Firefox logo — fox wrapped around the world</figcaption>
      </figure>
    
      <p>
        Praesent condimentum dui dui, sit amet rutrum diam tincidunt eu. Cras
        suscipit porta leo sit amet rutrum. Sed vehicula ornare tincidunt. Curabitur
        a ipsum ac diam mattis volutpat ac ut elit. Nullam luctus justo non
        vestibulum gravida. Morbi metus libero, pharetra non porttitor a, molestie
        nec nisi.
      </p>
    
      <p>
        In finibus viverra enim vel suscipit. Quisque consequat velit eu orci
        malesuada, ut interdum tortor molestie. Proin sed pellentesque augue. Nam
        risus justo, faucibus non porta a, congue vel massa. Cras luctus lacus nisl,
        sed tincidunt velit pharetra ac. Duis suscipit faucibus dui sed ultricies.
      </p>
    </article>
    

#### CSS

css

    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    body {
      width: 80%;
      margin: 0 auto;
    }
    
    h1 {
      font-size: 3rem;
      letter-spacing: 2px;
      column-span: all;
    }
    
    h1 + p {
      margin-top: 0;
    }
    
    p {
      line-height: 1.5;
      break-after: column;
    }
    
    figure {
      break-inside: avoid;
    }
    
    img {
      max-width: 70%;
      display: block;
      margin: 0 auto;
    }
    
    figcaption {
      font-style: italic;
      font-size: 0.8rem;
      width: 70%;
    }
    
    article {
      column-width: 200px;
      gap: 20px;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fragmentation Module Level 3  <br>\# break-within](https://drafts.csswg.org/css-break/#break-within) |
| [CSS Regions Module Level 1  <br>\# region-flow-break](https://drafts.csswg.org/css-regions/#region-flow-break) |
| [CSS Multi-column Layout Module Level 1  <br>\# break-before-break-after-break-inside](https://drafts.csswg.org/css-multicol/#break-before-break-after-break-inside) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside#see_also)

--------------------------------------------------------------------------------------------------------

*   [Learn: Multiple-column Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Multiple-column_Layout)
    
*   [Breaking Boxes With CSS Fragmentation](https://www.smashingmagazine.com/2019/02/css-fragmentation/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/break-inside/index.md?plain=1 "Folder: en-us/web/css/reference/properties/break-inside (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbreak-inside&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbreak-inside%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbreak-inside%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbreak-inside%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")