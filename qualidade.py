import psycopg2
import argparse

parser = argparse.ArgumentParser(description='Lê o banco de dados e devolve a informação pedida.')
parser.add_argument('-nome', type=str)
args = parser.parse_args()


nome=args.nome

conn = psycopg2.connect("dbname=postgres user=postgres password=esther")
cur = conn.cursor()

cur.execute("select idade from person where nome = '{0}'".format(nome))
resultado = cur.fetchall()[0][0]
print("A idade de {0} é {1}".format(nome, resultado))
