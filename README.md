# grackle
embeddable wpm tracking and visualization

Built on top of [wpm](https://github.com/cslarsen/wpm) Python package.
Data Vis with [Pixie Dust](https://github.com/ibm-watson-data-lab/pixiedust)

## General
- Pixie App (or other visualization) is setup for graphing progress
  - graphs from db
- Every time `.wpm` file is updated, the graph should update.
- The graph will be running from a Jupyter Notebook, so can display updated info as long as the Spark instance it is hosted from is running.

## Prerequisites
- [wpm](https://github.com/cslarsen/wpm)
- [Pixie Dust](https://github.com/ibm-watson-data-lab/pixiedust)

## Potential Road Map
### Fork with wpm
- Can add this setup as a PR to wpm, so it's like `wpm --show`

### Standalone Desktop App
- Can have like an Electron app show the visualization... would convert the whole thing to a desktop app instead of terminal
- saved to a db (for use on multiple computers)
- Can get really crafty and build a React-Native app with the same setup as desktop and have it measure mobile typing speed
  - could have user accounts so that data is tracked across devices

## Getting Started
List Existing Kernels:
`jupyter pixiedust list`

Run a notebook:
`jupyter notebook directory/containing/notebook`

Histogram Plot in terminal
`hist -f hist_plot.txt -b 40 -x wpm -c blue -p x`

## Eplot
Basic Example with eplot
`./eplot y_plot.txt -d`

File | Filter | Plot
`cat wpm_ec.csv | ./ec -, 1 3 | ./eplot -d`

File | race wpm accuracy | Plot
`cat wpm_ec.csv | ./ec -, 1 2 3 | ./eplot -d`

File | race wpm accuracty | Plot @Labels@
`cat wpm_ec.csv | ./ec -, 1 2 3 | ./eplot -M -t Race@wpm@Acc -d`

## References
- https://github.com/cslarsen/wpm
- https://github.com/chriswolfvision/eplot
- https://github.com/glamp/bashplotlib
- https://github.com/madbence/node-drawille
- https://www.analyticsvidhya.com/blog/2016/10/spark-dataframe-and-operations/
- https://stackoverflow.com/questions/123378/command-line-unix-ascii-based-charting-plotting-tool
