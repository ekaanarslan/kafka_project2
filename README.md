# kafka_project2
task2
1.ADIM
Aşağıdaki kodu terminalde yazarak kafka ve zookeeper servislerini çalıştırın.

	docker-compose -f dockercompose1.yml up

2.ADIM
Aşağıdaki kodu yeni bir terminale yazarak web_scraper_kafka python kodunu çalıştırıyoruz bu kod dizisi veriyi çekme ve kafkaya gönderme gibi görevleri başlatır.

	python web_scraper_kafka.py

3.ADIM
Aşağıdaki kodu yeni bir terminale yazarak rest_api python kodunu çalıştırıyoruz. bu kod Flask kullanarak bir JSON dosyasındaki verileri sunan basit bir REST API sağlar. 

	python rest_api.py

işlemimiz tamamlandı. Masaüstünde bir adet kafka_data.json dosyası oluşmuş olmalı web sitesindeki içerikler orda json formatında kaydedildi. Ayrıca tarayıcınızdan http://localhost:8080/data adresine giderek de bu kaydedilen verileri görebilirsiniz.
