[Skip to main content](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html#sphx-glr-download-gallery-misc-multiprocess-sgskip-py)
 to download the full example code.

Multiprocessing[#](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html#multiprocessing "Link to this heading")

===============================================================================================================================

Demo of using multiprocessing for generating data in one process and plotting in another.

Written by Robert Cimrman

import multiprocessing as mp
import time

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

Processing Class[#](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html#processing-class "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

This class plots data it receives from a pipe.

class ProcessPlotter:
    def \_\_init\_\_(self):
        self.x \= \[\]
        self.y \= \[\]

    def terminate(self):
        [plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')

    def call\_back(self):
        while self.pipe.poll():
            command \= self.pipe.recv()
            if command is None:
                self.terminate()
                return False
            else:
                self.x.append(command\[0\])
                self.y.append(command\[1\])
                self.ax.plot(self.x, self.y, 'ro')
        self.fig.canvas.draw()
        return True

    def \_\_call\_\_(self, pipe):
        print('starting plotter...')

        self.pipe \= pipe
        self.fig, self.ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
        timer \= self.fig.canvas.new\_timer(interval\=1000)
        timer.add\_callback(self.call\_back)
        timer.start()

        print('...done')
        [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Plotting class[#](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html#plotting-class "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

This class uses multiprocessing to spawn a process to run code from the class above. When initialized, it creates a pipe and an instance of `ProcessPlotter` which will be run in a separate process.

When run from the command line, the parent process sends data to the spawned process which is then plotted via the callback function specified in `ProcessPlotter:__call__`.

class NBPlot:
    def \_\_init\_\_(self):
        self.plot\_pipe, plotter\_pipe \= [mp.Pipe](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe")
()
        self.plotter \= ProcessPlotter()
        self.plot\_process \= [mp.Process](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process")
(
            target\=self.plotter, args\=(plotter\_pipe,), daemon\=True)
        self.plot\_process.start()

    def plot(self, finished\=False):
        send \= self.plot\_pipe.send
        if finished:
            send(None)
        else:
            data \= [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(2)
            send(data)

def main():
    pl \= NBPlot()
    for \_ in range(10):
        pl.plot()
        [time.sleep](https://docs.python.org/3/library/time.html#time.sleep "time.sleep")
(0.5)
    pl.plot(finished\=True)

if \_\_name\_\_ \== '\_\_main\_\_':
    if [plt.get\_backend](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_backend "matplotlib.get_backend")
() \== "MacOSX":
        [mp.set\_start\_method](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method")
("forkserver")
    main()

[`Download Jupyter notebook: multiprocess_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/de8fc1e307771dcbeaff29d10070a95b/multiprocess_sgskip.ipynb)

[`Download Python source code: multiprocess_sgskip.py`](https://matplotlib.org/stable/_downloads/4639c390333b84440ec779fe5753a134/multiprocess_sgskip.py)

[`Download zipped: multiprocess_sgskip.zip`](https://matplotlib.org/stable/_downloads/2e60a67740cfbb97262c8d3c3080e772/multiprocess_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page