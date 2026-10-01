gleidson Alves
ra:a7850c44436a53c25468

##problema da empresa
uma empresa deseja criar um servidor para permitir de forma automatizada que os empregados possam calcular o valor a ser recebido fornecendo quantas foram as horas trabalhadas e qual o valor da hora do funcionario

##arquivos

-servidor.py: recebe a chamada rcp e executa o calculo
-cliente.py: solicita o calculo ao servidor e mostra a resposta

##resultado do texte

segue o terminal servidor
root@uwubura:/temp/prova# python3 servidor.py 
sevidor RPC aguardando solicitações...
127.0.0.1 - - [30/Sep/2026 22:28:15] "POST / HTTP/1.1" 200 -

//
segue o terminal cliente

root@uwubura:/temp/prova# python3 cliente.py 
valor do pagamento:  200
root@uwubura:/temp/prova# 

//

##explicação

1 onde foi feito o calculo:
o calculo foi feito no servidor que ja estava aguardando solicitações quando o cliente fez o pedido, o cliente então apenas apresentou o resultado

2 quem iniciou a solicitação:
o cliente faz a solicitação, o servidor quando aberto possui em si as instruções e aguarda que algo seja solicitado dele

3 oque seria do cliente sem o servidor:
nada, o cliente falharia pois ele é apenas interface para apresentar os calculos do servidor, sem o servidor ele não poderia apresentar resultados

