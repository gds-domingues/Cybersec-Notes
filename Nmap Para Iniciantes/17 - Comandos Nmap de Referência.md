Este capítulo reúne os principais comandos utilizados com o Nmap, organizados por finalidade. Ele serve como um **guia prático para consulta rápida**, ideal tanto para iniciantes quanto para profissionais que desejam revisar suas opções de escaneamento.

---

## 19.1 Comandos Básicos

Esses comandos são fundamentais para quem está começando a usar o Nmap. Permitem escanear dispositivos e portas de forma simples e direta.

---

### 🔎 1. Escaneamento simples de um host

Verifica as portas mais comuns do host especificado:

`nmap 192.168.1.1`

---

### 🌐 2. Escaneamento de uma sub-rede inteira

Procura por dispositivos ativos dentro da faixa de IP:

`nmap 192.168.1.0/24`

---

### 🎯 3. Escaneamento de portas específicas

Escaneia apenas as portas indicadas:

`nmap -p 22,80,443 192.168.1.1`

---

### 🚪 4. Escaneamento completo de todas as 65535 portas

Ideal para uma análise profunda:

`nmap -p- 192.168.1.1`

---

## 19.2 Ajustes de Performance

Ajustar a velocidade e o comportamento do escaneamento pode ser essencial em redes grandes ou quando se deseja evitar a detecção por IDS/IPS.

---

### ⏱️ 1. Definir perfil de timing

Os perfis variam de `-T0` (muito lento e furtivo) até `-T5` (extremamente agressivo):

`nmap -T4 192.168.1.1`

> 📌 Use `-T4` para equilíbrio entre rapidez e confiabilidade.

---

### ⚙️ 2. Aumentar paralelismo

Acelera o escaneamento aumentando o número de threads simultâneas:

`nmap --min-parallelism 10 --max-parallelism 50 192.168.1.1`

---

### 🧩 3. Fragmentar pacotes para evasão de firewalls

Técnica usada para evitar detecção por firewalls ou sistemas de IDS:

`nmap -f 192.168.1.1`

---

## 19.3 Descoberta e Enumeração

Esses comandos ajudam a **identificar hosts ativos, detectar sistemas operacionais, serviços em execução e mais**.

---

### 📍 1. Ping Sweep – descobrir hosts ativos

Usado para mapear quais IPs da rede estão ligados:

`nmap -sn 192.168.1.0/24`

---

### 🧠 2. Detectar sistema operacional (OS Detection)

Faz fingerprinting do sistema alvo:

`nmap -O 192.168.1.1`

---

### 🛠️ 3. Detectar serviços e versões

Descobre quais serviços estão em execução e suas versões:

`nmap -sV 192.168.1.1`

---

### 📚 4. Listar scripts NSE disponíveis

Mostra todos os scripts inclusos no Nmap e suas descrições:

`nmap --script-help=all`

---

## 19.4 Scripts NSE Populares

Os scripts NSE (Nmap Scripting Engine) permitem automatizar tarefas e detectar vulnerabilidades. Aqui estão alguns dos mais usados.

---

### 📛 1. Detectar vulnerabilidades SMB (EternalBlue)

`nmap --script smb-vuln-ms17-010 -p445 192.168.1.1`

> 💥 Essa vulnerabilidade foi usada pelo ransomware WannaCry.

---

### 🔐 2. Identificar contas padrão em serviços HTTP

Verifica a existência de logins padrão em páginas de administração web:

`nmap --script http-default-accounts -p80 192.168.1.1`

---

### 🔒 3. Verificar a segurança de conexões SSL/TLS

Analisa a robustez da configuração criptográfica de um serviço HTTPS:

`nmap --script ssl-enum-ciphers -p443 192.168.1.1`

---

## 19.5 Opções de Saída

Salvar os resultados dos escaneamentos é essencial para auditorias, comparação futura e documentação.

---

### 📝 1. Salvar em texto simples

Formato amigável para leitura direta:

`nmap -oN resultados.txt 192.168.1.1`

---

### 🧬 2. Salvar em formato XML

Formato estruturado, ideal para automação e integração com outras ferramentas:

`nmap -oX resultados.xml 192.168.1.1`

---

### 🧰 3. Salvar em múltiplos formatos simultaneamente

Com `-oA`, você gera `.nmap`, `.xml` e `.gnmap` de uma vez:

`nmap -oA resultados 192.168.1.1`

---

## Conclusão

Este capítulo serve como uma **referência rápida e prática** para o uso do Nmap. Com esses comandos em mãos, você terá uma base sólida para realizar escaneamentos desde os mais simples até os mais avançados, com ajustes finos de performance, uso de scripts NSE e geração de relatórios completos.