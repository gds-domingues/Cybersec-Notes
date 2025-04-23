A fase de **reconhecimento** é a base de qualquer análise de segurança. Antes de explorar vulnerabilidades, é fundamental saber **quem está na rede, quais serviços estão em execução, quais portas estão abertas e qual o sistema operacional do alvo**.

O Nmap oferece uma gama de funcionalidades poderosas para realizar esse mapeamento de forma rápida e eficiente.

---

## 10.1 Identificando Hosts Ativos

Antes de gastar tempo escaneando serviços e portas, é importante descobrir **quais dispositivos estão realmente online** na rede.

---

### 🔍 1. Ping Sweep (`-sn`)

Este modo envia pacotes ICMP (ping) para determinar se os hosts estão ativos.

`nmap -sn 192.168.1.0/24`

- ✅ Retorna uma lista de dispositivos que respondem ao ping.
    
- ❌ Não realiza escaneamento de portas.
    

> 💡 Ideal para mapeamento inicial rápido de grandes redes.

---

### 🧠 2. Detecção Detalhada de Hosts (`-sP`)

Apesar de obsoleto nas versões mais novas (substituído por `-sn`), ainda é visto em muitos tutoriais.

`nmap -sP 192.168.1.0/24`

- Também detecta hosts ativos, com detalhes adicionais como MAC address e nome do fabricante.
    

> ⚠️ Para novas versões do Nmap, prefira o uso de `-sn`.

---

## 10.2 Descobrindo Portas e Serviços

Uma vez que os hosts ativos foram identificados, o próximo passo é descobrir **quais portas estão abertas** e **quais serviços estão sendo executados**.

---

### 🔓 1. Escaneamento Básico de Portas

Verifica apenas portas específicas (comuns em servidores):

`nmap -p 22,80,443 192.168.1.1`

> ✅ Rápido e focado. Útil quando você já sabe onde procurar.

---

### 📊 2. Escaneamento Completo de Portas

Varre **todas as 65.535 portas TCP** do alvo:

`nmap -p- 192.168.1.1`

> ⏳ Pode demorar, mas revela serviços em portas não convencionais.

---

### 🔍 3. Enumeração de Serviços e Versões (`-sV`)

Tenta identificar qual software está rodando em cada porta:

`nmap -sV -p22,80,443 192.168.1.1`

> 🧠 Essencial para identificar versões vulneráveis de serviços como Apache, SSH, etc.

---

## 10.3 Detectando Sistemas Operacionais

O Nmap consegue fazer uma boa estimativa do sistema operacional e do tipo de dispositivo sendo analisado.

---

### 🖥️ 1. Detecção de Sistema Operacional (`-O`)

Ativa heurísticas para identificar o sistema operacional com base nas respostas da pilha TCP/IP:

`nmap -O 192.168.1.1`

- Pode identificar Windows, Linux, BSD, dispositivos móveis etc.
    

> 🧠 Usa uma base de dados de fingerprinting para comparação.

---

### 🖧 2. Detecção Avançada com `-A`

Ativa várias opções ao mesmo tempo: detecção de SO, versão, traceroute, script scanning, etc.

`nmap -A 192.168.1.1`

> ⚠️ Muito poderosa, mas mais lenta e ruidosa — ideal para ambientes controlados.

---

## Conclusão

O processo de **reconhecimento e enumeração** com o Nmap é o primeiro passo para qualquer análise séria de segurança. Com poucos comandos, é possível identificar:

- Quais máquinas estão ativas.
    
- Quais portas estão abertas.
    
- Que serviços estão rodando.
    
- Quais sistemas operacionais estão em uso.
    

🔐 Ao dominar essas técnicas, você estará muito mais preparado para realizar **testes direcionados**, identificar falhas e proteger melhor seus ambientes.