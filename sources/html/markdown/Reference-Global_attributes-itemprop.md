*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#mdn-search)
    

`itemprop` HTML global attribute
================================

The **`itemprop`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is used to add properties to an item. Every HTML element can have an `itemprop` attribute specified, and an `itemprop` consists of a name-value pair. Each name-value pair is called a **property**, and a group of one or more properties forms an **item**. Property values are either a string or a URL and can be associated with a very wide range of elements including [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
, [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
, [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
, [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
, [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
, [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)
, and [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#examples)

------------------------------------------------------------------------------------------------------------

The example below shows the source for a set of elements marked up with `itemprop` attributes, followed by a table showing the resulting structured data.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#html)

### [Structured data](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#structured_data)

|     |     |     |
| --- | --- | --- |
|     | **Item** |     |
| **itemprop name** | **itemprop value** |
| itemprop | name | Avatar |
| itemprop | director | James Cameron |
| itemprop | genre | Science fiction |
| itemprop | trailer | ../movies/avatar-theatrical-trailer.html |

[Properties](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#properties)

----------------------------------------------------------------------------------------------------------------

Properties have values that are either a string or a URL. When a string value is a URL, it is expressed using the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element and its [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 attribute, the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element and its [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#src)
 attribute, or other elements that link to or embed external resources.

### [Three properties with values that are strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#three_properties_with_values_that_are_strings)

### [One property, "image", whose value is a URL](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#one_property_image_whose_value_is_a_url)

When a string value can't be easily read and understood by a person (e.g., a long string of numbers and letters), it can be displayed using the value attribute of the data element, with the more easily-understood-by-a human-version given in the element's contents (which is not part of the structured data - see example below).

### [An item with a property whose value is a product ID](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#an_item_with_a_property_whose_value_is_a_product_id)

The ID is not human-friendly, so the product's name is used instead.

For numeric data, the meter element and its value attribute can be used.

### [A meter element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#a_meter_element)

Similarly, for date- and time-related data, the time element and its datetime attribute can be used.

### [An item with one property, "birthday", whose value is a date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#an_item_with_one_property_birthday_whose_value_is_a_date)

Properties can also be groups of name-value pairs, by putting the itemscope attribute on the element that declares the property. Each value is either a string or a group of name-value pairs (i.e., an item).

### [An outer item representing a person, and an inner one representing a band](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#an_outer_item_representing_a_person_and_an_inner_one_representing_a_band)

The outer item above has two properties, "name" and "band". The "name" is "Amanda", and the "band" is an item in its own right, with two properties, "name" and "size". The "name" of the band is "Jazz Band", and the "size" is "12". The outer item in this example is a top-level microdata item. Items that are not part of others are called top-level microdata items.

### [All the properties separated from their items](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#all_the_properties_separated_from_their_items)

This example is the same as the previous one, but all the properties are separated from their items.

This gives the same result as the previous example. The first item has two properties, "name", set to "Amanda", and "band", set to another item. That second item has two further properties, "name", set to "Jazz Band", and "size", set to "12".

An item can have multiple properties with the same name and different values.

### [Ice cream with two flavors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#ice_cream_with_two_flavors)

This results in an item with two properties, both with the name "flavor" and having the values "Lemon sorbet" and "Apricot sorbet".

An element introducing a property can also introduce multiple properties at once, to avoid duplication when some of the properties have the same value.

### [An item with two properties, "favorite-color" and "favorite-fruit", both set to the value "orange"](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#an_item_with_two_properties_favorite-color_and_favorite-fruit_both_set_to_the_value_orange)

**Note:** There is no relationship between the microdata and the content of the document where the microdata is marked up.

### [Same structured data marked up in two different ways](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#same_structured_data_marked_up_in_two_different_ways)

There is no semantic difference between the following two examples

Both have a figure with a caption, and both, completely unrelated to the figure, have an item with a name-value pair with the name "name" and the value "The Castle". The only difference is that if the user drags the figcaption out of the document, the item will be included in the drag-and-drop data. The image associated with the item won't be included.

[Names and values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#names_and_values)

----------------------------------------------------------------------------------------------------------------------------

A property is an unordered set of unique tokens that are case-sensitive and represent the name-value pairs. The property value must have at least one token. In the example below, each data cell is a token.

### [Names examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#names_examples)

|     | Item |     |
| --- | --- | --- |
| itemprop **name** | itemprop **value** |
| --- | --- | --- |
| itemprop | country | Ireland |
| itemprop | Option | 2   |
| itemprop | https://www.flickr.com/photos/nlireland/6992065114/ | Ring of Kerry |
| itemprop | img | https://www.flickr.com/photos/nlireland/6992065114/ |
| itemprop | website | flickr |
| itemprop | (token) | (token) |

**Tokens** are either strings or URL's. An item is called a **typed item** if it is a URL. Otherwise, it is a string. Strings cannot contain a period or a colon (see below).

1.  If the item is a typed item it must be either:
    
    1.  A defined property name, or
    2.  A valid URL, which refers to the vocabulary definition, or
    3.  A valid URL that is used as a proprietary item property name (i.e., one not defined in a public specification), or
2.  If the item is not a typed item it must be:
    
    1.  A string that contains no `.` (U+002E FULL STOP) characters and no `:` characters (U+003A COLON) and is used as a proprietary item property name (again, one not defined in a public specification).

**Note:** The rules above disallow ":" characters in non-URL values because otherwise they could not be distinguished from URLs. Values with "." characters are reserved for future extensions. Space characters are disallowed because otherwise the values would be parsed as multiple tokens.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#value)

------------------------------------------------------------------------------------------------------

The property value of a name-value pair is as given for the first matching case in the following list:

*   If the element has an `itemscope` attribute
    
    *   The value is the **item** created by the element
*   If the element is a `meta` element
    
    *   The value is the value of the element's `content` attribute
*   If the element is an `audio`, `embed`, `iframe`, `img`, `source`, `track`, or `video` element
    
    *   The value is the resulting URL string that results from parsing the value of the element's src attribute relative to the node document (part of the [Microdata DOM API](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata)
        ) of the element at the time the attribute is set
*   If the element is an `a`, `area`, or `link` element
    
    *   The value is the resulting URL string that results from parsing the value of the element's href attribute relative to the node document of the element at the time the attribute is set
*   If the element is an `object` element
    
    *   The value is the resulting URL string that results from parsing the value of the element's data attribute relative to the node document of the element at the time the attribute is set
*   If the element is a `data` element
    
    *   The value is the value of the element's value attribute
*   If the element is a `meter` element
    
    *   The value is the value of the element's `value` attribute
*   If the element is a `time` element
    
    *   The value is the element's `datetime` value

Otherwise

*   The value is the element's _textContent_.

If a property's value is a `URL`, the property must be specified using a URL property element. The URL property elements are the `a`, `area`, `audio`, `embed`, `iframe`, `img`, `link`, `object`, `source`, `track`, and `video` elements.

### [Name order](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#name_order)

Names are unordered relative to each other, but if a particular name has multiple values, they do have a relative order.

In the following example, the "a" property has the values "1" and "2", _in that order_, but whether the "a" property comes before the "b" property or not is not important.

Here are several equivalent examples:

### [Representing structured data for a book](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#representing_structured_data_for_a_book)

This example uses microdata attributes to represent the following structured data:

|     |     |     |
| --- | --- | --- |
| itemscope | itemtype: itemid | https://schema.org/Book: urn:isbn:0-374-22848-5 |     |
| itemprop | title | Owls of the Eastern Ice |
| itemprop | author | Jonathan C Slaght |
| itemprop | datePublished | 2020-08-04 |

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# names:-the-itemprop-attribute](https://html.spec.whatwg.org/multipage/microdata.html#names:-the-itemprop-attribute) |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop#see_also)

------------------------------------------------------------------------------------------------------------

*   [Other different global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   Other microdata related global attributes:
    *   [`itemid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid)
        
    *   [`itemref`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref)
        
    *   [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
        
    *   [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/itemprop/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/itemprop (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemprop&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemprop%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemprop%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemprop%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")