### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.compat32-message.html "email.message.Message: Representing an email message using the compat32 API")
     |
*   [previous](https://docs.python.org/3/library/email.contentmanager.html "email.contentmanager: Managing MIME Content")
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
*   [`email`: Examples](https://docs.python.org/3/library/email.examples.html)
    
*    
    
    |
*   Theme Auto Light Dark |

[`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
: Examples[¶](https://docs.python.org/3/library/email.examples.html#email-examples "Link to this heading")

======================================================================================================================================================================================================================================================================

Here are a few examples of how to use the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package to read, write, and send simple email messages, as well as more complex MIME messages.

First, let’s see how to create and send a simple text message (both the text content and the addresses may contain Unicode characters):

Copy

\# Import smtplib for the actual sending function
import smtplib

\# Import the email modules we'll need
from email.message import EmailMessage

\# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    \# Create a text/plain message
    msg \= EmailMessage()
    msg.set\_content(fp.read())

\# me == the sender's email address
\# you == the recipient's email address
msg\['Subject'\] \= f'The contents of {textfile}'
msg\['From'\] \= me
msg\['To'\] \= you

\# Send the message via our own SMTP server.
s \= smtplib.SMTP('localhost')
s.send\_message(msg)
s.quit()

Parsing [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html)
 headers can easily be done by the using the classes from the [`parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")
 module:

Copy

\# Import the email modules we'll need
#from email.parser import BytesParser
from email.parser import Parser
from email.policy import default

\# If the e-mail headers are in a file, uncomment these two lines:
\# with open(messagefile, 'rb') as fp:
\#     headers = BytesParser(policy=default).parse(fp)

\#  Or for parsing headers in a string (this is an uncommon operation), use:
headers \= Parser(policy\=default).parsestr(
        'From: Foo Bar <user@example.com>\\n'
        'To: <someone\_else@example.com>\\n'
        'Subject: Test message\\n'
        '\\n'
        'Body would go here\\n')

\#  Now the header items can be accessed as a dictionary:
print('To: {}'.format(headers\['to'\]))
print('From: {}'.format(headers\['from'\]))
print('Subject: {}'.format(headers\['subject'\]))

\# You can also access the parts of the addresses:
print('Recipient username: {}'.format(headers\['to'\].addresses\[0\].username))
print('Sender name: {}'.format(headers\['from'\].addresses\[0\].display\_name))

Here’s an example of how to send a MIME message containing a bunch of family pictures that may be residing in a directory:

Copy

\# Import smtplib for the actual sending function.
import smtplib

\# Here are the email package modules we'll need.
from email.message import EmailMessage

\# Create the container email message.
msg \= EmailMessage()
msg\['Subject'\] \= 'Our family reunion'
\# me == the sender's email address
\# family = the list of all recipients' email addresses
msg\['From'\] \= me
msg\['To'\] \= ', '.join(family)
msg.preamble \= 'You will not see this in a MIME-aware mail reader.\\n'

\# Open the files in binary mode.  You can also omit the subtype
\# if you want MIMEImage to guess it.
for file in pngfiles:
    with open(file, 'rb') as fp:
        img\_data \= fp.read()
    msg.add\_attachment(img\_data, maintype\='image',
                                 subtype\='png')

\# Send the email via our own SMTP server.
with smtplib.SMTP('localhost') as s:
    s.send\_message(msg)

Here’s an example of how to send the entire contents of a directory as an email message: [\[1\]](https://docs.python.org/3/library/email.examples.html#id3)

Copy

#!/usr/bin/env python3

"""Send the contents of a directory as a MIME message."""

import os
import smtplib
\# For guessing MIME type based on file name extension
import mimetypes

from argparse import ArgumentParser

from email.message import EmailMessage
from email.policy import SMTP

def main():
    parser \= ArgumentParser(description\="""\\
Send the contents of a directory as a MIME message.
Unless the -o option is given, the email is sent by forwarding to your local
SMTP server, which then does the normal delivery process.  Your local machine
must be running an SMTP server.
""")
    parser.add\_argument('-d', '--directory',
                        help\="""Mail the contents of the specified directory,
                        otherwise use the current directory.  Only the regular
                        files in the directory are sent, and we don't recurse to
                        subdirectories.""")
    parser.add\_argument('-o', '--output',
                        metavar\='FILE',
                        help\="""Print the composed message to FILE instead of
                        sending the message to the SMTP server.""")
    parser.add\_argument('-s', '--sender', required\=True,
                        help\='The value of the From: header (required)')
    parser.add\_argument('-r', '--recipient', required\=True,
                        action\='append', metavar\='RECIPIENT',
                        default\=\[\], dest\='recipients',
                        help\='A To: header value (at least one required)')
    args \= parser.parse\_args()
    directory \= args.directory
    if not directory:
        directory \= '.'
    \# Create the message
    msg \= EmailMessage()
    msg\['Subject'\] \= f'Contents of directory {os.path.abspath(directory)}'
    msg\['To'\] \= ', '.join(args.recipients)
    msg\['From'\] \= args.sender
    msg.preamble \= 'You will not see this in a MIME-aware mail reader.\\n'

    for filename in os.listdir(directory):
        path \= os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
        \# Guess the content type based on the file's extension.  Encoding
        \# will be ignored, although we should check for simple things like
        \# gzip'd or compressed files.
        ctype, encoding \= mimetypes.guess\_file\_type(path)
        if ctype is None or encoding is not None:
            \# No guess could be made, or the file is encoded (compressed), so
            \# use a generic bag-of-bits type.
            ctype \= 'application/octet-stream'
        maintype, subtype \= ctype.split('/', 1)
        with open(path, 'rb') as fp:
            msg.add\_attachment(fp.read(),
                               maintype\=maintype,
                               subtype\=subtype,
                               filename\=filename)
    \# Now send or store the message
    if args.output:
        with open(args.output, 'wb') as fp:
            fp.write(msg.as\_bytes(policy\=SMTP))
    else:
        with smtplib.SMTP('localhost') as s:
            s.send\_message(msg)

if \_\_name\_\_ \== '\_\_main\_\_':
    main()

Here’s an example of how to unpack a MIME message like the one above, into a directory of files:

Copy

#!/usr/bin/env python3

"""Unpack a MIME message into a directory of files."""

import os
import email
import mimetypes

from email.policy import default

from argparse import ArgumentParser

def main():
    parser \= ArgumentParser(description\="""\\
Unpack a MIME message into a directory of files.
""")
    parser.add\_argument('-d', '--directory', required\=True,
                        help\="""Unpack the MIME message into the named
                        directory, which will be created if it doesn't already
                        exist.""")
    parser.add\_argument('msgfile')
    args \= parser.parse\_args()

    with open(args.msgfile, 'rb') as fp:
        msg \= email.message\_from\_binary\_file(fp, policy\=default)

    try:
        os.mkdir(args.directory)
    except FileExistsError:
        pass

    counter \= 1
    for part in msg.walk():
        \# multipart/\* are just containers
        if part.get\_content\_maintype() \== 'multipart':
            continue
        \# Applications should really sanitize the given filename so that an
        \# email message can't be used to overwrite important files
        filename \= part.get\_filename()
        if not filename:
            ext \= mimetypes.guess\_extension(part.get\_content\_type())
            if not ext:
                \# Use a generic bag-of-bits extension
                ext \= '.bin'
            filename \= f'part-{counter:03d}{ext}'
        counter += 1
        with open(os.path.join(args.directory, filename), 'wb') as fp:
            fp.write(part.get\_payload(decode\=True))

if \_\_name\_\_ \== '\_\_main\_\_':
    main()

Here’s an example of how to create an HTML message with an alternative plain text version. To make things a bit more interesting, we include a related image in the html part, and we save a copy of what we are going to send to disk, as well as sending it.

Copy

#!/usr/bin/env python3

import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make\_msgid

\# Create the base text message.
msg \= EmailMessage()
msg\['Subject'\] \= "Pourquoi pas des asperges pour ce midi ?"
msg\['From'\] \= Address("Pepé Le Pew", "pepe", "example.com")
msg\['To'\] \= (Address("Penelope Pussycat", "penelope", "example.com"),
             Address("Fabrette Pussycat", "fabrette", "example.com"))
msg.set\_content("""\\
Salut!

Cette recette \[1\] sera sûrement un très bon repas.

\[1\] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718

\--Pepé
""")

\# Add the html version.  This converts the message into a multipart/alternative
\# container, with the original text message as the first part and the new html
\# message as the second part.
asparagus\_cid \= make\_msgid()
msg.add\_alternative("""\\
<html>
  <head></head>
  <body>
    <p>Salut!</p>
    <p>Cette
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
            recette
        </a> sera sûrement un très bon repas.
    </p>
    <img src="cid:{asparagus\_cid}">
  </body>
</html>
""".format(asparagus\_cid\=asparagus\_cid\[1:\-1\]), subtype\='html')
\# note that we needed to peel the <> off the msgid for use in the html.

\# Now add the related image to the html part.
with open("roasted-asparagus.jpg", 'rb') as img:
    msg.get\_payload()\[1\].add\_related(img.read(), 'image', 'jpeg',
                                     cid\=asparagus\_cid)

\# Make a local copy of what we are going to send.
with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))

\# Send the message via local SMTP server.
with smtplib.SMTP('localhost') as s:
    s.send\_message(msg)

If we were sent the message from the last example, here is one way we could process it:

Copy

import os
import sys
import tempfile
import mimetypes
import webbrowser

\# Import the email modules we'll need
from email import policy
from email.parser import BytesParser

def magic\_html\_parser(html\_text, partfiles):
    """Return safety-sanitized html linked to partfiles.

    Rewrite the href="cid:...." attributes to point to the filenames in partfiles.
    Though not trivial, this should be possible using html.parser.
    """
    raise NotImplementedError("Add the magic needed")

\# In a real program you'd get the filename from the arguments.
with open('outgoing.msg', 'rb') as fp:
    msg \= BytesParser(policy\=policy.default).parse(fp)

\# Now the header items can be accessed as a dictionary, and any non-ASCII will
\# be converted to unicode:
print('To:', msg\['to'\])
print('From:', msg\['from'\])
print('Subject:', msg\['subject'\])

\# If we want to print a preview of the message content, we can extract whatever
\# the least formatted payload is and print the first three lines.  Of course,
\# if the message has no plain text part printing the first three lines of html
\# is probably useless, but this is just a conceptual example.
simplest \= msg.get\_body(preferencelist\=('plain', 'html'))
print()
print(''.join(simplest.get\_content().splitlines(keepends\=True)\[:3\]))

ans \= input("View full message?")
if ans.lower()\[0\] \== 'n':
    sys.exit()

\# We can extract the richest alternative in order to display it:
richest \= msg.get\_body()
partfiles \= {}
if richest\['content-type'\].maintype \== 'text':
    if richest\['content-type'\].subtype \== 'plain':
        for line in richest.get\_content().splitlines():
            print(line)
        sys.exit()
    elif richest\['content-type'\].subtype \== 'html':
        body \= richest
    else:
        print("Don't know how to display {}".format(richest.get\_content\_type()))
        sys.exit()
elif richest\['content-type'\].content\_type \== 'multipart/related':
    body \= richest.get\_body(preferencelist\=('html'))
    for part in richest.iter\_attachments():
        fn \= part.get\_filename()
        if fn:
            extension \= os.path.splitext(part.get\_filename())\[1\]
        else:
            extension \= mimetypes.guess\_extension(part.get\_content\_type())
        with tempfile.NamedTemporaryFile(suffix\=extension, delete\=False) as f:
            f.write(part.get\_content())
            \# again strip the <> to go from email form of cid to html form.
            partfiles\[part\['content-id'\]\[1:\-1\]\] \= f.name
else:
    print("Don't know how to display {}".format(richest.get\_content\_type()))
    sys.exit()
with tempfile.NamedTemporaryFile(mode\='w', delete\=False) as f:
    f.write(magic\_html\_parser(body.get\_content(), partfiles))
webbrowser.open(f.name)
os.remove(f.name)
for fn in partfiles.values():
    os.remove(fn)

\# Of course, there are lots of email messages that could break this simple
\# minded program, but it will handle the most common ones.

Up to the prompt, the output from the above is:

To: Penelope Pussycat <penelope@example.com>, Fabrette Pussycat <fabrette@example.com>
From: Pepé Le Pew <pepe@example.com>
Subject: Pourquoi pas des asperges pour ce midi ?

Salut!

Cette recette \[1\] sera sûrement un très bon repas.

Footnotes

#### Previous topic

[`email.contentmanager`: Managing MIME Content](https://docs.python.org/3/library/email.contentmanager.html "previous chapter")

#### Next topic

[`email.message.Message`: Representing an email message using the `compat32` API](https://docs.python.org/3/library/email.compat32-message.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=email%3A+Examples&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.examples.html&pagesource=library%2Femail.examples.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/email.examples.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/email.compat32-message.html "email.message.Message: Representing an email message using the compat32 API")
     |
*   [previous](https://docs.python.org/3/library/email.contentmanager.html "email.contentmanager: Managing MIME Content")
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
*   [`email`: Examples](https://docs.python.org/3/library/email.examples.html)
    
*    
    
    |
*   Theme Auto Light Dark |