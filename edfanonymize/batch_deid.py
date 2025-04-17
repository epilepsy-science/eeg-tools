import os
import shutil
import subprocess
import argparse

def find_eeg_folders(input_dir):
    """Finds all folders containing .edf or .bdf files."""
    edf_folders = set()
    for root, _, files in os.walk(input_dir):
        print(f"Checking {root} with files: {files}")
        for file in files:
            if file.lower().endswith((".edf", ".bdf")):
                print(f"Matched EEG file: {file} in {root}")
                edf_folders.add(root)
                break
    return edf_folders

def copy_folder(src, dest, input_dir):
    """Copies a folder and its contents to the destination."""
    rel_path = os.path.relpath(src, input_dir)
    if rel_path == ".":
        rel_path = os.path.basename(src)

    dest_path = os.path.join(dest, rel_path)
    
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
        print(f"Overwriting: {dest_path}")
        
    shutil.copytree(src, dest_path)
    return dest_path

def rename_bdf_to_edf(folder):
    """Renames all .bdf files to .edf in the given folder."""
    for file in os.listdir(folder):
        if file.lower().endswith(".bdf"):
            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, os.path.splitext(file)[0] + ".edf")
            os.rename(old_path, new_path)

def process_edf_files(folder, exe_path):
    """Runs application.exe on all .edf files in the folder."""
    for file in os.listdir(folder):
        if file.lower().endswith((".edf", ".bdf")):
            file_path = os.path.join(folder, file)
            file_id = os.path.splitext(file)[0]
            output_path = os.path.join(folder, file_id)
            cmd = [exe_path, file_path, output_path + "_deid.edf", file_id, file_id]
            print(f"Running: {cmd}")
            subprocess.run(cmd, shell=False, check=True)
            os.remove(file_path)

def main(input_dir, output_dir, exe_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    edf_folders = find_eeg_folders(input_dir)
    print(f"Found {len(edf_folders)} folders containing EDF/BDF files.")
    
    for folder in edf_folders:
        copied_folder = copy_folder(folder, output_dir, input_dir)
        process_edf_files(copied_folder, exe_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and process EDF/BDF files.")
    parser.add_argument("--input_dir", default="/app/input", help="Path to the input folder.")
    parser.add_argument("--output_dir", default="/app/output", help="Path to the output folder.")
    parser.add_argument("exe_path", default="edf-anonymize",  help="Path to the anonymizer")
    
    args = parser.parse_args()
    main(args.input_dir, args.output_dir, args.exe_path)
