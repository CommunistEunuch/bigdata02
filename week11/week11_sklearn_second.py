import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import xlabel
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df_cancer['target'] = cancer.target

#print(df_cancer.tail())
print(df_cancer.info())

plt.figure(figsize=(10,6))
sns.boxplot(x= 'target',y='mean radius',data=df_cancer)
plt.title('Mean radius of diabetes 0:Malignant 1:Benign')
plt.show()