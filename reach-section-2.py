import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

diabetes_data = pd.read_csv(filepath_or_buffer='data/diabetes.data',
                      sep='\t',
                      header=0)

path = 'plots/reach-section/question1'
os.makedirs(path, exist_ok=True)
sns.set()
sns.lineplot('AGE','BMI', data=diabetes_data)

plt.legend(['Age','BMI'])
plt.savefig(f'{path}/plot-age-bmi.png')
plt.clf()

path = 'plots/reach-section/question2'
os.makedirs(path, exist_ok=True)

sns.scatterplot('BMI', 'BP', data=diabetes_data)
plt.legend(['BMI vs BP'])
plt.savefig(f'{path}/scatter-bmi-bp.png')
plt.clf()



path = 'plots/reach-section/question3'
os.makedirs(path, exist_ok=True)
sns.distplot(diabetes_data['BMI'], bins=15, kde=False)
plt.legend(['BMI'])
plt.savefig(f'{path}/bmi_distplot.png')
plt.clf()


path = 'plots/reach-section/question4'
os.makedirs(path, exist_ok=True)
sns.set_style('white')  # ticks, darkgrid, whitegrid
diabetes_data['diagnosis-by-sex'] = diabetes_data['SEX'].map({1: "Male", 2: "Female"})
sns.countplot('diagnosis-by-sex', data=diabetes_data)
plt.savefig(f'{path}/diabetes_diagnosis_by_sex_countplot.png')
plt.clf()

path = 'plots/reach-section/question5'
os.makedirs(path, exist_ok=True)
sns.set()
fig, ax = plt.subplots(figsize=(12,12))
sns.heatmap(diabetes_data.corr(), annot=True, cmap='autumn')
ax.set_xticklabels(diabetes_data.columns, rotation=45)
ax.set_yticklabels(diabetes_data.columns, rotation=45)
plt.savefig(f'{path}/diabetes_heatmap.png')
plt.clf()

path = 'plots/reach-section/question6'
os.makedirs(path, exist_ok=True)
#darkgrid, whitegrid, dark, white, ticks
sns.set(style='darkgrid', palette='coolwarm')
sns.pairplot(diabetes_data, hue='AGE', diag_kind='hist')
plt.savefig(f'{path}/diabetes_pairplot.png')
plt.clf()

plt.close()
