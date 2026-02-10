#!/usr/bin/env python3
"""
Sistema de IA para Contabilidade de Empresas
AI Accounting System for Companies without Initial Conditions
"""

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import json


class TransactionType(Enum):
    """Tipos de transações contábeis"""
    RECEITA = "receita"  # Revenue
    DESPESA = "despesa"  # Expense
    ATIVO = "ativo"      # Asset
    PASSIVO = "passivo"  # Liability
    CAPITAL = "capital"  # Equity


class Transaction:
    """Representa uma transação contábil"""
    
    # Mapeamento de palavras-chave para categorias (IA de categorização)
    CATEGORY_KEYWORDS = {
        "Receitas de Vendas": ['venda', 'receita', 'pagamento cliente', 'faturamento'],
        "Despesas com Pessoal": ['salário', 'folha', 'pagamento funcionário'],
        "Despesas com Instalações": ['aluguel', 'condomínio', 'iptu'],
        "Despesas com Utilidades": ['energia', 'água', 'internet', 'telefone'],
        "Custo de Mercadorias": ['fornecedor', 'compra', 'matéria-prima'],
        "Despesas com Marketing": ['marketing', 'publicidade', 'propaganda'],
        "Ativos Fixos": ['equipamento', 'máquina', 'veículo', 'imóvel'],
        "Estoque": ['estoque', 'inventário'],
    }
    
    def __init__(self, description: str, amount: float, transaction_type: TransactionType, 
                 date: Optional[datetime] = None, category: Optional[str] = None):
        self.description = description
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date or datetime.now()
        self.category = category or self._auto_categorize()
    
    def _auto_categorize(self) -> str:
        """IA para categorização automática de transações"""
        description_lower = self.description.lower()
        
        # Verificar cada categoria baseada em palavras-chave
        for category, keywords in self.CATEGORY_KEYWORDS.items():
            if any(word in description_lower for word in keywords):
                return category
        
        # Categoria padrão baseada no tipo de transação
        if self.transaction_type == TransactionType.RECEITA:
            return "Outras Receitas"
        elif self.transaction_type == TransactionType.DESPESA:
            return "Outras Despesas"
        else:
            return "Outros"
    
    def to_dict(self) -> Dict:
        """Converte transação para dicionário"""
        return {
            'description': self.description,
            'amount': self.amount,
            'type': self.transaction_type.value,
            'date': self.date.isoformat(),
            'category': self.category
        }


class Company:
    """Representa uma empresa e sua contabilidade"""
    
    def __init__(self, name: str):
        self.name = name
        self.transactions: List[Transaction] = []
        self.creation_date = datetime.now()
    
    def add_transaction(self, description: str, amount: float, 
                       transaction_type: TransactionType) -> Transaction:
        """Adiciona uma transação"""
        transaction = Transaction(description, amount, transaction_type)
        self.transactions.append(transaction)
        return transaction
    
    def get_balance(self) -> float:
        """Calcula o saldo atual (receitas - despesas)"""
        receitas = sum(t.amount for t in self.transactions 
                      if t.transaction_type == TransactionType.RECEITA)
        despesas = sum(t.amount for t in self.transactions 
                      if t.transaction_type == TransactionType.DESPESA)
        return receitas - despesas
    
    def get_total_assets(self) -> float:
        """Calcula total de ativos"""
        return sum(t.amount for t in self.transactions 
                  if t.transaction_type == TransactionType.ATIVO)
    
    def get_total_liabilities(self) -> float:
        """Calcula total de passivos"""
        return sum(t.amount for t in self.transactions 
                  if t.transaction_type == TransactionType.PASSIVO)
    
    def get_equity(self) -> float:
        """Calcula patrimônio líquido"""
        capital = sum(t.amount for t in self.transactions 
                     if t.transaction_type == TransactionType.CAPITAL)
        return capital + self.get_balance()
    
    def generate_balance_sheet(self) -> Dict:
        """Gera balanço patrimonial"""
        return {
            'company': self.name,
            'date': datetime.now().isoformat(),
            'assets': self.get_total_assets(),
            'liabilities': self.get_total_liabilities(),
            'equity': self.get_equity(),
            'balance_check': self.get_total_assets() - (self.get_total_liabilities() + self.get_equity())
        }
    
    def generate_income_statement(self) -> Dict:
        """Gera demonstração de resultados"""
        receitas = sum(t.amount for t in self.transactions 
                      if t.transaction_type == TransactionType.RECEITA)
        despesas = sum(t.amount for t in self.transactions 
                      if t.transaction_type == TransactionType.DESPESA)
        
        # Categorizar despesas
        despesas_por_categoria = {}
        for t in self.transactions:
            if t.transaction_type == TransactionType.DESPESA:
                if t.category not in despesas_por_categoria:
                    despesas_por_categoria[t.category] = 0
                despesas_por_categoria[t.category] += t.amount
        
        return {
            'company': self.name,
            'date': datetime.now().isoformat(),
            'revenue': receitas,
            'expenses': despesas,
            'expenses_by_category': despesas_por_categoria,
            'net_income': receitas - despesas
        }
    
    def get_ai_recommendations(self) -> List[str]:
        """IA gera recomendações financeiras"""
        recommendations = []
        
        balance = self.get_balance()
        receitas = sum(t.amount for t in self.transactions 
                      if t.transaction_type == TransactionType.RECEITA)
        despesas = sum(t.amount for t in self.transactions 
                      if t.transaction_type == TransactionType.DESPESA)
        
        # Análise de lucratividade
        if despesas > 0:
            margin = (receitas - despesas) / receitas * 100 if receitas > 0 else 0
            if margin < 10:
                recommendations.append(
                    f"⚠️ Margem de lucro baixa ({margin:.1f}%). "
                    "Considere reduzir custos ou aumentar preços."
                )
            elif margin > 30:
                recommendations.append(
                    f"✅ Ótima margem de lucro ({margin:.1f}%). "
                    "Empresa está saudável financeiramente."
                )
        
        # Análise de saldo
        if balance < 0:
            recommendations.append(
                f"🔴 Saldo negativo (R$ {balance:.2f}). "
                "Urgente: buscar fontes de receita ou reduzir despesas."
            )
        elif balance > 0 and receitas > 0:
            recommendations.append(
                f"✅ Saldo positivo (R$ {balance:.2f}). "
                "Considere investir o excedente para crescimento."
            )
        
        # Análise de categorias de despesas
        if self.transactions:
            despesas_categorias = {}
            for t in self.transactions:
                if t.transaction_type == TransactionType.DESPESA:
                    if t.category not in despesas_categorias:
                        despesas_categorias[t.category] = 0
                    despesas_categorias[t.category] += t.amount
            
            if despesas_categorias:
                maior_despesa = max(despesas_categorias.items(), key=lambda x: x[1])
                if receitas > 0 and (maior_despesa[1] / receitas > 0.4):
                    recommendations.append(
                        f"💡 '{maior_despesa[0]}' representa {maior_despesa[1]/receitas*100:.1f}% "
                        "das receitas. Avaliar possibilidades de otimização."
                    )
        
        # Recomendação inicial
        if not self.transactions:
            recommendations.append(
                "📊 Sistema iniciado sem condições iniciais. "
                "Comece registrando suas transações para análise financeira."
            )
        
        return recommendations


