# 🤖 Sistema de IA para Contabilidade

Um sistema inteligente de contabilidade para empresas que **funciona completamente sem condições iniciais**.

## 🎯 Características Principais

- ✅ **Sem Configuração Inicial**: Comece a usar imediatamente, sem necessidade de definir plano de contas ou configurações complexas
- 🤖 **Categorização Automática**: IA categoriza transações automaticamente baseada em descrição
- 📊 **Relatórios Inteligentes**: Balanço patrimonial, DRE e análises financeiras
- 💡 **Recomendações Personalizadas**: IA analisa sua situação financeira e sugere ações
- 🌐 **100% em Português**: Interface e mensagens totalmente em português brasileiro
- 🔧 **Zero Dependências**: Usa apenas bibliotecas padrão do Python

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/tainaraDosReis2026/Conta-.git
cd Conta-

# Execute (requer Python 3.6+)
python3 accounting_ai.py
```

## 🚀 Uso Rápido

```python
from accounting_ai import AccountingAI, TransactionType

# Crie o sistema de IA
ai = AccountingAI()

# Crie uma empresa (SEM condições iniciais!)
empresa = ai.create_company("Minha Empresa")

# Adicione transações
empresa.add_transaction("Venda de produtos", 5000.00, TransactionType.RECEITA)
empresa.add_transaction("Salário funcionários", 2000.00, TransactionType.DESPESA)
empresa.add_transaction("Aluguel", 1000.00, TransactionType.DESPESA)

# Gere relatório completo
print(ai.generate_report("Minha Empresa"))
```

## 📋 Tipos de Transações

- `TransactionType.RECEITA` - Receitas e vendas
- `TransactionType.DESPESA` - Despesas e custos
- `TransactionType.ATIVO` - Ativos (equipamentos, estoque, etc.)
- `TransactionType.PASSIVO` - Passivos e obrigações
- `TransactionType.CAPITAL` - Capital e investimentos

## 🎓 Exemplos

Execute os exemplos completos:

```bash
python3 examples.py
```

### Exemplo 1: Empresa de Serviços

```python
ai = AccountingAI()
empresa = ai.create_company("Tech Consulting")

empresa.add_transaction("Consultoria Cliente A", 10000.00, TransactionType.RECEITA)
empresa.add_transaction("Salários", 5000.00, TransactionType.DESPESA)
empresa.add_transaction("Equipamentos", 3000.00, TransactionType.ATIVO)

print(ai.generate_report("Tech Consulting"))
```

### Exemplo 2: Comércio

```python
loja = ai.create_company("Loja de Roupas")

loja.add_transaction("Capital inicial", 20000.00, TransactionType.CAPITAL)
loja.add_transaction("Vendas do mês", 15000.00, TransactionType.RECEITA)
loja.add_transaction("Compra mercadorias", 8000.00, TransactionType.DESPESA)
loja.add_transaction("Aluguel loja", 2000.00, TransactionType.DESPESA)

print(ai.generate_report("Loja de Roupas"))
```

## 🤖 Recursos de IA

### Categorização Automática

A IA analisa a descrição das transações e categoriza automaticamente:

- "Venda de produtos" → Receitas de Vendas
- "Salário funcionários" → Despesas com Pessoal
- "Aluguel escritório" → Despesas com Instalações
- "Conta de energia" → Despesas com Utilidades
- "Compra equipamento" → Ativos Fixos

### Análise Financeira Inteligente

O sistema analisa automaticamente:

- **Margem de lucro**: Identifica se está saudável ou precisa melhorias
- **Fluxo de caixa**: Alerta sobre saldo negativo ou positivo
- **Estrutura de custos**: Identifica categorias de despesas muito altas
- **Saúde financeira**: Recomendações personalizadas para seu negócio

### Exemplo de Recomendações

```
🤖 RECOMENDAÇÕES DA IA
  1. ✅ Ótima margem de lucro (58.1%). Empresa está saudável financeiramente.
  2. ✅ Saldo positivo (R$ 4650.00). Considere investir o excedente para crescimento.
  3. 💡 'Despesas com Pessoal' representa 53.3% das receitas. Avaliar possibilidades de otimização.
```

## 📊 Relatórios Disponíveis

### Balanço Patrimonial
- Total de Ativos
- Total de Passivos
- Patrimônio Líquido

### Demonstração de Resultados (DRE)
- Receitas totais
- Despesas por categoria
- Lucro líquido

### Análise de Categorias
- Despesas detalhadas por categoria
- Percentual de cada categoria sobre receita

## 🏗️ Estrutura do Projeto

```
Conta-/
├── accounting_ai.py    # Sistema principal de IA
├── examples.py         # Exemplos de uso
├── requirements.txt    # Dependências (nenhuma externa!)
└── README.md          # Esta documentação
```

## 🔧 Classes Principais

### `AccountingAI`
Sistema principal que gerencia empresas

### `Company`
Representa uma empresa e suas transações

### `Transaction`
Representa uma transação contábil com categorização automática

## 💻 Requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa

## 🌟 Diferenciais

1. **Zero Setup**: Não precisa configurar plano de contas, categorias ou regras
2. **IA Integrada**: Categorização e análise automáticas
3. **Português Nativo**: Desenvolvido pensando no mercado brasileiro
4. **Leve**: Sem dependências externas, fácil de integrar
5. **Extensível**: Código limpo e fácil de customizar

## 📝 Licença

Este projeto é open source e está disponível para uso livre.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📞 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório.

---

Desenvolvido com ❤️ para simplificar a contabilidade de empresas brasileiras
