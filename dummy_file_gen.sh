#!/bin/bash
# generate a dummy file for testing
OUTFILE=$1
BLOCK=$2
COUNT=$3
if ()
BLOCK="1MB" # write block size MB or MiB
COUNT="5"   # no. of blocks to write
# size = BLOCK * COUNT
echo $BLOCK
echo $COUNT
dd if=/dev/zero of=test1.dat bs=$BLOCK count=$COUNT