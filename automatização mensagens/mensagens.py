#definir a mensagem que vai ser enviada 
#definir a pessoa para quem vai enviar
#enviar via whatsapp

import pywhatkit as kit

# Definir o número de telefone no formato internacional e a mensagem
numero = '+5561993308545'  # Exemplo: +55 código do país + DDD + número
mensagem = 'Oiie , se essa mensagem chegou é porque deu certo a automatização!'

# Definir o horário de envio
hora_envio = 19  # 16 para 4 PM
minuto_envio = 13  # 45 minutos

# Enviar a mensagem
kit.sendwhatmsg(numero, mensagem, hora_envio, minuto_envio)
