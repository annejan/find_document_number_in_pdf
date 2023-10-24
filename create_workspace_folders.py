import csv
import os
import sys
import shutil
import glob


def main(csv_filepath):
    # Ensure 'workspaces' directory exists
    if not os.path.exists("workspaces"):
        os.makedirs("workspaces")

    with open(csv_filepath, mode="r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            folder_id = row["id"].zfill(
                3
            )  # Left-fill with 0's to ensure it's 3 chars long
            source_folder = row["folder"]

            # Create new folder inside 'workspaces' directory
            new_folder_path = os.path.join("workspaces", folder_id)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            # Check for the existence of 'pdfs.txt' in the source folder and copy if exists
            pdf_file_path = os.path.join(source_folder, "pdfs.txt")
            if os.path.exists(pdf_file_path):
                print(
                    f"Found 'pdfs.txt' in {source_folder}. Copying to {new_folder_path}..."
                )
                shutil.copy(pdf_file_path, new_folder_path)

            # Copy all .xlsx files from source folder to new folder
            xlsx_files = glob.glob(os.path.join(source_folder, "*.xlsx"))
            for xlsx_file in xlsx_files:
                print(f"Copying {xlsx_file} to {new_folder_path}...")
                shutil.copy(xlsx_file, new_folder_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_csv_file>")
        sys.exit(1)

    csv_filepath = sys.argv[1]
    main(csv_filepath)
