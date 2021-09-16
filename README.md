# Super Single - Player Image Uploader (SS-PIU)
![piu](https://i.imgur.com/xQBwCA2.jpg)

Script básico para manutenção de imagens em entities-api

## Instalação
```
pip3 install -r requirements.txt
```

## Contexto
Para incluir um novo logo para uma entidade são necessárias duas imagens: uma redonda e outra quadrada, a redonda é aquela vista na home (tela de busca) e a quadrada no resto dos lugares ex, tela de congrats. IMPORTANTE: Ao realizar a chamada para inserção em entities-api o nome ira definir qual imagem ele ira considerar redonda ou quadrada, as imagens redondas devem ser upadas com a seguinte sintaxe: {{key_entidade}}.png e as quadradas {{key_entidade}}_alternative.png.
Você pode encontrar um exemplo em: https://internal-api.mercadopago.com/single-player/entities-api/entities/0106_4 no campo "image" do json.
  
Exemplo da estrutura e onde deve morar o script:
![exemplo_estrutura](https://i.imgur.com/oWQVp5h.png)


## Uso
Existem dois comandos básicos para usar:
- **create-dictionary** esse comando irá criar um arquivo (file_dictionary.csv) csv necessário para que o script entenda qual pasta procurar (coluna 1) e qual respectiva key da entidade (coluna 2). Só é preciso criar o dicionário a partir da pasta das imagens redondas
```
python3 logos_save.py create-dictionary --dir="ios-redondo-png" --fill_entity_name=True
```
* Atenção:
  * A flag *--fill-entity* tentara preencher a segunda coluna, por padrão esse comportamente é omitido.
  * É importante o arquivo "file_dictionary.csv" esteja bem formatado, o nome das entidades na coluna 1 deve ser o mesmo das pastas, o script consegue preencher essa colunas sem problemas com o comando acima, apenas revise para ver se não há nada faltando. Entidades que possuirem nome mas estiverem sem key serão ignoradas.

- **create-imgs**: Esse comando cria uma pasta chamada formated_image_name na raiz do script, lá ele cria as imagens com o nome correto (a key de entities) para inserir em entities-api.
```
python3 logos_save.py create-imgs --dir_alternative="ios-quadrado-png" --dir="ios-redondo-png" --file_dict="files_dictionary.csv"
```
* Atenção:
  * O campo --dir deve ser onde estão as imagens quadradas e dir_alternative as redondas. O script funciona bem para o modo como estão dispostos os diretorios de imagens para iOS: PASTA_RAIZ/Nome_Entidade/Nome_Entidade@3x.png
  * Obs: A flag *--upload* por padrão é False, sendo assim para fazer o upload de fato para entities-api é preciso explicitar isso, senão somente será criado o diretorio com as imagens.
  * Para fazer o upload é necessário estar conectado a VPN.

