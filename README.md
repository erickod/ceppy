# Ceppy
Consulta CEPs em vários serviços (Correios, ViaCep, OpenCep) de maneira totalmente assíncrona

## Comece por aqui
Nesta seção você encontrará instruções de como instalar o pacote e também encontrará exemplos de uso

### Requerimentos

Esse projeto é compatível com as versões `3.10` e `3.11` do python no momento. A compatibilização com versões anteriores está prevista, e qualquer contribuição é bem vinda.

### Instalação

##### PIP
```
pip install ceppy
```

##### Poetry
```
poetry add ceppy
```

### Fazendo uma consulta
Tenha em mente que a lib vai retornar o serviço que responder mais rápido

```python
from ceppy import Cep

cep = Cep("75140070")
```

### Acessando os dados da consulta
Você pode usar os atributos listados abaixo para acessar os dados do Cep:

```python
from ceppy import Cep

cep = Cep("75140070")

print(cep.number) # 75140070
print(cep.state) # GO
print(cep.city) # Anápolis
print(cep.street) # Rua Senador Mardocheu Diniz
print(cep.district) # Dom Pedro II
print(cep.query_service) #CorreiosService
print(cep.status) # query_done
```

Você também pode converter os dados para dict

```python
from ceppy import Cep

cep = Cep("75140070")
print(dict(cep))

{
 'street': 'Rua Senador Mardocheu Diniz', 
 'district': 'Dom Pedro II', 
 'city': 'Anápolis', 
 'state': 'GO', 
 'cep': '75140070', 
 'provider': 'CorreiosService'
 }

```


## Este projeto utiliza

* [AioHTTP](https://docs.aiohttp.org/en/stable/) - Requisições HTTP
* [Poetry](https://python-poetry.org/) - Gerenciamento de dependências e publicação
* [Pytest](https://docs.pytest.org/) - Testes automatizados

## Autor

* **Erick Duarte** - *Implementação inicial* - [erickod](https://github.com/erickod)

## Licença

O projeto está disponível através da licença MIT - Consulte o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
