O **Nmap** oferece diversos métodos de escaneamento para atender a diferentes objetivos, desde a simples descoberta de dispositivos ativos até auditorias mais profundas de segurança. Cada tipo de escaneamento é ideal para um cenário específico, levando em consideração fatores como privilégios de acesso, performance, discrição e objetivos técnicos.

Neste capítulo, vamos explorar os principais tipos de escaneamento, explicando como funcionam, quando utilizá-los e quais são suas vantagens e limitações.

---

## 4.1 Escaneamento TCP Connect (`-sT`)

Esse é o tipo mais básico de escaneamento e, por isso, ideal para **usuários iniciantes ou sem privilégios administrativos** (root).

### ✅ Como funciona:

O Nmap realiza uma conexão TCP completa com a porta de destino, utilizando o processo conhecido como **three-way handshake**:

1. O Nmap envia um pacote SYN.
    
2. Se a porta estiver aberta, o host responde com SYN-ACK.
    
3. O Nmap completa o handshake com um ACK.
    

Se a porta estiver fechada, o host responderá com um pacote RST (reset).

### 💻 Comando:

`nmap -sT 192.168.1.1`

### 🔍 Vantagens:

- Funciona mesmo sem privilégios elevados (root ou administrador).
    
- Compatível com praticamente todas as redes.
    
- Fácil de interpretar.
    

### ⚠️ Desvantagens:

- Mais lento em redes grandes.
    
- Muito fácil de ser detectado por sistemas de defesa, como firewalls e IDS (sistemas de detecção de intrusão).
    

> **Dica:** É uma boa escolha em ambientes controlados ou em laboratórios de testes.

---

## 4.2 Escaneamento SYN Stealth (`-sS`)

Este é o **escaneamento padrão do Nmap**, conhecido como **semi-aberto** ou stealth scan, por não completar totalmente a conexão TCP. É amplamente utilizado em auditorias de segurança profissional.

### ✅ Como funciona:

- O Nmap envia apenas o pacote SYN.
    
- Se a porta estiver aberta, o host responde com SYN-ACK.
    
- O Nmap **não** envia o ACK para finalizar a conexão — em vez disso, ele envia um pacote RST, encerrando prematuramente a comunicação.
    

Essa tática evita que a conexão seja registrada em logs do servidor, tornando o escaneamento mais **furtivo**.

### 💻 Comando:

`nmap -sS 192.168.1.1`

### 🔍 Vantagens:

- Mais rápido que o `-sT`.
    
- Menos visível em logs e monitoramentos.
    
- Excelente custo-benefício entre performance e discrição.
    

### ⚠️ Desvantagens:

- **Requer privilégios administrativos/root** para funcionar.
    
- Pode ser bloqueado por firewalls configurados para descartar pacotes SYN suspeitos.
    

> **Recomendado** para pentesters, analistas de segurança e entusiastas que buscam mais precisão e performance.

---

## 4.3 Escaneamento UDP (`-sU`)

Muitas vezes negligenciado, o escaneamento UDP é **essencial para identificar serviços que não usam o protocolo TCP**, como DNS (porta 53), SNMP (161) e DHCP (67/68).

### ✅ Como funciona:

- O Nmap envia pacotes UDP para a porta de destino.
    
- Se a porta estiver **fechada**, o host responde com um pacote **ICMP Port Unreachable**.
    
- Se a porta estiver **aberta**, é possível receber uma resposta UDP válida.
    
- Em muitos casos, **nenhuma resposta** pode indicar que a porta está aberta ou filtrada.
    

### 💻 Comando:

`nmap -sU 192.168.1.1`

> ⚠️ É comum combinar `-sU` com `-sS` para uma análise mais completa:

`nmap -sS -sU 192.168.1.1`

### 🔍 Vantagens:

- Fundamental para descobrir serviços UDP, muitas vezes usados em backdoors e ataques.
    

### ⚠️ Desvantagens:

- Muito mais lento que escaneamentos TCP.
    
- Pode produzir resultados ambíguos (sem resposta ≠ porta aberta).
    
- Frequentemente bloqueado por firewalls.
    

> **Dica:** Para tornar esse tipo de escaneamento mais rápido, utilize `--top-ports` para limitar o número de portas verificadas:

`nmap -sU --top-ports 20 192.168.1.1`

---

## 4.4 Descoberta de Hosts com ICMP Ping Sweep (`-sn`, substitui `-sP`)

Esse tipo de escaneamento não busca informações sobre **portas** ou **serviços**, mas sim identificar **quais dispositivos estão ativos em uma rede**.

> ⚠️ A opção `-sP` foi descontinuada em versões mais recentes do Nmap e substituída por `-sn`.

### ✅ Como funciona:

- O Nmap envia pacotes ICMP Echo Request (ping) e/ou outros tipos de sondagens (como TCP ACK ou SYN em portas comuns) para cada IP no intervalo especificado.
    
- Os IPs que respondem são considerados **ativos**.
    

### 💻 Comando:

`nmap -sn 192.168.1.0/24`

### 🔍 Vantagens:

- Extremamente rápido.
    
- Útil para **mapear redes** e identificar dispositivos ativos sem fazer escaneamento de portas.
    

### ⚠️ Desvantagens:

- Ineficaz em redes que bloqueiam ICMP ou respostas TCP não solicitadas.
    
- Pode deixar de detectar dispositivos com firewalls restritivos.
    

---

## Comparativo Resumido

|Tipo de Escaneamento|Flag|Requer Root|Velocidade|Discrição|Porta Alvo|
|---|---|---|---|---|---|
|TCP Connect|`-sT`|Não|Média|Baixa|TCP|
|SYN Stealth|`-sS`|Sim|Alta|Alta|TCP|
|UDP|`-sU`|Sim|Baixa|Média|UDP|
|ICMP Ping Sweep|`-sn`||