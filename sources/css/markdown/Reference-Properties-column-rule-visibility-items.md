*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#mdn-search)
    

`column-rule-visibility-items` CSS property
===========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#browser_compatibility)
 carefully before using this in production.

The **`column-rule-visibility-items`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines whether a column-rule segment is painted in gaps adjacent to empty areas.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#try_it)

--------------------------------------------------------------------------------------------------------------------

    column-rule-visibility-items: all;
    

    column-rule-visibility-items: around;
    

    column-rule-visibility-items: between;
    

    column-rule-visibility-items: normal;
    

    <section id="default-example">
      <section id="example-element">
        <p>One fish</p>
        <p>Two fish</p>
        <p>Red fish</p>
        <p>Blue fish</p>
        <cite>-- Dr. Seuss</cite>
      </section>
    </section>
    

    #example-element {
      display: grid;
      column-rule: solid 5px red;
      gap: 10px;
      grid-template-rows: repeat(3, 1fr);
      grid-template-columns: repeat(3, 1fr);
    }
    cite {
      grid-row: 3;
      grid-column: 3;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#syntax)

--------------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    column-rule-visibility-items: all;
    column-rule-visibility-items: around;
    column-rule-visibility-items: between;
    column-rule-visibility-items: normal;
    
    /* Global values */
    column-rule-visibility-items: inherit;
    column-rule-visibility-items: initial;
    column-rule-visibility-items: revert;
    column-rule-visibility-items: revert-layer;
    column-rule-visibility-items: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#values)

This property is specified as one of the following keyword values:

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#all)

The column rule should be painted in all gap segments, regardless of whether adjacent areas contain an item.

[`around`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#around)

The column rule should be painted in a gap segment if at least one of the two adjacent areas is occupied by an item.

[`between`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#between)

The column rule should be painted in a gap segment if both adjacent areas are occupied by items.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#normal)

With grid containers, behaves the same as `all`. In multicol layout, behaves the same as `between`. This is the default.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#description)

------------------------------------------------------------------------------------------------------------------------------

The `column-rule-visibility-items` property defines whether a column-rule segment is painted in column gaps adjacent to empty areas in [multi-row](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one column.

The `column-rule-visibility-items` and [`row-rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-visibility-items)
 properties can both be set using the [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------------

column-rule-visibility-items =   
  all      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  around   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  between  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#examples)

------------------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#basic_example)

In this example, we define a column rule to be drawn between two grid areas if at least one adjacent grid area contains a grid item.

#### HTML

We include a list of dynamic sports duos:

html

    <ol>
      <li>Simone Biles + Jonathan Owens</li>
      <li>Serena Williams + Venus Williams</li>
      <li>Aaron Judge + Giancarlo Stanton</li>
      <li>LeBron James + Dwyane Wade</li>
      <li>Xavi Hernandez + Andres Iniesta</li>
      <li>Kerri Walsh + Misty May Treanor</li>
    </ol>
    

#### CSS

We define the ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
) to be a grid container, creating 4 columns and 4 rows by setting both the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 and [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
 properties to `repeat(4, 1fr)`, and move the last item to the bottom-right grid area using [`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
 and [`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
 properties. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `20px` to provide enough room between the columns to fit our `5px` dashed rule.

Finally, we set `column-rule-visibility-items` to `between`, so that a column rule is painted in a column gap only if both adjacent grid areas contain a grid item.

css

    ol {
      display: grid;
      grid-template-rows: repeat(4, 1fr);
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    
      column-rule: dashed 5px blue;
      column-rule-visibility-items: between;
    }
    li:last-child {
      grid-row: 4;
      grid-column: 4;
    }
    

    li {
      margin-left: 1em;
    }
    @layer no-support {
      @supports not (column-rule-visibility-items: around) {
        body::before {
          content: "Your browser doesn't support the column-rule-visibility-items property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-column-rule-visibility-items](https://drafts.csswg.org/css-gaps-1/#propdef-column-rule-visibility-items) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
     shorthand
*   [`row-rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-visibility-items)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-rule-visibility-items/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-rule-visibility-items (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-visibility-items&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-visibility-items%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-visibility-items%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-visibility-items%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")