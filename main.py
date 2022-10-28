from db.database import Graph

db = Graph("bolt://3.236.131.224:7687", "neo4j", "warships-procurements-evacuation")

def create_professor(nome, idade, area):
    data = db.execute_query("create(p:Professor{nome: $nome, idade: $idade, area: $area})",
    {'nome': nome, 'idade': idade, 'area': area})

def create_materia(assunto, horario):
    data = db.execute_query("create(m:Materia{assunto: $assunto, horario: $horario})",
    {'assunto': assunto, 'horario': horario})

def relacao_professor_materia(nome, assunto, ano):
    data = db.execute_query("MATCH(p:Professor{nome: $nome}),(m:Materia{assunto: $assunto}) CREATE(p)-[:POSSUI{ano: $ano}]->(m);",
    {'nome': nome, 'assunto': assunto, 'ano': ano})

create_professor('Pedro', 21, 'S202')
create_professor('Iago', 21, 'S201')
create_professor('Lucas', 22, 'M019')
create_professor('Bruno', 20, 'M005')

create_materia('BD2', '19:30')
create_materia('Calculo', '15:30')

relacao_professor_materia('Pedro', 'BD2', 2021)
relacao_professor_materia('Bruno', 'Calculo', 2022)
