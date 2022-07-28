import pandas as pd
import numpy as np
import missingno as mno
import os
import subprocess



def get_owid():
    ''' Getting data from git pull request, source code is being pulled first and shown as output.
        Result is stored in the csv structure 
    '''

    git_pull = subprocess.Popen("/usr/bin/git pull",
                                cwd=os.path.dirname('data/raw/covid-19-data'),
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    (out,error)= git_pull.communicate()

    print("Error:"+str(error))
    print("out:"+str(out))

    #path='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    #raw_list=pd.read_csv(path,sep=',')
    #df_country_list=raw_list.iloc[:,2::]


    if __name__=='__main__':
        get_owid()

