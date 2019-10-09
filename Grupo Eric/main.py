import game
import menu
import over
import instruction


def main():
    option = 'main_menu'

    while option is not 'exit':
        if option == 'main_menu':
            option = menu.menu_loop()
        elif option == 'game':
            option = game.game_loop()
        elif option == 'instruction':
            option = instruction.instruction_loop()
        else:
            option = over.over_loop()


if __name__ == "__main__":
    main()
