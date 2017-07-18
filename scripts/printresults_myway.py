#!/usr/bin/env python
"""Print data from a resultset to the standard output.

Usage:
    python printresults.py <results-file.pickle>
"""
import argparse
from icarus.registry import RESULTS_READER

__all__ = ['print_results']

read = RESULTS_READER['PICKLE']

garr06 =    open('./GARR_06.csv' ,  'a')
garr08 =    open('./GARR_08.csv' ,  'a')
garr10 =    open('./GARR_10.csv' ,  'a')
wide06 =    open('./WIDE_06.csv' ,  'a')
wide08 =    open('./WIDE_08.csv' ,  'a')
wide10 =    open('./WIDE_10.csv' ,  'a')
geant06 =   open('./GEANT_06.csv' , 'a')
geant08 =   open('./GEANT_08.csv' , 'a')
geant10 =   open('./GEANT_10.csv' , 'a')
tiscali06 = open('./TISCALI_06.csv' , 'a')
tiscali08 = open('./TISCALI_08.csv' , 'a')
tiscali10 = open('./TISCALI_10.csv' , 'a')


def print_results(path):
    """Print a resultset saved as pickle.
    
    Parameters
    ----------
    input : str
        The path to the pickled resultset
    """
    rs = read(path)
    n = len(rs)
    i = 0
    exp = {}
    for experiment, results in rs:
        i += 1
        #print("EXPERIMENT %d/%d:" % (i, n)) 
        #print("  CONFIGURATION:")
        topology = experiment['topology']['name']
        alpha = experiment['workload']['alpha']
        strategy = experiment['strategy']['name']
        cache_size = experiment['cache_placement']['network_cache']
        cache_policy = experiment['cache_policy']['name']

        latency = results['LATENCY']['MEAN']
        intload = results['LINK_LOAD']['MEAN_INTERNAL']
        extload = results['LINK_LOAD']['MEAN_EXTERNAL']
        hitratio = results['CACHE_HIT_RATIO']['MEAN']
        pathstretch = results['PATH_STRETCH']['MEAN']

        exp[i] = {'topology': topology, 
                'alpha' : alpha,
                'strategy' : strategy,
                'cache_size' : cache_size,
                'cache_policy' : cache_policy, 
                'latency' : latency,
                'intload' : intload,
                'extload' : extload,
                'hitratio' : hitratio,
                'pathstretch' : pathstretch}
    for x in exp:
        if exp[x]['topology'] == 'GEANT':
            if exp[x]['alpha'] == 0.6:
                geant06.write(str(exp[x]['cache_policy']) + '-'
                        + str(exp[x]['strategy']) + '-'
                        + str(exp[x]['cache_size']) +'\n')
                geant06.write(str(exp[x]['hitratio']) + ' '
                        + str(exp[x]['pathstretch']) + ' '
                        + str(exp[x]['latency']) + ' '
                        + str(exp[x]['intload']) + ' '
                        + str(exp[x]['extload']) +'\n\n')
            elif exp[x]['alpha'] == 0.8:
                geant08.write(str(exp[x]['cache_policy']) + '-'
                        + str(exp[x]['strategy']) + '-'
                        + str(exp[x]['cache_size']) +'\n')
                geant08.write(str(exp[x]['hitratio']) + ' '
                        + str(exp[x]['pathstretch']) + ' '
                        + str(exp[x]['latency']) + ' '
                        + str(exp[x]['intload']) + ' '
                        + str(exp[x]['extload']) +'\n\n')
            elif exp[x]['alpha'] == 1.0:
                geant10.write(str(exp[x]['cache_policy']) + '-'
                        + str(exp[x]['strategy']) + '-'
                        + str(exp[x]['cache_size']) +'\n')
                geant10.write(str(exp[x]['hitratio']) + ' '
                        + str(exp[x]['pathstretch']) + ' '
                        + str(exp[x]['latency']) + ' '
                        + str(exp[x]['intload']) + ' '
                        + str(exp[x]['extload']) +'\n\n')
'''
        elif exp[x]['topology'] == 'GARR':
            if exp[x]['alpha'] == 0.6:
                print 'writing, ', exp[x]['latency']
                garr06.write(str(exp[x]))
            elif exp[x]['alpha'] == 0.8:
                garr08.write(exp[x])
            elif exp[x]['alpha'] == 1.0:
                garr10.write(exp[x])
            garr10.write("")

        elif exp[x]['topology'] == 'WIDE':
            if exp[x]['alpha'] == 0.6:
                wide06.write(exp[x])
            elif exp[x]['alpha'] == '0.8':
                wide08.write(exp[x])
            elif exp[x]['alpha'] == '1.0':
                wide10.write(exp[x])
            wide10.write("")

        elif exp[x]['topology'] == 'TISCALI':
            if exp[x]['alpha'] == '0.6':
                tiscali06.write(exp[x])
            elif exp[x]['alpha'] == '0.8':
                tiscali08.write(exp[x])
            elif exp[x]['alpha'] == '1.0':
                tiscali10.write(exp[x])
            tiscali10.write("")
            '''

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="The simulation results file")
    args = parser.parse_args()
    print_results(args.input)
    garr06.close()
    garr08.close()
    garr10.close()
    wide06.close()
    wide08.close()
    wide10.close()
    geant06.close()
    geant08.close()
    geant10.close()
    tiscali06.close()  
    tiscali08.close()
    tiscali10.close()






if __name__ == "__main__":
    main()
