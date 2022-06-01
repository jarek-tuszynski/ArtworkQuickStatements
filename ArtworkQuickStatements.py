# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:08:47 2022

@author: tuszynskij
"""

import pandas as pd
import urllib.parse


def main():
    in_fname  = 'ArtQS.txt'
    out_fname = 'ArtQS.xlsx'

    # read input file
    with open(in_fname) as f:
        lines = f.readlines()
    lines = lines[1:] # skip first line
    
    # parse the data, where each line is an URL
    qs_commands = []
    for line in lines:
        line = line.replace('https://quickstatements.toolforge.org/#/v1=','')
        line = line.replace('%7C','|').replace('\n','').replace('| ','|+')      

        for qs_command in line.split('#'):
            qs_command = urllib.parse.unquote(qs_command)
            qs_commands.append(qs_command.split('|'))
       
    # write output file 
    df = pd.DataFrame(qs_commands)
    df.drop_duplicates(inplace=True)
    df.to_excel(out_fname, index = False)

if __name__ == "__main__":
    main()
