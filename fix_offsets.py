import mne
import sys

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: fix_offsets.py <FILE_PATH>")
        return
    else:
        raw = mne.io.read_raw_edf(args[0], preload=True)

        # Normalize offsets by setting the physical min/max of all channels to be the same
        for ch in raw.ch_names:
            raw.set_channel_types({ch: "eeg"})  # Adjust if necessary

        # Save as a new EDF
        raw.export("normalized_file_new.edf", overwrite=True)
