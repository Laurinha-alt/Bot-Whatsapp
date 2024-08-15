#definir o numero para quem vai enviar
#definir a mensagem que vai ser enviada 
#Definir a hora
#Enviar a mensagem 

import pywhatkit as kit

numero = '+5561993308545'  # Exemplo: +55 código do país + DDD + número
mensagem = 'Oiie , se essa mensagem chegou é porque deu certo a automatização!'

hora_envio = 19  
minuto_envio = 44  

kit.sendwhatmsg(numero, mensagem, hora_envio, minuto_envio)
