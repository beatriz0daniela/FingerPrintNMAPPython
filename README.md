# FingerPrint NMAP com Python
segma4 - professor: Cabrini

atividade realizada pelos alunos: Beatriz, Isabela Thais e Wilson.

Nessa atividade utilizamos a biblioteca do nmap para scannear as portas tcp: 1026; 1883; 4041; 8666 e 27017. Foi capaz de identificar o finger print do fiware.

-Primeiro colocamos o ip da maquina;
-Depois colocamos variaveis com as portas e a função de scannar;
-Temos o if (condição) no final para identificar se as portas estão abertas, caso não esteja ele irá mostrar a mensagem ("O fiware não está instalado")

Detalhe: quando o codigo é executado, se colocar o cursor do mouse nas variaveis de result, tem escrito "open" ou "close"
