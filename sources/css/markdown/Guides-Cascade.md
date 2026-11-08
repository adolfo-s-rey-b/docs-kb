*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#mdn-search)
    

CSS cascading and inheritance
=============================

The **CSS cascading and inheritance** module defines the rules for assigning values to properties by way of cascading and inheritance. This module specifies the rules for finding the specified value for all properties on all elements.

One of the fundamental design principles of CSS is cascading of rules. It allows several style sheets to influence the presentation of a document. CSS property-value declarations define how a document is rendered. Multiple declarations may set different values for the same element and property combination, but only one value can be applied to any CSS property. The CSS cascade module defines how these conflicts are resolved.

The opposite also occurs. Sometimes there are no declarations defining the value of a property. The CSS cascade module defines how these missing values should be set via inheritance or from the property's initial value.

**Note:** The rules for finding the specified values in the page context and its margin boxes are described in the [CSS page module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#reference)

---------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#properties)

*   [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#at-rules_and_descriptors)

*   [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
    
*   [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
    

### [Keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#keywords)

*   [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    
*   [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    
*   [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    
*   [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    
*   [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    
*   [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
     flag

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#interfaces)

*   [`CSSLayerBlockRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSLayerBlockRule)
    
*   [`CSSGroupingRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSGroupingRule)
    
*   [`CSSLayerStatementRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSLayerStatementRule)
    
*   [`CSSRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSRule)
    

### [Glossary terms and definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#glossary_terms_and_definitions)

*   [Actual value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
    
*   [Anonymous layer](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers#the_layer_block_at-rule_for_named_and_anonymous_layers)
    
*   [Author origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#author_stylesheets)
    
*   [Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    
*   [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    
*   [Named layer](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers#the_layer_statement_at-rule_for_named_layers)
    
*   [Resolved value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#resolved_value)
    
*   [Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
    
*   [style origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
    
*   [Used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    
*   [User origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#user_stylesheets)
    
*   [User-agent origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#user-agent_stylesheets)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#guides)

---------------------------------------------------------------------------------

[Introducing the CSS Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)

Guide to the cascade algorithm that defines how user agents combine property values originating from different sources.

[CSS inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)

A guide to CSS inheritance.

[Learn: Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)

The most fundamental concepts of CSS — the cascade, specificity, and inheritance — which control how CSS is applied to HTML and how conflicts are resolved.

[Learn: Cascade layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers)

Introduction to [cascade layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
, a more advanced feature that builds on the fundamental concepts of the [CSS cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
 and [CSS specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#related_concepts)

-----------------------------------------------------------------------------------------------------

*   [Element-attached styles](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/style)
    
*   [Inline styles and the cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#inline_styles)
    
*   [Conditional rules for @imports](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import#importing_css_rules_conditional_on_media_queries)
    
*   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#specifications)

-------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 4](https://drafts.csswg.org/css-cascade/) |
| [CSS Cascading and Inheritance Level 5](https://drafts.csswg.org/css-cascade-5/) |
| [CSS Cascading and Inheritance Level 6](https://drafts.csswg.org/css-cascade-6/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade#see_also)

-------------------------------------------------------------------------------------

*   [CSS selectors module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
*   [CSS pseudo-elements module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
    
*   [CSS paged media module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
    
*   [CSS conditional rules module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
    
*   [CSS nesting module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
    
*   [Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 18, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cascade/index.md?plain=1 "Folder: en-us/web/css/guides/cascade (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcascade%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F81f8fcd666952c1782653a3675347c392cc997ca%0A*+Document+last+modified%3A+2025-11-18T10%3A30%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")