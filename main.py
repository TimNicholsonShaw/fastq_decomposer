import sys
import csv
import xlrd
from Bio import SeqIO
import gzip

#####################################################################
if __name__=="__main__":
    help = """
    -m: Manifest location
    -r1: read 1 location. Fastq format, can be gz compressed or not
    -r2: read 2 location. Fastq format, can be gq compressed or not
    -o: Folder to output files into
    """

    header = True  #default value
    outFolder = ""
    for x in range(0, len(sys.argv)):
        if sys.argv[x] == '-r1': r1Loc = sys.argv[x+1]
        if sys.argv[x] == '-r2': r2Loc = sys.argv[x+1]
        if sys.argv[x] == '-m' : manifestLoc = sys.argv[x+1]
        if sys.argv[x] == '-o' : outFolder = sys.argv[x+1]
        if sys.argv[x] == '-H': header = False
        if sys.argv[x] == '-h': print(help);sys.exit()


    manifest = []

    if manifestLoc.endswith("csv"):
        with open(manifestLoc) as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0] == "sampleID":
                    continue
                else:
                    manifest.append(line[0], line[2]+line[3])
    else:
        sheet = xlrd.open_workbook(manifestLoc).sheet_by_index(0)
        for i in range(header,sheet.nrows):
            manifest.append([sheet.cell_value(i,0),sheet.cell_value(i,2).rstrip() + sheet.cell_value(i,3).rstrip()])

    r1 = list(SeqIO.parse(gzip.open(r1Loc,'rt'),'fastq'))
    r2= list(SeqIO.parse(gzip.open(r2Loc,'rt'),'fastq'))
    assert len(r1) == len(r2)

    for line in manifest:
        r1_out = []
        r2_out = []
        name = line[0]
        barcode = line[1]
        for i in range(len(r1)):
            if r1[i].seq[:len(barcode)] == barcode:
                r1_out.append(r1[i])
                r2_out.append(r2[i])
        print(str(name) +": "+ str(len(r1_out)))
        SeqIO.write(r1_out,outFolder+name+"_r1.fastq",'fastq')
        SeqIO.write(r2_out, outFolder+name + "_r2.fastq", 'fastq')











