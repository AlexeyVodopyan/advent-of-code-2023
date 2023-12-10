def _card_score(
        card: str,
) -> int:
    # split sets of numbers
    winning_string, string_you_have = card.split(" | ")
    winning_numbers = winning_string.split(" ")
    numbers_you_have = string_you_have.split(" ")

    times_matches = -1
    for number in numbers_you_have:
        if number == "":
            continue
        if number in winning_numbers:
            times_matches += 1
    return 2 ** times_matches if times_matches >= 0 else 0


def sum_card_points(
        data: list[str],
) -> int:
    sum_of_cards = 0

    for card in data:
        card_string = card.split(f": ")[1]
        sum_of_cards += _card_score(card_string)

    return sum_of_cards


if __name__ == "__main__":
    file_path = 'input.txt'

    with open(file_path) as f:
        data = f.readlines()

    # clean data
    for i in range(len(data)):
        data[i] = data[i].strip("\n")

    print("Sum of point of cards: ",
          sum_card_points(data))
