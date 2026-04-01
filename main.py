import sys
import itertools

def print_header(title):
    print(f"\n{'='*10} {title} {'='*10}")

# --- SEKCJA 1: EAGER VS LAZY (WYDAJNOŚĆ) ---

def run_memory_benchmark(n=10_000_000):
    print_header("TEST WYDAJNOŚCI: LISTA VS GENERATOR")
    
    # Eager (Lista)
    try:
        data_list = [i**2 for i in range(n)]
        size_list_mb = sys.getsizeof(data_list) / (1024**2)
        print(f"[LISTA] Rozmiar dla {n:,} elementów: {size_list_mb:.2f} MB")
    except MemoryError:
        print("[LISTA] BŁĄD: Brak pamięCI RAM!")
        size_list_mb = 0

    # Lazy (Generator)
    data_gen = (i**2 for i in range(n))
    size_gen_bytes = sys.getsizeof(data_gen)
    print(f"[GENERATOR] Rozmiar dla {n:,} elementów: {size_gen_bytes} bajtów")
    
    if size_list_mb > 0:
        ratio = int((size_list_mb * 1024 * 1024) / size_gen_bytes)
        print(f"Wniosek: Generator jest ok. {ratio:,} razy lżejszy!")

# --- SEKCJA 2: MECHANIZMY ITERACJI ---

def demonstrate_iteration_basics():
    print_header("PODSTAWY ITERACJI")
    
    # Protokół iteracji (hasattr)
    owoce = ["jabłko", "banan"]
    print(f"Czy lista jest iterowalna? {hasattr(owoce, '__iter__')}")
    print(f"Czy liczba jest iterowalna? {hasattr(42, '__iter__')}")

    # Co Python robi pod maską pętli for?
    print("\nSymulacja pętli for (manualny iterator):")
    it = iter(owoce)
    while True:
        try:
            item = next(it)
            print(f" Pobrano: {item}")
        except StopIteration:
            print(" Koniec strumienia (StopIteration)")
            break

# --- SEKCJA 3: KLASY VS GENERATORY ---

class OdliczanieKlasa:
    def __init__(self, start):
        self.n = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        wynik = self.n
        self.n -= 1
        return wynik

def generator_odliczania(n):
    while n > 0:
        yield n
        n -= 1

def compare_class_vs_generator():
    print_header("KLASA VS GENERATOR")
    print("Wynik klasy:", list(OdliczanieKlasa(3)))
    print("Wynik generatora:", list(generator_odliczania(3)))

# --- SEKCJA 4: ZAAWANSOWANE GENERATORY ---

def fibonacci_generator():
    """Nieskończony ciąg Fibonacciego."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def demonstrate_infinite_sequences():
    print_header("NIESKOŃCZONE SEKWENCJE")
    
    # Fibonacci
    fib = fibonacci_generator()
    fib_10 = [next(fib) for _ in range(10)]
    print(f"Fibonacci (pierwsze 10): {fib_10}")
    
    # Generator ID (itertools.count)
    ids = itertools.count(start=100, step=10)
    print(f"Generowane ID: {next(ids)}, {next(ids)}, {next(ids)}")

# --- SEKCJA 5: PUŁAPKI I CECHY ---

def demonstrate_generator_exhaustion():
    print_header("ZUŻYCIE GENERATORA")
    gen = (x for x in range(1, 3))
    
    print(f"Pierwsze użycie: {list(gen)}")
    print(f"Drugie użycie (pusty): {list(gen)}")
    print("Pamiętaj: Generator jest jednorazowy!")

# --- SEKCJA 6: BIBLIOTEKA ITERTOOLS ---

def demonstrate_itertools():
    print_header("BIBLIOTEKA ITERTOOLS")
    
    # Cycle
    tury = itertools.cycle(["Gracz A", "Gracz B"])
    print(f"Tury gry: {next(tury)}, {next(tury)}, {next(tury)}")
    
    # Chain
    l1, l2 = [1, 2], [3, 4]
    polaczone = list(itertools.chain(l1, l2))
    print(f"Połączone wirtualnie (chain): {polaczone}")

# --- GŁÓWNY PUNKT WEJŚCIA ---

if __name__ == "__main__":
    # Uruchamiamy wszystkie prezentacje po kolei
    run_memory_benchmark(1_000_000)
    demonstrate_iteration_basics()
    compare_class_vs_generator()
    demonstrate_infinite_sequences()
    demonstrate_itertools()
    demonstrate_generator_exhaustion()
