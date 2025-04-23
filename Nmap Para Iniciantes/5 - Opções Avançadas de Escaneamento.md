À medida que você se aprofunda no uso do Nmap, é importante ir além do escaneamento básico. Felizmente, o Nmap é uma ferramenta extremamente poderosa, que oferece diversas opções avançadas para **refinar análises**, **identificar serviços**, **detectar sistemas operacionais** e até **executar scripts de segurança**.

Neste capítulo, vamos explorar esses recursos com exemplos práticos para ajudá-lo a dominar a arte do escaneamento com o Nmap.

---

## 5.1 Escaneamento de Portas Específicas

Por padrão, o Nmap escaneia as **1.000 portas TCP mais comuns**, com base em estatísticas de uso. No entanto, é possível especificar exatamente **quais portas** você deseja analisar — útil para auditorias direcionadas ou análises mais rápidas.

### 🎯 Como usar:

- Escanear portas específicas:
    `nmap -p 22,80,443 192.168.1.1`
    
    Esse comando verifica apenas as portas 22 (SSH), 80 (HTTP) e 443 (HTTPS).
    
- Escanear todas as **65.535 portas TCP**:
    `nmap -p- 192.168.1.1`
    
    > ⚠️ Esse tipo de escaneamento é mais **demorado**, mas muito eficaz em ambientes desconhecidos.
    
- Intervalo de portas:
    `nmap -p 20-100 192.168.1.1`
    
    Escaneia todas as portas do 20 ao 100, útil para detectar serviços fora das portas padrão.
    

### 🔎 Dica:

Combine com `-sS` ou `-sT` para definir o tipo de escaneamento:

`nmap -sS -p 21-25 192.168.1.1`

---

## 5.2 Detecção de Serviços (`-sV`)

Nem sempre saber que uma porta está **aberta** é suficiente. Muitas vezes, queremos saber **qual serviço está rodando naquela porta** e **qual a sua versão** — esse detalhe é essencial para identificar possíveis vulnerabilidades.

### 🔬 Como funciona:

O Nmap envia pacotes personalizados para a porta e analisa as respostas para identificar:

- Nome do serviço (ex: SSH, HTTP, FTP).
    
- Versão e banner do serviço.
    
- Software utilizado (ex: Apache, OpenSSH, nginx, etc).
    

### 💻 Comando:

`nmap -sV 192.168.1.1`

### 🧪 Exemplo de saída:

`PORT    STATE SERVICE VERSION 22/tcp  open  ssh     OpenSSH 7.4 80/tcp  open  http    Apache httpd 2.4.6`

> **Dica:** Combine com `-p` para escanear serviços em portas específicas:

`nmap -sV -p 22,80 192.168.1.1`

### 🔍 Quando usar:

- Durante **pentests**, para identificar software vulnerável.
    
- Em **auditorias de conformidade**, para verificar versões desatualizadas.
    
- Em **inventários de rede**, para mapear serviços ativos.
    

---

## 5.3 Detecção de Sistemas Operacionais (`-O`)

O Nmap também é capaz de estimar o **sistema operacional** de um host. Ele faz isso analisando o comportamento da pilha TCP/IP e outras características de rede.

### ⚙️ Como funciona:

Utiliza técnicas como:

- **TCP/IP fingerprinting**.
    
- Análise de **pacotes ICMP**, TTL, fragmentação e janelas TCP.
    
- Respostas a pacotes “anormais”.
    

### 💻 Comando:

`nmap -O 192.168.1.1`

### 📢 Dica adicional:

Use o modo **verboso** para obter mais detalhes:

`nmap -O -v 192.168.1.1`

### 📌 Observações:

- Requer **privilégios administrativos/root**.
    
- Resultados mais precisos com hosts que respondem de forma previsível.
    
- Não é 100% garantido, mas fornece uma **estimativa útil**.
    

---

## 5.4 Uso de Scripts com o Nmap Scripting Engine (NSE)

O **Nmap Scripting Engine (NSE)** é uma das funcionalidades mais poderosas da ferramenta. Ele permite executar scripts escritos em Lua para tarefas específicas de segurança, como:

- Enumeração de serviços.
    
- Detecção de vulnerabilidades conhecidas.
    
- Quebra de autenticação fraca.
    
- Análise de protocolos.
    

### 🧠 Como funciona:

Os scripts NSE são divididos em categorias:

- `auth` – autenticação (ex.: brute force).
    
- `vuln` – detecção de vulnerabilidades.
    
- `safe` – scripts seguros para uso em produção.
    
- `intrusive` – scripts mais agressivos.
    
- `discovery`, `exploit`, `malware`, etc.
    

### 💻 Exemplos práticos:

#### 1. Enumeração de usuários SMB:

`nmap --script smb-enum-users.nse -p445 192.168.1.1`

Esse script tenta listar os usuários configurados em um serviço SMB ativo na porta 445.

#### 2. Verificar vulnerabilidade do Apache Struts (CVE-2017-5638):

`nmap --script http-vuln-cve2017-5638.nse -p80 192.168.1.1`

### 🔍 Dicas:

- Você pode usar múltiplos scripts com vírgula:
    `nmap --script=ssh-brute,http-vuln-cve2017-5638.nse 192.168.1.1`
    
- Para ver todos os scripts disponíveis:
    `ls /usr/share/nmap/scripts/`
    
- Para executar **todos os scripts de uma categoria**:
    `nmap --script vuln 192.168.1.1`
    

> ⚠️ **Atenção**: scripts da categoria `intrusive` podem causar impactos no alvo. Use com responsabilidade, especialmente fora de ambientes de testes.

---

## Conclusão

Com essas opções avançadas, o Nmap se transforma em uma verdadeira **plataforma de exploração e auditoria de redes**, permitindo:

- Diagnóstico preciso de sistemas.
    
- Enumeração de serviços.
    
- Identificação de falhas conhecidas.
    
- Análise comportamental da rede.
    

Você está pronto para usar o Nmap como um profissional. No próximo capítulo, podemos abordar **técnicas de evasão e stealth**, ou aprofundar no **uso combinado de opções** para escaneamentos mais completos e personalizados.