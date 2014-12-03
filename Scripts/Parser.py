__author__ = 'Ben'

import re
import pickle


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


def mutation2():
    patient_gene = {}

    with open('mutation.maf', 'r') as file:
        line_count = 0

        for line in file:

            if(line_count == 0):
                line_count += 1
                continue

            temp = line.split()

            if('Silent' in temp[8]):
                continue
            else:
                gene = temp[0]
                patient = temp[15].split('-')[2]

            if patient not in patient_gene:
                patient_gene.setdefault(patient, []).append(gene)
            elif gene not in patient_gene[patient]:
                patient_gene[patient].append(gene)




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



def clinical2():
    patient_clinical = {}

    with open('clinical.txt', 'r') as file:
        for line in file:

            temp = line.split('\t')
            pat_id = temp[0].split('-')[2]
            status = temp[1]

            if 'Dead' in status and '[Not Available]' not in temp[3]:
                try:
                    time = int(temp[3].rstrip())
                    patient_clinical.setdefault(pat_id, []).append(time)
                    patient_clinical[pat_id].append(0)
                except AttributeError:
                    print(pat_id)
                    print(status)
            elif 'Alive' in status and '[Not Available]' not in temp[2]:
                time = int(temp[2].rstrip())
                patient_clinical.setdefault(pat_id, []).append(time)
                patient_clinical[pat_id].append(1)
            else:
                continue



    fp = open('clinical.pkl', 'wb')
    pickle.dump(patient_clinical, fp)
    fp.close()


clinical2()

