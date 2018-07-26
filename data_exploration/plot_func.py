import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


df['address']  = df[['block', 'StreetName']].apply(lambda x: ' '.join(x), axis=1)






def offense_df(df):
    fs = {}
    aa = df.OffenseType == 'Aggravated Assault'
    fs.update({'Aggravated Assault':aa})
    
    b = df.OffenseType == 'Burglary'
    fs.update({'Burglary':b})

    t = df.OffenseType == 'Theft'
    fs.update({'Theft':t})

    at = df.OffenseType == 'Auto Theft'
    fs.update({'Auto Theft':at})

    ra = df.OffenseType == 'Rape'
    fs.update({'Rape':ra})

    ro = df.OffenseType == 'Robbery'
    fs.update({'Robbery':ro})
    
    mu = df.OffenseType == 'Murder'
    fs.update({'Murder':mu})
    return fs


'''
# create a dataframe with just the two bottom offense types
dfrm = df.loc[(df.OffenseType =='Rape') | (df.OffenseType =='Murder')]


t='Offense type: Rape & Murder: Year'
xlab = ''
ylab = 'amount'

pf.barplot(dfrm,'year',t,xlab,ylab)


t='Offense type: Rape & Murder: Year'
xlab = ''
ylab = 'Crimes'

pf.couplot(dfrm,'Hour',t,xlab,ylab,nums=False,ymax=450)

'''



def couplot(frame,col,title,xlab,ylab,nums=True,leg='best',ymax=None,save=False):    
    fig,ax = plt.subplots(figsize=(10,5))
    ax = sns.countplot(x=col,
                       hue='OffenseType',
                       data=frame,
                       alpha=0.75)
    if ymax== None:
        max_value = frame['{}'.format(col)].value_counts().max()
    else:
        max_value = ymax
    plt.ylim(0,max_value)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha="right")

    height_factor=1.05
    if nums == True:
        for i in ax.patches:
            height = i.get_height()
            ax.text(i.get_x() + i.get_width()/2., height_factor*height,'%d' % int(height), ha='center', va='bottom')

    if save==True:
        plt.savefig('{}.png'.format(title), dpi = 600, facecolor='w',
                edgecolor='w',transparent=True, 
                bbox_inches=None, pad_inches=0.1, frameon=False)
        
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    ax.set_title(title)
    plt.legend(loc=leg)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    print(max_value)
    plt.show()


'''
t='Offense type'
xlab = ''
ylab = 'amount'

pf.barplot(df,'OffenseType',t,xlab,ylab,nums=False)

t='Offense type: Month'
xlab = ''
ylab = 'amount'

pf.barplot(df,'month',t,xlab,ylab)
'''
# list of top 10 premises, beats, street names
'''
premises = [premise for premise in df['Premise'].value_counts().head(10).reset_index()['index']]
beats= [beat for beat in df['Beat'].value_counts().head(10).reset_index()['index']]
streets = [street for street in df['StreetName'].value_counts().head(10).reset_index()['index']]
'''

def barplot(frame,col,title,nums=True,save=False):    
    fig,ax = plt.subplots(figsize=(10,5))
    ax = sns.countplot(x=col,data=frame,alpha=0.65, order=frame['{}'.format(col)].value_counts().index)
    max_value = frame['{}'.format(col)].value_counts().max()

    plt.ylim(0,max_value+(max_value/8))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha="right")
    ax.set_title(title)

    height_factor=1.05
    if nums == True:
        for i in ax.patches:
            height = i.get_height()
            ax.text(i.get_x() + i.get_width()/2., height_factor*height,'%d' % int(height), ha='center', va='bottom')

    if save==True:
        plt.savefig('{}.png'.format(title))
    
    plt.show()


