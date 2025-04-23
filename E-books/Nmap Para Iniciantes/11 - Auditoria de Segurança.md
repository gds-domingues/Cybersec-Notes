Com o reconhecimento realizado, chegou o momento de explorar potenciais **vulnerabilidades**. A auditoria de segurança visa identificar **falhas conhecidas**, **serviços inseguros** e **configurações incorretas** que possam ser exploradas por atacantes.

O Nmap, com sua poderosa **NSE (Nmap Scripting Engine)**, é uma ferramenta extremamente útil para essa tarefa.

---

## 11.1 Identificando Vulnerabilidades Conhecidas

Uma das formas mais diretas de descobrir brechas em sistemas é procurar por **vulnerabilidades já documentadas**, muitas das quais possuem identificadores como CVEs (Common Vulnerabilities and Exposures).

---

### 🛡️ 1. Usando o Script Geral de Vulnerabilidades

O script `vuln` executa uma varredura genérica em busca de várias falhas conhecidas:

`nmap --script vuln 192.168.1.1`

- Realiza uma análise completa utilizando múltiplos scripts NSE internos.
    
- Pode detectar vulnerabilidades como Heartbleed, SMBv1, e falhas HTTP conhecidas.
    

> ⚠️ Ideal para uma visão ampla, mas o escaneamento pode ser mais lento.

---

### 🎯 2. Scripts de Vulnerabilidades Específicas

Quando você conhece a vulnerabilidade que deseja testar (como em um pentest controlado), pode utilizar scripts direcionados.

#### CVE-2017-5638 – Apache Struts

Essa falha grave permitia execução remota de código via cabeçalhos HTTP.

`nmap --script http-vuln-cve2017-5638 -p80 192.168.1.1`

- Verifica se o servidor Apache Struts é vulnerável.
    
- Muito útil em ambientes que utilizam aplicações Java corporativas.
    

---

### 📦 3. Vulnerabilidades SMB – EternalBlue (MS17-010)

Uma das vulnerabilidades mais exploradas da última década, usada no ataque do WannaCry.

`nmap --script smb-vuln-ms17-010 -p445 192.168.1.1`

- Detecta se o serviço SMB está vulnerável à execução remota de código.
    
- Muito comum em redes Windows desatualizadas.
    

> ⚠️ Essa vulnerabilidade é crítica e deve ser tratada com urgência.

---

## 11.2 Avaliando Configurações de Segurança

Nem sempre os riscos estão ligados a falhas no código — muitas vezes eles vêm de **configurações fracas**, como senhas padrão ou protocolos expostos.

---

### 🔐 1. Detecção de Contas com Senhas Padrão

Muitos dispositivos de rede e sistemas embarcados vêm com credenciais padrão (admin/admin, root/root etc.). Você pode verificar se essas credenciais ainda estão ativas:

`nmap --script http-default-accounts 192.168.1.1`

- Testa uma lista de combinações padrão conhecidas.
    
- Muito útil para auditar roteadores, câmeras IP e appliances.
    

---

### 🧰 2. Verificação de Métodos de Autenticação SSH

Saber quais métodos de autenticação estão habilitados pode indicar possíveis vetores de ataque, como suporte a autenticação por senha:

`nmap --script ssh-auth-methods -p22 192.168.1.1`

- Retorna informações sobre os métodos aceitos (senha, chave pública, etc.).
    
- Pode ser usado para restringir acessos indesejados.
    

---

### 📡 3. Verificação de Configurações SNMP

O protocolo SNMP (Simple Network Management Protocol) é frequentemente mal configurado, permitindo acesso não autorizado a informações sensíveis.

`nmap --script snmp-info -p161 192.168.1.1`

- Retorna informações do sistema, como nome do host, serviços, localização física e mais.
    
- Pode indicar que a comunidade “public” está aberta.
    

> ⚠️ Em muitos casos, é possível explorar essas falhas para obter acesso administrativo ao dispositivo.

---

## Conclusão

A auditoria com o Nmap permite detectar:

- Vulnerabilidades conhecidas (CVE).
    
- Serviços com falhas de segurança.
    
- Configurações fracas ou incorretas.
    

🔍 Com a **Nmap Scripting Engine**, é possível adaptar os testes a diferentes alvos e ambientes, criando um processo de auditoria **personalizado, eficiente e automatizado**.