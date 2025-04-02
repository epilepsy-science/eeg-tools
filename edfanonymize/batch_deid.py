import os
import shutil
import subprocess
import argparse

def find_edf_folders(input_dir):
    """Finds all folders containing .edf files."""
    edf_folders = set()
    for root, _, files in os.walk(input_dir):
        if any(file.lower().endswith(".edf") for file in files):
            edf_folders.add(root)
    return edf_folders

def copy_folder(src, dest):
    """Copies a folder and its contents to the destination."""
    dest_path = os.path.join(dest, os.path.basename(src))
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)  # Remove if it exists to ensure a clean copy
        print(src)
        print(dest_path)
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
        if file.lower().endswith(".edf"):
            file_path = os.path.join(folder, file)
            file_id = os.path.splitext(file)[0]  # Get filename without extension
            output_path = os.path.join(folder, file_id)
            cmd = [exe_path, file_path, output_path + "_deid.edf", file_id, file_id]
            # cmd =["./anonymizer", "./output/IN_001/IN_0001.edf", "./output/IN_001/IN_0001_deid.edf", "IN_0001", "IN_0001"]
            print(f"Running: {cmd}")
            subprocess.run(cmd, shell=False, check=True)

            os.remove(file_path)

def main(input_dir, output_dir, exe_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the output directory if it doesn't exist

    edf_folders = find_edf_folders(input_dir)
    print(f"Found {len(edf_folders)} folders containing EDF files.")
    
    for folder in edf_folders:
        copied_folder = copy_folder(folder, output_dir)
        rename_bdf_to_edf(copied_folder)
        process_edf_files(copied_folder, exe_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and process EDF files.")
    parser.add_argument("input_dir", help="Path to the input folder.")
    parser.add_argument("output_dir", help="Path to the output folder.")
    parser.add_argument("exe_path", help="Path to the application.exe.")
    
    args = parser.parse_args()
    main(args.input_dir, args.output_dir, args.exe_path)
