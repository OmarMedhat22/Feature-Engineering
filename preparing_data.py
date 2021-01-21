import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('nan.csv')
df = pd.read_csv('NBO_WithGroupingCategories.csv')  

df = df.iloc[:,52:82]
#print(df.columns)
df = df.dropna(axis='rows',how='all')
#print(df.head())
df=df.reset_index()
del df['index']
#print(df.head())

print(df.shape)
#for j in range(0,df.shape[0]):

    #print(df.iloc[j])

df = df.fillna(0)
#df.to_csv ('zeros.csv', index = False, header=True)     

visits_number = 5

visits=[]
names=[]
for i in range(0,30,visits_number):
    print(i)
    visit = df.iloc[:,i:i+visits_number].copy()
    print(visit.columns)
    print(visit.shape)
    #visit = visit.dropna(axis='rows',how='all')
    single_visits=[]
    for j in range(0,visit.shape[0]):
        for z in range(0,visit.shape[1]):
            x = visit.iloc[j][z]
            if x !=0:
                single_visits.append(visit.iloc[j][z])
                break
            if z==(visit.shape[1]-1):
                if i==25:
                    single_visits.append(visits[0][j])
                else:
                    single_visits.append(0)

                
    visits.append(single_visits)            

number_of_columns = len(visits)
#visits = visits.reverse()
#visits = [visits[1],visits[0]]
visits=np.array(visits)
#print(visits.shape)
visits  = np.column_stack((visits))

#visits=visits.reshape(-1,number_of_columns)
print(visits.shape)

#df = pd.DataFrame(visits, columns = [i for i in names])  
df_final = pd.DataFrame(visits)  
print(df_final.shape)
print(df_final.tail())
df_final.to_csv ('categories_4.csv', index = False, header=True)     
