# FlaskApiRest
Projeto API Rest Python em Flask 


## Como rodar a aplicação em flask
Você deve criar um virtualenv e instalar as dependências que estão salvas em _requirements.txt_. Para executar a aplicação, basta chamar o arquivo main com o interpretador do python, da seguinte forma:

```bash
$ python main.py
```

## Como rodar a aplicação em wsgi
Para executar a aplicação, basta chamar o arquivo main com o comando abaixo, da seguinte forma:

```bash
$ uwsgi --ini="uwsgi.ini"
```

A aplicação será executada em _localhost_ na porta padrão 5000, conforme podemos verificar abaixo.

![](exemplo-execucao.png)

<br />

## Info

Se precisar de ajuda, a [seção info](./docs/info.md) da docs pode te auxiliar com links e informações úteis.