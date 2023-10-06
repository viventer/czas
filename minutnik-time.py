import time


def countdown_timer():
    # Format w którym sformatujemy czas.
    TIME_FORMAT = "%H:%M:%S"

    # Format w którym sformatujemy czas.
    input_time = input("Podaj czas w formacie hh:mm:ss: ")

    try:
        # Konwertujemy czas podany przezz usera na godziny minuty i sekundy
        hours, minutes, seconds = input_time.split(":")
        # Jeśli któraś z liczb jest mniejsza od 0 (ktoś podał ujemny czas) wywołujemy wyjątek.
        # Więcej o raise w jednym z kolejnych filmów ;)
        if int(hours) < 0 or int(minutes) < 0 or int(seconds) < 0:
            raise ValueError

        # Przeliczamy wszystkie jednostki na sekundy
        countdown_time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    # Jeśli format jest nieprawidłowy informujemy o błędzie.
    except ValueError:
        print("Błąd: Nieprawidłowy format czasu.")
        return

    # Tworzymy pętle "nieskończoną".
    while True:
        # Formatujemy pozostały czas, przy okazji musimy liczbę sekund przekonwertować na obiekt struct_time za pomocą funkcji gmtime().
        formatted_countdown_time = time.strftime(
            TIME_FORMAT, time.gmtime(countdown_time))
        # Wyświetlamy pozostały czas.
        print(formatted_countdown_time)

        # Jeśli minutnik doszedł do 0 - kończymy wykonywanie pętli.
        if (countdown_time == 0):
            print("Koniec czasu!")
            break

        # A jeśli if nie został spełniony odczekujemy sekundę.
        time.sleep(1)

        # Którą następnie odejmujemy od pozostałego czasu.
        countdown_time -= 1


countdown_timer()
