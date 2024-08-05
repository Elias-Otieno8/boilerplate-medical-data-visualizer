import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv(r'/workspace/boilerplate-medical-data-visualizer/medical_examination.csv')

# 2
bmi = df['weight']/((df['height']/100)**2)
df['overweight'] = (bmi > 25).astype(int)

# 3
for column in ['cholesterol','gluc']:
    df[column]=df[column].replace({1:0,2:1,3:1}).astype(df[column].dtype)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','alco','overweight','active','smoke'])


    # 6
    df_cat['total'] = 1 
    df_cat = df_cat.groupby(['cardio','variable','value'],as_index = False).count()   

    # 7
   

    # 8
    fig= sns.catplot(x="variable",y='total', hue="value", col="cardio",
                data=df_cat, kind="bar",
                height=6, aspect=.7,
                order=[ 'active','alco','cholesterol','gluc','overweight', 'smoke'],
                estimator=sum).fig
                  
   



    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <=df['ap_hi'])&
    (df['height']>=df['height'].quantile(0.025))&
    (df['height']<=df['height'].quantile(0.975))&
    (df['weight']>=df['weight'].quantile(0.025))&
    (df['weight']<=df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr(method='pearson')

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(11,9))

    # 15
    
    sns.heatmap(corr, linewidths=1,annot=True,mask=mask,fmt='.1f',center=0.08, square=True,  cbar_kws={"shrink": .5} )

    # 16
    fig.savefig('heatmap.png')
    return fig
