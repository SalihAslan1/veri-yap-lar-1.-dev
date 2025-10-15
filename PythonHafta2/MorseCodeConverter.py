MORSE_CODE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

metin = input("Lütfen Mors alfabesine çevirmek istediğiniz metni girin: ").strip()

if not metin:
    print("\n[UYARI] Metin boş olamaz.")
    exit()

metin_buyuk = metin.upper()

mors_kodu_parcalari = []

for karakter in metin_buyuk:

    if karakter in MORSE_CODE_MAP:
        mors_kodu_parcalari.append(MORSE_CODE_MAP[karakter])
    else:
        mors_kodu_parcalari.append('?')

mors_kodu = " ".join(mors_kodu_parcalari)

print("\n--- Sonuç ---")
print(f"Orijinal Metin:     \"{metin}\"")
print(f"Mors Alfabesi Karşılığı: {mors_kodu}")