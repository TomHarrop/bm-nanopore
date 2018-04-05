#!/usr/bin/env bash

canu \
    maxThreads=30 \
    -d output/canu_wt \
    -p wt \
    genomeSize=13k \
    corOutCoverage=1000 \
    -nanopore-raw \
    output/reads/wt_filtered.fq \
    &> output/logs/canu_wt.log &

canu \
    maxThreads=30 \
    -d output/canu_c \
    -p c \
    genomeSize=13k \
    corOutCoverage=1000 \
    -nanopore-raw \
    output/reads/c_filtered.fq \
    &> output/logs/canu_c.log &

wait
