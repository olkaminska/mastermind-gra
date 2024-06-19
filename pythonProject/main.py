import random
from tkinter import filedialog
from tkinter import *
import pickle
import tkinter.font as tkFont

colors1 = ["firebrick1", "chocolate1", "DarkGoldenRod1", "yellow green", "dodger blue", "dark orchid"]
colors2 = ["light pink", "peach puff", "light goldenrod yellow", "DarkSeaGreen1", "LightBlue1", "thistle1"]
colors3 = ["firebrick4", "OrangeRed3", "DarkOrange2", "dark green", "midnight blue", "purple4"]
kolory = ["", "", "", "", "", ""]
code = []
guess_list = ["", "", "", ""]
wygrane_latwy = 0
przegrane_latwy = 0
wygrane_trudny = 0
przegrane_trudny = 0
proba = 0
tryb = TRUE
tryb_tekst = " Dark mode"

for i in range(0, 6):
    kolory[i] = colors1[i]

menu_window = Tk()
menu_window.title("Menu")
menu_window.geometry("650x250")
menu_window.attributes("-fullscreen", True)
menu_window.configure(background = "snow")

menu = Frame(menu_window)
instrukcja = Frame(menu_window)
poziomy = Frame(menu_window)
gra = Frame(menu_window)
personalizuj = LabelFrame(menu_window, text = "Choose the color palette", bd = 0, fg = "black")
statystyki = Frame(menu_window)
wygrana = Frame(menu_window)
przegrana = Frame(menu_window)
odpowiedzi = Frame(menu_window)
wskazowki = Frame(menu_window)

sun = PhotoImage(file = r"C:\Users\PC\Downloads\brightness (1).png")
moon = PhotoImage(file = r"C:\Users\PC\Downloads\night-mode.png")

tryb_image = moon

font8 = tkFont.Font(family = "Dogica Pixel", size = 8, weight = tkFont.NORMAL)
font15 = tkFont.Font(family = "Dogica Pixel", size = 15, weight = tkFont.NORMAL)
font25 = tkFont.Font(family = "Dogica Pixel", size = 25, weight = tkFont.NORMAL)

personalizuj.configure(font = font25)

def zmien_kolor(kolor_tla, kolor_tekstu):
    menu_window.configure(background = kolor_tla)
    menu.configure(background = kolor_tla)
    instrukcja.configure(background = kolor_tla)
    poziomy.configure(background = kolor_tla)
    gra.configure(background = kolor_tla)
    personalizuj.configure(background = kolor_tla)
    statystyki.configure(background = kolor_tla)
    wygrana.configure(background = kolor_tla)
    przegrana.configure(background = kolor_tla)
    odpowiedzi.configure(background = kolor_tla)
    wskazowki.configure(background = kolor_tla)
    menu_window.option_add("*Label*Background", kolor_tla)
    menu_window.option_add("*Label*Foreground", kolor_tekstu)
    gra.option_add("*Label*Background", kolor_tla)
    gra.option_add("*Label*Foreground", kolor_tekstu)

zmien_kolor("snow", "black")

def przelacz(button):
    global tryb
    global tryb_tekst
    global moon
    global sun
    global tryb_image

    if tryb:
        tryb_image = sun
        tryb_tekst = " Light mode"
        zmien_kolor("grey12", "snow")
        personalizuj["fg"] = "snow"
        button.configure(text = tryb_tekst)
        button.configure(image = tryb_image)
        tryb = FALSE

    else:
        tryb_image = moon
        tryb_tekst = " Dark mode"
        zmien_kolor("snow", "black")
        personalizuj["fg"] = "black"
        button.configure(image = tryb_image)
        button.configure(text = tryb_tekst)
        tryb = TRUE

    return tryb, tryb_image, tryb_tekst

def wyczysc(ramka):
    for widget in ramka.winfo_children():
        widget.destroy()

def zapisz_do_pliku():
    global kolory
    global wygrane_latwy
    global przegrane_latwy
    global wygrane_trudny
    global przegrane_trudny

    plik = open("mastermind.dat", "wb")
    pickle.dump(kolory, plik)
    pickle.dump(wygrane_latwy, plik)
    pickle.dump(przegrane_latwy, plik)
    pickle.dump(wygrane_trudny, plik)
    pickle.dump(przegrane_trudny, plik)
    plik.close()

def otworzplik():
    global kolory
    global wygrane_latwy
    global przegrane_latwy
    global wygrane_trudny
    global przegrane_trudny

    plik_sciezka = filedialog.askopenfilename()
    plik = open(plik_sciezka, "rb")
    kolory = pickle.load(plik)
    wygrane_latwy = pickle.load(plik)
    przegrane_latwy = pickle.load(plik)
    wygrane_trudny = pickle.load(plik)
    przegrane_trudny = pickle.load(plik)
    plik.close()

