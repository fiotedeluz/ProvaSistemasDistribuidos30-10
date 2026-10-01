
from xmlrpc.server import SimpleXMLRPCServer

def calcular_pagamento(horas, valorPorHora):
    return horas * valorPorHora

servidor = SimpleXMLRPCServer(("localhost",8005))

servidor.register_function(

        calcular_pagamento,
        "calcular_pagamento"

        )

print("sevidor RPC aguardando solicitações...")

servidor.serve_forever()

