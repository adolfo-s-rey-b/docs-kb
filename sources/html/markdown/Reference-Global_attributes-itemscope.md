*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#mdn-search)
    

`itemscope` HTML global attribute
=================================

**`itemscope`** is a boolean [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 that defines the scope of associated metadata. Specifying the **`itemscope`** attribute for an element creates a new item, which results in a number of name-value pairs that are associated with the element.

A related attribute, [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
, is used to specify the valid URL of a vocabulary (such as [schema.org](https://schema.org/ "External link (opens in new tab)")
) that describes the item and its properties context. In each of the following examples, the vocabulary is from [schema.org](https://schema.org/ "External link (opens in new tab)")
.

Every HTML element may have an `itemscope` attribute specified. An `itemscope` element that does not have an associated `itemtype` must have an associated `itemref`.

**Note:** Find more about `itemtype` attributes at [https://schema.org/Thing](https://schema.org/Thing "External link (opens in new tab)")

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#usage_notes)

-------------------------------------------------------------------------------------------------------------------

### [itemscope id attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#itemscope_id_attributes)

When you specify the `itemscope` attribute for an element, a new item is created. The item consists of a group of name-value pairs. For elements with an `itemscope` attribute and an `itemtype` attribute, you may also specify an [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute. You can use the `id` attribute to set a global identifier for the new item. A global identifier allows the item to relate to other items found on pages across the Web.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#examples)

-------------------------------------------------------------------------------------------------------------

### [Representing structured data for a movie](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#representing_structured_data_for_a_movie)

The following example specifies the `itemtype` as "http://schema.org/Movie", and specifies four related `itemprop` attributes.

|     |     |     |
| --- | --- | --- |
| itemscope | Itemtype | Movie |     |
| itemprop | (itemprop name) | (itemprop value) |
| itemprop | director | James Cameron |
| itemprop | genre | Science Fiction |
| itemprop | name | Avatar |
| itemprop | Trailer | https://youtu.be/0AY1XIkX7bY |

### [Representing structured data for a recipe](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#representing_structured_data_for_a_recipe)

There are four `itemscope` attributes in the following example. Each `itemscope` attribute sets the scope of its corresponding `itemtype` attribute. The `itemtype`s, `Recipe`, `AggregateRating`, and `NutritionInformation` in the following example are part of the [schema.org](https://www.schema.org/ "External link (opens in new tab)")
 structured data for a recipe, as specified by the first `itemtype`, `http://schema.org/Recipe`.

|     |     |     |
| --- | --- | --- |
| itemscope | itemtype | Recipe |     |
| itemprop | name | Grandma's Holiday Apple Pie |
| itemprop | image | https://c1.staticflickr.com/1/30/42759561\_8631e2f905\_n.jpg |
| itemprop | datePublished | 2022-11-05 |
| itemprop | description | This is my grandmother's apple pie recipe. I like to add a dash of nutmeg. |
| itemprop | prepTime | PT30M |
| itemprop | cookTime | PT1H |
| itemprop | totalTime | PT1H30M |
| itemprop | recipeYield | 1 9" pie (8 servings) |
| itemprop | recipeIngredient | Thinly-sliced apples: 6 cups |
| itemprop | recipeIngredient | White sugar: 3/4 cup |
| itemprop | recipeInstructions | 1\. Cut and peel apples 2. Mix sugar and cinnamon. Use additional sugar for tart apples. |
| itemprop | author \[Person\] |     |
| itemprop | name | Carol Smith |
| itemscope | itemprop\[itemtype\] | aggregateRating \[AggregateRating\] |     |
| itemprop | ratingValue | 4.0 |
| itemprop | reviewCount | 35  |
| itemscope | itemprop\[itemtype\] | nutrition \[NutritionInformation\] |     |
| itemprop | servingSize | 1 medium slice |
| itemprop | calories | 250 cal |
| itemprop | fatContent | 12 g |

**Note:** A handy tool for extracting microdata structures from HTML is Google's [Rich Results Testing Tool](https://search.google.com/test/rich-results "External link (opens in new tab)")
. Try it on the HTML shown here.

#### HTML

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-itemscope](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemscope) |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Other different global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   Other microdata related global attributes:
    *   [`itemid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid)
        
    *   [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
        
    *   [`itemref`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref)
        
    *   [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/itemscope/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/itemscope (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemscope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemscope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fitemscope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fitemscope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")