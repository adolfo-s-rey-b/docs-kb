[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.82.html#main-content)

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
    

Changes for 0.82[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.82.html#changes-for-0-82 "Link to this heading")

======================================================================================================================================

\- toolbar import change in GTKAgg, GTKCairo and WXAgg

- Added subplot config tool to GTK\* backends -- note you must now
  import the NavigationToolbar2 from your backend of choice rather
  than from backend\_gtk because it needs to know about the backend
  specific canvas -- see examples/embedding\_in\_gtk2.py.  Ditto for
  wx backend -- see examples/embedding\_in\_wxagg.py


- hist bin change

    Sean Richards notes there was a problem in the way we created
    the binning for histogram, which made the last bin
    underrepresented.  From his post:

      I see that hist uses the linspace function to create the bins
      and then uses searchsorted to put the values in their correct
      bin. That's all good but I am confused over the use of linspace
      for the bin creation. I wouldn't have thought that it does
      what is needed, to quote the docstring it creates a "Linear
      spaced array from min to max". For it to work correctly
      shouldn't the values in the bins array be the same bound for
      each bin? (i.e. each value should be the lower bound of a
      bin). To provide the correct bins for hist would it not be
      something like

      def bins(xmin, xmax, N):
        if N==1: return xmax
        dx = (xmax-xmin)/N # instead of N-1
        return xmin + dx\*arange(N)


     This suggestion is implemented in 0.81.  My test script with these
     changes does not reveal any bias in the binning

      from matplotlib.numerix.mlab import randn, rand, zeros, Float
      from matplotlib.mlab import hist, mean

      Nbins = 50
      Ntests = 200
      results = zeros((Ntests,Nbins), typecode=Float)
      for i in range(Ntests):
          print 'computing', i
          x = rand(10000)
          n, bins = hist(x, Nbins)
          results\[i\] = n
      print mean(results)