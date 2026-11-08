*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#mdn-search)
    

`break-after` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2019.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`break-after`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how page, column, or region breaks should behave after a generated box. If there is no generated box, the property is ignored.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#try_it)

---------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#syntax)

---------------------------------------------------------------------------------------------------

Each possible break point (in other words, each element boundary) is affected by three properties: the `break-after` value of the previous element, the [`break-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
 value of the next element, and the [`break-inside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
 value of the containing element.

To determine if a break must be done, the following rules are applied:

1.  If any of the three concerned values is a _forced break value_ (`always`, `left`, `right`, `page`, `column`, or `region`), it has precedence. If more than one of them are such a break, the one of the element that appears the latest in the flow is taken (i.e., the `break-before` value has precedence over the `break-after` value, which itself has precedence over the `break-inside` value).
2.  If any of the three concerned values is an _avoid break value_ (`avoid`, `avoid-page`, `avoid-region`, or `avoid-column`), no such break will be applied at that point.

Once forced breaks have been applied, soft breaks may be added if needed, but not on element boundaries that resolve in a corresponding `avoid` value.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#values)

#### Generic break values

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#auto)

Allows, but does not force, any break (page, column, or region) to be inserted right after the principal box.

[`avoid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#avoid)

Avoids any break (page, column, or region) from being inserted right after the principal box.

[`always`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#always)

Forces a page break right after the principal box. The type of this break is that of the immediately-containing fragmentation context. If we are inside a multicol container then it would force a column break, inside paged media (but not inside a multicol container) a page break.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#all)

Forces a page break right after the principal box. Breaking through all possible fragmentation contexts. So a break inside a multicol container, which was inside a page container would force a column and page break.

#### Page break values

[`avoid-page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#avoid-page)

Avoids any page break right after the principal box.

[`page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#page)

Forces a page break right after the principal box.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#left)

Forces one or two page breaks right after the principal box, whichever will make the next page into a left page. It's the page placed on the left side of the spine of the book or the back side of the page in duplex printing.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#right)

Forces one or two page breaks right after the principal box, whichever will make the next page into a right page. It's the page placed on the right side of the spine of the book or the front side of the page in duplex printing.

[`recto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#recto)

Forces one or two page breaks right after the principal box, whichever will make the next page into a recto page. (A recto page is a right page in a left-to-right spread or a left page in a right-to-left spread.)

[`verso`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#verso)

Forces one or two page breaks right after the principal box, whichever will make the next page into a verso page. (A verso page is a left page in a left-to-right spread or a right page in a right-to-left spread.)

#### Column break values

[`avoid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#avoid-column)

Avoids any column break right after the principal box.

[`column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#column)

Forces a column break right after the principal box.

#### Region break values

[`avoid-region`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#avoid-region)

Avoids any region break right after the principal box.

[`region`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#region)

Forces a region break right after the principal box.

[Page break aliases](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#page_break_aliases)

---------------------------------------------------------------------------------------------------------------------------

For compatibility reasons, the legacy [`page-break-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-after)
 property should be treated by browsers as an alias of `break-after`. This ensures that sites using `page-break-after` continue to work as designed. A subset of values should be aliased as follows:

| page-break-after | break-after |
| --- | --- |
| `auto` | `auto` |
| `left` | `left` |
| `right` | `right` |
| `avoid` | `avoid` |
| `always` | `page` |

**Note:** The `always` value of `page-break-*` was implemented by browsers as a page break, and not as a column break. Therefore the aliasing is to `page`, rather than the `always` value in the Level 4 spec.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block-level elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

break-after =   
  auto          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  always        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-page    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  page          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  recto         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  verso         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-column  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  column        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-region  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  region          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#examples)

-------------------------------------------------------------------------------------------------------

### [Breaking into neat columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#breaking_into_neat_columns)

In the following example we have a container that contains an `<h1>` spanning all columns (achieved using `column-span: all`) and a series of `<h2>`s and paragraphs laid out in multiple columns using `column-width: 200px`.

By default, the subheadings and paragraphs were laid out rather messily because the headings were not in a uniform place. However, we used `break-after: column` on the `<p>` elements to force a column break after each one, meaning that you end up with an `<h2>` neatly at the top of each column.

#### HTML

#### CSS

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fragmentation Module Level 3  <br>\# propdef-break-after](https://drafts.csswg.org/css-break/#propdef-break-after) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after#see_also)

-------------------------------------------------------------------------------------------------------

*   [Learn: Multiple-column Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Multiple-column_Layout)
    
*   [Breaking Boxes With CSS Fragmentation](https://www.smashingmagazine.com/2019/02/css-fragmentation/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/break-after/index.md?plain=1 "Folder: en-us/web/css/reference/properties/break-after (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbreak-after&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbreak-after%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbreak-after%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbreak-after%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")