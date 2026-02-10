#!/usr/bin/env python3
"""
CLI (Command Line Interface) para o Sistema de IA de Contabilidade
Interface interativa para uso do sistema via terminal
"""

import sys
from accounting_ai import AccountingAI, TransactionType


class AccountingCLI:
    """Interface de linha de comando para o sistema de contabilidade"""
    
    def __init__(self):
        self.ai = AccountingAI()
        self.current_company = None
    
    def print_menu(self):
        """Exibe menu principal"""
        print("\n" + "="*60)
        print("🤖 SISTEMA DE IA PARA CONTABILIDADE")
        print("="*60)
        if self.current_company:
            print(f"📊 Empresa atual: {self.current_company}")
        else:
            print("📊 Nenhuma empresa selecionada")
        print("\nOpções:")
        print("  1. Criar/Selecionar empresa")
        print("  2. Adicionar transação")
        print("  3. Ver relatório completo")
        print("  4. Ver recomendações da IA")
        print("  5. Listar empresas")
        print("  0. Sair")
        print("="*60)
    
    def create_or_select_company(self):
        """Cria ou seleciona uma empresa"""
        name = input("\n📝 Nome da empresa: ").strip()
        if not name:
            print("❌ Nome inválido!")
            return
        
        company = self.ai.create_company(name)
        self.current_company = name
        print(f"✅ Empresa '{name}' selecionada!")
    
    def add_transaction(self):
        """Adiciona uma transação"""
        if not self.current_company:
            print("❌ Selecione uma empresa primeiro (opção 1)")
            return
        
        company = self.ai.get_company(self.current_company)
        
        print("\n💰 Nova Transação")
        description = input("Descrição: ").strip()
        if not description:
            print("❌ Descrição inválida!")
            return
        
        try:
            amount = float(input("Valor (R$): ").strip())
        except ValueError:
            print("❌ Valor inválido!")
            return
        
        print("\nTipo de transação:")
        print("  1. Receita")
        print("  2. Despesa")
        print("  3. Ativo")
        print("  4. Passivo")
        print("  5. Capital")
        
        type_choice = input("Escolha (1-5): ").strip()
        
        type_map = {
            '1': TransactionType.RECEITA,
            '2': TransactionType.DESPESA,
            '3': TransactionType.ATIVO,
            '4': TransactionType.PASSIVO,
            '5': TransactionType.CAPITAL
        }
        
        if type_choice not in type_map:
            print("❌ Opção inválida!")
            return
        
        transaction = company.add_transaction(description, amount, type_map[type_choice])
        print(f"\n✅ Transação adicionada!")
        print(f"   Categoria automática: {transaction.category}")
    
    def show_report(self):
        """Exibe relatório completo"""
        if not self.current_company:
            print("❌ Selecione uma empresa primeiro (opção 1)")
            return
        
        print(self.ai.generate_report(self.current_company))
    
    def show_recommendations(self):
        """Exibe apenas as recomendações"""
        if not self.current_company:
            print("❌ Selecione uma empresa primeiro (opção 1)")
            return
        
        company = self.ai.get_company(self.current_company)
        recommendations = company.get_ai_recommendations()
        
        print("\n" + "="*60)
        print("🤖 RECOMENDAÇÕES DA IA")
        print("="*60)
        
        if recommendations:
            for i, rec in enumerate(recommendations, 1):
                print(f"{i}. {rec}")
        else:
            print("Nenhuma recomendação no momento.")
        
        print("="*60)
    
    def list_companies(self):
        """Lista todas as empresas"""
        print("\n" + "="*60)
        print("📋 EMPRESAS CADASTRADAS")
        print("="*60)
        
        if not self.ai.companies:
            print("Nenhuma empresa cadastrada ainda.")
        else:
            for i, name in enumerate(self.ai.companies.keys(), 1):
                company = self.ai.companies[name]
                num_transactions = len(company.transactions)
                balance = company.get_balance()
                print(f"{i}. {name}")
                print(f"   Transações: {num_transactions}")
                print(f"   Saldo: R$ {balance:,.2f}")
        
        print("="*60)
    
    def run(self):
        """Executa o CLI"""
        print("\n🤖 Bem-vindo ao Sistema de IA para Contabilidade!")
        print("Sistema que funciona SEM condições iniciais!")
        
        while True:
            self.print_menu()
            choice = input("\nEscolha uma opção: ").strip()
            
            if choice == '0':
                print("\n👋 Até logo!")
                break
            elif choice == '1':
                self.create_or_select_company()
            elif choice == '2':
                self.add_transaction()
            elif choice == '3':
                self.show_report()
            elif choice == '4':
                self.show_recommendations()
            elif choice == '5':
                self.list_companies()
            else:
                print("❌ Opção inválida!")
            
            input("\nPressione ENTER para continuar...")


def main():
    """Ponto de entrada do CLI"""
    try:
        cli = AccountingCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Até logo!")
        sys.exit(0)


if __name__ == "__main__":
    main()
