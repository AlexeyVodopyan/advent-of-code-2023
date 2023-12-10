def _max_color_multipliers(
        game_set: str,
        current_max_multipliers: dict[str, int]
) -> dict[str, int]:
    game_set = game_set.strip("\n")
    game_contains = game_set.split(", ")
    for cubes in game_contains:
        cube_count, cube_color = cubes.split(" ")
        current_max_multipliers[cube_color] = \
            max(
                current_max_multipliers[cube_color],
                int(cube_count)
            )
    return current_max_multipliers


def _power_set_of_game(
        game: str,
) -> int:
    game_sets = game.split("; ")

    color_power_set = {
        k: 1
        for k
        in {"red", "green", "blue"}
    }

    for game_set in game_sets:
        color_power_set = (
            _max_color_multipliers(game_set,
                                   color_power_set)
        )

    power_set = 1

    for val in color_power_set.values():
        power_set *= val

    return power_set


def sum_possible_power_sets(
        data: list[str],
) -> int:
    sum_of_power_sets = 0

    for _id, game in enumerate(data, start=1):
        game_string = game.split(f"Game {_id}: ")[1]
        sum_of_power_sets += _power_set_of_game(game_string)

    return sum_of_power_sets


if __name__ == "__main__":
    file_path = 'input.txt'

    with open(file_path) as f:
        data = f.readlines()

    print("Sum of power sets of the games: ",
          sum_possible_power_sets(data))
