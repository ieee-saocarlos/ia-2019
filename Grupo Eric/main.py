import game
import menu
import over

def main():
    option = 'main_menu'

    while option is not 'exit':
        if option == 'main_menu':
            option = menu.menu_loop()
        if option == 'game':
            option = game.game_loop()
        if option == 'game_over':
            option = over.over_loop()


if __name__ == "__main__":
    main()