def wybierz_palete():
    global colors1
    global colors2
    global colors3
    global kolory
    global tryb_tekst
    global moon
    global sun

    def zmien_palete(paleta):
        for i in range(0, 6):
            kolory[i] = paleta[i]
        return kolory

    wybierz_colors1 = Button(personalizuj, text="Classic", activebackground = "gainsboro", font = font15, width = 14, command=lambda: [zmien_palete(colors1)])
    wybierz_colors1.pack(pady = (50, 7))

    wybierz_colors2 = Button(personalizuj, text = "Pastels", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [zmien_palete(colors2)])
    wybierz_colors2.pack(pady = 7)

    wybierz_colors3 = Button(personalizuj, text="Dark", activebackground = "gainsboro", font = font15, width = 14, command=lambda: [zmien_palete(colors3)])
    wybierz_colors3.pack(pady = 7)

    tryb_button = Button(personalizuj, text = tryb_tekst, font = font15, image = tryb_image, activebackground = "gainsboro", width = 240, height = 25, compound = LEFT,command = lambda: [przelacz(tryb_button)])
    tryb_button.pack(pady = (40, 40))

    wstecz_personalizuj = Button(personalizuj, text = "Back", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [wyczysc(personalizuj), personalizuj.pack_forget(), menu.pack()])
    wstecz_personalizuj.pack(pady = (50, 7))

    personalizuj.pack(pady = 220)

def instrukcja_pokaz():
    info1 = Label(instrukcja, text = "Welcome to Mastermind!", font = font25, wraplength = 890)
    info2 = Label(instrukcja, text="Your goal is to guess a code consisting of four randomly", font=font15)
    info3 = Label(instrukcja, text="generated colours in eight tries. You can choose between", font=font15)
    info4 = Label(instrukcja, text="two levels - easy and hard. In easy mode the colours in", font=font15)
    info5 = Label(instrukcja, text="code don't repeat and after guessing you get a hint for", font=font15)
    info6 = Label(instrukcja, text="each colour (whether the colour is in the right place, it's", font=font15)
    info7 = Label(instrukcja, text="somewhere in the code but in a different place or if it's", font=font15)
    info8 = Label(instrukcja, text="not in the code at all). In the hard mode you only get a hint", font=font15)
    info9 = Label(instrukcja, text="about a colour if it's in the right place and the colours in", font=font15)
    info10 = Label(instrukcja, text="the code might repeat.", font=font15)
    info11 = Label(instrukcja, text="Good luck!", font=font15)

    info1.pack(pady = (155, 40))
    info2.pack(pady=5)
    info3.pack(pady=5)
    info4.pack(pady=5)
    info5.pack(pady=5)
    info6.pack(pady=5)
    info7.pack(pady=5)
    info8.pack(pady=5)
    info9.pack(pady=5)
    info10.pack(pady=5)
    info11.pack(pady=30)

    zamknij_instrukcja = Button(instrukcja, text = "Back", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [wyczysc(instrukcja), instrukcja.pack_forget(), menu.pack()])
    zamknij_instrukcja.pack(pady = 50)

    menu.pack_forget()
    instrukcja.pack()

def pokaz_statystyki():
    global wygrane_latwy
    global wygrane_trudny
    global przegrane_trudny
    global przegrane_latwy

    naglowek = Label(statystyki, text = "Your statistics:", font = font25)
    naglowek.pack(pady = (220, 40))

    wl_tekst = Label(statystyki, text = "Easy mode - games won: " + str(wygrane_latwy), font = font15)
    wl_tekst.pack(pady = 15)

    pl_tekst = Label(statystyki, text = "Easy mode - games lost: " + str(przegrane_latwy), font = font15)
    pl_tekst.pack(pady = (15, 40))

    wt_tekst = Label(statystyki, text = "Hard mode - games won: " + str(wygrane_trudny), font = font15)
    wt_tekst.pack(pady = 15)

    pt_tekst = Label(statystyki, text = "Hard mode - games lost: " + str(przegrane_trudny), font = font15)
    pt_tekst.pack(pady = 15)

    zamknij_statystyki = Button(statystyki, text="Back", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [wyczysc(statystyki), statystyki.pack_forget(), menu.pack()])
    zamknij_statystyki.pack(pady = 70)

    statystyki.pack()

