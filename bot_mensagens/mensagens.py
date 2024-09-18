#definir o numero para quem vai enviar
#definir a mensagem que vai ser enviada 
#Definir a hora
#Enviar a mensagem 
import pywhatkit as kit
from datetime import datetime, timedelta
import time

numeros = [
    '+5534991090464',
    '+5534999256468',
    '+5534998403835'
]

mensagem = 'Ola boa tarde, tudo bem? Peço que por gentileza realize a pesquisa de Analgésicos e me informe assim que finalizá-la.'

agora = datetime.now()

tempo_minimo_envio = timedelta(minutes=5)

intervalo_entre_envios = timedelta(minutes=1)

for i, numero in enumerate(numeros):
    tempo_envio = agora + tempo_minimo_envio + intervalo_entre_envios * i
    
    hora_envio = tempo_envio.hour
    minuto_envio = tempo_envio.minute

    print(f"Enviando mensagem para {numero} às {hora_envio:02d}:{minuto_envio:02d}")
    
    try:
        kit.sendwhatmsg(numero, mensagem, hora_envio, minuto_envio)
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")

    time.sleep(10)

