# %% IMPORTS
import glob
import time
import pandas as pd
import ts_models as tsm
import multiprocessing
from ts_models import worker
from pathlib import Path


def  load_data():
    
    input_dir = r'data/input/'
    input_cache = input_dir + 'cache_input.ftr'

    print('Loading data...', end='')
    if not Path(input_cache).is_file():
        data_files = glob.glob( input_dir + "*.ftr")
        dfs = []
        [ dfs.append(pd.read_feather(filename)) for filename in data_files ]
        df = pd.concat(dfs, axis=0, ignore_index=True)  
        df.to_feather(input_cache)

    print('done!')
    return pd.read_feather(input_cache)    
    

def main():
    
    # LOAD INPUT DATA
    df = load_data()

    # CALCULATE THE MODLES (MULTIPROCESSING IMPLEMENATION)
    models = [
        'm1'
        , 'm2'
        , 'm3'
        , 'm4'
    ]

    jobs = []
    for i in range( len(models) ):
        
        # Remember also that non-daemonic processes will be automatically be joined.
        p = multiprocessing.Process(target=worker, args=(df, models[i], ))        
        p.daemon = True

        jobs.append(p)
        p.start()

    # CONTINUE WITH A SINGLE PROCESS TO EVALUATE THE ENCAPSULATED/INDEPENDENT RESULTS
    
    # e.g. load data from disk (storing / reading from disk from time to time is recommend for long running jobs)
    # add some "check if file exists" like in load_data() to be able to continue if a runtime crash occured


if __name__ == '__main__':
    main()

# %%
