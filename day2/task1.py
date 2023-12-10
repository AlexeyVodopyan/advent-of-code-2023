def _check_game_set_is_possible(
        game_set: str,
        bag_contains: dict[str, int]
) -> bool:
    game_set = game_set.strip("\n")
    game_contains = game_set.split(", ")

    for cubes in game_contains:
        cube_count, cube_color = cubes.split(" ")
        if int(cube_count) > bag_contains[cube_color]:
            return False
    return True


def _check_game_is_possible(
        game: str,
        bag_contains: dict[str, int]
) -> bool:
    game_sets = game.split("; ")

    for game_set in game_sets:
        if not _check_game_set_is_possible(game_set, bag_contains):
            return False
    else:
        return True


def sum_possible_game_ids(
        data: list[str],
        bag_contains: dict[str, int]
) -> int:
    id_sum = 0

    for _id, game in enumerate(data, start=1):
        game_string = game.split(f"Game {_id}: ")[1]
        if _check_game_is_possible(game_string, bag_contains):
            id_sum += _id

    return id_sum


if __name__ == "__main__":
    file_path = 'input.txt'

    with open(file_path) as f:
        data = f.readlines()

    bag_contains = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    print("Sum of possible game IDs: ",
          sum_possible_game_ids(data, bag_contains))
