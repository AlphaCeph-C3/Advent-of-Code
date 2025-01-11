import pathlib
import sys


def parse(puzzle_input):
    """Parse Input"""
    parsed_data = []
    list_of_dimensions = puzzle_input.split()
    for dimensions in list_of_dimensions:
        each_box_dimension = map(int, dimensions.split("x"))
        parsed_data.append(sorted(each_box_dimension))
    return parsed_data


def part1(data):
    """Solve for part 1."""
    total_wrapping_paper = 0
    # calculate the required sq ft of wrapping paper
    for box_dimension in data:
        l, w, h = box_dimension
        total_area_of_the_box = 2 * (l * w + w * h + h * l)
        slack_to_add = l * w
        # add it to the total_wrapping_paper
        total_wrapping_paper += total_area_of_the_box + slack_to_add
    return total_wrapping_paper


def part2(data):
    """Solve for part 2."""
    total_length_of_ribbon = 0
    # calculate the required feet of the ribbon
    for box_dimension in data:
        l, w, h = box_dimension
        smallest_perimeter_of_box = 2 * (l + w)
        feet_required_for_bow = l * w * h
        # add the total feet of ribbon required for the ribbon
        total_length_of_ribbon += smallest_perimeter_of_box + feet_required_for_bow
    return total_length_of_ribbon


def solve(puzzle_input):
    """Solve the puzzle for the given input."""

    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_files>")
        sys.exit(1)
    for path in sys.argv[1:]:
        print(f"\nProcessing {path}:")
        try:
            puzzle_input = pathlib.Path(path).read_text().strip()
            solutions = solve(puzzle_input)
            print("\n".join(str(solution) for solution in solutions))
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
