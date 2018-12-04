import csv
import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv("TurkeysData.csv")
#removing commas from the Value column and changing it to float dtype
df['Value'] = df['Value'].str.replace(',','').astype(float)
df_Greaterthan2009  = df[df["year"].map(lambda x: x >=2009)]
df_1989To2002 = df[df["year"].map(lambda x: 1989 <=x <=2002)]

#print (df_Greaterthan2009)
#print(df_2009To2018)
#print (df_Greaterthan2009.dtypes)


def createPlots():
    df_Greaterthan2009.plot.line(x="reference_period_desc", y="Value", title="Plot Greater than 2009")
    df_1989To2002.plot.line(x="reference_period_desc", y="Value", title="Plot from 1989 to 2002")
    plt.show()

def calcualteMeanMedian():
    print (df.groupby('year')['Value'].mean())
    print (df.groupby('year')['Value'].median())

def main():
    createPlots()
    calcualteMeanMedian()

main()


