# Sistema de Contabilidade para Pequenas Empresas

Um aplicativo web completo de contabilidade desenvolvido especificamente para pequenas empresas, oferecendo gestão financeira simplificada e eficiente.

## 📋 Funcionalidades

- **Dashboard Financeiro**: Visualização rápida de receitas, despesas e saldo
- **Gestão de Lançamentos**: Registro de todas as transações financeiras (receitas e despesas)
- **Cadastro de Clientes**: Gerenciamento completo de clientes
- **Cadastro de Fornecedores**: Controle de fornecedores
- **Plano de Contas**: Sistema contábil estruturado seguindo padrões brasileiros
- **Relatórios Financeiros**:
  - DRE (Demonstração do Resultado do Exercício)
  - Fluxo de Caixa
  - Balanço Patrimonial

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/tainaraDosReis2026/Conta-.git
cd Conta-
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python app.py
```

4. Acesse no navegador:
```
http://localhost:5000
```

### Produção

⚠️ **IMPORTANTE**: Para ambiente de produção:

1. Desabilite o modo debug:
```bash
export FLASK_DEBUG=False
python app.py
```

2. Use um servidor WSGI de produção como Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 💻 Tecnologias Utilizadas

- **Backend**: Python Flask
- **Banco de Dados**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: RESTful API

## 📊 Estrutura do Projeto

```
Conta-/
├── app.py              # Aplicação Flask principal
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html      # Interface web
└── README.md          # Documentação
```

## 🔧 API Endpoints

### Empresas
- `GET /api/empresas` - Listar empresas
- `POST /api/empresas` - Criar empresa
- `GET /api/empresas/<id>` - Obter empresa
- `PUT /api/empresas/<id>` - Atualizar empresa
- `DELETE /api/empresas/<id>` - Deletar empresa

### Clientes
- `GET /api/clientes` - Listar clientes
- `POST /api/clientes` - Criar cliente
- `GET /api/clientes/<id>` - Obter cliente
- `PUT /api/clientes/<id>` - Atualizar cliente
- `DELETE /api/clientes/<id>` - Deletar cliente

### Fornecedores
- `GET /api/fornecedores` - Listar fornecedores
- `POST /api/fornecedores` - Criar fornecedor
- `GET /api/fornecedores/<id>` - Obter fornecedor
- `PUT /api/fornecedores/<id>` - Atualizar fornecedor
- `DELETE /api/fornecedores/<id>` - Deletar fornecedor

### Lançamentos
- `GET /api/lancamentos` - Listar lançamentos
- `POST /api/lancamentos` - Criar lançamento
- `GET /api/lancamentos/<id>` - Obter lançamento
- `PUT /api/lancamentos/<id>` - Atualizar lançamento
- `DELETE /api/lancamentos/<id>` - Deletar lançamento

### Plano de Contas
- `GET /api/plano-contas` - Listar contas
- `POST /api/plano-contas` - Criar conta
- `GET /api/plano-contas/<id>` - Obter conta
- `PUT /api/plano-contas/<id>` - Atualizar conta
- `DELETE /api/plano-contas/<id>` - Deletar conta

### Relatórios
- `GET /api/relatorios/dre?inicio=YYYY-MM-DD&fim=YYYY-MM-DD` - DRE
- `GET /api/relatorios/fluxo-caixa?inicio=YYYY-MM-DD&fim=YYYY-MM-DD` - Fluxo de Caixa
- `GET /api/relatorios/balanco` - Balanço Patrimonial

## 📝 Uso Básico

1. **Registrar Lançamentos**: Na aba "Lançamentos", adicione receitas e despesas
2. **Cadastrar Clientes/Fornecedores**: Use as abas específicas para gerenciar contatos
3. **Visualizar Dashboard**: A aba "Dashboard" mostra resumo financeiro
4. **Gerar Relatórios**: Na aba "Relatórios", gere DRE e Fluxo de Caixa

## 🎯 Plano de Contas Padrão

O sistema já vem com um plano de contas básico:
- **Ativos**: Caixa, Bancos, Contas a Receber
- **Passivos**: Fornecedores, Contas a Pagar
- **Patrimônio**: Capital Social
- **Receitas**: Vendas, Serviços
- **Despesas**: Operacionais, Administrativas

## 🔒 Segurança

- Banco de dados SQLite local
- Validação de dados no backend
- Proteção contra SQL Injection via SQLAlchemy ORM

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

## 👥 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📧 Suporte

Para dúvidas ou suporte, abra uma issue no repositório do GitHub.
