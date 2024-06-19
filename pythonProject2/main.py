import random
import tkinter as tk
from tkinter import messagebox

# Kolory do wyboru
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
code = []
statistics = []


def motivation():

    mot = [
        'Never give up', 'If you work, it will work.', 'Prove them wrong',
        'No pain, no gain', 'Different doesn’t mean wrong (here it does though)',
        'Everything you can imagine is real.',
        'Wisdom comes only through suffering',
        'The best way out is always through', 'Slow and steady wins the race.'
    ]

    messagebox.showinfo("motivation", random.choice(mot))


def stat(correct):
    proc = (correct / 4) * 100
    return proc


# Funkcja generująca kod, który gracz musi odgadnąć
def generate_code():
    return [random.choice(COLORS) for _ in range(4)]


# Funkcja sprawdzająca ilość trafień
def check_guess(code, guess):
    correct = 0
    for i in range(4):
        if code[i] == guess[i]:
            correct += 1
    return correct


# Funkcja wyświetlająca wynik gry
def show_result(guesses, result):
    result_window = tk.Toplevel()
    result_window.title("Resuly")
    result_window.geometry("400x250")
    tk.Label(result_window, text=f"Number of tries: {guesses}").pack()
    tk.Label(result_window, text=result).pack()
    tk.Button(result_window, text="Close", command=result_window.destroy).pack()


# Funkcja grająca w grę Mastermind
def play_game():

    code = generate_code()
    guesses = 0
    messagebox.showinfo("Game rules",
                        "The player's task is to guess four colors out of six. After each attempt, they receive information about whether the given colors are in the correct, wrong position, or not present at all. The game ends only with a win by guessing all four positions. You never lose! On the easy level, the colors in the code do not repeat, whereas on the hard level, they do.")
    messagebox.showinfo("KEY", "KEY: \n :( - wrong guess \n :0 - wrong position \n :) - u got this one right")

    def select_level():
        tk.Tk().iconify()
        level_window = tk.Toplevel()
        level_window.title("Choose level")
        level_window.geometry("400x350")

        def select_hard():
            code = [
                random.choice(COLORS),
                random.choice(COLORS),
                random.choice(COLORS),
                random.choice(COLORS)
            ]
            level_window.destroy()
            game_window.deiconify()

        def select_easy():
            for i in range(0, 4):
                code[i] = random.choice(COLORS)
                COLORS.remove(code[i])

                level_window.destroy()
                game_window.deiconify()

        tk.Label(level_window, text="Choose level").pack()
        tk.Button(level_window, text="Easy", command=select_easy).pack(pady=10)
        tk.Button(level_window, text="Difficult", command=select_hard).pack()

    def check_code():

        pom = 1
        guess = 0
        nonlocal guesses

        guess = [color_choice.get() for color_choice in color_choices]
        guesses += 1
        correct = check_guess(code, guess)
        if correct == 4:
            show_result(guesses, "Congratulations! You won!")
            game_window.destroy()
        else:
            result_text = " ".join([f"{color} - :)  " if code[i] == color
                                    else f"{color} - :0"
            if color in code
            else f"{color} - :("
                                    for i, color in enumerate(guess)])
            proc = (correct / 4) * 100
            proc_str = int(proc)
            result_text = result_text + "\nPercentage of correct answers: " + str(proc_str) + " %\n"
            result_label.config(text=result_text)
            result_text = result_text + "Statistics:"
            result_label.config(text=result_text)

            motivation()
            statistics.append(proc_str)

            for i in range(0, guesses):
                result_text = result_text + " " + str(statistics[i]) + " %,"
                result_label.config(text=result_text)

    # Okno wyboru poziomu trudności
    select_level()

    # Okno gry
    game_window = tk.Toplevel()
    game_window.title("Mastermind")
    game_window.geometry("400x350")
    tk.Label(game_window, text="Good luck!").pack()
    game_window.iconify()

    # Pole wyboru kolorów
    color_choices = [tk.StringVar(game_window) for _ in range(4)]
    color_frames = [tk.Frame(game_window) for _ in range(4)]
    for i, color_frame in enumerate(color_frames):
        for color in COLORS:
            tk.Radiobutton(color_frame, variable=color_choices[i], value=color, bg=color, indicatoron=0,
                           width=5).pack(side="left", padx=2)
        color_frame.pack(pady=5)

    check_button = tk.Button(game_window, text="Check!", command=check_code)
    check_button.pack(pady=10)

    # Wynik
    result_label = tk.Label(game_window, text="")
    result_label.pack(pady=10)

    game_window.mainloop()


if __name__ == '__main__':
    play_game()