*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#mdn-search)
    

`text-indent` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-indent`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the length of empty space (indentation) that is put before lines of text in a block.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#try_it)

---------------------------------------------------------------------------------------------------

    text-indent: 0;
    

    text-indent: 30%;
    

    text-indent: -3em;
    

    text-indent: 3em each-line;
    

    text-indent: 3em hanging;
    

    text-indent: 3em hanging each-line;
    

    <section id="default-example">
      <div id="example-element">
        <p>
          This text is contained within a single paragraph. This paragraph is two
          sentences long.
        </p>
        <p>
          This is a new paragraph. There is a line break element
          <code>&lt;br&gt;</code> after this sentence.<br />There it is! Notice how
          it affects the indentation.
        </p>
      </div>
    </section>
    

    section {
      font-size: 1.25em;
      background-color: darkslateblue;
      align-items: start;
    }
    
    #example-element {
      text-align: left;
      margin-left: 3em;
      background-color: slateblue;
      color: white;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#syntax)

---------------------------------------------------------------------------------------------------

css

    /* <length-percentage> values */
    text-indent: 3mm;
    text-indent: 40px;
    text-indent: 15%;
    
    /* with keyword values */
    text-indent: 5em each-line;
    text-indent: 5vb hanging;
    text-indent: 5% hanging each-line;
    
    /* Global values */
    text-indent: inherit;
    text-indent: initial;
    text-indent: revert;
    text-indent: revert-layer;
    text-indent: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Indentation is specified as an absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
. Negative values are allowed. See [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values for possible units.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Indentation is a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. The percentage is relative to the container's own inner inline size.

[`each-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#each-line)

Indentation affects the first line of the block container as well as each line after a _forced line break_, but does not affect lines after a _soft wrap break_.

[`hanging`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#hanging)

Inverts which lines are indented. All lines _except_ the first line will be indented.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#description)

-------------------------------------------------------------------------------------------------------------

The `text-indent` [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the length of empty space (indentation) that is put before lines of text in a block container. The indentation set by the property occurs at the inline-start edge of the content box. The value is a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, optionally with one or both of the keywords `each-line` and/or `hanging`. The initial value is `0`.

Percent values are relative to the block container's inline-axis inner size, which is the dimension of the content-area only, excluding the container's padding and border.

The `<length-percentage>` can be a positive or negative value. A negative value creates an outdent equal to the absolute value of the `<length-percentage>` equivalent positive value. A negative value effectively pushes the text the size of the value, but in the opposite direction. For example, `text-indent: 3%;` indents the first line of text, adding white space that is 3% of the container's inner-size before the text, pushing the first line of content toward the inline-end direction. Setting `text-indent: -3%` outdents the first line of text, pushing the start of the first line of text 3% of the container's inner-size past the inline-start of the content area, into the padding and border, possibly overflowing the container.

A negative value is different from adding the `hanging` keyword to a positive value. Continuing with the same example, `text-indent: 3% hanging` doesn't outdent the first line of text. Rather, it indents all the lines of text _except_ the first line, by 3% of the container's inner-size.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length, plus any keywords as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

text-indent =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  hanging[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  each-line[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                 
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#basic_usage)

This example demonstrates the basic usage of the `text-indent` property.

#### HTML

We include two paragraphs of text.

html

    <p>
      Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
      nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
    </p>
    <p>
      Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
      nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
    </p>
    

#### CSS

We use the `text-indent` property to indent the first line of each paragraph by `5em`.

css

    p {
      text-indent: 5em;
      background: powderblue;
    }
    

#### Result

### [Percentage indent](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#percentage_indent)

Using the same HTML as in the previous example, here we demonstrate using percentage values and how percentage values are relative to the element's content area in the inline direction.

    <p>
      Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
      nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
    </p>
    <p>
      Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
      nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
    </p>
    

#### CSS

We set the `text-indent` to a percentage value. We also added padding and vertical stripes to better enable gauging the size of the indentation relative to the element's box model.

css

    p {
      text-indent: 30%;
    
      padding: 30px;
      background-image: repeating-linear-gradient(
        to right,
        transparent 0 9.5%,
        #dedede 9.5% 10%
      );
      background-color: plum;
    }
    

#### Result

### [Skipping indentation on the first paragraph](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#skipping_indentation_on_the_first_paragraph)

A common typographic practice when paragraph indentation is present is to skip the indentation for the first paragraph. As _The Chicago Manual of Style_ puts it, "the first line of text following a subhead may begin flush left or be indented by the usual paragraph indention."

Treating first paragraphs differently from subsequent paragraphs can be done using the [next-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator)
, as in the following example:

#### HTML

html

    <h2>Lorem ipsum</h2>
    
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu
      venenatis quam. Vivamus euismod eleifend metus vitae pharetra. In vel tempor
      metus. Donec dapibus feugiat euismod. Vivamus interdum tellus dolor. Vivamus
      blandit eros et imperdiet auctor. Mauris sapien nunc, condimentum a efficitur
      non, elementum ac sapien. Cras consequat turpis non augue ullamcorper, sit
      amet porttitor dui interdum.
    </p>
    
    <p>
      Sed laoreet luctus erat at rutrum. Proin velit metus, luctus in sapien in,
      tincidunt mattis ex. Praesent venenatis orci at sagittis eleifend. Nulla
      facilisi. In feugiat vehicula magna iaculis vehicula. Nulla suscipit tempor
      odio a semper. Donec vitae dapibus ipsum. Donec libero purus, convallis eu
      efficitur id, pulvinar elementum diam. Maecenas mollis blandit placerat. Ut
      gravida pellentesque nunc, in eleifend ante convallis sit amet.
    </p>
    
    <h2>Donec ullamcorper elit nisl</h2>
    
    <p>
      Donec ullamcorper elit nisl, sagittis bibendum massa gravida in. Fusce tempor
      in ante gravida iaculis. Integer posuere tempor metus. Vestibulum lacinia,
      nunc et dictum viverra, urna massa aliquam tellus, id mollis sem velit
      vestibulum nulla. Pellentesque habitant morbi tristique senectus et netus et
      malesuada fames ac turpis egestas. Donec vulputate leo ut iaculis ultrices.
      Cras egestas rhoncus lorem. Nunc blandit tempus lectus, rutrum hendrerit orci
      eleifend id. Ut at quam velit.
    </p>
    
    <p>
      Aenean rutrum tempor ligula, at luctus ligula auctor vestibulum. Sed
      sollicitudin velit in leo fringilla sollicitudin. Proin eu gravida arcu. Nam
      iaculis malesuada massa, eget aliquet turpis sagittis sed. Sed mollis tellus
      ac dui ullamcorper, nec lobortis diam pellentesque. Quisque dapibus accumsan
      libero, sed euismod ipsum ullamcorper sed.
    </p>
    

#### CSS

css

    p {
      text-align: justify;
      margin: 1em 0 0 0;
    }
    p + p {
      text-indent: 2em;
      margin: 0;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# text-indent-property](https://drafts.csswg.org/css-text/#text-indent-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent#see_also)

-------------------------------------------------------------------------------------------------------

*   Related CSS properties:
    *   [`text-justify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify)
        
    *   [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
        
    *   [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
        
    *   [`text-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering)
        
    *   [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
        
    *   [`hanging-punctuation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation)
        
*   [CSS text decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration)
     module
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module
*   [Learn to style HTML using CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-indent/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-indent (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-indent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-indent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-indent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-indent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")