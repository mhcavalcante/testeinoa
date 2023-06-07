# Projeto Inoa

# Teste Inoa

Esse projeto foi desenvolvido baseado em requisitos do desafio Inoa.

### Instruções de instalação

O projeto foi realizado utilizando o Python versão 3.10.7 e Django versão 4.2.1. O link a seguir também conta com a instalação do pip e do virtualenv, que foram utilizados durante a construção do projeto.

[https://docs.djangoproject.com/en/4.2/intro/install/](https://docs.djangoproject.com/en/4.2/intro/install/)

### Requerimentos do projeto

O projeto conta com um arquivo nomeado requirements.txt, que indica todos os pacotes necessários para rodá-lo. Com esse arquivo, é possível baixar todos os pacotes com apenas um comando no terminal.

```bash
pip install -r requirements.txt
```

### Configurações adicionais

Para enviar e-mails de notificação (compra e venda) deve-se fornecer um endereço de remetente e senha válida no arquivo ‘settings.py’. A autenticação que utilizei para testes com o Gmail requer a configuração de uma "senha de aplicativos". Essa opção é encontrada nas configurações do Gmail.

Para configurá-lo será necessário alterar as linhas com as informações de remetente:

```python
EMAIL_HOST_USER = ‘exemplo@gmail.com’
EMAIL_HOST_PASSWORD = ‘senha’
DEFAULT_FROM_EMAIL = ‘exemplo@gmail.com’
```

### Iniciar a aplicação

Para que o projeto funcione corretamente, existe a necessidade de rodar o serviço de obter cotações e enviar emails em background (django4-background-tasks). Para tanto, abra um novo terminal e utilize o seguinte comando :

```bash
py [manage.py](http://manage.py) process_tasks
```

Obs: Mantenha o terminal em execução durante o uso da aplicação.

### URLs

O aplicativo pode ser acessado utilizando a URL ‘host:port’. Exemplo: 127.0.0.1:8000

A partir dessa teremos outras URLs:

- Listar Ativos: acessada via ‘host:port/assets’
- Monitorar Ativos via ‘host:port/assets/add’
- Editar Ativos via ‘host:port/assets/update/{id}’
- Histórico via ‘host:port/assets/history/{id}’

Onde {id} é o código do ativo

### Telas

Index
![Untitled](https://github.com/mhcavalcante/testeinoa/assets/54690352/09443925-a0f9-4fba-aa10-680240e5514e)

Listar Ativos
![Untitled 1](https://github.com/mhcavalcante/testeinoa/assets/54690352/17329bee-b015-4076-8293-f68b2baf6ac7)

Monitorar Ativos
![Untitled 2](https://github.com/mhcavalcante/testeinoa/assets/54690352/84b6235d-3fa9-470f-85bf-d5780131a0ff)
