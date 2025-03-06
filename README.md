
# CsvSearch

A simple (and janky) tool to search a string in multiple CSV files at once




## First Installation

Before anything, be sure you have [Python 3.10](https://www.python.org/downloads/release/python-31011/) installed.

For the first install, double click on setup.bat file or run the following command :

```python
  python setup.py
```

Wait until the script finish and you'll be good to go !
## How to use ?

First, put all of your CSV files in the CSV folder then just double click on the run.bat file or run the following command :

```python
  python main.py
```

Now, input what you want to search in the CSV files (it is not case sensitive) and when you're done press enter. It may take some time depending on the number of CSV files and their size but you should be seeing the number of match found after a few seconds.

The results will get printed in "results.txt" with the name of the file where the string was found and the coordinate of the cell to find it easily.