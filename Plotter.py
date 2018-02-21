# https://github.com/dkogan/gnuplotlib
# Execute with: `Python2 Plotter.py`
import numpy as np
import gnuplotlib as gp

x = np.linspace(-5,5,100)

gp.plot( x, np.sin(x) )


gp.plot( (x, np.sin(x), {'with': 'boxes'}),
         (x, np.cos(x), {'legend': 'cosine'}),

         _with    = 'lines',
         terminal = 'dumb 80,40',
         unset    = 'grid')
