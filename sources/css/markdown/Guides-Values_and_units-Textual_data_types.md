*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types#mdn-search)
    

Textual data types
==================

Every CSS declaration consists of a property/value pair. The value can include various data types depending on the property, such as a single keyword, integer, function, or a combination of different types; some values have units, while others do not. This guide provides an overview of the textual data types. Refer to the page for each value type for more detailed information.

Text data types are either [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
, a quoted series of characters, an [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
, a "CSS Identifier" which is an unquoted string, or an optionally quoted [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
. A `<string>` is quoted with either single or double quotes. CSS identifiers, listed in the specifications as `<ident>` or [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, must be unquoted.

In CSS specifications, values that can be defined by the web developer — such as keyframe animation names, font-family names, or grid areas — are listed as a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
, [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
, or both.

When both quoted and unquoted user-defined text values are permitted, the specification will list `<custom-ident> | <string>`, meaning quotes are optional, such as is the case with \[keyframe animation names\]:

Some text values are not valid if encompassed in quotes. For example, the value of [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
 can be a `<custom-ident>`, so if we had a grid area named `content` we would use it without quotes:

In comparison, a data type that is a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
, such as a string value of the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property, must be quoted:

While you can generally create any name you want, including using emojis, the identifier can't be `none`, `unset`, `initial`, or `inherit`, start with a digit or two dashes, and generally you don't want it to be any other pre-defined CSS keyword. See the [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 and [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 reference pages for more details.

[Pre-defined keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types#pre-defined_keyword_values)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Pre-defined keywords are text values defined by the specification for that property. These keywords are also CSS identifiers, and are therefore used without quotes.

When viewing CSS property value syntax in a CSS specification or the MDN property page, allowable keywords will be listed in the following form. The following [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are the pre-defined keyword values allowed for [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
.

left | right | none | inline-start | inline-end

Such values are used without quotes:

[CSS-wide keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types#css-wide_keywords)

-----------------------------------------------------------------------------------------------------------------------------------

In addition to the pre-defined keywords that are part of the specification for a property, all CSS properties accept the CSS-wide, or "global", property values [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
, [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
, [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
, [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
, and [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
, which explicitly specify defaulting behaviors.

[`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)

Represents the value specified as the property's initial value.

[`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)

Represents the computed value of the property on the element's parent, provided it is inherited.

[`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)

Acts as either `inherit` or `initial`, depending on whether the property is inherited or not.

[`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)

Resets the property to its inherited value if it inherits from its parent or to the default value established by the user agent's stylesheet (or by user styles if any exist).

[`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)

Rolls back the value of a property in a [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
 to the value of the property in a CSS rule matching the element in a previous cascade layer. The value of the property with this keyword is recalculated as if no rules were specified on the target element in the current cascade layer.

[URLs](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types#urls)

---------------------------------------------------------------------------------------------------------

A [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 type uses functional notation, which accepts a `<string>` that is a URL. This may be an absolute URL or a relative URL. For example, if you wanted to include a background image, you might use either of the following:

The parameter for `url()` can be either quoted or unquoted. If unquoted, it is parsed as a `<url-token>`, which has extra requirements including escaping certain characters. See [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 for more information.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Numeric data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types)
    
*   [CSS data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [Learn: Values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
    
*   [CSS cascade and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Textual_data_types/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/values_and_units/textual_data_types/index.md?plain=1 "Folder: en-us/web/css/guides/values_and_units/textual_data_types (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FTextual_data_types&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Ftextual_data_types%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FTextual_data_types%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Ftextual_data_types%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")