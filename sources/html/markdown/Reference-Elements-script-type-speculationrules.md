*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#mdn-search)
    

`<script type="speculationrules">` HTML attribute value
=======================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/186)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#browser_compatibility)
 carefully before using this in production.

The **`speculationrules`** value of the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type)
 attribute of the [`<script>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 indicates that the body of the element contains speculation rules.

Speculation rules take the form of a JSON structure that determine what resources should be prefetched or prerendered by the browser. This is part of the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
.

**Note:** Speculation rules can be defined inside external text files referenced by the [`Speculation-Rules`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Speculation-Rules)
 HTTP header, using the same [JSON representation provided below](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#speculation_rules_json_representation)
. Specifying an HTTP header is useful in cases where developers are not able to directly modify the document itself.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#syntax)

-------------------------------------------------------------------------------------------------------------------

**Note:** The `src`, `async`, `nomodule`, `defer`, `crossorigin`, `integrity`, and `referrerpolicy` attributes must not be specified.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

The speculation rules definition is not a valid JSON object.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#description)

-----------------------------------------------------------------------------------------------------------------------------

A `<script type="speculationrules">` element must contain a valid JSON structure that defines speculation rules. The following examples show separate prefetch and prerender rules:

### [Speculation rules JSON representation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#speculation_rules_json_representation)

The JSON structure contains one or more fields at the top level, each one representing an action to define speculation rules for. At present the supported actions are:

[`"prefetch"` Optional](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#prefetch)

Rules for potential future navigations that should have their associated document response body downloaded, leading to significant performance improvements when those documents are navigated to. Note that none of the subresources referenced by the page are downloaded.

[`"prerender"` Optional](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#prerender)

Rules for potential future navigations that should have their associated documents fully downloaded, rendered, and loaded into an invisible tab. This includes loading all subresources, running all JavaScript, and even loading subresources and performing data fetches started by JavaScript. When those documents are navigated to, navigations will be instant, leading to major performance improvements.

**Note:** Consult the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
 main page for full details on how to use prefetch and prerender effectively.

Each action field contains an array, which in turn contains one or more objects. Each object contains a single rule defining a set of URLs and related parameters.

Each object can contain the following properties:

[`"source"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#source)

A string indicating the source of the URLs to which the rule applies. This is optional because the value can always be inferred from other properties.

This can be one of:

[`"document"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#document)

Specifies that the URLs will be matched from navigation links in the associated document (as defined in [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements), based on the conditions described by a `"where"` key. Note that the presence of a `"where"` key implies `"source": "document"`, so it is optional.

[`"list"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#list)

Specifies that the URLs will come from a list, specified in the `"urls"` key. Note that the presence of a `"urls"` key implies `"source": "list"`, so it is optional.

[`"urls"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#urls)

An array of strings representing a list of URLs to apply the rule to. These can be absolute or relative URLs. Relative URLs will be parsed relative to the document base URL (if inline in a document) or relative to the external resource URL (if externally fetched). `"urls"` and `"where"` cannot both be set in the same rule.

[`"where"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#where)

An object representing the conditions by which the rule matches URLs contained in the associated document. Effectively, the `"where"` object represents a test that is performed on every link on the page to see whether the speculation rule is applied to it. `"where"` and `"urls"` cannot both be set in the same rule.

This object can contain exactly one of the following properties:

[`"href_matches"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#href_matches)

A string containing a URL pattern, or an array containing multiple URL pattern strings, which follow the standard [URL Pattern API syntax](https://developer.mozilla.org/en-US/docs/Web/API/URL_Pattern_API)
. Links in the document whose URLs match the pattern(s) will have the rule applied.

[`"relative_to"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#relative_to)

In the case of an `"href_matches"` condition, this can specify where you want that condition to be matched relative to. This works in exactly the same way as the [rule-level `"relative_to"` key](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#relative_to_2)
, except that it only affects a single `"href_matches"` condition inside a `"where"` key.

[`"selector_matches"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#selector_matches)

A string containing a [CSS selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
, or an array containing multiple CSS selectors. Links in the document matched by those selectors will have the rule applied.

[`"and"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#and)

An array containing one or more objects containing conditions (`"href_matches"`, `"selector_matches"`, `"and"`, `"not"`, or `"or"`), all of which must match for the rule to be applied to them.

[`"not"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#not)

An object containing one condition (`"href_matches"`, `"selector_matches"`, `"and"`, `"not"`, or `"or"`) which, if it matches, will _not_ have the rule applied to it. All links that _do not_ match the condition _will_ have the rule applied.

[`"or"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#or)

An array containing one or more objects containing conditions (`"href_matches"`, `"selector_matches"`, `"and"`, `"not"`, or `"or"`), any of which can match for the rule to be applied to them.

`"where"` conditions can be nested multiple levels deep to create complex conditions, or you can choose to split them into separate rules to keep them simple. See [where examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#where_syntax_examples)
 for more explanation, and multiple examples of use.

[`"eagerness"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#eagerness)

A string providing a hint to the browser as to how eagerly it should prefetch/prerender link targets in order to balance performance advantages against resource overheads. Possible values are:

[`"immediate"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#immediate)

The author thinks the link is very likely to be followed, and/or the document may take significant time to fetch. Prefetch/prerender should start as soon as possible, subject only to considerations such as user preferences and resource limits.

[`"eager"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#eager)

The author wants to prefetch/prerender a large number of navigations, as early as possible. Prefetch/prerender should start on any slight suggestion that a link may be followed. For example, the user could move their mouse cursor towards the link, hover/focus it for a moment, or pause scrolling with the link in a prominent place.

[`"moderate"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#moderate)

The author is looking for a balance between `eager` and `conservative`. Prefetch/prerender should start when there is a reasonable suggestion that the user will follow a link in the near future. For example, the user could scroll a link into the viewport and hover/focus it for some time.

[`"conservative"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#conservative)

The author wishes to get some benefit from speculative loading with a fairly small tradeoff of resources. Prefetch/prerender should start only when the user is starting to click on the link, for example on [`mousedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event "mousedown")
 or [`pointerdown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerdown_event "pointerdown")
.

If `"eagerness"` is not explicitly specified, list (`"urls"`) rules default to `immediate` and document (`"where"`) rules default to `conservative`. The browser takes this hint into consideration along with its own heuristics, so it may select a link that the author has hinted as less eager than another, if the less eager candidate is considered a better choice.

[`"expects_no_vary_search"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#expects_no_vary_search)

A string providing a hint to the browser as to what [`No-Vary-Search`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/No-Vary-Search)
 header value will be set on responses for documents that it is receiving prefetch/prerender requests for. The browser can use this to determine ahead of time whether it is more useful to wait for an existing prefetch/prerender to finish, or start a new fetch request when the speculation rule is matched. See the [`"expects_no_vary_search"` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#expects_no_vary_search_example)
 for more explanation of how this can be used.

[`"referrer_policy"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#referrer_policy)

A string representing a specific referrer policy string to use when requesting the URLs specified in the rule — see [`Referrer-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy)
 for possible values. The purpose of this is to allow the referring page to set a stricter policy specifically for the speculative request than the policy the page already has set (either by default, or by using `Referrer-Policy`).

**Note:** A cross-site prefetch requires a referrer policy that is at least as strict as the default `"strict-origin-when-cross-origin"` value — so `"strict-origin-when-cross-origin"`, `"same-origin"`, `"strict-origin"`, or `"no-referrer"`. A laxer policy set in the speculation rules will override a stricter policy set on the referring page as long as it is still sufficiently strict for the cross-site case.

**Note:** In the case of document rules, the matched link's specified referrer policy (e.g., using the [`referrerpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#referrerpolicy)
 attribute) will be used, unless the rule specifies a policy that overrides it.

[`"relative_to"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#relative_to_2)

A string specifying where you want links matched by URL to be matched relative to. The value can be one of:

[`document`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#document_2)

URLs should be matched relative to the document the speculation rules are being set on.

[`ruleset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#ruleset)

URLs should be matched relative to the file the rules are specified in. This is the default value.

This key setting is only relevant for rules defined in an external file (set using the [`Speculation-Rules`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Speculation-Rules)
 header). When rules are specified inside the same document they are being set for (i.e., in an inline `<script>` element), it makes no difference.

[`"requires"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#requires)

An array of strings representing capabilities of the browser parsing the rule, which must be available if the rule is to be applied to the specified URLs.

**Warning:** Prefetches will automatically fail in browsers that cannot meet a specified requirement, even if they support the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
.

Possible values are:

[`"anonymous-client-ip-when-cross-origin"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#anonymous-client-ip-when-cross-origin)

(prefetch-only) Specifies that the rule matches only if the user agent can prevent the client IP address from being visible to the origin server if a cross-origin prefetch request is issued. Exactly how this works is dependent on browser implementation specifics. For example:

*   Chrome's implementation hides the IP address using a Google-owned proxy, therefore by default it only works for Google-controlled referrers (since in that case, sending the URLs of the destination to Google is not an additional privacy leak). When used on a non-Google-owned site, rules that include this will only match for users that turn on "Enhanced preloading" in `chrome://settings/preloading`.
*   Other Chromium-based browsers will have to provide their own solutions. Thorough testing in all target browsers is advised.
*   A future Safari implementation may possibly use something along the lines of [iCloud Private Relay](https://support.apple.com/en-us/102602 "External link (opens in new tab)")
    .
*   A future Firefox implementation might use something based on the [Mozilla VPN](https://www.mozilla.org/en-US/products/vpn/ "External link (opens in new tab)")
     product.

[`"tag"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#tag)

A string used to identify a rule or ruleset. This will be included in the [`Sec-Speculation-Tags`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Speculation-Tags)
 request header for any speculations covered by that rule.

[`"target_hint"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#target_hint)

A string indicating where the page expects the prerendered content to be activated. The directive not supported for prefetch speculations. Allowed values are:

[`"target_hint": "_blank"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#target_hint__blank)

Open rerendered content in a new page.

[`"target_hint": "_self"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#target_hint__self)

Open rerendered content in the current page. This is the default, if not specified.

**Note:** As speculation rules use a `<script>` element, they need to be explicitly allowed in the [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
 [`script-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src)
 directive if the site includes it. This is done by adding the `"inline-speculation-rules"` value along with a hash- or nonce-source.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Prefetch and prerender in the same set of rules](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#prefetch_and_prerender_in_the_same_set_of_rules)

The basic examples shown in the description section included separate speculation rules defined for prefetch and prerender. It is possible to define both in a single set of rules:

**Note:** This code snippet provides a list (`"urls"`) rule and a document (`"where"`) rule example.

### [Multiple rule sets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#multiple_rule_sets)

It is also allowable to include multiple sets of rules in a single HTML file:

And multiple rules in a single result set:

### [Dynamic rule insertion](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#dynamic_rule_insertion)

Below is an example that feature detects speculation rules and, if supported, dynamically adds a prerender speculation rule via JavaScript:

### [`where` syntax examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#where_syntax_examples)

A document-sourced rule contains a `"where"` property, which is an object containing criteria that define which links in the document are matched. Effectively, the `"where"` object represents a test that is performed on every link on the page to see whether the speculation rule is applied to it.

The most basic version will match a single URL pattern or CSS selector:

`"href_matches"` and `"selector_matches"` can also be set to an array of values, so multiple URL patterns or CSS selectors can be matched simultaneously:

URL patterns and selectors can also contain wildcard (`*`) characters, allowing a single value to match multiple URLs. For example, the object below could match `user/`, `user/settings`, `user/stats`, etc.

[Search parameters (or query strings)](https://developer.mozilla.org/en-US/docs/Web/API/URL/search)
 can also be targeted in `href_matches`. For example, the object below could match all same-origin URLs with a `category` search parameter (as the first or a subsequent parameter):

Any condition can be negated by placing it inside a `"not"` condition — this means that, when matched, a link _won't_ have the speculation rule applied to it, but when _not_ matched, it _will_. The following example will cause all links that _don't_ match the URL pattern `/logout` to have the rule applied to them, but not links that match `/logout`:

#### Combining multiple `"where"` conditions with `"and"` or `"or"`

Multiple conditions can be combined inside `"and"` or `"or"` conditions — these take the value of arrays containing multiple conditions, all or any of which (respectively) have to match for the speculation rules to apply to a link. Using `"and"` or `"or"`, conditions can be nested multiple levels deep — there is no specified limit on allowed nesting levels.

It is useful to think of the `"where"` object as being equivalent to an `if` statement. So

{ and: \[A, B, { or: \[C, { not: D }\] }\] }

is equivalent to

if (A && B && (C || !D)) {
  apply speculation rule
}

In the following complete speculation rule example, all same-origin pages are marked for prefetching except those known to be problematic — the `/logout` page, and any links marked up with a class of `.no-prerender`:

**Note:** The `where` pattern above does not include cross-site links, which are supported for prefetching (provided the user has no cookies set for the destination site, to protect against tracking) but not for prerendering.

### [`"relative_to"` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#relative_to_example)

For rule sets that are externally fetched (i.e., via the [`Speculation-Rules`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Speculation-Rules)
) response header, URLs in list rules and URL patterns in document rules are parsed relative to the containing external text file's URL by default. To parse URLs in a list rule relative to the document's base URL, `"relative_to"` is used like this:

For document rules, `"relative_to"` can be paired directly with `"href_matches"` and the document's base URL would only be used for patterns in that particular condition:

In the above example, only the first `"href_matches"` will be matched relative to the document's base URL.

`relative_to` is mainly relevant if the speculation rules JSON file is on a different origin to the document you wish to apply them to:

1.  If the document is located at `https://example.com/some/subpage.html` and the rules are at `https://example.com/resources/rules.json`, then `/home` always equates to `https://example.com/home` regardless of whether `relative_to` is set to `document` or `ruleset`.
    
2.  However, if the document is located at `https://example.com/some/subpage.html` and the rules are at `https://other.example/resources/rules.json` (for example, on a third-party or cookieless resource origin), then:
    
    *   `"relative_to": "document"` will cause `/home` to equate to `https://example.com/home`.
    *   `"relative_to": "ruleset"` will cause `/home` to equate to `https://other.example/home`.
    
    This is the typical use case for `"relative_to"`.
    
3.  Another potential (but rarer) use case is when your URLs are specified in the form `home` instead of `/home`. If the document is located at `https://example.com/some/subpage.html` and the rules are at `https://example.com/resources/rules.json`, then:
    
    *   `"relative_to": "document"` would cause `home` to equate to `https://example.com/some/home`.
    *   `"relative_to": "ruleset"` would cause `home` to equate to `https://example.com/resources/home`.

### [`"expects_no_vary_search"` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#expects_no_vary_search_example)

Consider the case of a user directory landing page, `/users`, which has an `id` parameter added to bring up information on a specific user, for example `/users?id=345`. Whether this URL should be considered identical for caching purposes depends on the behavior of the application:

1.  If this parameter has the effect of loading a completely new page containing the information for the specified user, then the URL should be cached separately.
2.  If this parameter has the effect of highlighting the specified user on the same page, and perhaps revealing a pullout panel displaying their data, then the URL should be considered the same for caching purposes. This could result in performance improvements around the loading of the user pages and could be achieved via a [`No-Vary-Search`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/No-Vary-Search)
     with a value of `params=("id")`.

How does this affect speculation rules? Consider the following code:

What would happen in this case when the user starts a navigation to `/users?id=345` when the headers for the prefetch of `/users` have not been received yet? At this point, the browser doesn't know what the `No-Vary-Search` value will be, if anything. If there was no `No-Vary-Search` value set, and the application behavior was more like Option 1 above, the prefetch would be wasted and the browser would need to go and fetch the separate `/users?id=345` page from scratch.

To solve this, we can provide a hint as to what the page author expects the `No-Vary-Search` value to be. A speculation rule can have an `"expects_no_vary_search"` field, which contains a string representation of the expected header value:

This indicates that Option 2 described above is what the server is expected to produce. If a navigation starts while there is an ongoing prefetch of `/users`, this informs the browser that it is appropriate to wait for the prefetch, instead of immediately starting another fetch for `/users?id=345`.

Document rules can also be used in conjunction with `"expects_no_vary_search"`, depending on the pattern used. For example, in the case of:

If a link is hovered over, the browser will start prefetching that specific link.

If the user hovers over another link before the prefetch completes, the `expects_no_vary_search` pattern tells the browser that there is no need to cancel the current prefetch, because all `/users` URLs with `id` URL parameter values effectively point to the same page for this context (and for caching purposes).

**Warning:** Additional care must be taken when using prerender with `No-Vary-Search` since the page may initially be prerendered with different URL parameters. `No-Vary-Search` is used for URL parameters that deliver the same resource from the server, but are used by the client for various reasons (client-side rendering, UTM parameters for analytics measurement, etc.). As the initial prerender may be for different URL parameters, any code depending on them should only run after prerender activation.

Multiple params can be provided in a space-separated array:

**Note:** As a [structured field](https://www.rfc-editor.org/info/rfc8941/ "External link (opens in new tab)")
, the parameters should be space-separated, quoted strings — as shown above — and not comma-separated, which developers may be more used to.

### [`eagerness` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#eagerness_example)

The following set of document rules shows how `eagerness` can be used to hint at the eagerness with which the browser should prerender each matching set of links.

Here we are hinting that:

*   All same-site links contained in the document should be conservatively prerendered (i.e., when the user starts to activate them).
*   Any product links (in this case, those with a `class` of `.product-link`) in the document should be eagerly prerendered (i.e., if the user makes any kind of move towards navigating to them).

**Note:** The effects of eagerness settings are less useful for list rules. By default, list rule URLs are prefetched/prerendered immediately as soon as the rules are parsed, which is what you'd expect — they are intended for explicit listing of high-priority URLs that you want to make available as soon as possible. For this reason, `eager` has the same effect as `immediate` in current implementations. Lower eagerness settings are for prefetching/prerendering when links are interacted with, and for these you are more likely to use document rules to find them on the page.

### [`tag` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#tag_example)

A `tag` can be included at the top level, to identify the overall ruleset:

Or to identify individual rules:

See [`Sec-Speculation-Tags`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Speculation-Tags)
 for more examples.

### [`target_hint` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#target_hint_example)

A `target_hint` can be included to indicate the target window in which matching prerender speculations will be opened:

The rules above allow the following links to be prerendered correctly in the appropriate targets:

`target_hint` is only needed for list rules, which use `urls`. They are not needed for document rules (which use `where`) since in these the target can be known from the `target` attribute of the `<a>` link element.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# speculative-loading](https://html.spec.whatwg.org/multipage/speculative-loading.html#speculative-loading) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Prerender pages in Chrome for instant page navigations](https://developer.chrome.com/docs/web-platform/prerender-pages "External link (opens in new tab)")
     on developer.chrome.com
*   [Speculative loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Speculative_loading)
    
*   [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/speculationrules/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/script/type/speculationrules/index.md?plain=1 "Folder: en-us/web/html/reference/elements/script/type/speculationrules (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fscript%2Ftype%2Fspeculationrules&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fscript%2Ftype%2Fspeculationrules%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fscript%2Ftype%2Fspeculationrules%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fscript%2Ftype%2Fspeculationrules%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F41a472e5bad6c6d2698d6e85c1172909cb102fa1%0A*+Document+last+modified%3A+2026-10-12T22%3A53%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")