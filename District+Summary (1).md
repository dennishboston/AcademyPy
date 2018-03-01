

```python
import pandas as pd
import numpy as np
```


```python
students_csv = "../raw_data/students_complete.csv"
schools_csv = "../raw_data/schools_complete.csv"
```


```python
students_df = pd.read_csv(students_csv)
schools_df = pd.read_csv(schools_csv)
```


```python
students_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
schools_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# average math test score
average_math = students_df["math_score"].mean()
# average reading test score
average_reading = students_df["reading_score"].mean()
# number of kids passing math
passing_math = students_df.loc[(students_df["math_score"] >= 60)]
# number of kids passing reading
passing_reading = students_df.loc[(students_df["reading_score"] >= 60)]
# total number of students in the district
total_students = students_df.name.count()
#total schools in district
total_schools = schools_df.name.count()
# district budget in dollars (add dollar sign)
total_budget = schools_df.budget.sum()
# I want this to return the % of kids who have a passing math score
percentage_passing_math = (passing_math.name.count() / total_students) * 100
# I want this to return the % of kids who have a passing reading score
percentage_passing_reading = (passing_reading.name.count() / total_students) * 100
# Average of Both of the above variables
passing_both = ((percentage_passing_math + percentage_passing_reading) / 2)
```


```python
#Name of each school
school_name = schools_df["name"]
#Type of each school
school_type = schools_df["type"]
#Total students per individual school
ind_students = schools_df["size"]
#Total budget per individual school
ind_budget = schools_df["budget"]
#Per student budget per school
ind_budget_per_student = ind_budget / ind_students
#Average Math score per school
groupby_ind_math = students_df['math_score'].groupby(students_df['school'])
ind_average_math = groupby_ind_math.mean()
#Average Reading score per school
groupby_ind_reading = students_df['reading_score'].groupby(students_df['school'])
ind_average_reading = groupby_ind_reading.mean()
#% Passing Math by school
ind_students1 = ind_students.groupby(schools_df['name'])
groupby_ind_passing_math = passing_math.groupby(students_df['school'])
percent_ind_passing_math = (groupby_ind_passing_math["school"].count()) / (ind_students1.sum()) * 100
percent_ind_passing_math
#% Passing Reading by school
groupby_ind_passing_reading = passing_reading.groupby(students_df['school'])
percent_ind_passing_reading = (groupby_ind_passing_reading['school'].count()) / (ind_students1.sum()) * 100
percent_ind_passing_reading 
#Overall Passing (avg of two above)
percent_ind_overall_passing = (percent_ind_passing_math + percent_ind_passing_reading) / 2
percent_ind_overall_passing

```




    school
    Bailey High School        94.764871
    Cabrera High School      100.000000
    Figueroa High School      94.218379
    Ford High School          94.651333
    Griffin High School      100.000000
    Hernandez High School     94.541532
    Holden High School       100.000000
    Huang High School         94.429208
    Johnson High School       94.591472
    Pena High School         100.000000
    Rodriguez High School     94.273568
    Shelton High School      100.000000
    Thomas High School       100.000000
    Wilson High School       100.000000
    Wright High School       100.000000
    dtype: float64




```python
#Table for the Key Metrics for the entire District
district_df = pd.DataFrame([[total_schools,total_students,total_budget,average_math,average_reading,percentage_passing_math, percentage_passing_reading,passing_both]],columns=['Total Schools','Total Students','Total Budget($)','Average Math Score','Average Reading Score', '% Passing Math','% Passing Reading', '% Overall Passing Rate'])
print ("**DISTRICT SUMMARY**")    
district_df
```

    **DISTRICT SUMMARY**





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>92.445749</td>
      <td>100.0</td>
      <td>96.222875</td>
    </tr>
  </tbody>
</table>
</div>




```python
#WHY DO THE FOLLOWING TABLES LOOK MUSHED TOGETHER /////FIND AND FIX SYNTAX
```


