import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({ 'A' : 1.,
	'B' : pd.Timestamp('20130102'),
	'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
	'D' : np.array([3] * 4,dtype='int32'),
	'E' : pd.Categorical(["test","train","test","train"]),
	'F' : 'foo' })

print df.describe()
print df[df.A > 0]
print df.mean()
print df.A.mean()

print df.apply(lambda x: x.max() - x.min())

# categoricals
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
df["grade"].cat.categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print df.sort_values(by="grade")
print df.groupby("grade").size()

# plotting
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.savefig('test.png')