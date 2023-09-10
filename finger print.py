#biblioteca utilizada 
import nmap

#Função do nmap para escanear as portas
ps = nmap.PortScanner()

#ip da maquina
ip = ("192.168.0.124")

#escanea as seguintes portas:
result1 = ps.scan( ip, "8666")
result1 = result1['scan'][ip]['tcp'][int("8666")]['state']
result2 = ps.scan( ip, "1026")
result2 = result2['scan'][ip]['tcp'][int("1026")]['state']
result3 = ps.scan( ip, "4041")
result3 = result3['scan'][ip]['tcp'][int("4041")]['state']
result4 = ps.scan( ip, "1883")
result4 = result4['scan'][ip]['tcp'][int("1883")]['state']
result5 = ps.scan( ip, "27017")
result5 = result5['scan'][ip]['tcp'][int("27017")]['state']

# condição das portas
if result1 == "open" and result2 == "open" and result3== "open" and result4 == "open" and result5 == "open":
    print("O fiware está instalado")
else:
    print("O fiware não está instalado")
