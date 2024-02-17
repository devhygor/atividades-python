"""
    Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""

# Define as constantes para usarmos como valores para verificarmos se o usuario e senha irao corresponder

USUARIO_DEFINIDO = 'usuario123'
SENHA_DEFINIDA = 'senha123'

def get_usuario_senha():
    usuario = input('Digite o seu usuario: ')
    senha = input('Digite a sua senha: ')

    return usuario, senha

def login(usuario, senha):
    if usuario == USUARIO_DEFINIDO and senha == SENHA_DEFINIDA:
        print('Os Valore corresponderam')
    else:
        print('Valores divergentes')

def main():
    usuario, senha = get_usuario_senha()
    login(usuario, senha)

if __name__ == '__main__':
    main()