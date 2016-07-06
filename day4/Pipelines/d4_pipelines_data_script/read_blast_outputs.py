'''
Read blast output files and write to a new file the values 
in the first and the third columns just for the first line 
of each file.
'''

import subprocess

seqs = ['P00519', 'P05480', 'P12931']

'''
for seq in seqs:
    command_line = ['blastp','-query',
                    seq + '.fasta','-out',
                    seq + '_blout', '-outfmt', '6','-db','nr.00']
    subprocess.call(command_line)

'''

out = open('blast_best_scores', 'w')

for seq in seqs:
    first_line = open(seq + '_blout').readline()
    column = first_line.split()
    out.write(column[0] + '\t' + column[2] + '\n')

out.close()    

