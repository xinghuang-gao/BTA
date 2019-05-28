# creat a violin plot with all quantified glutathionylated peptides by the TMT-BioGEE assay
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
peptide_file = "/Users/xing-huanggao/Desktop/Undefined/Data analysis/BTA assay/peptides.csv"
df = pd.read_csv(peptide_file)
headers = ['Sequence', 'MH+ /[Da]', 'Master Protein Accessions', 'Positions in Master Proteins', 'Modifications',
           'XCorr Sequest HT', 'PSMs', 'Quan Info', 'Tag-126', 'Tag-127', 'Tag-128', 'Tag-129', 'Tag-130', 'Tag-131']
df.columns = headers
df.dropna(inplace=True)

for col in df.columns[-6:]:  # select the data from columns need to be converted.
    # convert the selected data into nummeric by for statmement
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df. head()

# Perform a log2 conversion of the columns from df [126-131] using np
df['log2_126'] = np.log2(df['Tag-126'])
df['log2_127'] = np.log2(df['Tag-127'])
df['log2_128'] = np.log2(df['Tag-128'])
df['log2_129'] = np.log2(df['Tag-129'])
df['log2_130'] = np.log2(df['Tag-130'])
df['log2_131'] = np.log2(df['Tag-131'])
df.columns.get_loc("log2_131")

tips = df.iloc[:, 14:17]
plt.figure(figsize=(15, 16))
# run sns for violin plot with data log2_126 and 127
sns_plot = sns.violinplot(data=tips, palette="Set2")
sns_plot.set_xticklabels(['Control', 'Diamide', 'Diamide+H2S'])
sns_plot.set(ylabel='sulfhydrated peptides (log2)')

fig = sns_plot.get_figure()
fig.savefig("vln_sulfhydration.pdf")

tips2 = df.iloc[:, 17:21]
plt.figure(figsize=(15, 16))
# run sns for violin plot with data log2_126 and 127
sns_plot2 = sns.violinplot(data=tips2, palette="Set2")
sns_plot2.set_xticklabels(['Control', 'Diamide', 'Diamide+H2S'])
sns_plot2.set(ylabel='glutathionylated peptides (log2)')
sns.despine(offset=20, right=True)
fig = sns_plot2.get_figure()
fig.savefig("vln_glutathionylation.pdf")
