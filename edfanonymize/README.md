# Updated instructions

## Overview
Works with EDF and BDF files (BDF file with a .edf extension)
[See EDF format](https://www.edfplus.info/specs/edf.html)
[See BDF Format](https://www.biosemi.com/faq/file_format.htm)
This script does two things:
- Replaces any patient information that sits in the first 176 bytes of the header
    - Replaces patient name with the file name
    - Also replaces any identifying subject ID with the file name
    - Changes the date to Jan 1st of the year of the recording.

## Building
Requirements: gcc
Run `gcc edf-anonymize.c -o edf-anonymize` to build the application for your platform. 

Usage example: `./edf-anonymize ./inputs/IN_001/IN_0001.edf ./temp/OUTPUT_001.edf FAKE_NAME FAKE_SUBJ_ID 04.01`
This will write the edf to an output folder with the name, subject ID and date replaced to FAKE_NAME, FAKE_SUBJ_ID, 04.01 respectively

# Batching
`batch_deid.sh` for *Nix environments
`batch_deid.py` for Windows and any other environment that can run python



# Original legacy intructions
I'm attaching the small c program that I use to de-identify def, edf+c and edf+d (I think) files called edf-anonymize.c.

Create a folder and name it EDFanonymize within your cygwin home directory. I think you can get to your cygwin home directory through: Computer (C:)/cygwin64/home/mia (or whatever your home directory is called)

Then open up cygwin from your desktop icon shortcut and type pwd (for print working directory) to make sure you're in your home directory. If not, please navigate there. CD into your EDFanonymize folder. 

Once there, compile the program. This only needs to be done once. Type:
gcc edf-anonymize.c -o edf-anonymize

When it's done compiling (you'll get your cursor back in the prompt), then you can type in the following to run the command:

./edf-anonymize path/to/identifiable.edf deidentified.edf SubjectNumber SubjectNumber

./edf-anonymize S:\EEG\ScanData\CBD_Data\MAR008_002\MAR008_02.edf MAR008_02_deid.edf MAR008-02 MAR008-02


Where idetifiable.edf is the name of the .edf file that has patient info, deidentified.edf is what you want to call the deidentified .edf file that you will upload to the portal, and SubjectNumber is the patient's subject number (it is needed twice). It can date shift as well but I left out those instructions as it's not needed.

deidentified.edf will be written the the edfanonymize folder. You can then move it to the upload folder. 

Let me know if you have questions or want me to help set this up.

Thanks,
Jacqueline
