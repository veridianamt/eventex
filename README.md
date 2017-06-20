# Eventex 

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/veridianamt/eventex.svg?branch=master)](https://travis-ci.org/veridianamt/eventex)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6.
3. Ative o seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:veridianamt/eventex.git wttd
cd wttd
python -m venv .wttd
call .wttd/Scripts/activate
pip intall -r requirements.txt
copy contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstância
heroku config:push
heroku config:set SECRET_KEY=python contrib/secret_gen.py
heroku config:set DEBUG=False
# configuro o email
heroku git push master --force
```

