file_path = "2007names.txt"
import pandas as pd
df2007 = pd.read_csv(file_path, sep=',',header=None)
df2007
df2020 = pd.read_csv('2020names.txt',sep=',',header=None)
df2007.rename(columns = {0:'name',1:'gender',2:'cnt'},inplace=True)
df2020.rename(columns = {0:'name',1:'gender',2:'cnt'},inplace=True)
df2007['rank'] = df2007.groupby('gender')['cnt'].rank(method='dense',ascending=False)
most_pop_2007 = df2007[df2007['rank'] <=100]

df2020['rank'] = df2020.groupby('gender')['cnt'].rank(method='dense',ascending=False)
most_pop_2020 = df2020[df2020['rank'] <=100]
merged_df = pd.merge(most_pop_2007,most_pop_2020,how='outer',on=['name','gender'],indicator=True)
final = merged_df[merged_df['_merge'] == 'left_only']
final_girl = final[final['gender'] == 'F'].sort_values(by = 'rank_x')
final_boy = final[final['gender']== 'M'].sort_values(by = 'rank_x')
final_girl
