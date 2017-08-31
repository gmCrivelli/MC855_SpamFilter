# MC855_SpamFilter
Filtro de Spam para MC855 - Unicamp

Desenvolvido por:

Matheus Jun Ota  
Gustavo de Mello Crivelli  
Lucas de Souza e Silva  
Matheus Laborão Netto

## Arquivos

* **emailcollection.txt** - Coleção de emails Spam e Ham, retirados do [Enron Email Dataset](https://www.cs.cmu.edu/~./enron/)
* **smscollection.txt** - Coleção de SMS Spam e Ham
* **emailset.txt** - Contagem de palavras dividida em Spam e Ham, gerada via execução de mapper.py e reducer.py em Hadoop com input de emailcollection.txt
* **smsset.txt** - Contagem de palavras dividida em Spam e Ham, gerada via execução de mapper.py e reducer.py em Hadoop com input de smscollection.txt
* **mapper.py** - Mapper (Hadoop)
* **reducer.py** - Reducer (Hadoop)
* **classifier.py** - Classificador local de email/SMS em Spam ou Ham. Atualmente hardcoded para usar emailset.txt como classificador, aceita input do usuário ou leitura direta de emailcollection.txt .
* **output** - Resultados de classifier.py