def play_game():
    poziom = ""
    global kolory
    global guess_list
    guess = [StringVar(gra), StringVar(gra), StringVar(gra), StringVar(gra)]

    def reset_proby():
        global proba
        proba = 0

    def select_hard():
        global code
        nonlocal poziom
        poziom = "trudny"

        code = random.choices(kolory, weights=None, cum_weights=None, k=4)

        return code, poziom

    def select_easy():
        global code
        nonlocal poziom
        poziom = "latwy"

        code = random.sample(kolory, 4)

        return code, poziom

    def licz_statystyki(poziom, wynik):
        global wygrane_latwy
        global wygrane_trudny
        global przegrane_latwy
        global przegrane_trudny

        if poziom == "latwy" and wynik == "wygrana":
            wygrane_latwy += 1
            return wygrane_latwy
        elif poziom == "trudny" and wynik == "wygrana":
            wygrane_trudny += 1
            return wygrane_trudny
        elif poziom == "latwy" and wynik == "przegrana":
            przegrane_latwy += 1
            return przegrane_latwy
        elif poziom == "trudny" and wynik == "przegrana":
            przegrane_trudny += 1
            return przegrane_trudny

    def check_code(odpowiedz):
        global proba
        nonlocal poziom
        global przegrana
        global wygrana
        nonlocal guess

        for i in range(0, 4):
            guess_list[i] = odpowiedz[i].get()

        if poziom == "latwy":
            if proba < 8 and guess_list == code:
                licz_statystyki("latwy", "wygrana")
                wygralxs = Label(wygrana, text = "Congratulations! You won.", font = font25)
                wygralxs.pack(pady = (400, 50))

                powrot_menu = Button(wygrana, text="Back to menu", activebackground = "gainsboro", font = font15, width = 14, command=lambda: [wyczysc(wygrana), wyczysc(gra), wygrana.pack_forget(), reset_proby(), menu.pack()])
                powrot_menu.pack(pady = 50)

                gra.pack_forget()
                wskazowki.pack_forget()
                wygrana.pack()

            elif proba < 7 and guess_list != code:
                wyczysc(wskazowki)
                for i in range(0, 4):
                    if guess_list[i] == code[i]:
                        wlasciwe = Label(wskazowki, text = "Colour {} is in the right place.".format(i+1), font = font8)
                        wlasciwe.pack(pady = 10)
                    elif guess_list[i] != code[i] and guess_list[i] in code:
                        niewlasciwe = Label(wskazowki, text = "Colour {} is in the code, but in a different place.".format(i+1), font = font8)
                        niewlasciwe.pack(pady = 10)
                    elif guess_list[i] not in code:
                        niema = Label(wskazowki, text = "Colour {} is not in the code.".format(i+1), font = font8)
                        niema.pack(pady = 10)
                wskazowki.pack()

            elif proba >= 7 and guess_list != code:
                licz_statystyki("latwy", "przegrana")
                przegralxs = Label(przegrana, text = "You lost... Good luck next time.", font = font25)
                przegralxs.pack(pady = (400, 50))

                powrot_menu = Button(przegrana, text="Back to menu", activebackground = "gainsboro", font = font15, width = 14, command=lambda: [wyczysc(przegrana), wyczysc(gra), przegrana.pack_forget(), reset_proby(), menu.pack()])
                powrot_menu.pack(pady = 50)

                gra.pack_forget()
                wskazowki.pack_forget()
                przegrana.pack()

        elif poziom == "trudny":
            if proba < 8 and guess_list == code:
                licz_statystyki("trudny", "wygrana")
                wygralxs = Label(wygrana, text = "Congratulations! You won.", font = font25)
                wygralxs.pack(pady = (400, 50))

                powrot_menu = Button(wygrana, text="Back to menu", activebackground = "gainsboro", font = font15, width = 14, command=lambda: [wyczysc(wygrana), wyczysc(gra), wygrana.pack_forget(), reset_proby(), menu.pack()])
                powrot_menu.pack(pady = 50)

                gra.pack_forget()
                wskazowki.pack_forget()
                wygrana.pack()

            elif proba < 7 and guess_list != code:
                for widget in wskazowki.winfo_children():
                    widget.destroy()
                for i in range(0, 4):
                    if guess_list[i] == code[i]:
                        wlasciwe = Label(wskazowki, text="Colour {} is in the right place.".format(i + 1), font = font8)
                        wlasciwe.pack(pady = 10)
                    else:
                        niewiadomo = Label(wskazowki, text = "?", font = font8)
                        niewiadomo.pack(pady = 10)

                wskazowki.pack()

            elif proba >= 7 and guess_list != code:
                licz_statystyki("trudny", "przegrana")
                przegralxs = Label(przegrana, text = "You lost... Good luck next time.", font = font25)
                przegralxs.pack(pady = (400, 50))

                powrot_menu = Button(przegrana, text="Back to menu", activebackground = "gainsboro", font = font15, width = 14, command=lambda: [wyczysc(przegrana), wyczysc(gra), przegrana.pack_forget(), reset_proby(), menu.pack()])
                powrot_menu.pack(pady = 50)

                gra.pack_forget()
                wskazowki.pack_forget()
                przegrana.pack()

        proba += 1

        return proba

    rzad1 = Frame(gra, background="")
    rzad2 = Frame(gra, background="")
    rzad3 = Frame(gra, background="")
    rzad4 = Frame(gra, background="")

    Label(rzad1, text="Colour 1:   ", font = font8).pack(side = LEFT, pady = (200, 15))
    Label(rzad2, text="Colour 2:   ", font = font8).pack(side = LEFT, pady = 15)
    Label(rzad3, text="Colour 3:   ", font = font8).pack(side = LEFT, pady = 15)
    Label(rzad4, text="Colour 4:   ", font = font8).pack(side = LEFT, pady = 15)

    for kolor in kolory:
        Radiobutton(rzad1, variable = guess[0], value = kolor, bg = kolor, height = 2, width = 13, indicatoron = FALSE).pack(side = LEFT, padx = 5, pady = (200, 15))

    for kolor in kolory:
        Radiobutton(rzad2, variable = guess[1], value = kolor, bg = kolor, height = 2, width = 13, indicatoron = FALSE).pack(side = LEFT, padx = 5, pady = 15)

    for kolor in kolory:
        Radiobutton(rzad3, variable = guess[2], value = kolor, bg = kolor, height = 2, width = 13, indicatoron = FALSE).pack(side = LEFT, padx = 5, pady = 15)

    for kolor in kolory:
        Radiobutton(rzad4, variable = guess[3], value = kolor, bg = kolor, height = 2, width = 13, indicatoron = FALSE).pack(side = LEFT, padx = 5, pady = 15)

    rzad1.pack(padx = (200, 240))
    rzad2.pack(padx = (200, 240))
    rzad3.pack(padx = (200, 240))
    rzad4.pack(padx = (200, 240))

    powodzenia = Label(gra, text="Good luck!", font = font25)

    Button(gra, text="Check", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [check_code(guess), powodzenia.pack_forget()]).pack(pady = 40)

    powodzenia.pack(pady=50)

    wybierz = Label(poziomy, text = "Choose level", font = font25)
    wybierz.pack(pady = (265, 50))

    latwy_button = Button(poziomy, text = "Easy", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [select_easy(), wyczysc(poziomy), poziomy.pack_forget(), gra.pack()])
    latwy_button.pack(pady = 10)

    trudny_button = Button(poziomy, text = "Hard", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [select_hard(), wyczysc(poziomy), poziomy.pack_forget(), gra.pack()])
    trudny_button.pack(pady = 10)

    wstecz_poziomy = Button(poziomy, text = "Back", activebackground = "gainsboro", font = font15, width = 14, command = lambda: [wyczysc(poziomy), wyczysc(gra), poziomy.pack_forget(), menu.pack()])
    wstecz_poziomy.pack(pady = 90)

    poziomy.pack()

