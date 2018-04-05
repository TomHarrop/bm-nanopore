#!/usr/bin/env bash

unicycler \
    --threads 30 \
    --min_fasta_length 10000 \
    -l output/reads/c_filtered.fq \
    -o output/unicycler_c \
    &> output/logs/unicycler_c.log \
    &

unicycler \
    --threads 30 \
    --min_fasta_length 10000 \
    -l output/reads/wt_filtered.fq \
    -o output/unicycler_wt \
    &> output/logs/unicycler_wt.log \
    &

wait
