def sum_part_numbers(
        data: list[str]
) -> int:
    part_numbers_sum = 0

    prev_line_symbol_positions = set()
    prev_line_number_positions = dict()

    for row_number, row in enumerate(data):
        current_line_symbol_positions = set()
        current_line_number_positions = dict()

        possible_number = ""
        possible_number_starts_with_symbol = False
        possible_symbol_positions = set()

        for i, char in enumerate(row):

            # fill current line candidates
            if char.isdigit():
                if not possible_number and i != 0:
                    possible_symbol_positions.add(i - 1)

                    if row[i - 1] != ".":
                        possible_number_starts_with_symbol = True

                possible_number += char
                possible_symbol_positions.add(i)
            else:
                if possible_number:
                    possible_symbol_positions.add(i)
                    # check if number intersect with previous line symbols

                    if (
                            not prev_line_symbol_positions.intersection(
                                possible_symbol_positions) and not
                    possible_number_starts_with_symbol
                            and char == "."
                    ):
                        current_line_number_positions[
                            possible_number] = possible_symbol_positions
                    else:
                        part_numbers_sum += int(possible_number)

                    possible_number_starts_with_symbol = False
                    possible_number = ""
                    possible_symbol_positions = set()

                if char != ".":
                    current_line_symbol_positions.add(i)

        # check corner case if line ends with number
        if possible_number:
            if (
                    not prev_line_symbol_positions.intersection(
                        possible_symbol_positions) and not
            possible_number_starts_with_symbol
            ):
                current_line_number_positions[
                    possible_number] = possible_symbol_positions
            else:
                part_numbers_sum += int(possible_number)

        # check if previous line numbers intersect with current line symbols
        for number in prev_line_number_positions:
            if prev_line_number_positions[number].intersection(
                    current_line_symbol_positions):
                part_numbers_sum += int(number)

        prev_line_symbol_positions = current_line_symbol_positions
        prev_line_number_positions = current_line_number_positions

    return part_numbers_sum


if __name__ == "__main__":
    file_path = 'input.txt'

    with open(file_path) as f:
        data = f.readlines()

    # clean data
    for i in range(len(data)):
        data[i] = data[i].strip("\n")

    print("Sum of part numbers: ",
          sum_part_numbers(data))
