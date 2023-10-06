from datetime import datetime, timedelta
import time


def timer():
    # Format w którym sformatujemy czas.
    TIME_FORMAT = "%H:%M:%S"

    # Czas podany przez użytkownika.
    input_time = input("Podaj czas w formacie hh:mm:ss: ")

    try:
        # Konwertujemy stringa podanego przez usera na obiekt datetime.
        countdown_time = datetime.strptime(input_time, TIME_FORMAT)
    # Jeśli format jest nieprawidłowy informujemy o błędzie.
    except ValueError:
        print("Błąd: Nieprawidłowy format czasu.")
        return

    # Tworzymy pętle "nieskończoną".
    while True:
        # Formatujemy pozostały czas.
        formatted_countdown_time = countdown_time.strftime(TIME_FORMAT)
        # I go wyświetlamy.
        print(formatted_countdown_time)

        # Jeśli minutnik doszedł do 0 - kończymy wykonywanie pętli.
        if (countdown_time.second == 0):
            print("Koniec czasu!")
            break

        # A jeśli if nie został spełniony odczekujemy sekundę.
        time.sleep(1)

        # Którą następnie odejmujemy od pozostałego czasu.
        countdown_time -= timedelta(seconds=1)


timer()
