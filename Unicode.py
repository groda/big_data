# This file was generated from Unicode.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/Unicode.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Exploring Unicode categories
# 
# Anyone working with data will sooner or later come across Unicode. In this notebook we're going to download Unicode data directly from the official source and explore the various categories of Unicode characters using interactive Bokeh tables

# The file `UnicodeData.txt`, available from [unicode.org](https://www.unicode.org), the home of Unicode, is the core of the Unicode Character Database (UCD). It is an ASCII file that serves as the foundational data source for Unicode-related functionality, including Python's [unicodedata](https://docs.python.org/3/library/unicodedata.html) module.
# 
# The file contains detailed information about each Unicode character, including its properties and categorizations. The structure of `UnicodeData.txt` (i.e., its columns) and descriptions of the Unicode general categories are documented in the [Unicode® Standard Annex #44](https://www.unicode.org/reports/tr44). For direct reference, you can find information about the [columns of UnicodeData.txt](https://www.unicode.org/reports/tr44/#UnicodeData.txt) and the [list of categories](https://www.unicode.org/reports/tr44/#GC_Values_Table) in the annex.

# ## Download the data
# 
# Download the file `UnicodeData.txt` and save it to the dataframe `df`. Download categories and save them to the dictionary `categories`.

# In[1]:


import urllib.request
import pandas as pd
from collections import defaultdict
import re

url = 'https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt' # unicode data
url_cat = 'https://unicode.org/Public/UCD/latest/ucd/PropertyValueAliases.txt' # ctegories

df = pd.read_csv(url, sep=";", header=None)
df.columns = [str(c) for c in df.columns]

categories = defaultdict(str)
for line in urllib.request.urlopen(url_cat).readlines():
    line = line.decode('utf-8')
    if line.startswith('gc'):
        name, desc = re.split(r'\s*;\s*', line.strip())[1:3]
        desc = desc.split()[0]
        if len(name)>1:
            categories[name] = desc


print("Length of Unicode data dataframe: {}".format(len(df.index)))


# ## List categories
# 
# The Unicode standard has 31 different categories.

# In[2]:


from bokeh.models import ColumnDataSource
from bokeh.models.widgets import TableColumn, DataTable
from bokeh.io import reset_output, output_notebook, show

reset_output()
output_notebook()

cat_data = {'symbol': list(categories.keys()), 'name': list(categories.values())}
cat_source = ColumnDataSource(cat_data)

Columns = [TableColumn(field=c, title=c) for c in ['symbol', 'name']]
cat_table = DataTable(columns=Columns, source=cat_source, fit_columns=True)
show(cat_table)
print("Number of categories: {}".format(len(categories)))


# ## Filter Unicode characters by category
# 
# Create a Bokeh `DataTable` containing `df`. The `select` widget allows to filter the table by category.

# In[44]:


from bokeh.models import Callback, CustomJS, TabPanel, Tabs
from bokeh.models import Select
from bokeh.layouts import column

reset_output()
output_notebook()

val = 'Ll'

columns = ['code', 'Name', 'General_Category']
Columns = [TableColumn(field=str(c), title=columns[c]) for c in range(len(columns))] # bokeh columns

df = df.iloc[:,:3] # we'll consider only first three columns
source = ColumnDataSource(df[(df['2'] == val)])
all = ColumnDataSource(df)

data_table = DataTable(columns=Columns, source=source, fit_columns=True) # bokeh table

options = [("All", "-")] + [(key, f"{categories[key]} ({key})") for key in categories]
dropdown = Select(title="Select category", options=options)

update_value = CustomJS(args=dict(source=source, all=all, dropdown=dropdown), code="""
    var v = dropdown.value;
    if (v == "All") {
        source.data = all.data;
    }
    else {
    var data=all.data;
    var indices = [];
    for (var i = 0; i <= data[0].length; i++){
      if (data['2'][i] == v ) {
        indices.push(i)
      }
    }
    let columnNames = Object.keys(source.data);
    data = columnNames.map(col => indices.map(i => data[col][i]));
    // Extract the column names from `source`

    let filteredData = {};
    // Loop over column names and assign each array from `data` to the corresponding column
    for (let i = 0; i < columnNames.length; i++) {
       filteredData[columnNames[i]] = data[i];
    }
    source.data = filteredData;
    }
    source.change.emit();
""")

dropdown.js_on_change('value', update_value)

layout = column(dropdown, data_table)

show(layout)


# ## Numerical reference in HTML
# 
# Each Unicode character has its HTML code, called numeric character reference (NCR). In the table below we show the HTML codes and how they're rendered in the browser.

# In[48]:


from bokeh.models.widgets import HTMLTemplateFormatter
columns = ['code', 'Name', 'General_Category', 'Web escape']
Columns = [TableColumn(field=str(c), title=columns[c]) for c in range(len(columns))] # bokeh columns

df = df.iloc[:,:3] # we'll consider only first three columns
df.loc[:, '3'] = "&#x" + df.loc[:, '0'] + ";"

html_template = '<%= value %>'
html_formatter =  HTMLTemplateFormatter(template=html_template)
Columns.append(TableColumn(field='4', title='Web rendering', formatter=html_formatter))
df.loc[:, '4'] = "&#x" + df.loc[:, '0'] + ";"

val = 'Ll'
source = ColumnDataSource(df[(df['2'] == val)])
all = ColumnDataSource(df)

data_table = DataTable(columns=Columns, source=source, fit_columns=True) # bokeh table

options = [("All", "-")] + [(key, f"{categories[key]} ({key})") for key in categories]
dropdown = Select(title="Select category", options=options)

update_value = CustomJS(args=dict(source=source, all=all, dropdown=dropdown), code="""
    var v = dropdown.value;
    if (v == "All") {
        source.data = all.data;
    }
    else {
    var data=all.data;
    var indices = [];
    for (var i = 0; i <= data[0].length; i++){
      if (data['2'][i] == v ) {
        indices.push(i)
      }
    }
    let columnNames = Object.keys(source.data);
    data = columnNames.map(col => indices.map(i => data[col][i]));
    // Extract the column names from `source`

    let filteredData = {};
    // Loop over column names and assign each array from `data` to the corresponding column
    for (let i = 0; i < columnNames.length; i++) {
       filteredData[columnNames[i]] = data[i];
    }
    source.data = filteredData;
    }
    source.change.emit();
""")

dropdown.js_on_change('value', update_value)

layout = column(dropdown, data_table, sizing_mode='scale_width')

show(layout)


# Today I learned that you can express roman numerals with Unicode symbols, such as `Ⅰ	Ⅱ Ⅲ	Ⅳ	Ⅴ	Ⅵ	Ⅶ	Ⅷ	Ⅸ`, ... and small `ⅰ ⅱ ⅲ	ⅳ	ⅴ	ⅵ	ⅶ	ⅷ	ⅸ`, ...
