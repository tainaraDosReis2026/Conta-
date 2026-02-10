#!/usr/bin/env python3
"""
Testes para o Sistema de IA de Contabilidade
"""

from accounting_ai import AccountingAI, TransactionType, Transaction, Company


def test_company_creation():
    """Testa criação de empresa sem condições iniciais"""
    ai = AccountingAI()
    company = ai.create_company("Test Company")
    
    assert company.name == "Test Company"
    assert len(company.transactions) == 0
    print("✅ Teste de criação de empresa: PASSOU")


def test_transaction_addition():
    """Testa adição de transações"""
    company = Company("Test")
    
    t1 = company.add_transaction("Venda", 1000.00, TransactionType.RECEITA)
    assert len(company.transactions) == 1
    assert t1.amount == 1000.00
    
    t2 = company.add_transaction("Despesa", 500.00, TransactionType.DESPESA)
    assert len(company.transactions) == 2
    
    print("✅ Teste de adição de transações: PASSOU")


def test_balance_calculation():
    """Testa cálculo de saldo"""
    company = Company("Test")
    
    company.add_transaction("Receita 1", 1000.00, TransactionType.RECEITA)
    company.add_transaction("Receita 2", 500.00, TransactionType.RECEITA)
    company.add_transaction("Despesa 1", 300.00, TransactionType.DESPESA)
    
    balance = company.get_balance()
    assert balance == 1200.00, f"Expected 1200.00, got {balance}"
    
    print("✅ Teste de cálculo de saldo: PASSOU")


def test_auto_categorization():
    """Testa categorização automática"""
    company = Company("Test")
    
    # Teste de receitas
    t1 = company.add_transaction("Venda de produtos", 1000.00, TransactionType.RECEITA)
    assert "Receitas de Vendas" in t1.category or "Vendas" in t1.category
    
    # Teste de despesas
    t2 = company.add_transaction("Pagamento salários", 500.00, TransactionType.DESPESA)
    assert "Pessoal" in t2.category
    
    t3 = company.add_transaction("Aluguel escritório", 200.00, TransactionType.DESPESA)
    assert "Instalações" in t3.category
    
    t4 = company.add_transaction("Conta de energia", 100.00, TransactionType.DESPESA)
    assert "Utilidades" in t4.category
    
    print("✅ Teste de categorização automática: PASSOU")


def test_balance_sheet():
    """Testa geração de balanço patrimonial"""
    company = Company("Test")
    
    company.add_transaction("Capital", 10000.00, TransactionType.CAPITAL)
    company.add_transaction("Equipamento", 5000.00, TransactionType.ATIVO)
    company.add_transaction("Empréstimo", 3000.00, TransactionType.PASSIVO)
    
    balance_sheet = company.generate_balance_sheet()
    
    assert balance_sheet['assets'] == 5000.00
    assert balance_sheet['liabilities'] == 3000.00
    assert 'equity' in balance_sheet
    
    print("✅ Teste de balanço patrimonial: PASSOU")


def test_income_statement():
    """Testa geração de DRE"""
    company = Company("Test")
    
    company.add_transaction("Vendas", 5000.00, TransactionType.RECEITA)
    company.add_transaction("Custo", 2000.00, TransactionType.DESPESA)
    company.add_transaction("Despesa", 1000.00, TransactionType.DESPESA)
    
    income = company.generate_income_statement()
    
    assert income['revenue'] == 5000.00
    assert income['expenses'] == 3000.00
    assert income['net_income'] == 2000.00
    
    print("✅ Teste de demonstração de resultados: PASSOU")


def test_ai_recommendations():
    """Testa recomendações da IA"""
    company = Company("Test")
    
    # Caso 1: Empresa com boa margem
    company.add_transaction("Receita", 10000.00, TransactionType.RECEITA)
    company.add_transaction("Despesa", 3000.00, TransactionType.DESPESA)
    
    recommendations = company.get_ai_recommendations()
    assert len(recommendations) > 0
    assert any("positivo" in rec.lower() for rec in recommendations)
    
    print("✅ Teste de recomendações da IA: PASSOU")


def test_negative_balance_warning():
    """Testa alerta de saldo negativo"""
    company = Company("Test")
    
    company.add_transaction("Receita", 1000.00, TransactionType.RECEITA)
    company.add_transaction("Despesa", 2000.00, TransactionType.DESPESA)
    
    recommendations = company.get_ai_recommendations()
    assert any("negativo" in rec.lower() for rec in recommendations)
    
    print("✅ Teste de alerta de saldo negativo: PASSOU")


def test_no_initial_conditions():
    """Testa que o sistema funciona sem condições iniciais"""
    # Este é o teste mais importante: criar empresa vazia e começar a usar
    ai = AccountingAI()
    company = ai.create_company("Nova Empresa")
    
    # Empresa deve estar pronta para uso imediatamente
    assert company is not None
    assert len(company.transactions) == 0
    
    # Deve funcionar mesmo sem nenhuma transação
    balance_sheet = company.generate_balance_sheet()
    assert balance_sheet['assets'] == 0.0
    
    income = company.generate_income_statement()
    assert income['revenue'] == 0.0
    
    # Deve gerar recomendações mesmo sem transações
    recommendations = company.get_ai_recommendations()
    assert len(recommendations) > 0
    
    print("✅ Teste SEM condições iniciais: PASSOU")


def run_all_tests():
    """Executa todos os testes"""
    print("\n" + "="*60)
    print("🧪 EXECUTANDO TESTES DO SISTEMA DE IA")
    print("="*60 + "\n")
    
    tests = [
        test_no_initial_conditions,  # Teste mais importante primeiro!
        test_company_creation,
        test_transaction_addition,
        test_balance_calculation,
        test_auto_categorization,
        test_balance_sheet,
        test_income_statement,
        test_ai_recommendations,
        test_negative_balance_warning,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__}: FALHOU - {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__}: ERRO - {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"RESULTADOS: {passed} passou, {failed} falhou")
    print("="*60)
    
    if failed == 0:
        print("✅ TODOS OS TESTES PASSARAM!")
        return True
    else:
        print("❌ ALGUNS TESTES FALHARAM!")
        return False


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
