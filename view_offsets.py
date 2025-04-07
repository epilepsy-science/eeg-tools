import sys
import pyedflib

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: fix_offsets.py <FILE_PATH>")
        return
    else:
        edf_path = args[0]

        with pyedflib.EdfReader(edf_path) as f:
            num_signals = f.signals_in_file
            for i in range(num_signals):
                ch_name = f.getLabel(i)
                offset = f.getPhysicalMaximum(i) - f.getPhysicalMinimum(i)  # Approximate check for scaling issues
                print(f"Channel: {ch_name}, Offset: {offset}")

main()