```python
#Table for the Key Metrics for the each School in the district
individual_schools_df = pd.DataFrame([[school_name, school_type, ind_students, ind_budget, ind_budget_per_student, ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]], columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
individual_schools_df.set_index('School Name', inplace=True)
print("**SCHOOL SUMMARY**")
individual_schools_df
```

    **SCHOOL SUMMARY**





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget($)</th>
      <th>Per Student Budget($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>[Huang High School, Figueroa High School, Shelton High School, Hernandez High School, Griffin High School, Wilson High School, Cabrera High School, Bailey High School, Holden High School, Pena High School, Wright High School, Rodriguez High School, Johnson High School, Ford High School, Thomas High School]</th>
      <td>0     District
1     District
2      Charter
3...</td>
      <td>0     2917
1     2949
2     1761
3     4635
4 ...</td>
      <td>0     1910635
1     1884411
2     1056600
3   ...</td>
      <td>0     655.0
1     639.0
2     600.0
3     652....</td>
      <td>school
Bailey High School       77.048432
Cabr...</td>
      <td>school
Bailey High School       81.033963
Cabr...</td>
      <td>school
Bailey High School        89.529743
Cab...</td>
      <td>school
Bailey High School       100.0
Cabrera ...</td>
      <td>school
Bailey High School        94.764871
Cab...</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Table for the Key Metrics for the Top Performing Schools in the District//////get overall pass column to descend
tpf_df = pd.DataFrame([[school_name,school_type,ind_students,ind_budget,ind_budget_per_student,ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]],columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
print ("**TOP PERFORMING SCHOOLS**")
tpf_df.set_index('School Name', inplace=True)
tpf_df.sort_values(tpf_df.columns[8],ascending=False)
```

    **TOP PERFORMING SCHOOLS**





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget($)</th>
      <th>Per Student Budget($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>[Huang High School, Figueroa High School, Shelton High School, Hernandez High School, Griffin High School, Wilson High School, Cabrera High School, Bailey High School, Holden High School, Pena High School, Wright High School, Rodriguez High School, Johnson High School, Ford High School, Thomas High School]</th>
      <td>0     District
1     District
2      Charter
3...</td>
      <td>0     2917
1     2949
2     1761
3     4635
4 ...</td>
      <td>0     1910635
1     1884411
2     1056600
3   ...</td>
      <td>0     655.0
1     639.0
2     600.0
3     652....</td>
      <td>school
Bailey High School       77.048432
Cabr...</td>
      <td>school
Bailey High School       81.033963
Cabr...</td>
      <td>school
Bailey High School        89.529743
Cab...</td>
      <td>school
Bailey High School       100.0
Cabrera ...</td>
      <td>school
Bailey High School        94.764871
Cab...</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Table for the Key Metrics for the Lowest Performing Schools in the District//////get overall pass column to ascend
tpf_df = pd.DataFrame([[school_name,school_type,ind_students,ind_budget,ind_budget_per_student,ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]],columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
print ("**LOWEST PERFORMING SCHOOLS**")
tpf_df.set_index('School Name', inplace=True)
tpf_df.sort_values(tpf_df.columns[8],ascending=True)
```

    **LOWEST PERFORMING SCHOOLS**





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget($)</th>
      <th>Per Student Budget($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>[Huang High School, Figueroa High School, Shelton High School, Hernandez High School, Griffin High School, Wilson High School, Cabrera High School, Bailey High School, Holden High School, Pena High School, Wright High School, Rodriguez High School, Johnson High School, Ford High School, Thomas High School]</th>
      <td>0     District
1     District
2      Charter
3...</td>
      <td>0     2917
1     2949
2     1761
3     4635
4 ...</td>
      <td>0     1910635
1     1884411
2     1056600
3   ...</td>
      <td>0     655.0
1     639.0
2     600.0
3     652....</td>
      <td>school
Bailey High School       77.048432
Cabr...</td>
      <td>school
Bailey High School       81.033963
Cabr...</td>
      <td>school
Bailey High School        89.529743
Cab...</td>
      <td>school
Bailey High School       100.0
Cabrera ...</td>
      <td>school
Bailey High School        94.764871
Cab...</td>
    </tr>
  </tbody>
</table>
</div>




```python
grade_count = students_df['grade'].value_counts()
grade_count.head()
```




    9th     11408
    10th    10168
    11th     9695
    12th     7899
    Name: grade, dtype: int64




```python
# number of students per hs per grade
groupby_grade = students_df.groupby(['grade', 'school'])
groupby_grade.count().head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
    <tr>
      <th>grade</th>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">10th</th>
      <th>Bailey High School</th>
      <td>1239</td>
      <td>1239</td>
      <td>1239</td>
      <td>1239</td>
      <td>1239</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>466</td>
      <td>466</td>
      <td>466</td>
      <td>466</td>
      <td>466</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>763</td>
      <td>763</td>
      <td>763</td>
      <td>763</td>
      <td>763</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>708</td>
      <td>708</td>
      <td>708</td>
      <td>708</td>
      <td>708</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>406</td>
      <td>406</td>
      <td>406</td>
      <td>406</td>
      <td>406</td>
    </tr>
  </tbody>
</table>
</div>




```python
average_math_by_grade = groupby_grade['math_score'].sum() / groupby_grade['math_score'].count()
average_math_by_grade.head(20)

```




    grade  school               
    10th   Bailey High School       76.996772
           Cabrera High School      83.154506
           Figueroa High School     76.539974
           Ford High School         77.672316
           Griffin High School      84.229064
           Hernandez High School    77.337408
           Holden High School       83.429825
           Huang High School        75.908735
           Johnson High School      76.691117
           Pena High School         83.372000
           Rodriguez High School    76.612500
           Shelton High School      82.917411
           Thomas High School       83.087886
           Wilson High School       83.724422
           Wright High School       84.010288
    11th   Bailey High School       77.515588
           Cabrera High School      82.765560
           Figueroa High School     76.884344
           Ford High School         76.918058
           Griffin High School      83.842105
    Name: math_score, dtype: float64




```python
#math by grade dataframe ///////10th grade out put copies into all columns
print ("**MATH SCORES BY GRADE LEVEL**")

mbg_df = pd.DataFrame({"9th Grade":average_math_by_grade,
                       "10th Grade":average_math_by_grade,
                       "11th Grade":average_math_by_grade,
                       "12th Grade":average_math_by_grade
    
})
mbg_df
```

    **MATH SCORES BY GRADE LEVEL**





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
      <th>9th Grade</th>
    </tr>
    <tr>
      <th>grade</th>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="15" valign="top">10th</th>
      <th>Bailey High School</th>
      <td>76.996772</td>
      <td>76.996772</td>
      <td>76.996772</td>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.154506</td>
      <td>83.154506</td>
      <td>83.154506</td>
      <td>83.154506</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.539974</td>
      <td>76.539974</td>
      <td>76.539974</td>
      <td>76.539974</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.672316</td>
      <td>77.672316</td>
      <td>77.672316</td>
      <td>77.672316</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.229064</td>
      <td>84.229064</td>
      <td>84.229064</td>
      <td>84.229064</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.337408</td>
      <td>77.337408</td>
      <td>77.337408</td>
      <td>77.337408</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.429825</td>
      <td>83.429825</td>
      <td>83.429825</td>
      <td>83.429825</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.908735</td>
      <td>75.908735</td>
      <td>75.908735</td>
      <td>75.908735</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.691117</td>
      <td>76.691117</td>
      <td>76.691117</td>
      <td>76.691117</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.372000</td>
      <td>83.372000</td>
      <td>83.372000</td>
      <td>83.372000</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.612500</td>
      <td>76.612500</td>
      <td>76.612500</td>
      <td>76.612500</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.917411</td>
      <td>82.917411</td>
      <td>82.917411</td>
      <td>82.917411</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.087886</td>
      <td>83.087886</td>
      <td>83.087886</td>
      <td>83.087886</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.724422</td>
      <td>83.724422</td>
      <td>83.724422</td>
      <td>83.724422</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.010288</td>
      <td>84.010288</td>
      <td>84.010288</td>
      <td>84.010288</td>
    </tr>
    <tr>
      <th rowspan="15" valign="top">11th</th>
      <th>Bailey High School</th>
      <td>77.515588</td>
      <td>77.515588</td>
      <td>77.515588</td>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>82.765560</td>
      <td>82.765560</td>
      <td>82.765560</td>
      <td>82.765560</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.884344</td>
      <td>76.884344</td>
      <td>76.884344</td>
      <td>76.884344</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>76.918058</td>
      <td>76.918058</td>
      <td>76.918058</td>
      <td>76.918058</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.842105</td>
      <td>83.842105</td>
      <td>83.842105</td>
      <td>83.842105</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.136029</td>
      <td>77.136029</td>
      <td>77.136029</td>
      <td>77.136029</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>85.000000</td>
      <td>85.000000</td>
      <td>85.000000</td>
      <td>85.000000</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.446602</td>
      <td>76.446602</td>
      <td>76.446602</td>
      <td>76.446602</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.491653</td>
      <td>77.491653</td>
      <td>77.491653</td>
      <td>77.491653</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.328125</td>
      <td>84.328125</td>
      <td>84.328125</td>
      <td>84.328125</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.395626</td>
      <td>76.395626</td>
      <td>76.395626</td>
      <td>76.395626</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.383495</td>
      <td>83.383495</td>
      <td>83.383495</td>
      <td>83.383495</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.498795</td>
      <td>83.498795</td>
      <td>83.498795</td>
      <td>83.498795</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.195326</td>
      <td>83.195326</td>
      <td>83.195326</td>
      <td>83.195326</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.836782</td>
      <td>83.836782</td>
      <td>83.836782</td>
      <td>83.836782</td>
    </tr>
    <tr>
      <th rowspan="15" valign="top">12th</th>
      <th>Bailey High School</th>
      <td>76.492218</td>
      <td>76.492218</td>
      <td>76.492218</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.277487</td>
      <td>83.277487</td>
      <td>83.277487</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>77.151369</td>
      <td>77.151369</td>
      <td>77.151369</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>76.179963</td>
      <td>76.179963</td>
      <td>76.179963</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.356164</td>
      <td>83.356164</td>
      <td>83.356164</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.186567</td>
      <td>77.186567</td>
      <td>77.186567</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>82.855422</td>
      <td>82.855422</td>
      <td>82.855422</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.225641</td>
      <td>77.225641</td>
      <td>77.225641</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.863248</td>
      <td>76.863248</td>
      <td>76.863248</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.121547</td>
      <td>84.121547</td>
      <td>84.121547</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>77.690748</td>
      <td>77.690748</td>
      <td>77.690748</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.778976</td>
      <td>83.778976</td>
      <td>83.778976</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.497041</td>
      <td>83.497041</td>
      <td>83.497041</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.035794</td>
      <td>83.035794</td>
      <td>83.035794</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.644986</td>
      <td>83.644986</td>
      <td>83.644986</td>
      <td>83.644986</td>
    </tr>
    <tr>
      <th rowspan="15" valign="top">9th</th>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>77.083676</td>
      <td>77.083676</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.094697</td>
      <td>83.094697</td>
      <td>83.094697</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.403037</td>
      <td>76.403037</td>
      <td>76.403037</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.361345</td>
      <td>77.361345</td>
      <td>77.361345</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>82.044010</td>
      <td>82.044010</td>
      <td>82.044010</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.438495</td>
      <td>77.438495</td>
      <td>77.438495</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.787402</td>
      <td>83.787402</td>
      <td>83.787402</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>77.027251</td>
      <td>77.027251</td>
      <td>77.027251</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>77.187857</td>
      <td>77.187857</td>
      <td>77.187857</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.625455</td>
      <td>83.625455</td>
      <td>83.625455</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.859966</td>
      <td>76.859966</td>
      <td>76.859966</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>83.420755</td>
      <td>83.420755</td>
      <td>83.420755</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.590022</td>
      <td>83.590022</td>
      <td>83.590022</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.085578</td>
      <td>83.085578</td>
      <td>83.085578</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>83.264706</td>
      <td>83.264706</td>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
average_reading_by_grade = groupby_grade['reading_score'].sum() / groupby_grade['reading_score'].count()
average_reading_by_grade.head(20)

```




    grade  school               
    10th   Bailey High School       80.907183
           Cabrera High School      84.253219
           Figueroa High School     81.408912
           Ford High School         81.262712
           Griffin High School      83.706897
           Hernandez High School    80.660147
           Holden High School       83.324561
           Huang High School        81.512386
           Johnson High School      80.773431
           Pena High School         83.612000
           Rodriguez High School    80.629808
           Shelton High School      83.441964
           Thomas High School       84.254157
           Wilson High School       84.021452
           Wright High School       83.812757
    11th   Bailey High School       80.945643
           Cabrera High School      83.788382
           Figueroa High School     80.640339
           Ford High School         80.403642
           Griffin High School      84.288089
    Name: reading_score, dtype: float64




```python
#reading by grade dataframe  //// 10th grade out put copies into all columns
print ("**READING SCORES BY GRADE LEVEL**")

rbg_df = pd.DataFrame({"9th Grade":average_math_by_grade,
                       "10th Grade":average_math_by_grade,
                       "11th Grade":average_math_by_grade,
                       "12th Grade":average_math_by_grade
    
})
rbg_df
```

    **READING SCORES BY GRADE LEVEL**





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
      <th>9th Grade</th>
    </tr>
    <tr>
      <th>grade</th>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="15" valign="top">10th</th>
      <th>Bailey High School</th>
      <td>76.996772</td>
      <td>76.996772</td>
      <td>76.996772</td>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.154506</td>
      <td>83.154506</td>
      <td>83.154506</td>
      <td>83.154506</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.539974</td>
      <td>76.539974</td>
      <td>76.539974</td>
      <td>76.539974</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.672316</td>
      <td>77.672316</td>
      <td>77.672316</td>
      <td>77.672316</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.229064</td>
      <td>84.229064</td>
      <td>84.229064</td>
      <td>84.229064</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.337408</td>
      <td>77.337408</td>
      <td>77.337408</td>
      <td>77.337408</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.429825</td>
      <td>83.429825</td>
      <td>83.429825</td>
      <td>83.429825</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.908735</td>
      <td>75.908735</td>
      <td>75.908735</td>
      <td>75.908735</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.691117</td>
      <td>76.691117</td>
      <td>76.691117</td>
      <td>76.691117</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.372000</td>
      <td>83.372000</td>
      <td>83.372000</td>
      <td>83.372000</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.612500</td>
      <td>76.612500</td>
      <td>76.612500</td>
      <td>76.612500</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.917411</td>
      <td>82.917411</td>
      <td>82.917411</td>
      <td>82.917411</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.087886</td>
      <td>83.087886</td>
      <td>83.087886</td>
      <td>83.087886</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.724422</td>
      <td>83.724422</td>
      <td>83.724422</td>
      <td>83.724422</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.010288</td>
      <td>84.010288</td>
      <td>84.010288</td>
      <td>84.010288</td>
    </tr>
    <tr>
      <th rowspan="15" valign="top">11th</th>
      <th>Bailey High School</th>
      <td>77.515588</td>
      <td>77.515588</td>
      <td>77.515588</td>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>82.765560</td>
      <td>82.765560</td>
      <td>82.765560</td>
      <td>82.765560</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.884344</td>
      <td>76.884344</td>
      <td>76.884344</td>
      <td>76.884344</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>76.918058</td>
      <td>76.918058</td>
      <td>76.918058</td>
      <td>76.918058</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.842105</td>
      <td>83.842105</td>
      <td>83.842105</td>
      <td>83.842105</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.136029</td>
      <td>77.136029</td>
      <td>77.136029</td>
      <td>77.136029</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>85.000000</td>
      <td>85.000000</td>
      <td>85.000000</td>
      <td>85.000000</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.446602</td>
      <td>76.446602</td>
      <td>76.446602</td>
      <td>76.446602</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.491653</td>
      <td>77.491653</td>
      <td>77.491653</td>
      <td>77.491653</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.328125</td>
      <td>84.328125</td>
      <td>84.328125</td>
      <td>84.328125</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.395626</td>
      <td>76.395626</td>
      <td>76.395626</td>
      <td>76.395626</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.383495</td>
      <td>83.383495</td>
      <td>83.383495</td>
      <td>83.383495</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.498795</td>
      <td>83.498795</td>
      <td>83.498795</td>
      <td>83.498795</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.195326</td>
      <td>83.195326</td>
      <td>83.195326</td>
      <td>83.195326</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.836782</td>
      <td>83.836782</td>
      <td>83.836782</td>
      <td>83.836782</td>
    </tr>
    <tr>
      <th rowspan="15" valign="top">12th</th>
      <th>Bailey High School</th>
      <td>76.492218</td>
      <td>76.492218</td>
      <td>76.492218</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.277487</td>
      <td>83.277487</td>
      <td>83.277487</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>77.151369</td>
      <td>77.151369</td>
      <td>77.151369</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>76.179963</td>
      <td>76.179963</td>
      <td>76.179963</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.356164</td>
      <td>83.356164</td>
      <td>83.356164</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.186567</td>
      <td>77.186567</td>
      <td>77.186567</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>82.855422</td>
      <td>82.855422</td>
      <td>82.855422</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.225641</td>
      <td>77.225641</td>
      <td>77.225641</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.863248</td>
      <td>76.863248</td>
      <td>76.863248</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.121547</td>
      <td>84.121547</td>
      <td>84.121547</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>77.690748</td>
      <td>77.690748</td>
      <td>77.690748</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.778976</td>
      <td>83.778976</td>
      <td>83.778976</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.497041</td>
      <td>83.497041</td>
      <td>83.497041</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.035794</td>
      <td>83.035794</td>
      <td>83.035794</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.644986</td>
      <td>83.644986</td>
      <td>83.644986</td>
      <td>83.644986</td>
    </tr>
    <tr>
      <th rowspan="15" valign="top">9th</th>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>77.083676</td>
      <td>77.083676</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.094697</td>
      <td>83.094697</td>
      <td>83.094697</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.403037</td>
      <td>76.403037</td>
      <td>76.403037</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.361345</td>
      <td>77.361345</td>
      <td>77.361345</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>82.044010</td>
      <td>82.044010</td>
      <td>82.044010</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.438495</td>
      <td>77.438495</td>
      <td>77.438495</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.787402</td>
      <td>83.787402</td>
      <td>83.787402</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>77.027251</td>
      <td>77.027251</td>
      <td>77.027251</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>77.187857</td>
      <td>77.187857</td>
      <td>77.187857</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.625455</td>
      <td>83.625455</td>
      <td>83.625455</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.859966</td>
      <td>76.859966</td>
      <td>76.859966</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>83.420755</td>
      <td>83.420755</td>
      <td>83.420755</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.590022</td>
      <td>83.590022</td>
      <td>83.590022</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.085578</td>
      <td>83.085578</td>
      <td>83.085578</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>83.264706</td>
      <td>83.264706</td>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create the bins in which spending per student will be held

binsb = [0, 585, 610, 635, 660]

# Create the names for the four bins
school_spending = ["<$585","$585-610","$610-635","$635-660"]
pd.cut(schools_df["budget"], binsb, labels=school_spending)
```




    0     NaN
    1     NaN
    2     NaN
    3     NaN
    4     NaN
    5     NaN
    6     NaN
    7     NaN
    8     NaN
    9     NaN
    10    NaN
    11    NaN
    12    NaN
    13    NaN
    14    NaN
    Name: budget, dtype: category
    Categories (4, object): [<$585 < $585-610 < $610-635 < $635-660]




```python
# Create the bins in which School size will be held

binss = [0, 1500, 3000, 5000]

# Create the names for the bins
school_size = ["Small", "Medium", "Large"]
pd.cut(schools_df["size"], binss, labels=school_size)
```




    0     Medium
    1     Medium
    2     Medium
    3      Large
    4      Small
    5     Medium
    6     Medium
    7      Large
    8      Small
    9      Small
    10    Medium
    11     Large
    12     Large
    13    Medium
    14    Medium
    Name: size, dtype: category
    Categories (3, object): [Small < Medium < Large]




```python
schools_df["School Size"] = pd.cut(schools_df["size"], binss, labels=school_size)
schools_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>School Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>Medium</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_groups = schools_df.groupby("School Size")
school_groups.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>School Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>Large</td>
    </tr>
  </tbody>
</table>
</div>




```python
# bysize_df = students_df.groupby(schools_df['School Size'])
# bysize_df
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-e5b9617f9f95> in <module>()
    ----> 1 bysize_df = students_df.groupby(schools_df['School Size'])
          2 bysize_df


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in groupby(self, by, axis, level, as_index, sort, group_keys, squeeze, **kwargs)
       4414         return groupby(self, by=by, axis=axis, level=level, as_index=as_index,
       4415                        sort=sort, group_keys=group_keys, squeeze=squeeze,
    -> 4416                        **kwargs)
       4417 
       4418     def asfreq(self, freq, method=None, how=None, normalize=False,


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in groupby(obj, by, **kwds)
       1697         raise TypeError('invalid type: %s' % type(obj))
       1698 
    -> 1699     return klass(obj, by, **kwds)
       1700 
       1701 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in __init__(self, obj, keys, axis, level, grouper, exclusions, selection, as_index, sort, group_keys, squeeze, **kwargs)
        390                                                     level=level,
        391                                                     sort=sort,
    --> 392                                                     mutated=self.mutated)
        393 
        394         self.obj = obj


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in _get_grouper(obj, key, axis, level, sort, mutated)
       2697 
       2698         if is_categorical_dtype(gpr) and len(gpr) != len(obj):
    -> 2699             raise ValueError("Categorical dtype grouper must "
       2700                              "have len(grouper) == len(data)")
       2701 


    ValueError: Categorical dtype grouper must have len(grouper) == len(data)

