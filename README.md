# Taş Kağıt Makas Oyunu

## Hakkında

Bu proje, klasik Taş Kağıt Makas oyununun Python ile geliştirilmiş bir versiyonudur. Oyun, kullanıcının bilgisayara karşı oynamasını ve ilk iki turu kazananın oyunu kazanmasını sağlar. Kullanıcı dostu bir arayüz ile tasarlanmıştır ve oyuncuların skorlarını takip eder. Oyuncular istedikleri zaman 'q' tuşuna basarak oyundan çıkabilirler.

## Özellikler

- **Kullanıcı Dostu Arayüz:** Oyunun anlaşılması ve oynanması kolaydır.
- **Rastgele Bilgisayar Seçimi:** Bilgisayar her turda rastgele bir seçim yapar, bu da oyunu adil ve tahmin edilemez hale getirir.
- **Skor Takibi:** Oyuncuların skorları her turdan sonra güncellenir ve görüntülenir.
- **Oyundan Çıkış Seçeneği:** Oyuncu istediği zaman 'q' tuşuna basarak oyundan çıkabilir ancak ilk oyunun ilk turundan çıkması oyun tarafından hoş karşılanmaz.
- **Bilgisayarın Çıkış Şansı:** Bilgisayarın %2 olasılıkla oyundan çıkma şansı vardır, bu da oyuna biraz daha gerçekçilik katar :)
- **Geçersiz Seçim Kontrolü:** Geçersiz bir seçim yapıldığında, kullanıcıya "Geçersiz bir seçim yaptınız. Lütfen yeniden deneyin." mesajı gösterilir ve tekrar seçim yapması istenir.

## Kullanılan Teknolojiler

- **Python:** Oyunun geliştirilmesinde kullanılan programlama dili.
- **Random Kütüphanesi:** Bilgisayarın rastgele seçim yapmasını sağlamak için kullanılır.
  
## Kullanım

Bu kodu Google Colab veya yerel Python ortamınızda çalıştırabilirsiniz.

Google Colab'da veya Yerel Python Ortamında:

1. Kodu içeren dosyayı açın.
2. `tas_kagit_makas_GulseNur_Ozer()` fonksiyonunu çağırarak oyunu başlatın.

Oyun başladıktan sonra, her turda "Taş", "Kağıt" veya "Makas" seçeneklerinden birini seçmeniz istenecektir. Oyundan çıkmak için 'q' tuşuna basabilirsiniz.
  
