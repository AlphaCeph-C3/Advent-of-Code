import os
import shutil
import sys


# Function to create the puzzle directory
def create_puzzle_directory(year_day):
    day = year_day[-2:]

    # create the parent folder first
    os.makedirs(day, exist_ok=True)

    # list of files to copy and their new names
    files = (
        ("aoc_template.py", f"aoc{year_day}.py"),
        ("test_aoc_template.py", f"test_aoc{year_day}.py"),
        ("example1.txt", "example1.txt"),
        ("example2.txt", "example2.txt"),
        ("test_input.txt", "input.txt"),
    )

    # Create the files in the newly created parent directory
    for src, dest in files:
        shutil.copy(os.path.join("template", src), os.path.join(day, dest))

    print(f"New folder and files created for day: {day}")


# Main Function
def main():
    # Check if the arguments are passed
    if len(sys.argv) != 2:
        print(
            "Usage: python create_puzzle.py <year><day> (e.g., 201502 for year 2015, day 02)"
        )
        sys.exit(1)

    year_day = sys.argv[1]

    if not year_day.isdigit() and len(year_day) != 6:
        print("Invalid input. Please provide a valid year and day (e.g., 201502)")
        sys.exit(1)

    # Create the puzzle directory and files
    create_puzzle_directory(year_day)


if __name__ == "__main__":
    main()
