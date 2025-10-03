pessoa = {'nome':'Crislaine', 
          'idade':46, 
          'ano_formatura':2010, 
          'linguagens_programacao':['python', 'r', 'javascript', 'ruby'], 
          'brasileira':True, 
          'hobby':['nadar', 'ler', 'pedalar'], 
          'animal_estimacao':False}

# Imprima na tela o valor equivalente a chave "hobby"
pessoa['hobby']
print (pessoa['hobby'])

# Imprima na tela uma lista apenas com os valores do dicionário
pessoa.values ()
list(pessoa.values())
print (list (pessoa.values ()))

# Imprima na tela uma lista apenas com as chaves do dicionário
pessoa.keys()
list(pessoa.keys())
print (list(pessoa.keys()))

# Insira um novo par chave-valor no dicionário
pessoa['altura'] = 1.68

# Altere um valor no dicionário
pessoa['nome'] = 'Byanca'

# Remova um valor no dicionário
pessoa.pop ('idade')