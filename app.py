from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from decimal import Decimal
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contabilidade.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

# Modelos do Banco de Dados

class Empresa(db.Model):
    """Modelo para empresa"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    endereco = db.Column(db.String(300))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, default=lambda: datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'email': self.email,
            'data_cadastro': self.data_cadastro.strftime('%Y-%m-%d')
        }


class PlanoContas(db.Model):
    """Plano de Contas"""
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # ATIVO, PASSIVO, RECEITA, DESPESA, PATRIMONIO
    natureza = db.Column(db.String(20), nullable=False)  # DEVEDORA, CREDORA
    
    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'nome': self.nome,
            'tipo': self.tipo,
            'natureza': self.natureza
        }


class Cliente(db.Model):
    """Modelo para clientes"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    cpf_cnpj = db.Column(db.String(18))
    endereco = db.Column(db.String(300))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, default=lambda: datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf_cnpj': self.cpf_cnpj,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'email': self.email,
            'data_cadastro': self.data_cadastro.strftime('%Y-%m-%d')
        }


class Fornecedor(db.Model):
    """Modelo para fornecedores"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.String(18))
    endereco = db.Column(db.String(300))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, default=lambda: datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'endereco': self.endereco,
            'telefone': self.telefone,
            'email': self.email,
            'data_cadastro': self.data_cadastro.strftime('%Y-%m-%d')
        }


class Lancamento(db.Model):
    """Lançamentos contábeis"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False, default=lambda: datetime.utcnow().date())
    descricao = db.Column(db.String(300), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # RECEITA, DESPESA
    categoria = db.Column(db.String(100))
    conta_id = db.Column(db.Integer, db.ForeignKey('plano_contas.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))
    
    conta = db.relationship('PlanoContas', backref='lancamentos')
    cliente = db.relationship('Cliente', backref='lancamentos')
    fornecedor = db.relationship('Fornecedor', backref='lancamentos')

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.strftime('%Y-%m-%d'),
            'descricao': self.descricao,
            'valor': self.valor,
            'tipo': self.tipo,
            'categoria': self.categoria,
            'conta_id': self.conta_id,
            'conta_nome': self.conta.nome if self.conta else None,
            'cliente_id': self.cliente_id,
            'cliente_nome': self.cliente.nome if self.cliente else None,
            'fornecedor_id': self.fornecedor_id,
            'fornecedor_nome': self.fornecedor.nome if self.fornecedor else None
        }


# Rotas da API

@app.route('/')
def index():
    return render_template('index.html')


# Empresas
@app.route('/api/empresas', methods=['GET', 'POST'])
def empresas():
    if request.method == 'POST':
        dados = request.json
        if not dados or 'nome' not in dados or 'cnpj' not in dados:
            return jsonify({'error': 'Nome e CNPJ são obrigatórios'}), 400
        empresa = Empresa(
            nome=dados['nome'],
            cnpj=dados['cnpj'],
            endereco=dados.get('endereco'),
            telefone=dados.get('telefone'),
            email=dados.get('email')
        )
        db.session.add(empresa)
        db.session.commit()
        return jsonify(empresa.to_dict()), 201
    
    empresas = Empresa.query.all()
    return jsonify([e.to_dict() for e in empresas])


@app.route('/api/empresas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def empresa_detail(id):
    empresa = Empresa.query.get_or_404(id)
    
    if request.method == 'DELETE':
        db.session.delete(empresa)
        db.session.commit()
        return '', 204
    
    if request.method == 'PUT':
        dados = request.json
        empresa.nome = dados.get('nome', empresa.nome)
        empresa.cnpj = dados.get('cnpj', empresa.cnpj)
        empresa.endereco = dados.get('endereco', empresa.endereco)
        empresa.telefone = dados.get('telefone', empresa.telefone)
        empresa.email = dados.get('email', empresa.email)
        db.session.commit()
        return jsonify(empresa.to_dict())
    
    return jsonify(empresa.to_dict())


# Plano de Contas
@app.route('/api/plano-contas', methods=['GET', 'POST'])
def plano_contas():
    if request.method == 'POST':
        dados = request.json
        conta = PlanoContas(
            codigo=dados['codigo'],
            nome=dados['nome'],
            tipo=dados['tipo'],
            natureza=dados['natureza']
        )
        db.session.add(conta)
        db.session.commit()
        return jsonify(conta.to_dict()), 201
    
    contas = PlanoContas.query.all()
    return jsonify([c.to_dict() for c in contas])


@app.route('/api/plano-contas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def plano_contas_detail(id):
    conta = PlanoContas.query.get_or_404(id)
    
    if request.method == 'DELETE':
        db.session.delete(conta)
        db.session.commit()
        return '', 204
    
    if request.method == 'PUT':
        dados = request.json
        conta.codigo = dados.get('codigo', conta.codigo)
        conta.nome = dados.get('nome', conta.nome)
        conta.tipo = dados.get('tipo', conta.tipo)
        conta.natureza = dados.get('natureza', conta.natureza)
        db.session.commit()
        return jsonify(conta.to_dict())
    
    return jsonify(conta.to_dict())


# Clientes
@app.route('/api/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        dados = request.json
        cliente = Cliente(
            nome=dados['nome'],
            cpf_cnpj=dados.get('cpf_cnpj'),
            endereco=dados.get('endereco'),
            telefone=dados.get('telefone'),
            email=dados.get('email')
        )
        db.session.add(cliente)
        db.session.commit()
        return jsonify(cliente.to_dict()), 201
    
    clientes = Cliente.query.all()
    return jsonify([c.to_dict() for c in clientes])


@app.route('/api/clientes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def cliente_detail(id):
    cliente = Cliente.query.get_or_404(id)
    
    if request.method == 'DELETE':
        db.session.delete(cliente)
        db.session.commit()
        return '', 204
    
    if request.method == 'PUT':
        dados = request.json
        cliente.nome = dados.get('nome', cliente.nome)
        cliente.cpf_cnpj = dados.get('cpf_cnpj', cliente.cpf_cnpj)
        cliente.endereco = dados.get('endereco', cliente.endereco)
        cliente.telefone = dados.get('telefone', cliente.telefone)
        cliente.email = dados.get('email', cliente.email)
        db.session.commit()
        return jsonify(cliente.to_dict())
    
    return jsonify(cliente.to_dict())


# Fornecedores
@app.route('/api/fornecedores', methods=['GET', 'POST'])
def fornecedores():
    if request.method == 'POST':
        dados = request.json
        fornecedor = Fornecedor(
            nome=dados['nome'],
            cnpj=dados.get('cnpj'),
            endereco=dados.get('endereco'),
            telefone=dados.get('telefone'),
            email=dados.get('email')
        )
        db.session.add(fornecedor)
        db.session.commit()
        return jsonify(fornecedor.to_dict()), 201
    
    fornecedores = Fornecedor.query.all()
    return jsonify([f.to_dict() for f in fornecedores])


@app.route('/api/fornecedores/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def fornecedor_detail(id):
    fornecedor = Fornecedor.query.get_or_404(id)
    
    if request.method == 'DELETE':
        db.session.delete(fornecedor)
        db.session.commit()
        return '', 204
    
    if request.method == 'PUT':
        dados = request.json
        fornecedor.nome = dados.get('nome', fornecedor.nome)
        fornecedor.cnpj = dados.get('cnpj', fornecedor.cnpj)
        fornecedor.endereco = dados.get('endereco', fornecedor.endereco)
        fornecedor.telefone = dados.get('telefone', fornecedor.telefone)
        fornecedor.email = dados.get('email', fornecedor.email)
        db.session.commit()
        return jsonify(fornecedor.to_dict())
    
    return jsonify(fornecedor.to_dict())


# Lançamentos
@app.route('/api/lancamentos', methods=['GET', 'POST'])
def lancamentos():
    if request.method == 'POST':
        dados = request.json
        lancamento = Lancamento(
            data=datetime.strptime(dados['data'], '%Y-%m-%d').date(),
            descricao=dados['descricao'],
            valor=float(dados['valor']),
            tipo=dados['tipo'],
            categoria=dados.get('categoria'),
            conta_id=dados.get('conta_id'),
            cliente_id=dados.get('cliente_id'),
            fornecedor_id=dados.get('fornecedor_id')
        )
        db.session.add(lancamento)
        db.session.commit()
        return jsonify(lancamento.to_dict()), 201
    
    lancamentos = Lancamento.query.order_by(Lancamento.data.desc()).all()
    return jsonify([l.to_dict() for l in lancamentos])


@app.route('/api/lancamentos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def lancamento_detail(id):
    lancamento = Lancamento.query.get_or_404(id)
    
    if request.method == 'DELETE':
        db.session.delete(lancamento)
        db.session.commit()
        return '', 204
    
    if request.method == 'PUT':
        dados = request.json
        if 'data' in dados:
            lancamento.data = datetime.strptime(dados['data'], '%Y-%m-%d').date()
        lancamento.descricao = dados.get('descricao', lancamento.descricao)
        lancamento.valor = float(dados.get('valor', lancamento.valor))
        lancamento.tipo = dados.get('tipo', lancamento.tipo)
        lancamento.categoria = dados.get('categoria', lancamento.categoria)
        lancamento.conta_id = dados.get('conta_id', lancamento.conta_id)
        lancamento.cliente_id = dados.get('cliente_id', lancamento.cliente_id)
        lancamento.fornecedor_id = dados.get('fornecedor_id', lancamento.fornecedor_id)
        db.session.commit()
        return jsonify(lancamento.to_dict())
    
    return jsonify(lancamento.to_dict())


# Relatórios
@app.route('/api/relatorios/balanco', methods=['GET'])
def balanco():
    """Relatório de balanço patrimonial"""
    ativos = db.session.query(
        PlanoContas.nome,
        db.func.sum(Lancamento.valor).label('total')
    ).join(Lancamento).filter(
        PlanoContas.tipo == 'ATIVO'
    ).group_by(PlanoContas.nome).all()
    
    passivos = db.session.query(
        PlanoContas.nome,
        db.func.sum(Lancamento.valor).label('total')
    ).join(Lancamento).filter(
        PlanoContas.tipo == 'PASSIVO'
    ).group_by(PlanoContas.nome).all()
    
    patrimonio = db.session.query(
        PlanoContas.nome,
        db.func.sum(Lancamento.valor).label('total')
    ).join(Lancamento).filter(
        PlanoContas.tipo == 'PATRIMONIO'
    ).group_by(PlanoContas.nome).all()
    
    return jsonify({
        'ativos': [{'nome': a[0], 'valor': a[1]} for a in ativos],
        'passivos': [{'nome': p[0], 'valor': p[1]} for p in passivos],
        'patrimonio': [{'nome': p[0], 'valor': p[1]} for p in patrimonio]
    })


@app.route('/api/relatorios/dre', methods=['GET'])
def dre():
    """Demonstração do Resultado do Exercício (DRE)"""
    periodo_inicio = request.args.get('inicio')
    periodo_fim = request.args.get('fim')
    
    query = Lancamento.query
    if periodo_inicio:
        query = query.filter(Lancamento.data >= datetime.strptime(periodo_inicio, '%Y-%m-%d').date())
    if periodo_fim:
        query = query.filter(Lancamento.data <= datetime.strptime(periodo_fim, '%Y-%m-%d').date())
    
    receitas = query.filter(Lancamento.tipo == 'RECEITA').all()
    despesas = query.filter(Lancamento.tipo == 'DESPESA').all()
    
    total_receitas = sum(l.valor for l in receitas)
    total_despesas = sum(l.valor for l in despesas)
    lucro = total_receitas - total_despesas
    
    return jsonify({
        'receitas': [l.to_dict() for l in receitas],
        'despesas': [l.to_dict() for l in despesas],
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'lucro': lucro
    })


@app.route('/api/relatorios/fluxo-caixa', methods=['GET'])
def fluxo_caixa():
    """Relatório de fluxo de caixa"""
    periodo_inicio = request.args.get('inicio')
    periodo_fim = request.args.get('fim')
    
    query = Lancamento.query
    if periodo_inicio:
        query = query.filter(Lancamento.data >= datetime.strptime(periodo_inicio, '%Y-%m-%d').date())
    if periodo_fim:
        query = query.filter(Lancamento.data <= datetime.strptime(periodo_fim, '%Y-%m-%d').date())
    
    lancamentos = query.order_by(Lancamento.data).all()
    
    saldo = 0
    resultado = []
    for l in lancamentos:
        if l.tipo == 'RECEITA':
            saldo += l.valor
        else:
            saldo -= l.valor
        resultado.append({
            'data': l.data.strftime('%Y-%m-%d'),
            'descricao': l.descricao,
            'tipo': l.tipo,
            'valor': l.valor,
            'saldo': saldo
        })
    
    return jsonify({
        'lancamentos': resultado,
        'saldo_final': saldo
    })


def init_db():
    """Inicializar o banco de dados"""
    with app.app_context():
        db.create_all()
        
        # Criar plano de contas padrão se não existir
        if PlanoContas.query.count() == 0:
            contas_padrao = [
                PlanoContas(codigo='1.1.01', nome='Caixa', tipo='ATIVO', natureza='DEVEDORA'),
                PlanoContas(codigo='1.1.02', nome='Bancos', tipo='ATIVO', natureza='DEVEDORA'),
                PlanoContas(codigo='1.2.01', nome='Contas a Receber', tipo='ATIVO', natureza='DEVEDORA'),
                PlanoContas(codigo='2.1.01', nome='Fornecedores', tipo='PASSIVO', natureza='CREDORA'),
                PlanoContas(codigo='2.1.02', nome='Contas a Pagar', tipo='PASSIVO', natureza='CREDORA'),
                PlanoContas(codigo='3.1.01', nome='Capital Social', tipo='PATRIMONIO', natureza='CREDORA'),
                PlanoContas(codigo='4.1.01', nome='Receita de Vendas', tipo='RECEITA', natureza='CREDORA'),
                PlanoContas(codigo='4.1.02', nome='Receita de Serviços', tipo='RECEITA', natureza='CREDORA'),
                PlanoContas(codigo='5.1.01', nome='Despesas Operacionais', tipo='DESPESA', natureza='DEVEDORA'),
                PlanoContas(codigo='5.1.02', nome='Despesas Administrativas', tipo='DESPESA', natureza='DEVEDORA'),
            ]
            for conta in contas_padrao:
                db.session.add(conta)
            db.session.commit()
            print("Plano de contas padrão criado!")


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
