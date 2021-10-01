# coletor-de-dados
Coletores de dados de API's REST em Python.

## API's utilizadas:
- [coinlib](https://coinlib.io/apidocs)
- [rickandmortyapi](https://rickandmortyapi.com)
- [fortnitetracker](https://fortnitetracker.com/site-api)

## Instruções de execução

O trabalho foi feito utilizando **Python3.9**, portandto se faz necessário utilizar um interpretador Python.

Primeiro, instale as dependências necessárias executando o seguinte comando no terminal:

```
pip install -r requirements.txt
```

Então, para executar abra o terminal no diretório raiz e digite:
```
python collector.py -a {nome_api} -f {dir} -k {key}
```

Os parâmetro necessários são:

- **-a, --api-name:** Nome da api que deseja consultar [Obrigatório]
- **-f, --file:** Diretório onde será salvo o resultado da consulta [Obrigatório]
- **-k, --key:** Chave de acesso a API [Opcional]

Todos os comandos para CLI podem ser visualidos com:
```
python collector.py --help
```

