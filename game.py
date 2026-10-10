
import random
from logic import feedback


DIFFICULTIES = {
    "1": ("Easy", 3, "1234", 10),
    "2": ("Medium", 4, "123456", 10),
    "3": ("Hard", 5, "12345678", 8),
}


class Mastermind:
    def __init__(self):
        self.code = ""
        self.history = []
        self.turns = 0
        self.game_over = False
        self.symbols = ""
        self.code_length = 0
        self.difficulty = ""

    def run(self):
        if self.game_over:
            print("This game has already ended.")
            return

        print("Choose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("Enter q to quit.")

        while True:
            choice = input("Difficulty > ").strip().lower()

            if choice == "q":
                self.game_over = True
                print("Game cancelled.")
                return

            if choice in DIFFICULTIES:
                break

            print("Invalid choice. Enter 1, 2, 3, or q.")

        self.difficulty, self.code_length, self.symbols, self.turns = (
            DIFFICULTIES[choice]
        )
        self.code = "".join(
            random.choice(self.symbols)
            for _ in range(self.code_length)
        )

        print(f"\n{self.difficulty}: guess {self.code_length} digits.")
        print(f"Allowed symbols: {self.symbols}")
        print(f"You have {self.turns} guesses. Enter q to quit.")

        while self.turns > 0:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                print("Game ended. Thanks for playing.")
                return

            if (
                len(raw) != self.code_length
                or any(symbol not in self.symbols for symbol in raw)
            ):
                print(
                    f"Invalid guess. Enter exactly {self.code_length} "
                    f"digits using only {self.symbols}."
                )
                continue

            exact, partial = feedback(self.code, raw)

            self.history.append((raw, exact, partial))
            self.turns -= 1

            print(f"Exact: {exact} | Partial: {partial}")
            print("Guess history:")

            for number, (guess, e, p) in enumerate(self.history, start=1):
                print(
                    f"{number}. Guess: {guess} | "
                    f"Exact: {e} | Partial: {p}"
                )

            if exact == self.code_length:
                self.game_over = True
                print("You cracked the code! You win!")
                return

        self.game_over = True
        print(f"No guesses left. You lose. The code was {self.code}.")
