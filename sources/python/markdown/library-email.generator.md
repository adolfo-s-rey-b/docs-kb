### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.policy.html "email.policy: Policy Objects")
     |
*   [previous](https://docs.python.org/3/library/email.parser.html "email.parser: Parsing email messages")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
     »
*   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
     »
*   [`email.generator`: Generating MIME documents](https://docs.python.org/3/library/email.generator.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`email.generator`: Generating MIME documents[¶](https://docs.python.org/3/library/email.generator.html#module-email.generator "Link to this heading")

======================================================================================================================================================

**Source code:** [Lib/email/generator.py](https://github.com/python/cpython/tree/3.15/Lib/email/generator.py)

* * *

One of the most common tasks is to generate the flat (serialized) version of the email message represented by a message object structure. You will need to do this if you want to send your message via [`smtplib.SMTP.sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail")
, or print the message on the console. Taking a message object structure and producing a serialized representation is the job of the generator classes.

As with the [`email.parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")
 module, you aren’t limited to the functionality of the bundled generator; you could write one from scratch yourself. However the bundled generator knows how to generate most email in a standards-compliant way, should handle MIME and non-MIME email messages just fine, and is designed so that the bytes-oriented parsing and generation operations are inverses, assuming the same non-transforming [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 is used for both. That is, parsing the serialized byte stream via the [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser")
 class and then regenerating the serialized byte stream using [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
 should produce output identical to the input [\[1\]](https://docs.python.org/3/library/email.generator.html#id3)
. (On the other hand, using the generator on an [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 constructed by program may result in changes to the `EmailMessage` object as defaults are filled in.)

The [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 class can be used to flatten a message into a text (as opposed to binary) serialized representation, but since Unicode cannot represent binary data directly, the message is of necessity transformed into something that contains only ASCII characters, using the standard email RFC Content Transfer Encoding techniques for encoding email messages for transport over channels that are not “8 bit clean”.

To accommodate reproducible processing of SMIME-signed messages [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 disables header folding for message parts of type `multipart/signed` and all subparts.

class email.generator.BytesGenerator(_outfp_, _mangle\_from\_\=None_, _maxheaderlen\=None_, _\*_, _policy\=None_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "Link to this definition")

Return a `BytesGenerator` object that will write any message provided to the [`flatten()`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator.flatten "email.generator.BytesGenerator.flatten")
 method, or any surrogateescape encoded text provided to the [`write()`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator.write "email.generator.BytesGenerator.write")
 method, to the [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object)
 _outfp_. _outfp_ must support a `write` method that accepts binary data.

If optional _mangle\_from\__ is `True`, put a `>` character in front of any line in the body that starts with the exact string `"From "`, that is `From` followed by a space at the beginning of a line. _mangle\_from\__ defaults to the value of the [`mangle_from_`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.mangle_from_ "email.policy.Policy.mangle_from_")
 setting of the _policy_ (which is `True` for the [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.compat32 "email.policy.compat32")
 policy and `False` for all others). _mangle\_from\__ is intended for use when messages are stored in Unix mbox format (see [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
 and [WHY THE CONTENT-LENGTH FORMAT IS BAD](https://www.jwz.org/doc/content-length.html)
).

If _maxheaderlen_ is not `None`, refold any header lines that are longer than _maxheaderlen_, or if `0`, do not rewrap any headers. If _maxheaderlen_ is `None` (the default), wrap headers and other message lines according to the _policy_ settings.

If _policy_ is specified, use that policy to control message generation. If _policy_ is `None` (the default), use the policy associated with the [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 or [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 object passed to `flatten` to control the message generation. See [`email.policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 for details on what _policy_ controls.

Added in version 3.2.

Changed in version 3.3: Added the _policy_ keyword.

Changed in version 3.6: The default behavior of the _mangle\_from\__ and _maxheaderlen_ parameters is to follow the policy.

flatten(_msg_, _unixfrom\=False_, _linesep\=None_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator.flatten "Link to this definition")

Print the textual representation of the message object structure rooted at _msg_ to the output file specified when the `BytesGenerator` instance was created.

If the [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 option [`cte_type`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.cte_type "email.policy.Policy.cte_type")
 is `8bit` (the default), copy any headers in the original parsed message that have not been modified to the output with any bytes with the high bit set reproduced as in the original, and preserve the non-ASCII _Content-Transfer-Encoding_ of any body parts that have them. If `cte_type` is `7bit`, convert the bytes with the high bit set as needed using an ASCII-compatible _Content-Transfer-Encoding_. That is, transform parts with non-ASCII _Content-Transfer-Encoding_ (_Content-Transfer-Encoding: 8bit_) to an ASCII compatible _Content-Transfer-Encoding_, and encode RFC-invalid non-ASCII bytes in headers using the MIME `unknown-8bit` character set, thus rendering them RFC-compliant.

If _unixfrom_ is `True`, print the envelope header delimiter used by the Unix mailbox format (see [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
) before the first of the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 headers of the root message object. If the root object has no envelope header, craft a standard one. The default is `False`. Note that for subparts, no envelope header is ever printed.

If _linesep_ is not `None`, use it as the separator character between all the lines of the flattened message. If _linesep_ is `None` (the default), use the value specified in the _policy_.

clone(_fp_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator.clone "Link to this definition")

Return an independent clone of this `BytesGenerator` instance with the exact same option settings, and _fp_ as the new _outfp_.

write(_s_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator.write "Link to this definition")

Encode _s_ using the `ASCII` codec and the `surrogateescape` error handler, and pass it to the _write_ method of the _outfp_ passed to the `BytesGenerator`’s constructor.

As a convenience, [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 provides the methods [`as_bytes()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_bytes "email.message.EmailMessage.as_bytes")
 and `bytes(aMessage)` (a.k.a. [`__bytes__()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__bytes__ "email.message.EmailMessage.__bytes__")
), which simplify the generation of a serialized binary representation of a message object. For more detail, see [`email.message`](https://docs.python.org/3/library/email.message.html#module-email.message "email.message: The base class representing email messages.")
.

Because strings cannot represent binary data, the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 class must convert any binary data in any message it flattens to an ASCII compatible format, by converting them to an ASCII compatible _Content-Transfer-Encoding_. Using the terminology of the email RFCs, you can think of this as `Generator` serializing to an I/O stream that is not “8 bit clean”. In other words, most applications will want to be using [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
, and not `Generator`.

class email.generator.Generator(_outfp_, _mangle\_from\_\=None_, _maxheaderlen\=None_, _\*_, _policy\=None_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "Link to this definition")

Return a `Generator` object that will write any message provided to the [`flatten()`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.flatten "email.generator.Generator.flatten")
 method, or any text provided to the [`write()`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.write "email.generator.Generator.write")
 method, to the [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object)
 _outfp_. _outfp_ must support a `write` method that accepts string data.

If optional _mangle\_from\__ is `True`, put a `>` character in front of any line in the body that starts with the exact string `"From "`, that is `From` followed by a space at the beginning of a line. _mangle\_from\__ defaults to the value of the [`mangle_from_`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.mangle_from_ "email.policy.Policy.mangle_from_")
 setting of the _policy_ (which is `True` for the [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.compat32 "email.policy.compat32")
 policy and `False` for all others). _mangle\_from\__ is intended for use when messages are stored in Unix mbox format (see [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
 and [WHY THE CONTENT-LENGTH FORMAT IS BAD](https://www.jwz.org/doc/content-length.html)
).

If _maxheaderlen_ is not `None`, refold any header lines that are longer than _maxheaderlen_, or if `0`, do not rewrap any headers. If _maxheaderlen_ is `None` (the default), wrap headers and other message lines according to the _policy_ settings.

If _policy_ is specified, use that policy to control message generation. If _policy_ is `None` (the default), use the policy associated with the [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 or [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 object passed to `flatten` to control the message generation. See [`email.policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 for details on what _policy_ controls.

Changed in version 3.3: Added the _policy_ keyword.

Changed in version 3.6: The default behavior of the _mangle\_from\__ and _maxheaderlen_ parameters is to follow the policy.

flatten(_msg_, _unixfrom\=False_, _linesep\=None_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.flatten "Link to this definition")

Print the textual representation of the message object structure rooted at _msg_ to the output file specified when the `Generator` instance was created.

If the [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 option [`cte_type`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.cte_type "email.policy.Policy.cte_type")
 is `8bit`, generate the message as if the option were set to `7bit`. (This is required because strings cannot represent non-ASCII bytes.) Convert any bytes with the high bit set as needed using an ASCII-compatible _Content-Transfer-Encoding_. That is, transform parts with non-ASCII _Content-Transfer-Encoding_ (_Content-Transfer-Encoding: 8bit_) to an ASCII compatible _Content-Transfer-Encoding_, and encode RFC-invalid non-ASCII bytes in headers using the MIME `unknown-8bit` character set, thus rendering them RFC-compliant.

If _unixfrom_ is `True`, print the envelope header delimiter used by the Unix mailbox format (see [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
) before the first of the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 headers of the root message object. If the root object has no envelope header, craft a standard one. The default is `False`. Note that for subparts, no envelope header is ever printed.

If _linesep_ is not `None`, use it as the separator character between all the lines of the flattened message. If _linesep_ is `None` (the default), use the value specified in the _policy_.

Changed in version 3.2: Added support for re-encoding `8bit` message bodies, and the _linesep_ argument.

clone(_fp_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.clone "Link to this definition")

Return an independent clone of this `Generator` instance with the exact same options, and _fp_ as the new _outfp_.

write(_s_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.write "Link to this definition")

Write _s_ to the _write_ method of the _outfp_ passed to the `Generator`’s constructor. This provides just enough file-like API for `Generator` instances to be used in the [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function.

As a convenience, [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 provides the methods [`as_string()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_string "email.message.EmailMessage.as_string")
 and `str(aMessage)` (a.k.a. [`__str__()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.__str__ "email.message.EmailMessage.__str__")
), which simplify the generation of a formatted string representation of a message object. For more detail, see [`email.message`](https://docs.python.org/3/library/email.message.html#module-email.message "email.message: The base class representing email messages.")
.

The `email.generator` module also provides a derived class, [`DecodedGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.DecodedGenerator "email.generator.DecodedGenerator")
, which is like the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 base class, except that non-_text_ parts are not serialized, but are instead represented in the output stream by a string derived from a template filled in with information about the part.

class email.generator.DecodedGenerator(_outfp_, _mangle\_from\_\=None_, _maxheaderlen\=None_, _fmt\=None_, _\*_, _policy\=None_)[¶](https://docs.python.org/3/library/email.generator.html#email.generator.DecodedGenerator "Link to this definition")

Act like [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
, except that for any subpart of the message passed to [`Generator.flatten()`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator.flatten "email.generator.Generator.flatten")
, if the subpart is of main type _text_, print the decoded payload of the subpart, and if the main type is not _text_, instead of printing it fill in the string _fmt_ using information from the part and print the resulting filled-in string.

To fill in _fmt_, execute `fmt % part_info`, where `part_info` is a dictionary composed of the following keys and values:

*   `type` – Full MIME type of the non-_text_ part
    
*   `maintype` – Main MIME type of the non-_text_ part
    
*   `subtype` – Sub-MIME type of the non-_text_ part
    
*   `filename` – Filename of the non-_text_ part
    
*   `description` – Description associated with the non-_text_ part
    
*   `encoding` – Content transfer encoding of the non-_text_ part
    

If _fmt_ is `None`, use the following default _fmt_:

> “\[Non-text (%(type)s) part of message omitted, filename %(filename)s\]”

Optional _mangle\_from\__ and _maxheaderlen_ are as with the [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
 base class.

Footnotes

#### Previous topic

[`email.parser`: Parsing email messages](https://docs.python.org/3/library/email.parser.html "previous chapter")

#### Next topic

[`email.policy`: Policy Objects](https://docs.python.org/3/library/email.policy.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email.generator%3A+Generating+MIME+documents&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.generator.html&pagesource=library%2Femail.generator.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.generator.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.policy.html "email.policy: Policy Objects")
     |
*   [previous](https://docs.python.org/3/library/email.parser.html "email.parser: Parsing email messages")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
     »
*   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
     »
*   [`email.generator`: Generating MIME documents](https://docs.python.org/3/library/email.generator.html)
    
*    
    
    |
*   Theme Auto Light Dark |