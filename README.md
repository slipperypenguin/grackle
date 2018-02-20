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
