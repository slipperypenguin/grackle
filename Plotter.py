# https://github.com/dkogan/gnuplotlib
# Execute with: `Python2 Plotter.py`
import pandas as pd
import numpy as np
import gnuplotlib as gp


df = pd.read_csv('wpm_ec.csv')
df.columns = ['race','wpm','Accuracy', 'Rank', 'Racers', 'text_id', 'Timestamp', 'Database', 'Keyboard']

#print df

race = df['race']
wpm = df['wpm']
#print race
#print wpm.values
print wpm

#df[[Race, wpm]]



x = np.linspace(0, 5, 100, endpoint=False)


## Plot syntax:
#   gp.plot(curve, curve, ...., Plot-and-Curve-options)
#gp.plot( (x, np.cos(x), {'legend': 'cosine'}),


gp.plot( (wpm, {'legend': 'WPM'}),

         title    = 'WPM Graph',
         _with    = 'lines',
         terminal = 'dumb 80,40',
         unset    = 'grid')
