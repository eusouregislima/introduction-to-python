nome_completo = "Regis Lima"

nome_completo_aspas = """Regis
Lima"""

nome_completo_quebra = "Regis \
Lima"

nome = "Regis"
sobrenome = "Lima"

# Formatação
print("Nome completo (1a forma):", nome_completo) # Saída: Nome completo (1a forma): Regis Lima
print("Nome completo (2a forma):" + nome_completo) # Saída: Nome completo (2a forma):Regis Lima
# Observar que quando usa-se o +, não é gerado espaço automático
print("Nome completo (3a forma):" + "Regis" + "Lima") # Saída: Nome completo (3a forma):RegisLima
print("Nome completo (4a forma):" + "Regis", "Lima") # Saída: Nome completo (4a forma):Regis Lima
print("Nome completo (5a forma):", nome_completo_aspas) # Saída: Nome completo (5a forma): Regis
# Lima -> Houve quebra de linha

print("Nome completo (6a forma):", nome_completo_quebra) # Saída: Nome completo (6a forma): Regis Lima
print("Nome completo (7a forma): %s" % nome_completo) # Saída: Nome completo (7a forma): Regis Lima
print("Nome completo (8a forma): %s %s" % (nome, sobrenome)) # Saída: Nome completo 8a forma): Regis Lima
# O %s é um marcador de posição (placeholder) usado para reservar strings.
print(f"Nome completo (9a forma): {nome} {sobrenome}") # Saída: Nome completo 9a forma): Regis Lima
# Esse f é a função format()
print("Nome completo (10a forma): {} {}".format(nome, sobrenome)) # Saída: Nome completo 9a forma): Regis Lima
# A mesma coisa deixando a função mais visível

