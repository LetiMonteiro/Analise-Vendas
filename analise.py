# ==========================================================
# PRIMEIRO PROJETO DE CIÊNCIA DE DADOS COM PANDAS
# -bem etalhado para estudo e reestudo
#
# Objetivo:
# Realizar uma análise simples de um arquivo CSV contendo
# informações de vendas e responder perguntas importantes,
# como:
#
# - Qual produto vendeu mais?
# - Qual categoria faturou mais?
# - Qual foi o faturamento total?
# - Qual foi o dia com maior faturamento?
# - Qual é o ticket médio das vendas?
# ==========================================================


# ----------------------------------------------------------
# IMPORTAÇÃO DA BIBLIOTECA
# ----------------------------------------------------------

# Importa a biblioteca Pandas e atribui o apelido "pd".
# O Pandas é uma das bibliotecas mais utilizadas em Ciência
# de Dados para manipulação e análise de dados em formato
# de tabelas (DataFrames).
import pandas as pd


# ----------------------------------------------------------
# LEITURA DO ARQUIVO CSV
# ----------------------------------------------------------

# Lê o arquivo chamado "vendas.csv".
#
# O método read_csv() abre o arquivo e transforma seu
# conteúdo em um DataFrame, estrutura semelhante a uma
# planilha do Excel.
df = pd.read_csv("vendas.csv")


# Exibe todos os dados carregados para conferir se o
# arquivo foi lido corretamente.
print(df)


# ----------------------------------------------------------
# CRIAÇÃO DA COLUNA FATURAMENTO
# ----------------------------------------------------------

# Cria uma nova coluna chamada "Faturamento".
#
# Para cada linha da tabela será feito o cálculo:
#
# Quantidade × Preço
#
# Exemplo:
#
# 2 Notebooks × R$ 3.500 = R$ 7.000
#
# O Pandas faz esse cálculo automaticamente para todas
# as linhas da tabela.
df["Faturamento"] = df["Quantidade"] * df["Preco"]


# Mostra novamente a tabela já contendo a nova coluna.
print(df)


# ----------------------------------------------------------
# PRODUTO MAIS VENDIDO
# ----------------------------------------------------------

# Agrupa todas as linhas pelo nome do produto e soma a
# quantidade vendida de cada um.
#
# Exemplo:
#
# Notebook -> 6 unidades
# Mouse -> 12 unidades
# Camiseta -> 18 unidades
produto = df.groupby("Produto")["Quantidade"].sum()


print("\nQuantidade vendida por produto:")
print(produto)


# idxmax() retorna o índice que possui o maior valor.
#
# Nesse caso retorna o nome do produto que vendeu mais.
print("\nProduto mais vendido:")
print(produto.idxmax())


# ----------------------------------------------------------
# CATEGORIA QUE MAIS FATUROU
# ----------------------------------------------------------

# Agrupa os dados pela categoria e soma o faturamento de
# cada uma delas.
#
# Exemplo:
#
# Eletrônicos -> R$ 22.460
# Roupas -> R$ 1.380
# Calçados -> R$ 2.400
categoria = df.groupby("Categoria")["Faturamento"].sum()


print("\nFaturamento por categoria:")
print(categoria)


# Retorna a categoria que possui o maior faturamento.
print("\nCategoria que mais faturou:")
print(categoria.idxmax())


# ----------------------------------------------------------
# FATURAMENTO TOTAL DA EMPRESA
# ----------------------------------------------------------

# Soma todos os valores existentes na coluna Faturamento.
#
# Dessa forma descobrimos quanto a empresa faturou no
# período analisado.
total = df["Faturamento"].sum()


print("\nFaturamento total:")
print(f"R$ {total:,.2f}")


# ----------------------------------------------------------
# DIA COM MAIOR FATURAMENTO
# ----------------------------------------------------------

# Agrupa os dados pela data e soma o faturamento realizado
# em cada dia.
dia = df.groupby("Data")["Faturamento"].sum()


print("\nFaturamento por dia:")
print(dia)


# idxmax() retorna a data que teve maior faturamento.
print("\nDia com maior faturamento:")
print(dia.idxmax())


# ----------------------------------------------------------
# TICKET MÉDIO
# ----------------------------------------------------------

# mean() calcula a média dos valores existentes na coluna
# Faturamento.
#
# O ticket médio representa quanto, em média, vale cada
# venda realizada.
ticket = df["Faturamento"].mean()


print("\nTicket médio:")
print(f"R$ {ticket:.2f}")


# ----------------------------------------------------------
# RELATÓRIO FINAL
# ----------------------------------------------------------

# Exibe um resumo organizado das principais informações
# obtidas durante a análise dos dados.

print("\n" + "=" * 50)
print("RELATÓRIO FINAL")
print("=" * 50)

print(f"Produto mais vendido: {produto.idxmax()}")

print(f"Categoria que mais faturou: {categoria.idxmax()}")

print(f"Faturamento total: R$ {total:,.2f}")

print(f"Dia com maior faturamento: {dia.idxmax()}")

print(f"Ticket médio: R$ {ticket:.2f}")


# ----------------------------------------------------------
# EXPORTAÇÃO DOS RESULTADOS
# ----------------------------------------------------------

# Salva um novo arquivo chamado "resultado.csv".
#
# Esse arquivo conterá todos os dados originais mais a
# coluna "Faturamento" criada durante a análise.
#
# index=False impede que o índice do DataFrame seja salvo
# como uma coluna extra no arquivo CSV.
df.to_csv("resultado.csv", index=False)

# ----------------------------------------------------------
# GRÁFICO DE FATURAMENTO POR CATEGORIA
# ----------------------------------------------------------

# Importa a biblioteca Matplotlib.
# Ela é uma das bibliotecas mais utilizadas para criação
# de gráficos em Python e Ciência de Dados.
import matplotlib.pyplot as plt


# Cria um gráfico de barras utilizando os dados da variável
# "categoria", que contém o faturamento total de cada categoria.
categoria.plot(
    kind="bar"
)


# Define o título do gráfico.
plt.title("Faturamento por Categoria")


# Define o texto do eixo X.
plt.xlabel("Categoria")


# Define o texto do eixo Y.
plt.ylabel("Faturamento (R$)")


# Adiciona uma grade horizontal para facilitar a leitura
# dos valores apresentados.
plt.grid(axis="y")


# Ajusta automaticamente o tamanho do gráfico para evitar
# sobreposição dos elementos.
plt.tight_layout()


# Exibe o gráfico na tela.
plt.show()