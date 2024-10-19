import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")
# 2
bmi = df["weight"] / ((df["height"] / 100) ** 2)
overweight = np.where( bmi > 25, 1, 0)
df["overweight"] = overweight
# 3
df["cholesterol"] = np.where(df["cholesterol"] > 1, 1, 0)
df["gluc"] = np.where(df["gluc"] > 1, 1, 0)
# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars= ["id", "cardio"], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # 7
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    # 8
    fig.savefig('catplot.png')
    # 9
    return fig
# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()
    df_heat.index = df_heat["id"]
    df_heat = df_heat[
    (df_heat['ap_lo'] <= df_heat['ap_hi']) &
    (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
    (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
    (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
    (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
]
    # 12
    corr = df_heat.corr()
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))    # 14
    fig, ax = plt.subplots(figsize=(10, 8))
    # 15
    fig = sns.heatmap(corr, mask=mask, fmt=".2f", cmap="coolwarm")
    fig = ax.get_figure()
    fig.savefig('heatmap.png')
    # 16
    return fig
