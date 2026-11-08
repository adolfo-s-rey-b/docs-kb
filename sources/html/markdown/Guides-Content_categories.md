*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#mdn-search)
    

Content categories
==================

Most [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 elements are a member of one or more **content categories** — these categories group elements that share common characteristics. This is a loose grouping (it doesn't actually create a relationship among elements of these categories), but they help define and describe the categories' shared behavior and their associated rules. It's possible for [elements to not be a member of _any_ of these categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#elements_without_a_category)
.

The content categories are used to define the _content model_ of elements, in other words, what each element can take as descendants. For example, the `<p>` element can only contain _phrasing content_, while the `<div>` element can contain _flow content_. Some elements, like `<ins>`, have a [_transparent_ content model](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)
.

There are seven main content categories, which can be summarized with the Venn diagram below:

![A Venn diagram showing how the various content categories interrelate. The following sections explain these relationships in text.](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories/content_categories_venn.png)

**Note:** A more detailed discussion of these content categories and their comparative functionalities is beyond the scope of this article; for that, you may wish to read the [relevant portions of the HTML specification](https://html.spec.whatwg.org/multipage/dom.html#kinds-of-content "External link (opens in new tab)")
.

[Metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)

-----------------------------------------------------------------------------------------------------------------

Elements belonging to the _metadata content_ category modify the presentation or the behavior of the rest of the document, set up links to other documents, or convey other _out-of-band_ information. Everything in the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
, including the `<title>`, `<link>`, `<script>`, `<style>`, and the lesser used `<base>`, is metadata content. There is a `<meta>` element for metadata that cannot be represented by these other elements.

The metadata elements are:

*   [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
    
*   [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
    
*   [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
    
*   [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)
    
*   [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    
*   [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
    
*   [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
    
*   [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
    

Some of these elements belong to more than one content category. For example, `<script>` is a member of the metadata, flow, and phrasing content categories, and is a script-supporting element; `<script>` can be used where metadata content, phrasing content, or script-supporting elements are expected.

[Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)

---------------------------------------------------------------------------------------------------------

Flow content is a broad category that encompasses most elements that can go inside the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element, including heading elements, sectioning elements, phrasing elements, embedding elements, interactive elements, and form-related elements. It also includes text nodes (but not those that only consist of white space characters).

The flow elements are:

*   [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    
*   [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
    
*   [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    
*   [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    
*   [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    
*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    
*   [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
    
*   [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
    
*   [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
    
*   [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
    
*   [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
    
*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    
*   [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
    
*   [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
    
*   [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    
*   [`<data>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data)
    
*   [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
    
*   [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
    
*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
    
*   [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
    
*   [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
    
*   [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
    
*   [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
    
*   [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    
*   [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
    
*   [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
    
*   [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
    
*   [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    
*   [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
    
*   [`<geolocation>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/geolocation)
    
*   [`<h1>`\-`<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    
*   [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    
*   [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)
    
*   [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr)
    
*   [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
    
*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
    
*   [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    
*   [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    
*   [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
    
*   [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
    
*   [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
    
*   [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
    
*   [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
    
*   [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    
*   [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    
*   [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)
    
*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    
*   [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
    
*   [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
    
*   [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
    
*   [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
    
*   [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
    
*   [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
    
*   [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    
*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s)
    
*   [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
    
*   [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    
*   [`<search>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search)
    
*   [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
    
*   [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small)
    
*   [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
    
*   [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
    
*   [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
    
*   [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
    
*   [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    
*   [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
    
*   [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    
*   [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
    
*   [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u)
    
*   [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
    
*   [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
    
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    
*   [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
    
*   [Autonomous custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
    
*   Plain text

A few other elements belong to this category, but only if a specific condition is fulfilled:

*   [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
    , if it is a descendant of a [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
     element
*   [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
    , if the [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
     attribute is present
*   [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
    , if the [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
     attribute is present

[Sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)

---------------------------------------------------------------------------------------------------------------------

Sectioning content, a subset of flow content, creates a [section in the current outline](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 defining the scope of [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
 and [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
 elements.

The sectioning elements are:

*   [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    
*   [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    
*   [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    
*   [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    

[Heading content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#heading_content)

---------------------------------------------------------------------------------------------------------------

Heading content, a subset of flow content, defines the title of a section. This definition applies both to sections marked by an explicit [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)
 elements and to those implicitly defined by the heading content itself.

The heading elements are:

*   [`<h1>`\-`<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    
*   [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)
    

**Note:** Though likely to contain heading content, the [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
 is not heading content itself.

[Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)

-----------------------------------------------------------------------------------------------------------------

Phrasing content, a subset of flow content, refers to the text and the markup within a document. Sequences of phrasing content make up paragraphs.

The phrasing elements are:

*   [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
    
*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    
*   [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
    
*   [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
    
*   [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
    
*   [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
    
*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    
*   [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
    
*   [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
    
*   [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    
*   [`<data>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data)
    
*   [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
    
*   [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
    
*   [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    
*   [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
    
*   [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
    
*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    
*   [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    
*   [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
    
*   [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
    
*   [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    
*   [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)
    
*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    
*   [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
    
*   [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
    
*   [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
    
*   [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    
*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s)
    
*   [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
    
*   [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
    
*   [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small)
    
*   [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
    
*   [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
    
*   [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
    
*   [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    
*   [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
    
*   [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
    
*   [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u)
    
*   [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
    
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    
*   [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
    
*   [Autonomous custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
    
*   Plain text

A few other elements belong to this category, but only if a specific condition is fulfilled:

*   [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    , if it contains only phrasing content
*   [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
    , if it is a descendant of a [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
     element
*   [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
    , if it contains only phrasing content
*   [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
    , if it contains only phrasing content
*   [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
    , if the [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
     attribute is present
*   [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
    , if it contains only phrasing content
*   [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
    , if the [`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)
     attribute is present

[Embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#embedded_content)

-----------------------------------------------------------------------------------------------------------------

Embedded content, a subset of flow content, imports another resource or inserts content from another markup language or namespace into the document.

The embedded content elements are:

*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    
*   [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
    
*   [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
    
*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
    
*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    
*   [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
    
*   [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
    
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    

[Interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)

-----------------------------------------------------------------------------------------------------------------------

Interactive content, a subset of flow content, includes elements that are specifically designed for user interaction.

The interactive content elements are:

*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    
*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
    
*   [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
    
*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    
*   [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    

Some elements belong to this category only under specific conditions:

*   [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    , if the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
     attribute is present
*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    , if the [`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#controls)
     attribute is present
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    , if the [`usemap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#usemap)
     attribute is present
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    , if the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
     attribute is not in the hidden state
*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    , if the [`usemap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object#usemap)
     attribute is present
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    , if the [`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#controls)
     attribute is present

[Palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)

-----------------------------------------------------------------------------------------------------------------

**Palpable content** is content that is neither empty nor hidden; it is content that is rendered and substantive. Palpable content is not used to define content models but is used to define a general rule: Elements whose content model allows any flow content or phrasing content should have at least one node in its contents that is palpable content and that does not have the `hidden` attribute specified.

The palpable elements are:

*   [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    
*   [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
    
*   [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    
*   [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    
*   [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    
*   [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
    
*   [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
    
*   [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
    
*   [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
    
*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    
*   [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
    
*   [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
    
*   [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    
*   [`<data>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data)
    
*   [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
    
*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
    
*   [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
    
*   [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
    
*   [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    
*   [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed)
    
*   [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
    
*   [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    
*   [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
    
*   [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
    
*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
    
*   [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    
*   [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    
*   [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
    
*   [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
    
*   [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
    
*   [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
    
*   [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    
*   [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    
*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    
*   [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
    
*   [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
    
*   [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
    
*   [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
    
*   [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    
*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s)
    
*   [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
    
*   [`<search>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search)
    
*   [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small)
    
*   [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
    
*   [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
    
*   [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
    
*   [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    
*   [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
    
*   [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
    
*   [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u)
    
*   [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
    
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    
*   [Autonomous custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
    
*   Plain text that is not inter-element [whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
    

Some elements belong to this category only under specific conditions:

*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    , if the [`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#controls)
     attribute is present
*   [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
    , if the element's children include at least one name-value group
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    , if the [type](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
     attribute is not in the hidden state
*   [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
    , if its children include at least one [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
     element
*   [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
    , if its children include at least one [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
     element

[Elements without a category](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#elements_without_a_category)

---------------------------------------------------------------------------------------------------------------------------------------

Several elements are not a member of _any_ content category. These include:

*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    
*   [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    
*   [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    
*   [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
    
*   [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
    
*   [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
    
*   [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
    
*   [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
    
*   [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
    
*   [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
    
*   [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
    
*   [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
    
*   [`<param>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param)
    
*   [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)
    
*   [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    
*   [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    
*   [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)
    
*   [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
    
*   [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    
*   [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    
*   [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
    
*   [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    
*   [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
    
*   [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)
    

[Script-supporting elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#script-supporting_elements)

-------------------------------------------------------------------------------------------------------------------------------------

**Script-supporting elements** are elements that don't directly contribute to a document's rendered output. Instead, they serve to support scripts, either by containing or specifying script code directly or by specifying data that will be used by scripts. Nearly all elements, including those that only take specific elements (such as [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
, which takes [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements), can contain script-supporting elements.

The script-supporting elements are:

*   [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    
*   [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
    

[Form-associated content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)

-------------------------------------------------------------------------------------------------------------------------------

Form-associated content is a subset of flow content comprising elements that have a form owner and can be used everywhere flow content is expected. A form owner is either the containing [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element or the `<form>` whose `id` is specified in the element's `form` attribute.

The form-associated elements are:

*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    
*   [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
    
*   [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    

This category contains several sub-categories:

[listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)

Elements that are listed in the [`HTMLFormElement.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements)
 and [`HTMLFieldSetElement.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFieldSetElement/elements)
 collections. Includes [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[submittable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#submittable)

Elements that can be used for constructing the form data set when the form is submitted. Includes [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[resettable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#resettable)

Elements that can be affected when a form is reset. Includes [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[autocapitalize-and-autocorrect-inheriting](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#autocapitalize-and-autocorrect-inheriting)

Elements that inherit the [`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize)
 and [`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)
 attributes from their form owner. Includes [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)

Elements that can be associated with [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 elements. Includes [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 (all types other than `hidden`), [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[Transparent content model](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)

-----------------------------------------------------------------------------------------------------------------------------------

In addition to the listed content categories, an element's content model may also be defined as "transparent". If an element X's permitted content is "transparent", then we look at the parent of X. We intersect the permitted content of X's parent with the content categories of X, and the result is what "transparent" means in this context. If the parent of X also has a transparent content model, then we continue up the tree until we find a non-transparent content model. When there's no such parent, "transparent" means "flow content".

For example, a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 element accepts phrasing content. The [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
 element is of category phrasing content when it contains only phrasing content. Therefore, an [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
 element can be placed inside a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 element. The `<ins>` element's permitted content is "transparent", which when nested in `<ruby>` means "phrasing content". However, [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
 elements are not phrasing content. Therefore, an [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
 element cannot be nested inside this `<ins>` element, even though both `<rt>` and `<ins>` can be inside `<ruby>`, and `<ins>` is "transparent".

Transparent is a _content model_, not a _content category_, so it only defines what an element can contain, not where the element can be placed. That is, when determining an element's children's licitness, you cannot "see through" transparent children. For example, a [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 element accepts only [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements and script-supporting elements, and does not allow `<del>` or `<ins>`, even if the `<del>` only contains `<li>` elements.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/content_categories/index.md?plain=1 "Folder: en-us/web/html/guides/content_categories (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FContent_categories&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fcontent_categories%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FContent_categories%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fcontent_categories%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb58d84c261b9cfa66d46a070ba205c53e18ee3e0%0A*+Document+last+modified%3A+2026-10-27T23%3A22%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")