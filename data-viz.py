
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
diabetes_data = pd.read_csv(filepath_or_buffer='data/diabetes.data',
                      sep='\t',
                      header=0)

#Create Scatter Data images for 3 features at a time
for col1_idx, column1 in enumerate(diabetes_data.columns):
    path = 'plots/diabetes-dataset-plots-exploration-scatter-plots/' + column1
    os.makedirs(path, exist_ok=True)
    for col2_idx, column2 in enumerate(diabetes_data.columns):
        for col3_idx, column3 in enumerate(diabetes_data.columns):
            if col1_idx < col2_idx & col2_idx < col3_idx:
                fig, axes = plt.subplots(1, 1, figsize=(5, 5))
                axes.grid(axis='y', alpha=0.5)
                axes.grid(axis='x', alpha=0.5)
                #found using line code below a bit ambiguous
                #axes.scatter(diabetes_data[column1], diabetes_data[column2],diabetes_data[column3], label=f'{column1} - {column2} - {column3}', color='g', marker='o')
                # found using code below more informative
                axes.scatter(diabetes_data[column1],diabetes_data[column2], label=f'{column1} to {column2}', color='r', marker='s')
                axes.scatter(diabetes_data[column1],diabetes_data[column2], label=f'{column1} to {column3}', color='g', marker='^')
                axes.set_title(f'{column1} vs {column2} vs {column3}')
                axes.legend()
                plt.savefig(f'{path}/{column1}_{column2}_{column3}_scatter.png', dpi=300)
                plt.close(fig)



#Create Correlation Heatmap

# Correlation Heatmap
path = 'plots/correlation-heat-map'
os.makedirs(path, exist_ok=True)
fig, axes = plt.subplots(1, 1, figsize=(40, 40))

correlation = diabetes_data.corr().round(2)
im = axes.imshow(correlation)
cbar = axes.figure.colorbar(im, ax=axes)
cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")
numrows = len(correlation.iloc[0])
numcolumns = len(correlation.columns)
axes.set_xticks(np.arange(numrows))
axes.set_yticks(np.arange(numcolumns))
axes.set_xticklabels(correlation.columns)
axes.set_yticklabels(correlation.columns)
plt.setp(axes.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(numrows):
    for j in range(numcolumns):
        text = axes.text(j, i, correlation.iloc[i, j], ha='center', va='center', color='w')
axes.set_title('Heatmap of Correlation of Dimensions')
fig.tight_layout()
plt.savefig(f'{path}/diabetes_data_correlation_heatmap.png')

#3D Scatter plots
path = 'plots/diabetes-dataset-plots-exploration-3d-plots'
os.makedirs(path, exist_ok=True)
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection='3d')
for col1_idx, column1 in enumerate(diabetes_data.columns):
    path = 'plots/diabetes-dataset-plots-exploration-3d-plots/' + column1
    os.makedirs(path, exist_ok=True)
    for col2_idx, column2 in enumerate(diabetes_data.columns):
        for col3_idx, column3 in enumerate(diabetes_data.columns):
            if col1_idx < col2_idx & col2_idx < col3_idx:
                fig = plt.figure()
                axes = fig.add_subplot(1, 1, 1, projection='3d')

                axes.scatter(diabetes_data[column1], diabetes_data[column2],diabetes_data[column3], label=f'{column1} - {column2} - {column3}', color='g', marker='o')

                axes.set_title(f'{column1} vs {column2} vs {column3}')
                axes.legend()
                axes.set_xlabel(f'{column1}')
                axes.set_ylabel(f'{column2}')
                axes.set_zlabel(f'{column3}')
                plt.savefig(f'{path}/{column1}_{column2}_{column3}_scatter.png', dpi=300)
                plt.close(fig)


plt.savefig(f'{path}/test_3d.png')
plt.close()

