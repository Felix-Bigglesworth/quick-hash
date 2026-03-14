#!/bin/bash

# This script generates a dummy data for testing
# File data is from '/dev/zero' so all files with the same size will have the same hash
# Enable RANDOM_DATA to write random data from '/dev/urandom'

# Initialize defaults
RANDOM_DATA=0              # Set to 1 to enable random data
BLOCK_SIZE='1MB'
BLOCK_COUNT=10
DATA_SRC='/dev/zero'

# HELP TEXT
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "This script creates a dummy file with a random name for testing purposes"
    echo "The file size is equal to BLOCK_COUNT in Megabytes"
    echo "example:" 
	echo "./dummy_data.sh [BLOCK_COUNT]"
    exit 0
fi

# handle arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -r)
            # enable random data
            RANDOM_DATA=1
            shift 1
            ;;
        #-b)
            # declare block size
            #declare BLOCK_SIZE="$2"
            #shift 2
            #;;
        *)
            # handle positional args
            if [[ -n "$1" ]]; then BLOCK_COUNT="$1"; fi
            shift 1
            ;;
    esac
done

# Define Functions
generate_name() {
    # Returns a unique file name in the format `file_#.dat` starting at 1
    # (eg. file_1.dat, file_2.dat, ..., file_N.dat)

    # initialize variables
    declare -i NUM
    BASE='file_'
    NUM=1
    EXT='.dat'

    # Increment by 1 for each existing file
    while [[ -f "${BASE}${NUM}${EXT}" ]]; do
        NUM+=1
    done
    
	#Return file name
    local OUT_FILE="${BASE}${NUM}${EXT}"
    echo "$OUT_FILE"
}

# ---- START MAIN SCRIPT ----

if [[ RANDOM_DATA -eq 1 ]]; then 
    DATA_SRC='/dev/urandom'; fi
echo "Input data is from: ${DATA_SRC}"

# Generate file name
OUT_FILE="$(generate_name)"
echo "output file: ${OUT_FILE}"
dd if=$DATA_SRC of=$OUT_FILE bs=$BLOCK_SIZE count=$BLOCK_COUNT