graj_button = Button(menu, text = "Play", font = font25, background = "snow2", activebackground = "gainsboro", command = lambda: [play_game(), menu.pack_forget()])
graj_button.pack(pady = (210, 40))

instrukcja_button = Button(menu, text = "How to play?", font = font15, background = "snow2", activebackground = "gainsboro", width = 14, command = lambda: instrukcja_pokaz())
instrukcja_button.pack(pady = 7)

personalizuj_button = Button(menu, text = "Settings", font = font15, background = "snow2", activebackground = "gainsboro", width = 14, command = lambda: [wybierz_palete(), menu.pack_forget()])
personalizuj_button.pack(pady = 7)

statsy_button = Button(menu, text = "Statistics", font = font15, background = "snow2", activebackground = "gainsboro", width = 14, command = lambda: [pokaz_statystyki(), menu.pack_forget()])
statsy_button.pack(pady = 7)

wczytaj_button = Button(menu, text = "Load game", font = font15, background = "snow2", activebackground = "gainsboro", width = 14, command = otworzplik)
wczytaj_button.pack(pady = 7)


zapisz_button = Button(menu, text = "Save game", font = font15, background = "snow2", activebackground = "gainsboro", width = 14, command = zapisz_do_pliku)
zapisz_button.pack(pady = 7)

zamknij_button = Button(menu, text = "Exit", font = font15, background = "snow2", activebackground = "gainsboro", width = 14, command = menu_window.destroy)
zamknij_button.pack(pady = (50, 7))

menu.pack()

menu_window.option_add("*Button*Background", "snow2")
menu_window.mainloop()