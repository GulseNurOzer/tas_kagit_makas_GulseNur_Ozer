import random

def tas_kagit_makas_GulseNur_Ozer():
    # Oyun kurallarını açıklayan karşılama mesajı
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!\n")
    print("Oyun kuralları: Taş, Kağıt veya Makas seçin.")
    print("Taş makası kırar, makas kağıdı keser, kağıt taşı sarar.")
    print("İlk iki turu kazanan oyunun galibi olur.")
    print("Oyundan çıkmak için 'q' tuşuna basın.\n")

    # Oyundaki seçeneklerin tanımlanması
    secenekler = ['Taş', 'Kağıt', 'Makas']

    oyun_sayisi = 0


    while True:
        # Yeni oyunun başlatılması
        oyun_sayisi += 1  # Yeni oyun başladığında sayacı arttırır.
        print(f"\n### {oyun_sayisi}. Oyun Başladı! Bol Şanslar!! ###")

        # Sayaçların başlatılması
        oyuncu_galibiyet = 0
        bilgisayar_galibiyet = 0
        tur_sayisi = 0

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
            tur_sayisi += 1
            print(f"\n{tur_sayisi}. Tur:")

            # Kullanıcıdan bir tane geçerli seçenek alınması veya oyundan çıkış yapması
            oyuncu_secim = input("Lütfen Taş, Kağıt veya Makas seçin (veya çıkmak için 'q' tuşuna basın): ").capitalize()

            if oyuncu_secim == 'Q':
               if oyun_sayisi == 1 and tur_sayisi == 1:
                  print("Oyuna daha başlamadan çıkıyorsunuz! Oyunu başlatmak için fonksiyonu neden çağırdınız? Gerçekten oynamak istediğinizde yeniden gelin!")
               else:
                   print("Oyundan ayrıldınız.\nGame Over")
               return

            if oyuncu_secim not in secenekler:
                print("Geçersiz bir seçim yaptınız. Lütfen yeniden deneyin.")
                tur_sayisi -= 1
                continue

            # Bilgisayarın rastgele seçimi
            if random.random() < 0.02:  # Bilgisayara da %2 olasılıkla çıkış yapabilme şansı tanıdım:)
                bilgisayar_secim = "Çıkış"
            else:
                bilgisayar_secim = random.choice(secenekler)

            if bilgisayar_secim == "Çıkış":
                print("Bilgisayar oyundan ayrılmak istedi...\nGame Over")
                return
            else:
                print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

            # Turu kazananın belirlenmesi
            if oyuncu_secim == bilgisayar_secim:
                print("Bu tur berabere!")
            elif (oyuncu_secim == 'Taş' and bilgisayar_secim == 'Makas') or \
                 (oyuncu_secim == 'Kağıt' and bilgisayar_secim == 'Taş') or \
                 (oyuncu_secim == 'Makas' and bilgisayar_secim == 'Kağıt'):
                print("Bu turu siz kazandınız!")
                oyuncu_galibiyet += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyet += 1

            print(f"Skor: Siz: {oyuncu_galibiyet} - Bilgisayar: {bilgisayar_galibiyet}")


        # Oyunun genel galibinin belirlenmesi
        if oyuncu_galibiyet == 2:
            print(f"\n**Tebrikler! {oyun_sayisi}.Oyunu {tur_sayisi}.Turda kazandınız!**")
        else:
            print(f"\n**Bilgisayar {oyun_sayisi}.Oyunu {tur_sayisi}.Turda kazandı!**")

       # Oyunun devam edip etmemesi için oyuncudan mesaj alma
        while True:
            devam = input("Oyunu bir daha oynamak ister misiniz? (Evet için 'E', Hayır için 'H'): ").capitalize()
            if devam in ['E', 'H']:
                break
            else:
                print("Geçersiz giriş. Lütfen 'E' veya 'H' girin.")

      # Bilgisayarın ve oyuncunun mesajına göre oyunun devam edilip edilmemesine karar verme(oyunun devam etmesi için ikisi de evet demelidir.)
        bilgisayar_devam = random.choice(['Evet', 'Hayır'])

        if bilgisayar_devam == 'Evet':
           print("Bilgisayarın Cevabı: Evet oynamak istiyorum. Hadi bir daha oynayalım!")
        else:
            print("Bilgisayarın Cevabı:Hayır, artık oynamak istemiyorum.")

        if devam == 'E' and bilgisayar_devam == 'Evet':
            print("\nİkiniz de oynamak istiyorsunuz! Yeni oyun hazırlanıyor...")
        elif devam == 'E' and bilgisayar_devam == 'Hayır':
            print("\nBilgisayar oyundan ayrıldı. Oyun kapatılıyor...\nGame Over")
            break
        elif devam == 'H' and bilgisayar_devam == 'Evet':
            print("\nSiz oynamak istemiyorsunuz. Oyun kapatılıyor...\nGame Over")
            break
        else:
            print("\nİkiniz de oynamak istemiyorsunuz. Oyun kapatıldı.")
            break

