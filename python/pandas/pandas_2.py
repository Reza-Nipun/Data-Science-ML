import pandas as pd
import numpy as np

'''
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data.replace([-999,-1000],np.nan,inplace=True)
'''

'''
data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two',
'three', 'four'])
data.rename(index = {'Ohio':'SanF'}, columns={'one':'one_p','two':'two_p'},inplace=True)
data.rename(index = str.upper, columns=str.title,inplace=True)
print(data)
'''

'''
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
pd.cut(ages,bins,right=False)
pd.value_counts(cats)
print(cats)
print(pd.value_counts(cats))

bin_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']
new_cats = pd.cut(ages, bins,labels=bin_names)
print(pd.value_counts(new_cats))
print(pd.value_counts(new_cats).cumsum())
'''

'''
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
'key2' : ['one', 'two', 'one', 'two', 'one'],
'data1' : np.random.randn(5),
'data2' : np.random.randn(5)})
print(df)

grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())
'''

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
print(df[:3])
print(df['20130101':'20130104'])
print(df.loc[:,['A','B']])
print(df.loc['20130102':'20130103',['A','B']])
print(df.iloc[3])
print(df.iloc[2:4, 0:2])
print(df.iloc[[1,5],[0,2]])
print(df[df.B > 1])

df2 = df.copy()
df2['E']=['one', 'one','two','three','four','three']
print(df2)
print(df2[df2['E'].isin(['two','four'])])
print(df2[~df2['E'].isin(['two','four'])])
print(df.query('A > C'))
print(df.query('A < B | C > A'))

data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
print(data.pivot_table(values='ounces',index='group',aggfunc=np.mean).round(2))
print(data.pivot_table(values='ounces',index='group',aggfunc='count'))
