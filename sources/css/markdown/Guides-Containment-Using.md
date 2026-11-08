*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#mdn-search)
    

Using CSS containment
=====================

CSS containment improves the performance of web pages by allowing the browser to isolate a subtree of the page from the rest of the page. If the browser knows that a part of the page is independent from the rest of the content, rendering can be optimized and performance improved.

The [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 and [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 properties enable developers to inform user agents whether or not an element should render its contents at all, and whether it should render its contents when it is offscreen. The user agent then applies containment to elements when appropriate, potentially deferring layout and rendering until needed.

This guide describes the basic aims of CSS containment and how to leverage `contain` and `content-visibility` for a better user experience.

[Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#basic_example)

---------------------------------------------------------------------------------------------------------

Web pages often contain multiple sections which are, logically, independent of each other. CSS containment enables them to be treated truly independently from each other when it comes to rendering.

For example, blogs usually contain several articles, each containing a headline and content, as in the markup below.

html

    <h1>My blog</h1>
    <article>
      <h2>Heading of a nice article</h2>
      <p>Content here.</p>
    </article>
    <article>
      <h2>Another heading of another article</h2>
      <p>More content here.</p>
    </article>
    

With CSS, we apply the [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 property with a value of `content` to each article. The `content` value is shorthand for `contain: layout paint style`:

css

    article {
      contain: content;
    }
    

Logically, each article is independent of the other articles on the page. This information is something that is usually known, and likely quite obvious, to the web developer creating the page. However, browsers don't know the intent of your content and cannot assume that an article or other section of content will be entirely self-contained.

This property provides a way of explaining this to the browser and giving it explicit permission to make performance optimizations. It tells the browser that the internal layout of the element is completely separate from the rest of the page, and that everything about the element is painted inside its bounds. Nothing can visibly overflow.

By setting `contain: content` on each `<article>` we have indicated this; we have told the browser that each article is independent. The browser can then use this information to make decisions about how to render each `<article>` of content. For example, it might not render articles that are outside the viewable area.

When additional articles are appended at the end of the page, the browser does not need to recalculate layout or repaint the preceding content; it also doesn't need to touch any area outside of the containing element's subtree. If box model properties are dependent, however, the browser will need to recalculate layout and repaint. For example, if the `<article>` is styled such that its size depends on its contents (e.g., with `height: auto`), then the browser will need to account for its size changing.

[Key concepts and terminology](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#key_concepts_and_terminology)

---------------------------------------------------------------------------------------------------------------------------------------

### [`contain` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#contain_values)

There are four types of containment: layout, paint, size, and style. Use the [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 property to specify the type or types you want to apply to an element by including any combination of these types.

#### Layout containment

css

    article {
      contain: layout;
    }
    

Layout is normally scoped to the entire document, which means that if you move one element the entire document needs to be treated as if things could have moved anywhere. By using `contain: layout` you can tell the browser it only needs to check this element — everything inside the element is scoped to that element and does not affect the rest of the page, with the containing box establishing an independent [formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Formatting_contexts)
.

In addition:

*   [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
     layout will be performed independently inside the specified element.
*   Margins won't collapse across a layout containment boundary.
*   The layout container is a [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
     for `absolute`\- and `fixed`\-positioned descendants.
*   The containing box creates a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    , therefore [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
     can be used.

**Note:** The `style` and `layout` values of `contain` are automatically applied when using the [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
 and [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 properties.

#### Paint containment

css

    article {
      contain: paint;
    }
    

Paint containment essentially clips the box to the padding edge of the [principal box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model#the_principal_box)
. There can be no visible overflow. The same additional notes are true for `paint` containment as `layout` containment (see above).

Another advantage is that if the element with containment applied is offscreen, the browser does not need to paint its child elements — these are also offscreen as they are contained completely by that box.

#### Size containment

css

    article {
      contain: size;
    }
    

Size containment does not offer much in the way of performance optimizations when used on its own. However, size containment means that the size of the size-contained element's children cannot affect the size of the element itself — its size is computed as if it had no children.

If you set `contain: size` on an element, you need to specify the size of the element using [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
, or the longhand properties [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
 and [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
, in that order. If no size is set, the element risks being zero-sized in most cases.

css

    article {
      contain: size;
      contain-intrinsic-size: 100vw auto none;
    }
    

#### Style containment

css

    article {
      contain: style;
    }
    

Despite the name, style containment does not provide scoped styles such as you would get with the [Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 or [`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
. The main use case for the `style` value is to prevent situations where a [CSS counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
 could be changed in an element, which could then affect the rest of the tree.

Using `contain: style` ensures the [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
 and [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
 properties create new counters scoped to that subtree only.

You can include more than one containment type by including multiple space-separated values, such as `contain: layout paint` or by using one of the two [special values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#special_values)
.

#### Special values

There are two special values of `contain` that are shorthand for the first three or all four of the containment types:

*   `content`
*   `strict`

We encountered the first in the example above. Using `contain: content` turns on `layout`, `paint`, and `style` containment. As it omits `size`, it is a safe value to apply widely.

The `contain: strict` declaration, which behaves the same as the declaration `contain: size layout paint style` (which includes four space-separated values), provides the most containment. It is riskier to use as it applies `size` containment; the risk exists that a box could end up zero-sized due to a reliance on the size of its children.

To remove this risk, always set a size when using `strict`:

css

    article {
      contain: strict;
      contain-intrinsic-size: 80vw auto none;
    }
    

The above is the same as:

css

    article {
      contain: size layout paint style;
      contain-intrinsic-size: 80vw auto none;
    }
    

### [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#content-visibility)

When you have a lot of content that would benefit from heavy containment that will often be offscreen — for example if all your blog posts are viewable on the blog home pages as an infinitely scrollable blog — `content-visibility: auto` can be used to apply all of the containments at once.

The [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 property controls whether or not an element renders its contents at all, along with forcing a strong set of containments, allowing user agents to potentially omit large swathes of layout and rendering work until it becomes needed. It enables the user agent to skip an element's rendering work (including layout and painting) until it is needed — which makes the initial page load much faster.

Its possible values are:

*   `visible`: The default behavior — an element's contents are laid out and rendered as normal.
*   `hidden`: The element [skips its contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents)
    . The skipped contents will not be accessible to user agent features such as find-in-page, tab-order navigation, etc., nor be selectable or focusable.
*   `auto`: The element turns on layout containment, style containment, and paint containment, as if `contain: content` was set. If the element is not [relevant to the user](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#relevant_to_the_user)
    , it also skips its contents. Unlike `hidden`, the skipped content is still available for user interactions, remaining focusable, selectable, in regular tab order, and available to in-content search.

### [Relevant to the user](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#relevant_to_the_user)

User-agents have a concept of content being [relevant to the user](https://drafts.csswg.org/css-contain/#relevant-to-the-user "External link (opens in new tab)")
. An element becomes "relevant to the user" if any of the following are true:

*   The element appears in the viewport, or a user-agent-defined margin around the viewport (50% of the viewport dimensions, to give the app time to prepare for when the element visibility changes).
*   The element or its contents receive focus.
*   The element or its contents are selected, for example by dragging over the text with the mouse cursor or by some other highlight operation.
*   The element or its contents are placed in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
    .

When `content-visibility: auto` is set, and the browser determines that content is relevant to the user, the browser will render that content.

### [Skips its contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents)

When you set `content-visibility: hidden` on an element, you are telling the browser that it is not relevant to the user, and therefore its [contents should be skipped](https://drafts.csswg.org/css-contain/#skips-its-contents "External link (opens in new tab)")
 and not rendered. This helps to improve performance.

The browser will also skip an element's contents when `content-visibility: auto` is set on it, and the browser determines that its content is _not_ relevant to the user.

When an element skips its contents:

*   It has layout, style, paint, and size containment turned on.
*   Its contents are not painted, as if [`visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
     was set on it.
*   Its contents do not receive pointer events, as if [`pointer-events: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events)
     was set on it.

This happens in both the cases mentioned above, but with `content-visibility: auto` the content can be searched, receive focus, and otherwise move from not relevant to relevant. This is not the case for `content-visibility: hidden`.

**Note:** To animate the transition from `content-visibility: hidden` to a visible value, you will need to set [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
 and [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
 styles. See [transitioning `display` and `content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using#transitioning_display_and_content-visibility)
 to learn more.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#see_also)

-----------------------------------------------------------------------------------------------

*   [CSS containment module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
    
*   [Learn: CSS performance optimization](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/CSS)
    
*   [CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [An Introduction to CSS Containment](https://blogs.igalia.com/mrego/2019/01/11/an-introduction-to-css-containment/ "External link (opens in new tab)")
     via Igalia.com (2019)
*   The [`contentvisibilityautostatechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event "contentvisibilityautostatechange")
     event

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/containment/using/index.md?plain=1 "Folder: en-us/web/css/guides/containment/using (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FContainment%2FUsing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcontainment%2Fusing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FContainment%2FUsing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcontainment%2Fusing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")