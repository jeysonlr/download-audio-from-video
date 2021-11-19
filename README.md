

## Para criar e usar ambiente virtual
$ python -m venv venv   -- cria o ambiente virtual

dentro do terminal Powershell execute o comando 
$ .venvScriptsActivate.ps1

se ocorrer algum erro ao executar o comando acima, execute o seguinte comando no powershel com modo de administrador
$ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

abra um novo terminal e instale as dependencias


##  Script utilizado para baixar audios no formato mp3 direto de um video do YouTube.


## Pré-requisitos :pushpin:

```
pip install pytube
```

```
pip install moviepy
```

## Como rodar a aplicação :arrow_forward:

No terminal navegar até o diretório onde se encontram os arquivos, e digitar:

```
python downloadMP3.py
```

## Bibliotecas utilizadas :books:

- [MoviePy](https://pypi.org/project/moviepy/)
- [PyTube](https://pypi.org/project/pytube/)
