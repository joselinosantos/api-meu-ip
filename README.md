## API meu IP
### Retorna o IP público do usuário
**O IP do exemplo é meramente ilustrativo. Cuidado ao expor endereço de IP público.**

![API Meu IP](https://github.com/joselinosantos/api-meu-ip/blob/main/meu_ip.png)

### Técnicas utilizadas
1. Web scrapping para obter o IP a partir do site: https://www.meuip.com.br/
2. Retornar os dados em JSON no endpoint /meuip

### Ferramentas
1. Biblioteca Urllib3 para scrapping: https://pypi.org/project/urllib3/
2. Biblioteca BeautifulSoup para parse (melhor formato) dos dados: https://beautiful-soup-4.readthedocs.io/en/latest/
3. Flask - Framework web leve e rápido em Python: https://flask.palletsprojects.com/en/3.0.x/

### Execução
**Abra o terminal e acesse a pasta do projeto**
1. Instale o virtualenv
```
    pip install virtualenv
```
2. Crie o ambiente virtual
```
    python3 -m venv .venv
```
3. Ative o ambiente virtual
```
    . .venv /bin/activate
```
4. Instale as bibliotecas necessárias
```
    pip install -r requirements.txt
```
5. Execute o arquivo main.py
```
    python3 main.py
```
6. Acesse o endereço http://127.0.0.1:5002/meuip no navegador ou alguma ferramenta para teste de API como: 
  * Insomnia https://insomnia.rest/download
  * Postman: https://www.postman.com/
