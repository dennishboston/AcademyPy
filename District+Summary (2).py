
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


students_csv = "../raw_data/students_complete.csv"
schools_csv = "../raw_data/schools_complete.csv"


# In[3]:


students_df = pd.read_csv(students_csv)
schools_df = pd.read_csv(schools_csv)


# In[4]:


students_df.head()


# In[5]:


schools_df.head()


# In[6]:


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


# In[7]:


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


# In[8]:


#Table for the Key Metrics for the entire District
district_df = pd.DataFrame([[total_schools,total_students,total_budget,average_math,average_reading,percentage_passing_math, percentage_passing_reading,passing_both]],columns=['Total Schools','Total Students','Total Budget($)','Average Math Score','Average Reading Score', '% Passing Math','% Passing Reading', '% Overall Passing Rate'])
print ("**DISTRICT SUMMARY**")    
district_df


# In[9]:


#WHY DO THE FOLLOWING TABLES LOOK MUSHED TOGETHER /////FIND AND FIX SYNTAX


# In[10]:


#Table for the Key Metrics for the each School in the district
individual_schools_df = pd.DataFrame([[school_name, school_type, ind_students, ind_budget, ind_budget_per_student, ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]], columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
individual_schools_df.set_index('School Name', inplace=True)
print("**SCHOOL SUMMARY**")
individual_schools_df


# In[11]:


#Table for the Key Metrics for the Top Performing Schools in the District//////get overall pass column to descend
tpf_df = pd.DataFrame([[school_name,school_type,ind_students,ind_budget,ind_budget_per_student,ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]],columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
print ("**TOP PERFORMING SCHOOLS**")
tpf_df.set_index('School Name', inplace=True)
tpf_df.sort_values(tpf_df.columns[8],ascending=False)


# In[12]:


#Table for the Key Metrics for the Lowest Performing Schools in the District//////get overall pass column to ascend
tpf_df = pd.DataFrame([[school_name,school_type,ind_students,ind_budget,ind_budget_per_student,ind_average_math, ind_average_reading, percent_ind_passing_math, percent_ind_passing_reading, percent_ind_overall_passing]],columns=["School Name", "School Type", "Total Students", "Total School Budget($)", "Per Student Budget($)", "Average Math Score", "Average Reading Score","% Passing Math", "% Passing Reading", "Overall Passing Rate"])
print ("**LOWEST PERFORMING SCHOOLS**")
tpf_df.set_index('School Name', inplace=True)
tpf_df.sort_values(tpf_df.columns[8],ascending=True)


# In[13]:


grade_count = students_df['grade'].value_counts()
grade_count.head()


# In[14]:


# number of students per hs per grade
groupby_grade = students_df.groupby(['grade', 'school'])
groupby_grade.count().head()


# In[15]:


average_math_by_grade = groupby_grade['math_score'].sum() / groupby_grade['math_score'].count()
average_math_by_grade.head(20)


# In[16]:


#math by grade dataframe ///////10th grade out put copies into all columns
print ("**MATH SCORES BY GRADE LEVEL**")

mbg_df = pd.DataFrame({"9th Grade":average_math_by_grade,
                       "10th Grade":average_math_by_grade,
                       "11th Grade":average_math_by_grade,
                       "12th Grade":average_math_by_grade
    
})
mbg_df


# In[17]:


average_reading_by_grade = groupby_grade['reading_score'].sum() / groupby_grade['reading_score'].count()
average_reading_by_grade.head(20)


# In[18]:


#reading by grade dataframe  //// 10th grade out put copies into all columns
print ("**READING SCORES BY GRADE LEVEL**")

rbg_df = pd.DataFrame({"9th Grade":average_math_by_grade,
                       "10th Grade":average_math_by_grade,
                       "11th Grade":average_math_by_grade,
                       "12th Grade":average_math_by_grade
    
})
rbg_df


# In[22]:


# Create the bins in which spending per student will be held

binsb = [0, 585, 610, 635, 660]

# Create the names for the four bins
school_spending = ["<$585","$585-610","$610-635","$635-660"]
pd.cut(schools_df["budget"], binsb, labels=school_spending)


# In[23]:


# Create the bins in which School size will be held

binss = [0, 1500, 3000, 5000]

# Create the names for the bins
school_size = ["Small", "Medium", "Large"]
pd.cut(schools_df["size"], binss, labels=school_size)


# In[26]:


schools_df["School Size"] = pd.cut(schools_df["size"], binss, labels=school_size)
schools_df


# In[31]:


school_groups = schools_df.groupby("School Size")
school_groups.head()


# In[33]:


# bysize_df = students_df.groupby(schools_df['School Size'])
# bysize_df

