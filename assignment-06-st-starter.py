# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# show the title
st.title('Titanic App by Jiayi Li')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

st.subheader('Box Plot of the Ticket Price with Different Classes')
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

Fare_1 = df[df['Pclass'] == 1]['Fare']
Fare_2 = df[df['Pclass'] == 2]['Fare']
Fare_3 = df[df['Pclass'] == 3]['Fare']    

ax[0].set_xlabel('Fare\nPClass = 1')
ax[0].set_ylabel('Fare')
ax[1].set_xlabel('Fare\nPClass = 2')
ax[2].set_xlabel('Fare\nPClass = 3')

ax[0].boxplot(Fare_1)
ax[1].boxplot(Fare_2)
ax[2].boxplot(Fare_3)

ax[0].set_xticks([])
ax[1].set_xticks([])
ax[2].set_xticks([])

st.pyplot(fig)

