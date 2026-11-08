*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#mdn-search)
    

`inset()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inset()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 function defines a rectangle at the specified inset distances from each side of the reference box. It is a basic shape function used to define one of the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 [data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#try_it)

-----------------------------------------------------------------------------------------------------

    clip-path: inset(30px);
    

    clip-path: inset(1rem 2rem 3rem 4rem);
    

    clip-path: inset(20% 30% round 20px);
    

    clip-path: inset(4rem 20% round 1rem 2rem 3rem 4rem);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #default-example {
      background: #ffee99;
    }
    
    #example-element {
      background: linear-gradient(to bottom right, #ff5522, #0055ff);
      width: 100%;
      height: 100%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#syntax)

-----------------------------------------------------------------------------------------------------

css

    shape-outside: inset(20px 50px 10px 0 round 50px);
    border-shape: inset(10px 20px 10px 20px round 20px);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#values)

[`<length-percentage>{1,4}`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#length-percentage14)

When all of the four arguments are supplied they represent the top, right, bottom, and left offsets from the reference box inward that define the positions of the edges of the inset rectangle. These arguments follow the syntax of the margin shorthand, which let you set all four insets with one, two, or four values.

If a pair of insets for a dimension adds up to more than 100% of that dimension, both values are proportionally reduced so their sum equals 100%. For example, the value `inset(90% 10% 60% 10%)` has a top inset of `90%` and a bottom inset of `60%`. These values are reduced proportionally to `inset(60% 10% 40% 10%)`. Shapes such as this, that enclose no area and have no [`shape-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
, do not affect wrapping.

[`<border-radius>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#border-radius)

The optional [`<border-radius>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 argument(s) define rounded corners for the inset rectangle using the border-radius shorthand syntax.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

<inset()> =   
  inset( <length-percentage>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<'border-radius'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<border-radius>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 =   
  <length-percentage \[0,∞\]>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <length-percentage \[0,∞\]>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#examples)

---------------------------------------------------------------------------------------------------------

### [Basic inset example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#basic_inset_example)

In the example below we have an `inset()` shape used to pull content over the floated element. Change the offset values to see how the shape changes.

html

    <div class="box">
      <div class="shape"></div>
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    .box {
      width: 400px;
      margin: 0 auto;
    }
    
    .shape {
      float: left;
      width: 150px;
      height: 100px;
      clip-path: inset(45px 50px 15px 0 round 50px);
      shape-outside: inset(40px 40px 10px 0 round 50px);
      background-color: coral;
      border-radius: 20px;
      margin: 0;
      padding: 20px;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# funcdef-basic-shape-inset](https://drafts.csswg.org/css-shapes/#funcdef-basic-shape-inset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset#see_also)

---------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    , [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    , [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module
*   [Guide to basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/inset/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape/inset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Finset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Finset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Finset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Finset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd0970bc03cf30a9a8089954cc542a17dbe9eba3%0A*+Document+last+modified%3A+2026-07-16T09%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")