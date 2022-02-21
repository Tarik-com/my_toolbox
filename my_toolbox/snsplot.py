import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_sns(row,col,fontsize=10,df,type_of_plot="lineplot",size=(10,10),names=df.columns,step=1):

    fig,ax=plt.subplots(nrows=row,ncols=col,figsize=(size))
    ax = ax.ravel()

    for name, ax in zip(names,ax):
        y=np.arange(1,len(df[name])+1,step)
        exec(f"sns.{type_of_plot}(data=df,x=name,y=y,ax=ax)")
        ax.set_title(name,fontsize=fontsize)
    fig.tight_layout()
    return "la classe Nan"
