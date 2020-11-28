# Criando um ambiente virtual Python

## Instalando pyenv

- Atualizar a listas de pacotes:

```bash
sudo apt-get update
```

- Instalar as dependências:

```bash
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev \
tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2
```

- Instalar o pyenv

```bash
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

- Editar o arquivo ~/.bashrc

```bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

- Reinicie o terminal

## Configurando o pyenv

- Instale a versão do Python no pyenv

```bash
pyenv install 3.8.6
```

- Defina a versão instalada como atual

```bash
pyenv global 3.8.6
```

## Criando o ambiente virtual

- Crie um novo ambiente virtual 

```bash
python -m venv .venv
```

- Ative o ambiente

```bash
source .venv/bin/activate
```