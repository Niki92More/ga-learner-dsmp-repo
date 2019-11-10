# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
data['Gender']
gender_count=data['Gender'].value_counts()
print(gender_count)
gender_count.plot.barh()
#data.plot.bar(gender_count)
#data.plot.bar(x='Gender', y='gender_count')

#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
labels = 'bad', 'good', 'natural'
plt.pie(alignment,labels=labels)


# --------------
#Code starts here
sc_df=data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df=data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence=ic_df.Intelligence.std().round(2)
ic_combat=ic_df.Combat.std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high=data['Total'].quantile(.99)
print(total_high)
super_best=data[data['Total']>total_high]
super_best_names=super_best['Name'].tolist()
print(super_best_names)
 


# --------------

#data.boxplot(column=['Intelligence', 'Speed', 'Power'])


fig, (ax_1, ax_2,ax_3) = plt.subplots(1, 3, sharex=True, sharey=True)
ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Power')


