import  pandas as pd
import xml.etree.ElementTree as xml

sd=pd.read_csv('sales_demo.csv')
pr=pd.read_csv('products_demo.csv')


print(type(sd), type(pr))

print(sd.shape)
print(pr.shape)

print(sd.columns)

print(pr['ProductID'].nunique())
print(len(pr))


m_inner1=pd.merge(sd,pr, on="ProductID", how="inner")
print(m_inner1.shape)


m_left=pd.merge(sd,pr, on='ProductID', how='left')
m_left1=pd.merge(pr,sd, on='ProductID',how='left')

print(m_left.shape, m_left1.shape)
print()

m_right=pd.merge(sd,pr, on='ProductID', how='right')
m_right1=pd.merge(pr,sd, on='ProductID',how='right')
print(m_right.shape, m_right1.shape)

m_outer=pd.merge(sd,pr, on="ProductID", how="outer")
m_outer1=pd.merge(pr,sd, on="ProductID", how="outer")
print(m_outer.shape,m_outer1.shape)



#Combine two dataframes vertically

print("\nCombine two dataframes vertically\n")
s1=pd.read_csv('sales.csv')
s2=pd.read_csv('sales_q2.csv')
print("\n")
#check whether the two dataframes have the same structure
print(s1.shape,s2.shape)
print(s1.columns)
print(s2.columns)
print("\n")
s_all=pd.concat([s1,s2], ignore_index=True)
s_all1=pd.concat([s1,s2])
print(s1.shape, s2.shape, s_all.shape, s_all1.shape)
print(s_all.head())
print("\n")
print(s_all1.head())
print(s_all)
print("\n")
print(s_all1)

s_all.to_csv('sales_all.csv', index=False)
s_all.to_csv('sales_all1.csv')

#index=False creates the file without the index numbers of the dataframe

s_all.to_excel('sales_all.xlsx',index=False)
# s_all1.to_json('sales_all.json', index=False)
# s_all1.to_json('sales_all1.json')
s_all.to_xml('sales_all.xml', index=False, parser='etree')
s_all1.reset_index(drop=True, inplace=True)
s_all1.to_xml('sales_all.xml', index=False, parser='etree')

s_all1.to_html('sales_all1.html')