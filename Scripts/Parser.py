__author__ = 'Ben'

import re

def methylation():
    gene_bvalue = {}

    with open('meth.txt', 'r') as file:
        line_count = 0

        for line in file:

            if(line_count <= 1):
                line_count += 1
                continue

            temp = line.split()
            bvalue = temp[1]
            gene = temp[2]

            if(bvalue == 'NA' or gene == 'NA' or gene == '' or ';' in gene):
                continue

            bvalue = float(bvalue)

            gene_bvalue.setdefault(gene, bvalue)

def RNASeq():
    gene_rpkm = {}

    with open('rna_seq.txt', 'r') as file:
        line_count = 0

        for line in file:

            if(line_count == 0):
                line_count += 1
                continue

            temp = line.split()
            rpkm = temp[3]
            temp2 = re.findall(r"[\w]+", temp[0])
            gene = temp2[0]

            if 'calculated' in gene:
                continue

            rpkm = float(rpkm)

            gene_rpkm.setdefault(gene, rpkm)



def mutation():
    mutated_gene = []
    with open('mutation.maf', 'r') as file:
        line_count = 0

        for line in file:

            if(line_count == 0):
                line_count += 1
                continue

            temp = line.split()

            if('Silent' in temp[8]):
                continue

            gene = temp[0]

            mutated_gene.append(gene)


def clinical():

    with open('clinical.txt' 'r') as file:
        line_count = 0

        for line in file:

            if(line_count <= 1):
                line_count += 1
                continue

            temp = line.split()
            status = temp[15]

            if('Dead' in status):
                time = temp[17]
            else:
                time = temp[16]