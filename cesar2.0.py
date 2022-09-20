'''Criptografia: escreva uma frase, digite uma chave de 26 caractere alfabeticos, escolha "e/E" para criptografar ou
digite uma frase criptografada, use a mesma chave de 26 caractere alfabeticos e escolha "d/D" para desecriptar'''



texto = str(input('Digite o texto:')).strip()
chave = str(input('Digite a chave')).strip().upper()
while chave.isalpha() == False or len(chave)!=26:  
    print('Chave inválida, digite uma chave alfabetica com 26 caractere')
    chave = str(input('Digite a chave')).strip().upper()
modo = input('Escolha E para encriptar ou D para decriptar o texto: ').strip().upper()
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caracteres = 'abcdefghijklmnopqrstuvwxyz'
for caractere in texto: #para cada carcterie no texto
    if caractere in caracteres: #se tiver no caracteries, trans a chave em minuscula
        chave = chave.lower()
CARACTERESV = ' '
CARACTERESESP = ',.!?:;'

convertido = list() #TEXTO PARA SAIR
num = 0
for caractere in texto:     
    if modo == 'E':
        if caractere in caracteres:
            if caractere in chave: 
                num = caracteres.find(caractere)                             
                num = num                                      
                convertido.append(chave[num])             
        elif caractere in CARACTERES:
            if caractere in chave: 
                num = CARACTERES.find(caractere)                             
                num = num                                    
                convertido.append(chave[num])  
        elif caractere in CARACTERESV:
            convertido.append(CARACTERESV)
        elif caractere in CARACTERESESP:
            num = CARACTERESESP.find(caractere)
            convertido.append(CARACTERESESP[num])

    elif modo == 'D':
        num = chave.find(caractere)                  
        if caractere in CARACTERES: 
            num = num                          
            convertido.append(CARACTERES[num])        
        elif caractere in caracteres:
            num = num
            convertido.append(caracteres[num])
        elif caractere in CARACTERESV:
            convertido.append(CARACTERESV)
        elif caractere in CARACTERESESP:
            num = CARACTERESESP.find(caractere)
            convertido.append(CARACTERESESP[num])
junto = ''.join(convertido) #tira os caracterie da lista e junta
    
print(junto)
