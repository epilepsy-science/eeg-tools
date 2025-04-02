#!/bin/bash

#List all of the .edf files in current directory in a variable
edf_files=$(find Y:\SampleData_PREVeNT\UTH_PREVeNT\ -name *.edf)

#Print edfs filenames to screen
echo "EDF Files:"
echo $edf_files

#Loop through to anonymize edf files. edf-anonymize is a c-program downloaded from #Physionet. It take the file name, the output file name, and the subject number. It can #take more arguments but that's all it's being given here.
for i in $edf_files; do
    ./edf-anonymize "$i" "$(basename ${i} .edf)_deid.edf" UTH UTH
    #echo $i
done