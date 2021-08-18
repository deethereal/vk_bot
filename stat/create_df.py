import pandas as pd, numpy as np
id2name_color={207227130:['Матвей','#ff0000'], 125928980:['Никита','#ff5e00'], 62501050:['Коля','#ffee00'], 150078285:['Cемен','#33b80f'], 218917421:['Саша','#00d5ff'], 206312673:['Денис',"#005eff"], 236709769:['Влад','#6600ff'], 240702553:['Ира','#000000']}

hs = []
for i in range(23):
    h=str(i)
    nh=str(i+1)
    if i<10:
        h='0'+h
        if i<9:
            nh='0'+nh
    hs.append(h+'-'+nh)
names=[]
colors = []
for k in id2name_color.keys():
    names.append(id2name_color[k][0])
    colors.append(id2name_color[k][1])
hs.append('23-00')

hours = pd.DataFrame(columns=names,index=hs,data=np.zeros(shape=(len(hs),len(names))))
hours=hours.rename_axis('hours')
hours.to_csv('dataframe.csv')
