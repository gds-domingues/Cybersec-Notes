O Nmap não é apenas uma ferramenta para reconhecimento inicial. Ele também pode ser extremamente útil para **monitorar alterações em redes ao longo do tempo**. Isso é essencial para administradores que desejam identificar **novos dispositivos**, **mudanças inesperadas em serviços** ou possíveis **atividades maliciosas** em uma infraestrutura.

---

## 12.1 Detectando Novos Dispositivos

Em redes corporativas ou ambientes dinâmicos, é comum que dispositivos entrem ou saiam da rede. Monitorar essas mudanças é uma boa prática de segurança e gestão.

---

### 🕒 1. Verificação Agendada da Rede

Você pode agendar escaneamentos periódicos com o Nmap para registrar quais dispositivos estão ativos em uma rede local:

`nmap -sn 192.168.1.0/24 -oX scan_results.xml`

- A opção `-sn` (ping scan) verifica quais hosts estão ativos, sem fazer varredura de portas.
    
- O resultado em formato XML (`-oX`) é ideal para processamento e comparação automática.
    

> 📌 **Dica**: Use um `cronjob` no Linux para rodar esse comando automaticamente todos os dias ou a cada hora.

Exemplo de entrada no `crontab` para escanear todo dia às 2 da manhã:

`0 2 * * * nmap -sn 192.168.1.0/24 -oX /caminho/scan_$(date +\%F).xml`

---

### 🔍 2. Comparação de Escaneamentos: `ndiff`

Após coletar escaneamentos em momentos diferentes, você pode compará-los para detectar alterações:

`ndiff scan_old.xml scan_new.xml`

- O `ndiff` compara dois arquivos XML e exibe o que mudou.
    
- Ideal para detectar **novos hosts**, **hosts que saíram da rede** ou **mudanças de IP**.
    

> ✅ Ferramenta muito útil em ambientes de produção onde novas máquinas são adicionadas com frequência.

---

## 12.2 Detectando Serviços Inesperados

Além de novos dispositivos, é importante saber se **novos serviços** foram iniciados em máquinas conhecidas. Isso pode indicar atualizações legítimas... ou comprometimento.

---

### 🚪 1. Verificação de Portas Abertas Recentemente

Faça escaneamentos completos com `-p-` para identificar **todas** as portas abertas:

`nmap -p- 192.168.1.1 -oX scan_results.xml`

- O `-p-` escaneia todas as 65535 portas TCP.
    
- Guarde os resultados e compare com versões anteriores usando o `ndiff`.
    

> 🎯 Essa técnica revela mudanças como um serviço de SSH que foi aberto sem autorização, ou um servidor web ativado acidentalmente.

---

### 📬 2. Automatizando Alertas

Você pode criar scripts que verifiquem mudanças em escaneamentos e **disparem alertas** por e-mail, Slack ou outro canal. Exemplo básico em Bash:

#!/bin/bash

# Realiza um novo scan completo e salva em XML
nmap -p- 192.168.1.1 -oX scan_new.xml

# Compara com o scan anterior
ndiff scan_old.xml scan_new.xml > diff.txt

# Se houver diferenças, envia e-mail
if [ -s diff.txt ]; then
    mail -s "Alterações detectadas na rede" admin@exemplo.com < diff.txt
fi

# Atualiza o arquivo antigo com o novo scan
mv scan_new.xml scan_old.xml

- Executa o novo escaneamento.
    
- Compara com o anterior.
    
- Envia um e-mail se houver mudanças.
    
- Substitui o escaneamento antigo pelo novo.
    

> ⚙️ Com pequenas adaptações, isso pode ser integrado a sistemas de monitoramento como Zabbix, Nagios ou Grafana.

---

## Conclusão

Monitorar a rede com o Nmap permite:

- Detectar **novos dispositivos não autorizados**.
    
- Verificar se **serviços inesperados** foram abertos.
    
- Criar **alertas automáticos** para mudanças de comportamento na rede.
    

🔐 Este processo ajuda a manter a rede segura e sob controle, sendo uma das práticas fundamentais de **defesa em profundidade**.