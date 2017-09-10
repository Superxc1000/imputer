# imputer
Functions to impute missing data in dataframe. Currently, I have one created for regression and another for classification. Just added a dummy data set for demo purposes.  Uses XGBoost version  .6.

Usage:

import grew


data = dataset()
print data
```
prints 

```
<table style="width:100%">
  <tr>
    <th>rain</th>
    <th>some_num</th> 
    <th>some_str</th>
    <th>sprinkler</th>
    <th>wet_sidewalk</th>
  </tr>
 

In this example 'sprinkler' and 'rain' variables are meant to be independent random variables, while 'wet_sidewalk' is true iff 'rain' OR 'sprinkler' is true. 'some_numeric' and 'some_string' are just nonsense numeric and string columns thrown in there for completeness.

All the imputers expect data in a the form of a pandas DataFrame, where:

- numeric columns are treated as continuous variables and can have missing values denoted `np.NaN`
- iteger columns are treated as categorical variables and must have values from `-1` to `n - 1`, where `n` is the number of classes. `-1` is used to denote a missing value.
- string  columns are treated as categorical. Missing values can be denoted by any string specified by user.
