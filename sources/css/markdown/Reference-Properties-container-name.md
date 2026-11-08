*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#mdn-search)
    

`container-name` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **container-name** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a list of query container names used by the [@container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule in a [container query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#values)

This property is specified as a space-separated list of `<custom-ident>` values or the keyword `none`:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#none)

The default value. The query container has no name.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

A case-sensitive string that is used to identify the container. The following conditions apply:

*   The name must not equal `or`, `and`, `not`, or `default`.
*   The name value must not be in quotes.
*   The dashed ident intended to denote author-defined identifiers (e.g., `--container-name`) is permitted.
*   A list of multiple names separated by a space is allowed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `none` or an ordered list of identifiers |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

container-name =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#description)

----------------------------------------------------------------------------------------------------------------

With no name specified, a container query will apply styles to elements based on attributes such as the [size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_size_queries)
 or [scroll-state](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
 of the nearest ancestor with a [containment context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#naming_containment_contexts)
.

**Note:** Size containers' descendants can be sized using [container query length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#container_query_length_units)
.

When a containment context is given a name, it can be specifically targeted by setting that name on a [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule.

It is possible to create a query container by assigning a `container-name` to an element, and then query only the existence of that name in the associated `@container` at-rule, with no query expression specified. These so-called [**name-only container queries**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
 enable selectively applying styles to elements based only on whether they have an ancestor with a specific `container-name` set.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#examples)

----------------------------------------------------------------------------------------------------------

### [Using a container name](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#using_a_container_name)

Given the following HTML example which is a card component with a title and some text:

To create a containment context, add the `container-type` property to an element in CSS. The following example creates two containment contexts, one for the card meta information and one for the post excerpt:

**Note:** A shorthand syntax for these declarations are described in the [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
 page.

Writing a container query via the [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule will apply styles to the elements of the container when the query evaluates to true. The following example has two container queries, one that will apply only to the contents of the `.post-excerpt` element and one that will apply to both the `.post-meta` and `.post-excerpt` contents:

For more information on writing container queries, see the [CSS Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
 page.

### [Using multiple container names](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#using_multiple_container_names)

You can also provide multiple names to a container context separated by a space:

This will allow you to target the container using either name in the [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule. This is useful if you want to target the same container with multiple container queries where either condition could be true:

### [Using a name-only container query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#using_a_name-only_container_query)

This example demonstrates how to use a [name-only container query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
.

#### HTML

We include a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 with an `id` of `container`, and three [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements, two inside the container, and one outside the container:

#### CSS

We assign a name to the container:

We can then selectively apply styles only to elements inside containers with that name set, as shown in the next snippet.

#### Result

The specified styles should be applied only to the first and second [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements, but not to the third.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Conditional Rules Module Level 5  <br>\# container-name](https://drafts.csswg.org/css-conditional-5/#container-name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name#see_also)

----------------------------------------------------------------------------------------------------------

*   [CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [Using container size and style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)
    
*   [Using container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
    
*   [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
     at-rule
*   CSS [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
     shorthand property
*   CSS [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
     property
*   CSS [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/container-name/index.md?plain=1 "Folder: en-us/web/css/reference/properties/container-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontainer-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontainer-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontainer-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontainer-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")