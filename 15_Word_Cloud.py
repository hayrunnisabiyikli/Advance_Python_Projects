from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Örnek bir veri kümesi oluştur
data = {'Review': [
    "Harika bir ürün, çok memnun kaldım",
    "Hızlı kargo, teşekkürler",
    "Ürün beklediğim gibi çıkmadı",
    "Fiyat performans açısından iyi",
    "Tavsiye ederim, çok kaliteli",
    "Kötü bir deneyim yaşadım",
    "Ürün iyi paketlenmişti",
    "Hızlı teslimat, memnun kaldım"
]}

# Veri çerçevesini oluştur
df = pd.DataFrame(data)

# STOPWORDS kümesini kullanarak gereksiz kelimeleri filtrele
stopwords = set(STOPWORDS)

# Boş bir metin stringi oluştur
words = ''

# Her bir inceleme için metinleri birleştir
for review in df.Review:
    tokens = str(review).split()
    tokens = [i.lower() for i in tokens]
    words += ' '.join(tokens) + ' '

# WordCloud nesnesini oluştur
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(words)

# WordCloud görüntüsünü çiz
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# WordCloud'u göster
plt.show()