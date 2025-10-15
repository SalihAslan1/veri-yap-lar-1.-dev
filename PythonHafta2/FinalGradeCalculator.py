VIZE_AGIRLIGI = 0.40
FINAL_AGIRLIGI = 0.60
GECME_NOTU = 60.0
try:
    vize_notu = float(input("Lütfen vize notunuzu (0-100 arası) girin: "))

    if not (0 <= vize_notu <= 100):
        print("\n[HATA] Notlar 0 ile 100 arasında olmalıdır.")
        exit()

except ValueError:
    print("\n[HATA] Geçersiz girdi. Lütfen sadece rakam kullanın.")
    exit()

vize_puani = vize_notu * VIZE_AGIRLIGI

gerekli_final_puani = GECME_NOTU - vize_puani

min_final_notu = gerekli_final_puani / FINAL_AGIRLIGI

print("\n--- Final Notu Hesaplama Sonucu ---")
print(f"Ders Geçme Notu: {GECME_NOTU}")
print(f"Vize Ağırlığı:   {VIZE_AGIRLIGI * 100}%")
print(f"Final Ağırlığı:  {FINAL_AGIRLIGI * 100}%")
print("-----------------------------------")

if min_final_notu <= 0:
    print(f"Vize notunuz ({vize_notu:.2f}), dersi geçmek için yeterlidir. Finalden 0 (sıfır) almanız yeterli.")

elif min_final_notu <= 100:
    print(f"Dersi geçmek için (Ortalama {GECME_NOTU} olmak zorunda):")
    print(f"Final sınavından en az {min_final_notu:.2f} almanız gerekiyor.")

else:
    print("Üzgünüz, Vize notunuz çok düşük.")
    print(f"Dersi geçmek için Finalden {min_final_notu:.2f} almanız gerekiyor. Bu imkansız.")
    print("Dersi geçmek için yeterli puana ulaşma şansınız kalmamıştır.")