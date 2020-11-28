# Django 101: Saindo do Zero 

Seguindo em meus estudos no framework Django, após assistir a live #146 do canal do
Youtube
[Live de Python](https://www.youtube.com/channel/UCAaKeg-BocRqphErdtIUFFw), 
ministrada por Renan Moura, decidi criar um índice do vídeo.

O objetivo da live é dar uma ideia geral do funcionamento básico do framework 
Django, desenvolvendo o exemplo de uma aplicação web de lista de tarefas.

## 1. Configurações do projeto

### 1.1. Ambiente virtual

- [Criando e ativando a venv](https://youtu.be/6a2ID5Ld6is?t=2723)

> _Versão do Python >= 3.8._

### 1.2. Instalação do Django

- [Django 101 - Saindo do zero](https://youtu.be/6a2ID5Ld6is?t=0)
- [Instalando o Django](https://youtu.be/6a2ID5Ld6is?t=272)
> _Versão do Django >= 3.1._
- [Conhecendo o comando django-admin](https://youtu.be/6a2ID5Ld6is?t=347)

### 1.3. Criando um projeto

- [Criando o projeto](https://youtu.be/6a2ID5Ld6is?t=383)
- [Conhecendo o comando ./manage](https://youtu.be/6a2ID5Ld6is?t=408)

### 1.4. Criando uma app

- [Criando uma app django](https://youtu.be/6a2ID5Ld6is?t=467)
- [Conhecendo o arquivo urls.py](https://youtu.be/6a2ID5Ld6is?t=565)
- [Conhecendo o arquivo settings.py](https://youtu.be/6a2ID5Ld6is?t=594)
- [Instalando a app core](https://youtu.be/6a2ID5Ld6is?t=610)
- [Como é composto um projeto Django](https://youtu.be/6a2ID5Ld6is?t=680)

## 2. Iniciando o CRUD:

- [Criando o arquivo urls.py da app core](https://youtu.be/6a2ID5Ld6is?t=737)
- [Conhecendo o comando ./manage check](https://youtu.be/6a2ID5Ld6is?t=1070)

### 2.1. Criando a consulta (READ)

- [Criando a função de consulta da app core](https://youtu.be/6a2ID5Ld6is?t=1132)
- [Criando o templates da app core](https://youtu.be/6a2ID5Ld6is?t=1230)
- [Conhecendo o comando ./manage runserver](https://youtu.be/6a2ID5Ld6is?t=1316)
- [Criando o arquivo models.py da app core](https://youtu.be/6a2ID5Ld6is?t=1496)
- [Criando e aplicando a primeira migração](https://youtu.be/6a2ID5Ld6is?t=1770)
- [Recuperando os registros na view](https://youtu.be/6a2ID5Ld6is?t=1861)
- [Resumo da arquitetura do projeto](https://youtu.be/6a2ID5Ld6is?t=1957)

### 2.2. Criando o cadastro (CREATE)

- [Criando a url de cadastro da tarefa](https://youtu.be/6a2ID5Ld6is?t=2252)
- [Criando a função de cadastro da tarefa](https://youtu.be/6a2ID5Ld6is?t=2279)
- [Criando o arquivo forms.py da app core](https://youtu.be/6a2ID5Ld6is?t=2332)
- [Renderizando o form a partir da view](https://youtu.be/6a2ID5Ld6is?t=2893)
- [Criando o arquivo form.html](https://youtu.be/6a2ID5Ld6is?t=2968)
- [Criando a lógica de inserção de dados no banco de dados](https://youtu.be/6a2ID5Ld6is?t=3151)
- [Criando a url de exibição da tarefa cadastrada](https://youtu.be/6a2ID5Ld6is?t=3359)
- [Criando a view de exibição da tarefa cadastrada](https://youtu.be/6a2ID5Ld6is?t=3387)
- [Criando o arquivo detail.html](https://youtu.be/6a2ID5Ld6is?t=3576)
- [Conhecendo o comando ./manage shell](https://youtu.be/6a2ID5Ld6is?t=3700)
- [Atualizando o html da consulta](https://youtu.be/6a2ID5Ld6is?t=3795)

### 2.3. Criando a exclusão (DELETE)

- [Criando a view de exclusão da tarefa](https://youtu.be/6a2ID5Ld6is?t=3937)
- [Criando a url de exclusão da tarefa](https://youtu.be/6a2ID5Ld6is?t=3991)
- [Atualizando o html da consulta](https://youtu.be/6a2ID5Ld6is?t=4046)

### 2.4. Criando a atualização (UPDATE)

- [Criando a view de atualização da tarefa](https://youtu.be/6a2ID5Ld6is?t=4101)
- [Criando a url de atualização da tarefa](https://youtu.be/6a2ID5Ld6is?t=4219)

## 3. Finalizando

- [Perguntas/Respostas](https://youtu.be/6a2ID5Ld6is?t=4482)

--- 

## 4. Gerando um índice para a descrição do vídeo

Aproveitando para estudar um pouco mais de _regex_ com Python, fiz o script 
abaixo que recebe o arquivo markdown acima e imprime o índice formatado.

Basicamente, o script lê linha a linha do arquivo e _parseia_ a string, 
separando o título e timestamp (originalmente representando em segundos).

### 4.1. O script

```python
#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import re
import sys
import time


def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    regex = re.compile(r'^(- )\[(?P<title>.*)\]\((https:.*=(?P<timestamp>\d{0,4}))\)$')

    for line in lines:
        if re.match(regex, line):
            title, timestamp = re.match(regex, line).groupdict().values()
            print(time.strftime('%H:%M:%S', time.gmtime(int(timestamp))), 
                  title)


if __name__ == '__main__':
    main(*sys.argv[1:])    
```

### 4.2. A saída

Abaixo, a saída do processamento anterior. Esse índice pode ser inserido na 
descrição do Youtube, dando o efeito de divisões na timeline.

```
00:00:00 Django 101 - Saindo do zero
00:04:32 Instalando o Django
00:05:47 Conhecendo o comando django-admin
00:06:23 Criando o projeto
00:06:48 Conhecendo o comando ./manage
00:07:47 Criando uma app django
00:09:25 Conhecendo o arquivo urls.py
00:09:54 Conhecendo o arquivo settings.py
00:10:10 Instalando a app core
00:11:20 Como é composto um projeto Django
00:12:17 Criando o arquivo urls.py da app core
00:17:50 Conhecendo o comando ./manage check
00:18:52 Criando a função de consulta da app core
00:20:30 Criando o templates da app core
00:21:56 Conhecendo o comando ./manage runserver
00:24:56 Criando o arquivo models.py da app core
00:29:30 Criando e aplicando a primeira migração
00:31:01 Recuperando os registros na view
00:32:37 Resumo da arquitetura do projeto
00:37:32 Criando a url de cadastro da tarefa
00:37:59 Criando a função de cadastro da tarefa
00:38:52 Criando o arquivo forms.py da app core
00:45:23 Criando e ativando a venv
00:48:13 Renderizando o form a partir da view
00:49:28 Criando o arquivo form.html
00:52:31 Criando a lógica de inserção de dados no banco de dados
00:55:59 Criando a url de exibição da tarefa cadastrada
00:56:27 Criando a view de exibição da tarefa cadastrada
00:59:36 Criando o arquivo detail.html
01:01:40 Conhecendo o comando ./manage shell
01:03:15 Atualizando o html da consulta
01:05:37 Criando a view de exclusão da tarefa
01:06:31 Criando a url de exclusão da tarefa
01:07:26 Atualizando o html da consulta
01:08:21 Criando a view de atualização da tarefa
01:10:19 Criando a url de atualização da tarefa
01:14:42 Perguntas/Respostas
```
