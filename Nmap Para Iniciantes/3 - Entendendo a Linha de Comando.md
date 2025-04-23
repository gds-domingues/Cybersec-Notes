O Nmap é uma ferramenta **baseada em linha de comando**, o que significa que todas as suas funcionalidades são acessadas digitando comandos diretamente no terminal (Linux/macOS) ou no Prompt de Comando/PowerShell (Windows). Embora isso possa parecer intimidador no início, a estrutura de uso do Nmap é muito lógica e simples de aprender.

---

## Estrutura básica do comando

A sintaxe padrão de qualquer comando Nmap segue o formato:

`nmap [opções] [alvo]`
### Vamos entender cada parte:

- 🛠️ **[opções]**: São parâmetros que definem como o Nmap irá se comportar durante o escaneamento. Com elas, você pode escolher o tipo de varredura, quais portas escanear, quais scripts usar, qual formato de saída salvar, e muito mais.
    
- 🎯 **[alvo]**: É o endereço IP, nome de domínio, intervalo de IPs ou até um arquivo contendo uma lista de alvos a serem escaneados.
    

---

## Exemplo básico

Um primeiro teste pode ser feito com um domínio especialmente disponibilizado pelos desenvolvedores do Nmap:

`nmap scanme.nmap.org`

Esse comando realiza um escaneamento padrão (TCP connect scan) no domínio `scanme.nmap.org`. Ele irá verificar as **1000 portas mais comuns** e fornecer um relatório simples com os serviços encontrados.

> ⚠️ Sempre obtenha **autorização** antes de escanear alvos que não sejam públicos ou que não pertençam a você. Escaneamentos sem permissão podem ser considerados atividades maliciosas.

---

## Escaneando múltiplos alvos

Uma das grandes vantagens do Nmap é a sua capacidade de escanear múltiplos dispositivos com um único comando. Veja as formas mais comuns:

### 🔢 Lista de IPs

`nmap 192.168.1.1 192.168.1.2`

Escaneia os dois IPs especificados individualmente.

### 📶 Intervalo de IPs

`nmap 192.168.1.1-10`

Escaneia todos os IPs de `192.168.1.1` até `192.168.1.10`.

### 🌐 Sub-rede inteira (CIDR)

`nmap 192.168.1.0/24`

Escaneia todos os 256 endereços da sub-rede `192.168.1.0/24` (ou seja, de `192.168.1.0` a `192.168.1.255`), identificando hosts ativos.

> 💡 A notação CIDR (`/24`, `/16`, etc.) indica o tamanho da sub-rede. É amplamente usada em redes corporativas.

---

## Opções úteis iniciais

Existem dezenas (ou até centenas) de opções possíveis no Nmap, mas algumas delas são especialmente úteis para quem está começando.

### 🔌 `-p`: Especifica portas a escanear

Por padrão, o Nmap escaneia as 1000 portas mais comuns. Mas você pode personalizar isso com a opção `-p`:

`nmap -p 80,443 scanme.nmap.org`

Escaneia **apenas as portas 80 (HTTP)** e **443 (HTTPS)**.

Você também pode usar intervalos:

`nmap -p 1-1000 192.168.0.1`

Escaneia as portas de 1 a 1000.

---

### 🧠 `-A`: Escaneamento avançado

Essa opção ativa múltiplas funcionalidades de uma só vez:

- Detecção de sistema operacional
    
- Identificação de versão de serviços
    
- Escaneamento com scripts NSE
    
- Traceroute
    

`nmap -A scanme.nmap.org`

> ⚠️ Pode ser mais demorado e ruidoso (gera mais tráfego de rede). Use com cautela em redes grandes.

---

### 💾 `-oX`, `-oN`: Salvando a saída do escaneamento

Você pode salvar os resultados do Nmap em diferentes formatos:

- `-oN`: formato texto legível (normal)
    
- `-oX`: formato XML (útil para análises automatizadas)
    

`nmap -oN resultado.txt scanme.nmap.org nmap -oX resultado.xml scanme.nmap.org`

> ✏️ Há também `-oG` (greppable, para scripts) e `-oA` (salva nos três formatos simultaneamente: `.nmap`, `.xml`, `.gnmap`).

---

## Dica prática: Combine opções

Você pode combinar várias opções em um único comando:

`nmap -p 22,80 -A -oN resultado.txt 192.168.0.1`

Esse comando:

- Escaneia as portas 22 e 80,
    
- Usa escaneamento avançado (`-A`),
    
- Salva os resultados em texto (`-oN`),
    
- Contra o alvo `192.168.0.1`.
    

---

### Comando interativo para iniciantes:

Se você quiser aprender de forma mais visual e passo a passo, pode usar a interface gráfica do Nmap chamada **Zenmap** (especialmente útil no Windows), mas aprender os comandos é fundamental para dominar a ferramenta por completo.