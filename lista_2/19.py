numero= int(input('Digiye um numero entre 0 e 1000:'))
if numero <0 or numero> 1000:
    print('Numero invalido. porfavor, digiteum numeroentre 0 e 1000.')
else:
    centenas= numero //100
    dezenas= (numero % 100) // 10
    unidades= (numero % 100)% 10
    resultado=''

    if centenas >0: 
        if centenas== 1:     
            resultado +='1 centena' 
        else: 
            resultado += f'{centenas} centenas'
            
            if dezenas>0 :
                if centenas > 0 : 
                    resultado +=','
                    if dezenas ==1:
                        resultado+='dezena'
                    else: 
                        resultado += f'{dezenas}dezenas'

                        if unidades > 0:
                            if centenas >0 or dezenas >0 :
                                resultado += 'e'
                                if unidades== 1 :
                                    resultado +='1 unidade'
                                else: 
                                    resultado+= f'{unidades} unidades'

                                    print('resultados') 