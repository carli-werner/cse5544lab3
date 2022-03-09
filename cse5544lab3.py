import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.title('Lab 3 CSE 5544')
st.header('By: Carli Werner')

# read in Data 
data = 'https://raw.githubusercontent.com/carli-werner/cse5544lab3/main/Copy%20of%20CSE5544.Lab1.ClimateData%20-%20Sheet1.csv'
df_data = pd.read_csv(data)

code = '''# read in Data 
data = 'https://raw.githubusercontent.com/carli-werner/cse5544lab3/main/Copy%20of%20CSE5544.Lab1.ClimateData%20-%20Sheet1.csv'
df_data = pd.read_csv(data)
'''
st.code(code, language = 'python')

st.header('General Data Exploration')
st.dataframe(df_data)
body = ('This data has some missing values. I will convert them to NaNs so my program can interpret them. In addition, an item called "OECD-Present" is present.' 
 + ' This is an aggregation of values from all the countries, so I will remove it to avoid skewing central tendencies. ')

st.write(body) 

code = '''
# Convert missing data to NAN
# Remove OCED-Total
df_data.replace('..', np.nan, inplace = True)
df_data.drop(index = 41, inplace = True)
'''
st.code(code, language = 'python')
# Convert missing data to NAN
# Remove OCED-Total
df_data.replace('..', np.nan, inplace = True)
df_data.drop(index = 41, inplace = True)

# Convert data to decimal
years = list(range(1990, 2020))
for year in years:
  df_data[str(year)] = df_data[str(year)].astype('float')

  code = '''# reformat data to work better with seaborns graphing functions
emissions = list()
years2 = list()
regions = list()
length = len(df_data.index)
for year in years:
  years2.extend(np.repeat(str(year), length))
  regions.extend(df_data['Country\year'])
  emissions.extend(df_data[str(year)])
  
f_data = pd.DataFrame()
f_data['Year'] = years2
f_data['Country'] = regions
f_data['Emissions'] = emissions'''


# reformat data to work better with seaborns graphing functions
emissions = list()
years2 = list()
regions = list()
length = len(df_data.index)
for year in years:
  years2.extend(np.repeat(str(year), length))
  regions.extend(df_data['Country\year'])
  emissions.extend(df_data[str(year)])
  
f_data = pd.DataFrame()
f_data['Year'] = years2
f_data['Country'] = regions
f_data['Emissions'] = emissions

st.subheader('Long-Form Data')
st.code(code, language = 'python')
st.write(f_data)

# plot unethical heatmap
st.header('Unethical vs. Ethical Heatmap') 
st.subheader('Heatmap (unethical) with rainbow color scheme')

code = '''c = alt.Chart(f_data, width = 600, height = 500).mark_rect().encode(
    x='Country:N',
    y='Year:O',
    color= alt.Color('Emissions:Q',
                     scale = alt.Scale(scheme = 'rainbow'))
).properties(
    title = 'Heatmap of Emissions Per Country by Year',
    width=750,
    height=600
  )'''

st.code(code, language = 'python')
c = alt.Chart(f_data, width = 600, height = 500).mark_rect().encode(
    x='Country:N',
    y='Year:O',
    color= alt.Color('Emissions:Q',
                     scale = alt.Scale(scheme = 'rainbow'))
).properties(
    title = 'Heatmap of Emissions Per Country by Year',
    width=750,
    height=600
  )

st.altair_chart(c)

#plot  Heatmap (ethical) with unform (black body) color scheme 
st.subheader('Heatmap (ethical) with unform (black body) color scheme')
code = '''d = alt.Chart(f_data, width = 600, height = 500).mark_rect().encode(
    x='Country:N',
    y='Year:O',
    color= alt.Color('Emissions:Q',
                     scale = alt.Scale(scheme = 'inferno'))
).properties(
      title = 'Heatmap of Emissions Per Country by Year',
      width=750,
      height=600
    )'''
st.code(code, language = 'python')
d = alt.Chart(f_data, width = 600, height = 500).mark_rect().encode(
    x='Country:N',
    y='Year:O',
    color= alt.Color('Emissions:Q',
                     scale = alt.Scale(scheme = 'inferno'))
).properties(
      title = 'Heatmap of Emissions Per Country by Year',
      width=750,
      height=600
    )

st.altair_chart(d)

description = ("I prefer the heatmap with the blackbody scheme because the progression of emissions is much more clear than in the rainbow scheme. "+
 "The rainbow scheme is circular, meaning countries with low emissions and countries with high emissions appear in almost identical color. " +
 "This is unethical, because a person who doesn't take time to read the legend could perceive the relationship between countries/emissions/years improperly. "+
 "The blackbody scheme is much more ethical because brightness increases linearly with emissions.")

st.write(description)

st.header('Unethical vs. Ethical Scatter Plot')
st.subheader('Unethical Scatter Plot')
code = '''# Unethical Scatter Plot
x = alt.Chart(f_data).mark_circle().encode(
    x='Year:O',
    y='Emissions:Q',
    color='Country:N',
).properties(
    width=750,
    height=500
)'''

st.code(code, language = 'python')

# Unethical Scatter Plot
x = alt.Chart(f_data).mark_circle().encode(
    x='Year:O',
    y='Emissions:Q',
    color='Country:N',
).properties(
    width=750,
    height=500
)

st.altair_chart(x)

# Ethical Scatter Plot 
st.subheader('Ethical Scatter Plot')
code = '''y = alt.Chart(f_data).mark_circle().encode(
    x='Year:O',
    y='Emissions:Q',
    facet=alt.Facet('Country:N', columns=4)
).resolve_scale(
  x='independent',
).properties(title = "Emssions Per Year by Country", width = 260, height = 150)
'''
st.code(code, language = 'python')

y = alt.Chart(f_data).mark_circle().encode(
    x='Year:O',
    y='Emissions:Q',
    facet=alt.Facet('Country:N', columns=4)
).resolve_scale(
  x='independent',
).properties(title = "Emssions Per Year by Country", width = 260, height = 150)
st.altair_chart(y)

description = ('The above visualization is a much better way to display emissions per year by country. ' +
'The graph has a title, and each data point is clearly visible. In addition, the relationship between emissions, ' +
'country, and year, is much more clear.')

st.write(description)