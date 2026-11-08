[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/embedding_webagg_sgskip.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/embedding_webagg_sgskip.html#sphx-glr-download-gallery-user-interfaces-embedding-webagg-sgskip-py)
 to download the full example code.

Embedding WebAgg[#](https://matplotlib.org/stable/gallery/user_interfaces/embedding_webagg_sgskip.html#embedding-webagg "Link to this heading")

================================================================================================================================================

This example demonstrates how to embed Matplotlib WebAgg interactive plotting in your own web application and framework. It is not necessary to do all this if you merely want to display a plot in a browser or use Matplotlib's built-in Tornado-based server "on the side".

The framework being used must support web sockets.

import argparse
import io
import json
import mimetypes
from pathlib import [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
import signal
import socket

try:
    import tornado
except ImportError as err:
    raise RuntimeError("This example requires tornado.") from err
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

import numpy as np

import matplotlib as mpl
from matplotlib.backends.backend\_webagg import (FigureManagerWebAgg,
                                                new\_figure\_manager\_given\_figure)
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

def create\_figure():
    """
    Creates a simple example figure.
    """
    fig \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
()
    ax \= fig.add\_subplot()
    t \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 3.0, 0.01)
    s \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* t)
    ax.plot(t, s)
    return fig

\# The following is the content of the web page.  You would normally
\# generate this using some sort of template facility in your web
\# framework, but here we just use Python string formatting.
html\_content \= """<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- TODO: There should be a way to include all of the required javascript
               and CSS so matplotlib can add to the set in the future if it
               needs to. -->
    <link rel="stylesheet" href="\_static/css/page.css" type="text/css">
    <link rel="stylesheet" href="\_static/css/boilerplate.css" type="text/css">
    <link rel="stylesheet" href="\_static/css/fbm.css" type="text/css">
    <link rel="stylesheet" href="\_static/css/mpl.css" type="text/css">
    <script src="mpl.js"></script>

    <script>
      /\* This is a callback that is called when the user saves
         (downloads) a file.  Its purpose is really to map from a
         figure and file format to a url in the application. \*/
      function ondownload(figure, format) {
        window.open('download.' + format, '\_blank');
      };

      function ready(fn) {
        if (document.readyState != "loading") {
          fn();
        } else {
          document.addEventListener("DOMContentLoaded", fn);
        }
      }

      ready(
        function() {
          /\* It is up to the application to provide a websocket that the figure
             will use to communicate to the server.  This websocket object can
             also be a "fake" websocket that underneath multiplexes messages
             from multiple figures, if necessary. \*/
          var websocket\_type = mpl.get\_websocket\_type();
          var websocket = new websocket\_type("%(ws\_uri)sws");

          // mpl.figure creates a new figure on the webpage.
          var fig = new mpl.figure(
              // A unique numeric identifier for the figure
              %(fig\_id)s,
              // A websocket object (or something that behaves like one)
              websocket,
              // A function called when a file type is selected for download
              ondownload,
              // The HTML element in which to place the figure
              document.getElementById("figure"));
        }
      );
    </script>

    <title>matplotlib</title>
  </head>

  <body>
    <div id="figure">
    </div>
  </body>
</html>
"""

class MyApplication([tornado.web.Application](https://www.tornadoweb.org/en/stable/web.html#tornado.web.Application "tornado.web.Application")
):
    class MainPage([tornado.web.RequestHandler](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "tornado.web.RequestHandler")
):
        """
        Serves the main HTML page.
        """

        def get(self):
            manager \= self.application.manager
            ws\_uri \= f"ws://{self.request.host}/"
            content \= html\_content % {
                "ws\_uri": ws\_uri, "fig\_id": manager.num}
            self.write(content)

    class MplJs([tornado.web.RequestHandler](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "tornado.web.RequestHandler")
):
        """
        Serves the generated matplotlib javascript file.  The content
        is dynamically generated based on which toolbar functions the
        user has defined.  Call \`FigureManagerWebAgg\` to get its
        content.
        """

        def get(self):
            self.set\_header('Content-Type', 'application/javascript')
            js\_content \= FigureManagerWebAgg.get\_javascript()

            self.write(js\_content)

    class Download([tornado.web.RequestHandler](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "tornado.web.RequestHandler")
):
        """
        Handles downloading of the figure in various file formats.
        """

        def get(self, fmt):
            manager \= self.application.manager
            self.set\_header(
                'Content-Type', mimetypes.types\_map.get(fmt, 'binary'))
            buff \= [io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
()
            manager.canvas.figure.savefig(buff, format\=fmt)
            self.write(buff.getvalue())

    class WebSocket([tornado.websocket.WebSocketHandler](https://www.tornadoweb.org/en/stable/websocket.html#tornado.websocket.WebSocketHandler "tornado.websocket.WebSocketHandler")
):
        """
        A websocket for interactive communication between the plot in
        the browser and the server.

        In addition to the methods required by tornado, it is required to
        have two callback methods:

            - \`\`send\_json(json\_content)\`\` is called by matplotlib when
              it needs to send json to the browser.  \`json\_content\` is
              a JSON tree (Python dictionary), and it is the responsibility
              of this implementation to encode it as a string to send over
              the socket.

            - \`\`send\_binary(blob)\`\` is called to send binary image data
              to the browser.
        """
        supports\_binary \= True

        def open(self):
            \# Register the websocket with the FigureManager.
            manager \= self.application.manager
            manager.add\_web\_socket(self)
            if hasattr(self, 'set\_nodelay'):
                self.set\_nodelay(True)

        def on\_close(self):
            \# When the socket is closed, deregister the websocket with
            \# the FigureManager.
            manager \= self.application.manager
            manager.remove\_web\_socket(self)

        def on\_message(self, message):
            \# The 'supports\_binary' message is relevant to the
            \# websocket itself.  The other messages get passed along
            \# to matplotlib as-is.

            \# Every message has a "type" and a "figure\_id".
            message \= [json.loads](https://docs.python.org/3/library/json.html#json.loads "json.loads")
(message)
            if message\['type'\] \== 'supports\_binary':
                self.supports\_binary \= message\['value'\]
            else:
                manager \= self.application.manager
                manager.handle\_json(message)

        def send\_json(self, content):
            self.write\_message([json.dumps](https://docs.python.org/3/library/json.html#json.dumps "json.dumps")
(content))

        def send\_binary(self, blob):
            if self.supports\_binary:
                self.write\_message(blob, binary\=True)
            else:
                data\_uri \= ("data:image/png;base64," +
                            blob.encode('base64').replace('\\n', ''))
                self.write\_message(data\_uri)

    def \_\_init\_\_(self, figure):
        self.figure \= figure
        self.manager \= new\_figure\_manager\_given\_figure(id(figure), figure)

        super().\_\_init\_\_(\[\
            \# Static files for the CSS and JS\
            (r'/\_static/(.\*)',\
             [tornado.web.StaticFileHandler](https://www.tornadoweb.org/en/stable/web.html#tornado.web.StaticFileHandler "tornado.web.StaticFileHandler")\
,\
             {'path': FigureManagerWebAgg.get\_static\_file\_path()}),\
\
            \# Static images for the toolbar\
            (r'/\_images/(.\*)',\
             [tornado.web.StaticFileHandler](https://www.tornadoweb.org/en/stable/web.html#tornado.web.StaticFileHandler "tornado.web.StaticFileHandler")\
,\
             {'path': [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")\
([mpl.get\_data\_path](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")\
(), 'images')}),\
\
            \# The page that contains all of the pieces\
            ('/', self.MainPage),\
\
            ('/mpl.js', self.MplJs),\
\
            \# Sends images and events to the browser, and receives\
            \# events from the browser\
            ('/ws', self.WebSocket),\
\
            \# Handles the downloading (i.e., saving) of static images\
            (r'/download.(\[a-z0-9.\]+)', self.Download),\
        \])

if \_\_name\_\_ \== "\_\_main\_\_":
    parser \= [argparse.ArgumentParser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
()
    parser.add\_argument('-p', '--port', type\=int, default\=8080,
                        help\='Port to listen on (0 for a random port).')
    args \= parser.parse\_args()

    figure \= create\_figure()
    application \= MyApplication(figure)

    http\_server \= [tornado.httpserver.HTTPServer](https://www.tornadoweb.org/en/stable/httpserver.html#tornado.httpserver.HTTPServer "tornado.httpserver.HTTPServer")
(application)
    sockets \= [tornado.netutil.bind\_sockets](https://www.tornadoweb.org/en/stable/netutil.html#tornado.netutil.bind_sockets "tornado.netutil.bind_sockets")
(args.port, '')
    http\_server.add\_sockets(sockets)

    for s in sockets:
        addr, port \= s.getsockname()\[:2\]
        if s.family is [socket.AF\_INET6](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
:
            addr \= f'\[{addr}\]'
        print(f"Listening on http://{addr}:{port}/")
    print("Press Ctrl+C to quit")

    ioloop \= [tornado.ioloop.IOLoop.instance](https://www.tornadoweb.org/en/stable/ioloop.html#tornado.ioloop.IOLoop.instance "tornado.ioloop.IOLoop.instance")
()

    def shutdown():
        ioloop.stop()
        print("Server stopped")

    old\_handler \= [signal.signal](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal")
(
        [signal.SIGINT](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT")
,
        lambda sig, frame: ioloop.add\_callback\_from\_signal(shutdown))

    try:
        ioloop.start()
    finally:
        [signal.signal](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal")
([signal.SIGINT](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT")
, old\_handler)

[`Download Jupyter notebook: embedding_webagg_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/b5cbdfa83b33e22687e6420da37101b9/embedding_webagg_sgskip.ipynb)

[`Download Python source code: embedding_webagg_sgskip.py`](https://matplotlib.org/stable/_downloads/d558d74d36a57f66fc595a6bb564b180/embedding_webagg_sgskip.py)

[`Download zipped: embedding_webagg_sgskip.zip`](https://matplotlib.org/stable/_downloads/59c672a91dcea1dced69f3ae02baf2a7/embedding_webagg_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)