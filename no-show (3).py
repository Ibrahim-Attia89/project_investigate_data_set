#!/usr/bin/env python
# coding: utf-8

# 
# # Project: No show appointments Data Analysis.
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# - this data set have information about medical appointments for more than one hundred thousand patient in Brazil.
# - our main goal is to find out what are the main factors for predicting wether the patient will show up or not ?
# - how does having both (hipertension and diabetes) correlate to showing up ?!
# - how does Scholarship correlate to showing up ?
# - how does sms reciving correlate to showing up ?

# - Installing necessary libraries such as numpy, Pandas, seaborn and matplotlib 

# In[81]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# ### General Properties

# - Loading the data set into a data frame to be easy handeled and take a brief look

# In[82]:


df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# - Find how many columns and rows in our data frame

# In[83]:


df.shape


# - Get a describtion for each column (5-number summary)

# In[84]:


df.describe()


# - Find out how many missing values, null values and the data type for each column to detect any future problems

# In[85]:


df.info()


# - Check for duplicated rows in order to eliminate them from our data frame

# In[86]:


duplicateRowsDF = df[df.duplicated()]
duplicateRowsDF


# - So we have no null, duplicated or missing values and data types are suitable.
# But we have column names in different formats needs to be united and we have some irrelevant columns.

# ### Data Cleaning (remove irrelevant columns and rename the rest!)

# - Remove irrelevant columns which are the columns that have no effect on our analysis

# In[87]:


df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'], axis = 1, inplace = True)


# - Rename all columns so it can be easily used in Data Wrangling

# In[88]:


df.rename(columns = lambda x: x.strip().lower().replace("-","_"), inplace = True)


# - Make sure changes are done and saved in our data frame

# In[89]:


df.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# ### First find the general charcteristics

# - It is important to view the general charcteristics of our data set to determine what questions this data can answer. 

# - By plotting the relationship between every two variables we can have better understanding of our data set.

# In[90]:


sns.pairplot(df);


# - the relation between every pair of variables is very thin as you can see in the plot for example the relation between Age and having Diabetes its almost a straight line 

# ### Research Question 1 (how does having both (hipertension and diabetes) correlate to showing up ?!)

# - Chronic diseases like Diabetes and Hipertension are very common so it's a very important factor to our analysis. 

# -  we need to study them together as they most likely to have the same effect.

# -  I will draw the relation between having both (hipertension and diabetes) and no showing up to see which category show up more in there appointment.

# In[72]:


sns.barplot(data=df, x="diabetes", y="hipertension", hue="no_show")
plt.title("The relation between having both (hipertension and diabetes)and no_show_up");


# - As we can see in the plot Patients with chronic diseases ( hipertension and diabetes ) showed up for there appointment more than people without chronic diseases ( hipertension and diabetes )

# - before continuing our analysis I suggest to  make different data frames for absent patients (no_show) and present patients (showed_up) to make it easy for us to analize each set.

# In[66]:


absent = df.query('no_show == "Yes"')
present = df.query('no_show == "No"')


# ### Research Question 2 (how does Scholarship correlate to showing up ?)
# - scholarship = Bolsa Família :  social welfare program of the Government of Brazil, part of the Fome Zero network of federal assistance programs. Bolsa Família provides financial aid to poor Brazilian families; and if they have children, families must ensure that the children attend school and are vaccinated.
# 

# - scholarship is an indicator to the Social situation of the patient so it's important to be studied

# sketch a histogram to show the distribution of each set against shcolarship to determine the effect of having a scholarship on both groups (showed up or didn't show up). 

# In[76]:


absent.scholarship.hist(alpha = 0.5, label = 'absent', figsize = (10,10))
present.scholarship.hist(alpha = 0.5, label = 'present', figsize = (10,10))
plt.title("Having a scholarship effect")
plt.ylabel("Count of Patients")
plt.xlabel("Scholarship")
plt.legend();


# - The histogram showed that patients without scholarship showed up in a significant difference to those how did have a scholarship.

# - Get the statistical difference :Find the mean for each set against scholarship to assure the result we concluded from the histogram.

# In[48]:


absent.scholarship.mean(), present.scholarship.mean()


# - So patients without scholarship showed up in a significant difference to those how did have a scholarship.

# ### Research Question 3  (how does reciving sms reminder correlate to showing up ?!)
# 

# - Study the effect of having sms reminder on showing up or not as its an important factor and also evaluate the cost of it against its benifit.

# - Sketch a histogram to show the distribution of each set against reciving sms.

# In[77]:


absent.sms_received.hist(alpha = 0.5, label = 'absent', figsize = (10,10))
present.sms_received.hist(alpha = 0.5, label = 'present', figsize = (10,10))
plt.title("Sms reciving effect")
plt.ylabel("Count of Patients")
plt.xlabel("Sms recived")
plt.legend();


# - The histogram showed that absent patients recived more sms reminder than present patients.

# - find the mean for each set against sms recived  to assure the result we concluded from the histogram.

# In[78]:


absent.sms_received.mean(), present.sms_received.mean()


# - So absent patients recived more sms reminder than present patients.

# ## Limitations

# ### There could be many other variables to improve the quality of this analysis such as:
# - Appointment fees expensive or cheap.
# - Quality of health care in each hospital high, medium or low.

# <a id='conclusions'></a>
# ## Conclusions

# - Patients with chronic diseases ( hipertension and diabetes ) showed up for there appointment more than people without chronic diseases ( hipertension and diabetes ).                                            
# - Patients without scholarship showed up in a significant difference to those who did have a scholarship.
# - Absent patients recived more sms reminder than present patients.

# In[ ]:




