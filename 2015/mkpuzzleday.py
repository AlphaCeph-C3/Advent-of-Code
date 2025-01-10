#! /usr/bin/env python
import os
import shutil
import sys


# function to create a generic test_aoc_template file and modify the contents
def create_test_file(input_name, year, day):
    read_file = "template/test_aoc_template.py"
    write_file = f"{input_name}/test_aoc{year}{day}.py"
    replace_word = f"aoc{year}{day}"

    with open(read_file, "r") as file:
        initial_contents = file.read()

        updated_contents = initial_contents.replace("aoc_template", replace_word, 1)

    with open(write_file, "w") as file:
        file.write(updated_contents)


# Function to create the puzzle directory
def create_puzzle_directory(input_name):
    year = 2015
    day = input_name[:2]

    # create the parent folder first
    os.makedirs(input_name, exist_ok=True)

    # list of files to copy and their new names
    files = (
        ("aoc_template.py", f"aoc{year}{day}.py"),
        ("example1.txt", "example1.txt"),
        ("example2.txt", "example2.txt"),
        ("test_input.txt", "input.txt"),
    )

    # Create the files in the newly created parent directory
    for src, dest in files:
        shutil.copy(os.path.join("template", src), os.path.join(input_name, dest))

    create_test_file(input_name, year, day)
    print(f"New folder and files created for day: {input_name}")


# Main Function
def main():
    # Check if the arguments are passed
    if len(sys.argv) != 2:
        print(
            "Usage: python create_puzzle.py <folder_name_with_day_no_preceding> (e.g., for day 02 write 02_santa_rescue)"
        )
        sys.exit(1)

    input_name = sys.argv[1]

    # Create the puzzle directory and files
    create_puzzle_directory(input_name)


if __name__ == "__main__":
    main()
