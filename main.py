from termcolor import colored

class Game():
    def __init__(self) -> None:
        self.running = True

        self.commands = {
        "exit": self.exit,
        "help": self.help,
        }

    def help(self) -> None:
        print("""
help

commands:
help: show this prompt
exit: exit the menu

        """)

    def exit(self) -> None:
        self.running = False

    def main_menu(self) -> None:
        print('\n')
        inp = input("-> ")

        if inp in self.commands:
            self.commands[inp]()
        else:
            print("that command doesnt exist, please try again...")

    def run(self) -> None:
        while self.running:
            self.main_menu()

if __name__ == "__main__":
    game = Game()
    game.run()
