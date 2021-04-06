"""
 YOGUNLUK DONUSUMLERI(INTENSITY TRANSFORMATIONS)-TEMEL TON DONUSUMLERI
 -Bu yontem giris fotografındaki pixel degerlerini(r), bir tane "Donusum Fonk"(T) ile cikis fotografindaki
 pixel degerlerine(s) donusturur.----> s = T(r)
 -Genelde 8bit fotolarla ugrastigimiz icin giris fotosundaki pixel degerleri 0-255arasindadir. Belirledigimiz
 donusum fonksiyonu bu degerleri yine 0-255 arasında olacak sekilde belirli bir düzene göre değiştirir.
 Bu dönüşümlerin 3ü yoğun bir şekilde kullanılıyor:
 >Linear Dönüşümler,
 >Logaritmik(Ters Logaritmik) Dönüşümler,
 >Kuvvet Dönüşümleri


 1)Fotoğrafların Negatifi(Image Negatives)
 Yoğunluk değerleri [0, L-1] arasında olan bir fotoğrafın negatifi, "Negatif Dönüşüm Fonksiyonu" kullanılarak elde edilir.
 s=L-1-r   ,L fotonun sahip olabileceği max yogunluk degeridir. 8bit foto için L=256

 fotoğrafın boyutu fotoda kaç pixel oldugunu gösterir
"""



import cv2

foto = cv2.imread("mamogram.jpg") #fotoyu pythona yukledik
print(foto.shape)

cv2.imshow("fotograf", foto) #fotoyu yeni pencerede gosterme islemleri
cv2.waitKey(0)
cv2.destroyAllWindows()

# foto[:, :, 0] ---> [butun yukseklik değerlerini ver, butun genislik değerlerini ver, mavi kanalını ver]
# 0->blue, 1->green, 2->red