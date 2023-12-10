def extract_sum_calibration_val(data: list[str]) -> int:
    calibration_sum = 0
    for calibration_value in data:
        value = ""
        for char in calibration_value:
            if char.isnumeric():
                value += char

        value = value[0] + value[-1]

        calibration_sum += int(value)
    return calibration_sum


if __name__ == "__main__":
    file_path = 'input.txt'

    with open(file_path) as f:
        data = f.readlines()

    print("Sum of calibration values: ",
          extract_sum_calibration_val(data))

