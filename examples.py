#!/usr/bin/env python3
"""
Exemplo interativo do Sistema de IA para Contabilidade
"""

from accounting_ai import AccountingAI, TransactionType


def exemplo_basico():
    """Exemplo básico de uso"""
    print("\n" + "="*60)
    print("EXEMPLO 1: Uso Básico - Empresa Nova (SEM condições iniciais)")
    print("="*60)
    
    ai = AccountingAI()
    empresa = ai.create_company("Tech Startup Ltda")
    
    # Adicionar transações
    empresa.add_transaction("Receita de consultoria", 15000.00, TransactionType.RECEITA)
    empresa.add_transaction("Pagamento salários", 8000.00, TransactionType.DESPESA)
    empresa.add_transaction("Aluguel", 2000.00, TransactionType.DESPESA)
    
    print(ai.generate_report("Tech Startup Ltda"))


def exemplo_comercio():
    """Exemplo de comércio"""
    print("\n" + "="*60)
    print("EXEMPLO 2: Comércio - Começando do Zero")
    print("="*60)
    
    ai = AccountingAI()
    loja = ai.create_company("Loja de Roupas")
    
    # Primeiro mês de operação
    loja.add_transaction("Capital inicial dos sócios", 20000.00, TransactionType.CAPITAL)
    loja.add_transaction("Compra de estoque inicial", 15000.00, TransactionType.ATIVO)
    loja.add_transaction("Vendas semana 1", 5000.00, TransactionType.RECEITA)
    loja.add_transaction("Vendas semana 2", 6500.00, TransactionType.RECEITA)
    loja.add_transaction("Vendas semana 3", 7200.00, TransactionType.RECEITA)
    loja.add_transaction("Vendas semana 4", 8300.00, TransactionType.RECEITA)
    loja.add_transaction("Custo mercadorias vendidas", 12000.00, TransactionType.DESPESA)
    loja.add_transaction("Aluguel loja", 3000.00, TransactionType.DESPESA)
    loja.add_transaction("Salário vendedor", 2500.00, TransactionType.DESPESA)
    loja.add_transaction("Energia e água", 400.00, TransactionType.DESPESA)
    loja.add_transaction("Marketing Facebook Ads", 800.00, TransactionType.DESPESA)
    
    print(ai.generate_report("Loja de Roupas"))


def exemplo_prestacao_servicos():
    """Exemplo de prestação de serviços"""
    print("\n" + "="*60)
    print("EXEMPLO 3: Prestação de Serviços - Freelancer")
    print("="*60)
    
    ai = AccountingAI()
    freelancer = ai.create_company("Designer Freelancer")
    
    # Operação mensal
    freelancer.add_transaction("Projeto Cliente A", 3500.00, TransactionType.RECEITA)
    freelancer.add_transaction("Projeto Cliente B", 4200.00, TransactionType.RECEITA)
    freelancer.add_transaction("Projeto Cliente C", 2800.00, TransactionType.RECEITA)
    freelancer.add_transaction("Internet", 120.00, TransactionType.DESPESA)
    freelancer.add_transaction("Software Adobe", 250.00, TransactionType.DESPESA)
    freelancer.add_transaction("Energia", 150.00, TransactionType.DESPESA)
    freelancer.add_transaction("Computador", 5000.00, TransactionType.ATIVO)
    
    print(ai.generate_report("Designer Freelancer"))


def exemplo_com_problemas():
    """Exemplo de empresa com problemas financeiros"""
    print("\n" + "="*60)
    print("EXEMPLO 4: Empresa com Desafios Financeiros")
    print("="*60)
    
    ai = AccountingAI()
    empresa = ai.create_company("Empresa com Dificuldades")
    
    # Situação problemática
    empresa.add_transaction("Vendas do mês", 5000.00, TransactionType.RECEITA)
    empresa.add_transaction("Salários", 3500.00, TransactionType.DESPESA)
    empresa.add_transaction("Aluguel", 2000.00, TransactionType.DESPESA)
    empresa.add_transaction("Fornecedores", 1800.00, TransactionType.DESPESA)
    empresa.add_transaction("Utilidades", 500.00, TransactionType.DESPESA)
    empresa.add_transaction("Marketing", 1200.00, TransactionType.DESPESA)
    
    print(ai.generate_report("Empresa com Dificuldades"))
    print("\n💡 Note como a IA identifica os problemas e sugere ações!")


def demonstrar_categorizacao_automatica():
    """Demonstra a categorização automática da IA"""
    print("\n" + "="*60)
    print("EXEMPLO 5: Categorização Automática pela IA")
    print("="*60)
    
    ai = AccountingAI()
    empresa = ai.create_company("Demo Categorização")
    
    print("\n📋 Testando categorização automática:")
    
    transacoes_teste = [
        ("Venda de produtos para cliente", 1000.00, TransactionType.RECEITA),
        ("Pagamento folha de pessoal", 500.00, TransactionType.DESPESA),
        ("Conta de energia elétrica", 200.00, TransactionType.DESPESA),
        ("Compra de máquina industrial", 5000.00, TransactionType.ATIVO),
        ("Investimento em publicidade Google", 300.00, TransactionType.DESPESA),
    ]
    
    for desc, valor, tipo in transacoes_teste:
        t = empresa.add_transaction(desc, valor, tipo)
        print(f"  '{desc}' → Categoria: {t.category}")
    
    print(ai.generate_report("Demo Categorização"))


def main():
    """Executa todos os exemplos"""
    print("\n🤖 SISTEMA DE IA PARA CONTABILIDADE")
    print("Sistema que funciona COMPLETAMENTE SEM condições iniciais!")
    print("\nCaracterísticas:")
    print("  ✅ Não requer configuração inicial")
    print("  ✅ Categorização automática de transações")
    print("  ✅ Análise financeira inteligente")
    print("  ✅ Recomendações personalizadas")
    print("  ✅ Relatórios detalhados")
    
    exemplo_basico()
    exemplo_comercio()
    exemplo_prestacao_servicos()
    exemplo_com_problemas()
    demonstrar_categorizacao_automatica()
    
    print("\n" + "="*60)
    print("✅ Todos os exemplos executados com sucesso!")
    print("="*60)


if __name__ == "__main__":
    main()