class AccountingAI:
    """Sistema de IA para contabilidade"""
    
    def __init__(self):
        self.companies: Dict[str, Company] = {}
    
    def create_company(self, name: str) -> Company:
        """Cria uma nova empresa sem condições iniciais"""
        if name in self.companies:
            return self.companies[name]
        
        company = Company(name)
        self.companies[name] = company
        print(f"✅ Empresa '{name}' criada com sucesso!")
        print("💡 Sistema iniciado sem condições iniciais - pronto para uso!")
        return company
    
    def get_company(self, name: str) -> Optional[Company]:
        """Obtém uma empresa existente"""
        return self.companies.get(name)
    
    def generate_report(self, company_name: str) -> str:
        """Gera relatório completo de uma empresa"""
        company = self.get_company(company_name)
        if not company:
            return f"Empresa '{company_name}' não encontrada."
        
        report = f"\n{'='*60}\n"
        report += f"RELATÓRIO CONTÁBIL - {company.name}\n"
        report += f"{'='*60}\n\n"
        
        # Balanço Patrimonial
        balance_sheet = company.generate_balance_sheet()
        report += "📊 BALANÇO PATRIMONIAL\n"
        report += f"  Ativos:     R$ {balance_sheet['assets']:>12,.2f}\n"
        report += f"  Passivos:   R$ {balance_sheet['liabilities']:>12,.2f}\n"
        report += f"  Patrimônio: R$ {balance_sheet['equity']:>12,.2f}\n\n"
        
        # Demonstração de Resultados
        income_statement = company.generate_income_statement()
        report += "💰 DEMONSTRAÇÃO DE RESULTADOS\n"
        report += f"  Receitas:       R$ {income_statement['revenue']:>12,.2f}\n"
        report += f"  Despesas:       R$ {income_statement['expenses']:>12,.2f}\n"
        report += f"  Lucro Líquido:  R$ {income_statement['net_income']:>12,.2f}\n\n"
        
        if income_statement['expenses_by_category']:
            report += "📈 DESPESAS POR CATEGORIA\n"
            for category, amount in income_statement['expenses_by_category'].items():
                report += f"  {category}: R$ {amount:>12,.2f}\n"
            report += "\n"
        
        # Recomendações da IA
        recommendations = company.get_ai_recommendations()
        if recommendations:
            report += "🤖 RECOMENDAÇÕES DA IA\n"
            for i, rec in enumerate(recommendations, 1):
                report += f"  {i}. {rec}\n"
        
        report += f"\n{'='*60}\n"
        return report


def main():
    """Exemplo de uso do sistema"""
    print("🤖 Sistema de IA para Contabilidade")
    print("=" * 60)
    print("Sistema que funciona SEM condições iniciais!")
    print("=" * 60)
    
    # Criar sistema
    ai = AccountingAI()
    
    # Criar empresa sem condições iniciais
    empresa = ai.create_company("Minha Empresa Ltda")
    
    print("\n📝 Registrando transações de exemplo...\n")
    
    # Adicionar transações
    empresa.add_transaction("Venda de produtos", 5000.00, TransactionType.RECEITA)
    empresa.add_transaction("Venda de serviços", 3000.00, TransactionType.RECEITA)
    empresa.add_transaction("Salário funcionários", 2000.00, TransactionType.DESPESA)
    empresa.add_transaction("Aluguel escritório", 1000.00, TransactionType.DESPESA)
    empresa.add_transaction("Energia elétrica", 200.00, TransactionType.DESPESA)
    empresa.add_transaction("Internet", 150.00, TransactionType.DESPESA)
    empresa.add_transaction("Compra equipamento", 3000.00, TransactionType.ATIVO)
    empresa.add_transaction("Capital inicial", 10000.00, TransactionType.CAPITAL)
    
    # Gerar relatório
    print(ai.generate_report("Minha Empresa Ltda"))
    
    # Demonstrar exportação JSON
    print("\n📤 Exportando dados em JSON...")
    income_statement = empresa.generate_income_statement()
    print(json.dumps(income_statement, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
