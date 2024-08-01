def loginUsuario(perfil):
    perfil = perfil.lower()
    
    if perfil == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuario')



loginUsuario('augusto')        

