#!/bin/bash

# This script generates a dummy data for testing
# File data is from '/dev/zero' so all files with the same size will have the same hash
# Enable RANDOM_DATA to write random data from '/dev/urandom'

RANDOM_DATA=0              # Set to 1 to enable random data
BLOCK_SIZE='1MB'
BLOCK_COUNT=100
DATA_SRC='/dev/zero'


if [[ RANDOM_DATA -eq 1 ]]; then DATA_SRC='/dev/urandom'
echo "Input data is from: ${DATA_SRC}"

# HELP ARGUMENTS
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "This script creates a dummy file with a random name for testing purposes"
    echo "The file size is equal to BLOCK_COUNT in Megabytes"
    echo "example: $> ./dummy_data.sh [BLOCK_COUNT]"
    echo "   
    exit 0
fi

if [[ - "$1" ]]


generate_name() {
    # Returns a unique file name in the format `file_#.dat` starting at 1
    # (eg. file_1.dat, file_2.dat, ..., file_N.dat)

    # initialize variables
    declare -i NUM
    BASE='file'
    NUM=1
    EXT='.dat'

    # Increment by 1 for each existing file
    while [[ -f "${BASE}${NUM}${EXT}" ]]; do
        NUM+=1
    done

    local OUT_FILE="${BASE}${NUM}${EXT}"
    echo "$OUT_FILE"
}

OUT_FILE=$(generate_name)

echo "dd if=$DATA_SRC of=$OUT_FILE bs=$BLOCK_SIZE count=$BLOCK_COUNT"
