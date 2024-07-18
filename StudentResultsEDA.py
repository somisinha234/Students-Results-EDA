
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_score.csv")
print(df.head())

df.describe()

df.info()

df.isnull().sum()

df.head()

"""Gender Distribution"""

plt.figure(figsize = (5,5))
ax = sns.countplot(data = df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()

#from the above chart that we have analysed that:
#the number of females in the data is more than number of males

gb = df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)

plt.figure(figsize = (4,3))
sns.heatmap(gb,annot=True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()

#From the above chart we have concluded that the education of the parents have good impact on student score

gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)

plt.figure(figsize = (4,3))
sns.heatmap(gb1,annot = True)
plt.show()

#from the above chart we have concluded that there is no impact on the
#student's score due to their parent's marital status

sns.boxplot(data = df,x="MathScore")
plt.show()

sns.boxplot(data = df, x="ReadingScore")
plt.show()

sns.boxplot(data = df, x="WritingScore")
plt.show()

print(df["EthnicGroup"].unique())

"""Distribution of Ethnic Grroups"""

groupA = df.loc[(df["EthnicGroup"]=="group A")].count()
groupB = df.loc[(df["EthnicGroup"]=="group B")].count()
groupC = df.loc[(df["EthnicGroup"]=="group C")].count()
groupD = df.loc[(df["EthnicGroup"]=="group D")].count()
groupE = df.loc[(df["EthnicGroup"]=="group E")].count()

l = ["group A","group B","group C","group D","group E"]
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist,labels = l,autopct = "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()
