**EN**
**Sentience Mail Engine**
This is a practical NLP (Natural Language Processing) project created to automate email analysis. The goal is to identify customer intent and emotions to help support teams work faster.

I designed this project to show how we can turn raw text into organized data:

**Object-Oriented Setup**: Instead of writing a simple script, I used a class structure (SentienceEngine). This makes the code organized and easy to add to other projects later.

**Text Cleaning**: I used Regex to remove email addresses and special characters. It is important to make sure the AI analyzes only the relevant words.

**Sentiment & Priority**: Using TextBlob, the system looks for negative emotions. When a customer is unhappy, the engine automatically flags the message as "High Priority."

**Reliable Coding**: I added error handling (try-except) and logging so if the input is empty or wrong, the program doesn't crash, it just records the error and keeps running.

I included a donut chart to show the distribution of intents, it makes the results easier to understand.

**TR**
**Sentience Mail Engine** 
Bu proje, e-posta analizini otomatikleştirmek için geliştirdiğim pratik bir NLP çalışması. Temel amaç, müşteri niyetini ve duygusunu tespit ederek destek ekiplerinin daha hızlı çalışmasına yardımcı olmaktır.

Projeyi, ham metni düzenli bir veriye dönüştürme sürecini göstermek için şu adımlarla tasarladım:

**OOP**: Basit bir kod yazmak yerine SentienceEngine sınıf yapısını kullandım. Böylece kodun daha düzenli durmasını ve ileride başka projelere kolayca eklenmesini sağladım.

**Metin Temizleme**: E-posta adreslerini ve özel karakterleri temizlemek için Regex kullandım. Bu adım, yapay zekanın sadece ilgili kelimeleri analiz etmesi için önemli.

**Duygular ve Öncelik İlişkisi**: TextBlob kullanarak negatif duyguları taradım. Eğer bir müşteri mutsuzsa, sistem mesajı otomatik olarak "Yüksek Öncelikli" olarak işaretliyor.

**Güvenilir Kodlama**: Hata yönetimi (try-except) ve loglama ekledim. Bu sayede, hatalı veya boş bir veri geldiğinde program çökmek yerine durumu kaydedip çalışmaya devam ediyor.

Jupyter Notebook kısmında niyet dağılımını gösteren bir donut chart hazırladım, böylece sonuçların kolayca anlaşabilmesini sağlamak istedim.