'''

title = 'Crime Timeline'
xlab = 'time (hours)'
ylab= ''
pf.time_plot7d(df,'ALL',
            df_aa,'Aggravated Assault',
            df_b,'Burglary',
            df_t,'Theft',
            df_at,'Auto Theft',
            df_ra,'Rape',
            df_mu,'Murder','OffenseType',title,xlab,ylab)


'''





 
def time_plot1d(f1,f1_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    
    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend([f1_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    
    if save==True:
        plt.savefig('{}.png'.format(title), dpi = 600,
        transparent=True,bbox_inches=None, pad_inches=0.1, frameon=False)
    plt.show()

 
def time_plot2d(f1,f1_name,f2,f2_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    ax = f2.groupby(f2.Hour)['{}'.format(col)].count().plot()
    
    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend([f1_name,f2_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    if save==True:
        plt.savefig('{}.png'.format(title))
    plt.show()



def time_plot3d(f1,f1_name,f2,f2_name,f3,f3_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    ax = f2.groupby(f2.Hour)['{}'.format(col)].count().plot()
    ax = f3.groupby(f3.Hour)['{}'.format(col)].count().plot()
    
    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend([f1_name,f2_name,f3_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

    if save == True:
        plt.savefig('{}.png'.format(title), dpi = 600, 
                transparent=True, 
                bbox_inches=None, pad_inches=0.1, frameon=False)
    plt.show()


def time_plot4d(f1,f1_name,f2,f2_name,f3,f3_name,f4,f4_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    ax = f2.groupby(f2.Hour)['{}'.format(col)].count().plot()
    ax = f3.groupby(f3.Hour)['{}'.format(col)].count().plot()
    ax = f4.groupby(f4.Hour)['{}'.format(col)].count().plot()
    
    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend([f1_name,f2_name,f3_name,f4_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    if save == True:
        plt.savefig('{}.png'.format(title), dpi = 600,
            transparent=True, 
                bbox_inches=None, pad_inches=0.1, frameon=False)
    plt.show()




def time_plot5d(f1,f1_name,f2,f2_name,f3,f3_name,f4,f4_name,f5,f5_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    ax = f2.groupby(f2.Hour)['{}'.format(col)].count().plot()
    ax = f3.groupby(f3.Hour)['{}'.format(col)].count().plot()
    ax = f4.groupby(f4.Hour)['{}'.format(col)].count().plot()
    ax = f5.groupby(f5.Hour)['{}'.format(col)].count().plot()
    
    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend([f1_name,f2_name,f3_name,f4_name,f5_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    if save == True:
        plt.savefig('{}.png'.format(title))
    plt.show()




def time_plot6d(f1,f1_name,f2,f2_name,f3,f3_name,f4,f4_name,f5,f5_name,f6,f6_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    ax = f2.groupby(f2.Hour)['{}'.format(col)].count().plot()
    ax = f3.groupby(f3.Hour)['{}'.format(col)].count().plot()
    ax = f4.groupby(f4.Hour)['{}'.format(col)].count().plot()
    ax = f5.groupby(f5.Hour)['{}'.format(col)].count().plot()
    ax = f6.groupby(f6.Hour)['{}'.format(col)].count().plot()
    
    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend([f1_name,f2_name,f3_name,f4_name,f5_name,f6_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    if save == True:
        plt.savefig('{}.png'.format(title))
    plt.show()



def time_plot7d(f1,f1_name,f2,f2_name,f3,f3_name,f4,f4_name,f5,f5_name,f6,f6_name,f7,f7_name,col,title,xlab,ylab,save=False):
    plt.figure(figsize = (15,5))
    ax = f1.groupby(f1.Hour)['{}'.format(col)].count().plot(xlim=(0,23))
    ax = f2.groupby(f2.Hour)['{}'.format(col)].count().plot()
    ax = f3.groupby(f3.Hour)['{}'.format(col)].count().plot()
    ax = f4.groupby(f4.Hour)['{}'.format(col)].count().plot()
    ax = f5.groupby(f5.Hour)['{}'.format(col)].count().plot()
    ax = f6.groupby(f6.Hour)['{}'.format(col)].count().plot()
    ax = f7.groupby(f7.Hour)['{}'.format(col)].count().plot()

    ax.set_xticks(np.arange(0, 24))

    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    plt.legend([f1_name,f2_name,f3_name,f4_name,f5_name,f6_name,f7_name],
    bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    if save == True:
        plt.savefig('{}.png'.format(title), dpi = 600, facecolor='w',
                edgecolor='w',transparent=True, 
                bbox_inches=None, pad_inches=0.1, frameon=False)
    plt.show()