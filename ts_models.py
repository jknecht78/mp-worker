import multiprocessing

def worker(_df, _model):

    def pseudo(_df, _model):
        # simulating CPU LOAD
        x = 0
        for i in range(0, 10**5):
            x += x + i

        df_ = _df
        df_['model'] = _model 

        # storing results to disk just to be on the safe side
        filename = r'data/output/' + f"{_model}.ftr"
        df_.to_feather(filename)
        return _df


    def m1(_df, _model):
        #TODO REPLACE PSEUDO BY MODEL
        df_ = pseudo(_df, _model)
        return df_


    def m2(_df, _model):
        #TODO REPLACE PSEUDO BY MODEL
        df_ = pseudo(_df, _model)
        return df_


    def m3(_df, _model):
        #TODO REPLACE PSEUDO BY MODEL
        df_ = pseudo(_df, _model)
        return df_


    def m4(_df, _model):
        #TODO REPLACE PSEUDO BY MODEL
        df_ = pseudo(_df, _model)
        return df_


    name = multiprocessing.current_process().name
    print(f'{name} - starting')

    if _model == 'm1':
        return m1(_df, _model)

    elif _model == 'm1':
        return m2(_df, _model)

    elif _model == 'm2':
        return m3(_df, _model)

    elif _model == 'm3':
        return m4(_df, _model)


    elif _model == 'm4':    
        return m4(_df, _model)

    else:        
        exit('Error: Unkown model')