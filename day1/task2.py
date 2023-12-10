def _find_valid_digit(string_with_digit: str, reverse: bool = False) -> str:
    valid_string_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    possible_string_digit = ""

    for char in string_with_digit[::-1] if reverse else string_with_digit:

        if char.isnumeric():
            value = char
            break
        else:
            if reverse:
                possible_string_digit = char + possible_string_digit
            else:
                possible_string_digit += char

            break_upper_loop = False

            for string_digit in valid_string_digits:
                if possible_string_digit in string_digit:
                    if possible_string_digit == string_digit:
                        break_upper_loop = True
                        value = valid_string_digits[string_digit]
                        break
                    else:
                        break
            else:
                if reverse:
                    possible_string_digit = possible_string_digit[:-1]
                else:
                    possible_string_digit = possible_string_digit[1:]

                if valid_string_digits.get(possible_string_digit):
                    # corner case: hcfssghtwonsjcdhbnfx42
                    value = valid_string_digits[possible_string_digit]
                    break

            if break_upper_loop:
                break

    return value


def extract_sum_calibration_val(data: list[str]) -> int:
    calibration_sum = 0

    for calibration_value in data:
        first_value = _find_valid_digit(calibration_value)
        last_value = _find_valid_digit(calibration_value, reverse=True)
        value = first_value + last_value

        calibration_sum += int(value)

    return calibration_sum


if __name__ == "__main__":
    file_path = 'input.txt'

    with open(file_path) as f:
        data = f.readlines()

    print("Sum of calibration values: ", extract_sum_calibration_val(data))
