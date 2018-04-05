#!/usr/bin/env python3

from Bio import SeqIO
import gzip


#############
# FUNCTIONS #
#############

def filter_reads_by_length(read_file, start_len, stop_len):
    with gzip.open(read_file, 'rt') as handle:
        return list(x for x in SeqIO.parse(handle, 'fastq-sanger')
                    if (len(x) > start_len and len(x) < stop_len))


###########
# GLOBALS #
###########

wt_read_file = 'data/bm-wt/merged/merged_sorted.fq.gz'
wt_filtered = 'output/reads/wt_filtered.fq'

c_read_file = 'data/bm-c/merged/merged_sorted.fq.gz'
c_filtered = 'output/reads/c_filtered.fq'

########
# MAIN #
########

wt_reads = filter_reads_by_length(wt_read_file, 12000, 14001)
c_reads = filter_reads_by_length(c_read_file, 12000, 14001)

SeqIO.write(wt_reads, wt_filtered, 'fastq-sanger')
SeqIO.write(c_reads, c_filtered, 'fastq-sanger')
