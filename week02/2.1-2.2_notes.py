# coding: utf-8
import numpy as np
import pandas as pd
df = pd.DataFrame('lessons/week-02/2.1-intro-to-data-cleaning/assets/datasets/sales_info.csv')
df = pd.read_csv('lessons/week-02/2.1-intro-to-data-cleaning/assets/datasets/sales_info.csv')
df
df.dtypes()
df.dtypes
df
df.head
df.head()
df['new_vol_sold'] = df['volume_sold'].apply(df['volume_sold'] + 1)
def add_one(item):
    return item += 1
def add_one(item):
    return item = item + 1
def add_one(item):item = item + 1
def add_one(item):item = item + 1
def add_one(item):
    item += 1
    return item
df['new_vol_sold'] = df['volume_sold'].apply(add_one)
df
df.head()
df['new_2015_margin'] = df['2015_margin'].apply(add_one)
df
df.head()
del df['new_vol_sold']
df.head()
df.value_counts()
df['new_2015_margin'].value_counts()
df.head
df.head()
add_one(10)
df['new_2015_margin'] = df['2015_margin'].apply(add_one)
df['new_2015_q1_sales'] = df['2015_q1_sales'].apply(x = x + 3)
df.apply(np.mean())
df.apply(np.mean)
df.apply(np.median)
df['new_2015_margin'] = df['2015_margin'].apply(add_one)
df['new_2015_q1_sales'] = df['2015_q1_sales'].apply(df['2015_q1_sales'] + 3)
df['new_2015_margin'] = df['2015_margin'].apply(add_one)
df['new_2015_q1_sales'] = df['2015_q1_sales'].apply(df['2015_q1_sales'] + 3)
get_ipython().magic(u'save output.txt')
df['new_2015_margin'] = df['2015_margin'].apply(add_one)
df['new_2015_q1_sales'] = df['2015_q1_sales'].apply(df['2015_q1_sales'] + 3)
df['new_2015_margin'] = df['2015_margin'].apply(add_one)
df['new_2015_q1_sales'] = df['2015_q1_sales'].apply(lambda x: x + 3)
df
df.head()
s = pd.Series(['a','b','c','a'], dtype='category')
s
df = pd.DataFrame({'not_a_categorical': ['a','b','c','a']})
df['is_a_categorical'] = df['not_a_categorical'].astype('category')
df
df.dtypes
df = pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df
pd.get_dummies(df['key'])
df = pd.DataFrame({'not_a_categorical': ['a','b','c','a']})
df['is_a_categorical'] = df['not_a_categorical'].astype('category')
df
df.dtypes
def find_the_a(value):
    if value == 'a':
        return 1
    else:
        return 0
    
df['dummy_variable_a'] = df['not_a_categorical'].apply(find_the_a)
df
df.dtypes
pd.get_dummies(df['not_a_categorical'])
star_wars_data = pd.read_csv('/home/nick/notes/week2/StarWars.csv')
star_wars_data.head()
star_wars_data['Education'].values_counts()
star_wars_data['Education'].value_counts()
star_wars_education = pd.get_dummies(star_wars_data['Education'])
star_wars_education = sw_education
sw_education = star_wars_education
del star_wars_education
star_wars_education
sw_education
sw_education.head()
sw_education.describe()
sw_education['College_Educated'] = sw_education['Bachelor degree'] + sw_education['Graduate degree']
sw_education['College_Educated'].sum()
sw_education['College_Educated'].describe()
star_wars_data['Education'].value_counts()
star_wars_data['Age'].value_counts()
get_ipython().magic(u'save test 1-81')
