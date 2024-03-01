'''
    Exercícios instancias de uma classe
'''


class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

# Atribuir o valor 'Italiana' ao atributo categoria da instância restaurante_praca 
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante
print(f'Nome do restaurante praca = {restaurante_praca.nome}')

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'

#Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

#Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
novo_status_restaurante_pizza = 'Ativo' if restaurante_pizza.ativo == True else 'Desativado'
print(f'O estado da instancia restaurante_pizza esta como {novo_status_restaurante_pizza}')

#Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'\nImprimir no console o nome e a categoria da instância restaurante_praca\n')
print(f'Nome restaurante_praca = {restaurante_praca.nome}')
print(f'Categoria restaurante_praca = {restaurante_praca.categoria}')