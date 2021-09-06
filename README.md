# Super Single - Player Image Uploader (SS-PIU)
![piu](https://i.imgur.com/xQBwCA2.jpg)

Script básico para manutenção de imagens em entities-api

## Instalação
```
pip3 install requirements.txt
```

## Uso
Existem dois comandos básico para usar:
- **create-dictionary** esse comando ira criar um arquivo csv necessário para que o script entenda qual pasta procurar (coluna 1) e qual respectiva key da entidade (coluna 2). 
Obs: a flag *--fill-entity* tentara preencher a segunda coluna, por padrão esse comportamente é omitido.
```
python3 logos_save.py create-dictionary --dir="iOS - Quadrado - MLB" --fill_entity_name=True
```

- **create-imgs**: Esse comando cria uma pasta chamada formated_image_name na raiz do script, lá ele cria as imagens com o nome correto (a key de entities) para inserir em entities-api.
Obs: A flag *--upload* por padrão é False, sendo assim para fazer o upload de fato para entities-api é preciso explicitar isso, senão somente será criado o diretorio com as imagens.
```
python3 logos_save.py create-imgs --dir_alternative="iOS - Redondo - MLB/" --dir="iOS - Quadrado - MLB/"
```

