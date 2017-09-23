import game_input

def reset_workers():
    game_input.open_menu()
    game_input.left_click(game_input.COORDINATES.get("worker_button"))
    game_input.left_click(game_input.COORDINATES.get("recover_button"))
    game_input.left_click(game_input.COORDINATES.get("confirm_recover_button"))
    game_input.left_click(game_input.COORDINATES.get("repeat_all_button"))
    game_input.close_menu()
