import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# assign the csv file location named as kegg
kegg = "/Users/xing-huanggao/Desktop/Undefined/Data analysis/BTA assay/KEGG pathway/KEGG.csv"

# read kegg file with pd as df
df = pd.read_csv(kegg)

# remove the NaN data points
df.dropna(inplace=True)
df['-logpvalue'] = np.log10(df['PValue'])*-1
# create a new column by calculating -logpvalue x the number of counts

df['logp x count'] = df['-logpvalue'] * df['Count']

# sort the column named logp x count
df_sort = df.sort_values(by=['logp x count'], ascending=False)

# create a figure with defined resoultion.
plt.figure(figsize=(15, 15))

# create a bar plot with the data of top 14 in kegg pathways
sns_kegg = sns.barplot(x=df_sort["logp x count"].iloc[1:14],
                       y=df_sort["Term"].iloc[1:14])  # omit the top 1 antibiotic pathway

fig = sns_kegg.get_figure()
fig.savefig("kegg_top14.pdf")
# KEGG pathway analysis
the resion was made on May 29 2019
