*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#mdn-search)
    

`<time>` HTML time (date) element
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<time>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

It may represent one of the following:

*   A time on a 24-hour clock.
*   A precise date in the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar "External link (opens in new tab)")
     (with optional time and timezone information).
*   [A valid time duration](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-duration-string "External link (opens in new tab)")
    .

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#try_it)

-------------------------------------------------------------------------------------------

    <p>
      The Cure will be celebrating their 40th anniversary on
      <time datetime="2018-07-07">July 7</time> in London's Hyde Park.
    </p>
    
    <p>
      The concert starts at <time datetime="20:00">20:00</time> and you'll be able
      to enjoy the band for at least <time datetime="PT2H30M">2h 30m</time>.
    </p>
    

    time {
      font-weight: bold;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#attributes)

---------------------------------------------------------------------------------------------------

Like all other HTML elements, this element supports the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`datetime`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#datetime)

This attribute indicates the time and/or date of the element and must be in one of the formats described below.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#usage_notes)

-----------------------------------------------------------------------------------------------------

This element is for presenting dates and times in a machine-readable format. For example, this can help a user agent offer to add an event to a user's calendar.

This element should not be used for dates prior to the introduction of the Gregorian calendar (due to complications in calculating those dates).

The _datetime value_ (the machine-readable value of the datetime) is the value of the element's `datetime` attribute, which must be in the proper format (see below). If the element does not have a `datetime` attribute, **it must not have any element descendants**, and the _datetime value_ is the element's child text content.

### [Valid datetime values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#valid_datetime_values)

| Description | Microsyntax | Examples |
| --- | --- | --- |
| Valid month string | `_YYYY_-_MM_` | `2011-11`, `2013-05` |
| Valid date string | `_YYYY_-_MM_-_DD_` | `1887-12-01` |
| Valid yearless date string | `_MM_-_DD_` | `11-12` |
| Valid time string | `_HH_:_MM_`  <br>`_HH_:_MM_:_SS_`  <br>`_HH_:_MM_:_SS_._mmm_` | `23:59`  <br>`12:15:47`  <br>`12:15:52.998` |
| Valid local date and time string | `_YYYY_-_MM_-_DD_ _HH_:_MM_`  <br>`_YYYY_-_MM_-_DD_ _HH_:_MM_:_SS_`  <br>`_YYYY_-_MM_-_DD_ _HH_:_MM_:_SS_._mmm_`  <br>`_YYYY_-_MM_-_DD_T_HH_:_MM_`  <br>`_YYYY_-_MM_-_DD_T_HH_:_MM_:_SS_`  <br>`_YYYY_-_MM_-_DD_T_HH_:_MM_:_SS_._mmm_` | `2013-12-25 11:12`  <br>`1972-07-25 13:43:07`  <br>`1941-03-15 07:06:23.678`  <br>`2013-12-25T11:12`  <br>`1972-07-25T13:43:07`  <br>`1941-03-15T07:06:23.678` |
| Valid time-zone offset string | `Z`  <br>`+_HHMM_`  <br>`+_HH_:_MM_`  <br>`-_HHMM_`  <br>`-_HH_:_MM_` | `Z`  <br>`+0200`  <br>`+04:30`  <br>`-0300`  <br>`-08:00` |
| Valid global date and time string | Any combination of a valid local date and time string followed by a valid time-zone offset string | `2013-12-25 11:12+0200`  <br>`1972-07-25 13:43:07+04:30`  <br>`1941-03-15 07:06:23.678Z`  <br>`2013-12-25T11:12-08:00` |
| Valid week string | `_YYYY_-W_WW_` | `2013-W46` |
| Four or more ASCII digits | `_YYYY_` | `2013`, `0001` |
| Valid duration string | `P_d_DT_h_H_m_M_s_S`  <br>`P_d_DT_h_H_m_M_s_._X_S`  <br>`P_d_DT_h_H_m_M_s_._XX_S`  <br>`P_d_DT_h_H_m_M_s_._XXX_S`  <br>`PT_h_H_m_M_s_S`  <br>`PT_h_H_m_M_s_._X_S`  <br>`PT_h_H_m_M_s_._XX_S`  <br>`PT_h_H_m_M_s_._XXX_S`  <br>`_w_w _d_d _h_h _m_m _s_s` | `P12DT7H12M13S`  <br>`P12DT7H12M13.3S`  <br>`P12DT7H12M13.45S`  <br>`P12DT7H12M13.455S`  <br>`PT7H12M13S`  <br>`PT7H12M13.2S`  <br>`PT7H12M13.56S`  <br>`PT7H12M13.999S`  <br>`7d 5h 24m 13s` |

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#examples)

-----------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#basic_example)

#### HTML

html

    <p>The concert starts at <time datetime="2018-07-07T20:00:00">20:00</time>.</p>
    

#### Result

### [`datetime` example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#datetime_example)

#### HTML

html

    <p>
      The concert took place on <time datetime="2001-05-15T19:00">May 15</time>.
    </p>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[time](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLTimeElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTimeElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-time-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#see_also)

-----------------------------------------------------------------------------------------------

*   The [`<data>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data)
     element, allowing you to signal other kinds of values.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/time/index.md?plain=1 "Folder: en-us/web/html/reference/elements/time (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftime&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftime%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftime%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftime%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f3d7018159127dbe92842413fb45d0aa7e8193%0A*+Document+last+modified%3A+2026-08-27T13%3A16%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")