# Execute with: `Python2 Plotter.py`
import pandas as pd
#import numpy as np
import gnuplotlib as gp

#~/.wpm.csv
#df = pd.read_csv('wpm_ec.csv')
df = pd.read_csv('~/.wpm.csv')
df.columns = ['race','wpm','Accuracy', 'Rank', 'Racers', 'text_id', 'Timestamp', 'Database', 'Keyboard']

wpm = df['wpm']
print wpm

#x = np.linspace(0, 5, 100, endpoint=False)

## Plot syntax:
#   gp.plot(curve, curve, ...., Plot-and-Curve-options)

gp.plot( (wpm, {'legend': 'WPM'}),

         title='WPM Graph',
         _with='lines lc rgb "red"',
         terminal='dumb 80,40',
         unset='grid')
