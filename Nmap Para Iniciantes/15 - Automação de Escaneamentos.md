Monitorar continuamente uma rede é uma tarefa essencial para detectar mudanças, novos dispositivos ou serviços potencialmente maliciosos. O Nmap pode ser facilmente automatizado para realizar escaneamentos periódicos e alertar sobre alterações — garantindo que a postura de segurança da rede se mantenha sob controle.

---

## 15.1 Usando Cronjobs para Escaneamentos Recorrentes

Um **cronjob** é uma tarefa agendada no sistema Linux que pode ser programada para rodar comandos ou scripts em horários definidos. Isso permite que você configure escaneamentos automáticos diariamente, semanalmente ou até por hora.

---

### 📜 1. Criando um Script Bash

O primeiro passo é criar um script simples que execute o Nmap e salve os resultados:

`#!/bin/bash nmap -sS -oX /var/log/nmap_results.xml 192.168.1.0/24`

> ✅ **Explicação dos parâmetros**:
> 
> - `-sS`: escaneamento do tipo SYN (rápido e discreto);
>     
> - `-oX`: salva a saída no formato XML, ideal para comparações automáticas e integração com outras ferramentas.
>     

Salve esse script como `nmap_script.sh` e dê permissão de execução:

`chmod +x nmap_script.sh`

---

### 🕒 2. Agendando o Script com `cron`

Para executar o script automaticamente todos os dias às 2 da manhã:

1. Acesse o editor de cron do usuário:

`crontab -e`

2. Adicione a seguinte linha ao final do arquivo:
    

`0 2 * * * /caminho/completo/para/nmap_script.sh`

> 🧠 **Dica**: você pode redirecionar a saída para um log com `>> /var/log/nmap_cron.log 2>&1` para facilitar o debug de erros.

---

## 15.2 Monitoramento com Ndiff

O **Ndiff** é uma ferramenta complementar ao Nmap que compara os resultados de dois escaneamentos XML, mostrando o que mudou — como dispositivos que entraram ou saíram da rede, ou novas portas abertas.

---

### 💾 1. Salvando Escaneamentos para Comparação

Execute dois escaneamentos em momentos diferentes e salve os arquivos:

`nmap -oX old_scan.xml 192.168.1.0/24 sleep 3600  # Aguarde algum tempo (simulando o intervalo entre escaneamentos) nmap -oX new_scan.xml 192.168.1.0/24`

---

### 🔍 2. Comparando com Ndiff

Use o `ndiff` para ver o que mudou:

`ndiff old_scan.xml new_scan.xml`

A saída pode ser algo como:

`+ Host: 192.168.1.105 () Status: Up + Host: 192.168.1.105 () Port: 80/tcp Open - Host: 192.168.1.103 () Status: Down`

> 📈 Isso ajuda a identificar **novos hosts conectados à rede**, **serviços inesperados**, **mudanças de status** ou até **ataques como pivoting** dentro da rede.

---

### ⚠️ Automação + Ndiff + Alerta

Combinando `cron`, `ndiff` e um pequeno script em shell ou Python, é possível **enviar alertas automáticos por e-mail ou Telegram** toda vez que uma mudança for detectada. Exemplo básico de script:

`#!/bin/bash ndiff old.xml new.xml > diff.txt if [ -s diff.txt ]; then    mail -s "Mudanças na rede detectadas" you@example.com < diff.txt fi`

---

## Conclusão

A automação com Nmap e Ndiff permite:

✅ Monitorar redes continuamente;  
✅ Detectar alterações indesejadas;  
✅ Agir proativamente antes que ameaças se consolidem.