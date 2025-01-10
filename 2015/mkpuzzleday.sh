#!/bin/sh

# Check if the correct number of arguments are provided
if [[ $# -ne 1]]; then
	echo "Usage: $0 <year><day> (e.g., 201502 for year 2015, day 02)"
	exit 1
fi

# Get the year and day from the argument
year_day=$1

# Chek if the input matches the format YYYYDD
if [[ ! $year_day =~ ^[0-9]{6}$ ]]; then
	echo "Invalid input. Please provide a valid year and day (e.g., 201502)"
	exit 1
fi

# Create the new folder based on the year and day
mkdir $year_day


# Copy and rename the files
cp template/aoc_template.py $year_day/aoc${year_day}.py
cp template/test_aoc_template.py $year_day/test_aoc${year_day}.py
touch $year_day/example1.txt $year_day/example2.txt $year_day/input.txt

# Confirm creation
echo "New folder and files created for $year_day"


