Durante uma varredura, o Nmap coleta uma enorme quantidade de informações. Para tornar esse conteúdo útil, é essencial **salvar os resultados em formatos apropriados**, seja para documentação, integração com outras ferramentas ou para futuras análises.

Neste capítulo, vamos explorar os principais formatos de saída que o Nmap oferece e como eles podem ser utilizados de forma prática.

---

## 9.1 Salvando a Saída

O Nmap oferece vários modos de salvar os resultados de um escaneamento, cada um com uma finalidade diferente:

---

### 📄 1. Texto Simples (`-oN`)

Gera um relatório no formato padrão do terminal, fácil de ler manualmente.

`nmap -oN scan.txt 192.168.1.1`

> 💡 Ideal para documentações rápidas e relatórios humanos.

---

### 🧩 2. XML (`-oX`)

Gera a saída em XML, adequada para integração com ferramentas automatizadas.

`nmap -oX scan.xml 192.168.1.1`

> ⚙️ Útil para importar em frameworks como o Metasploit, ou para scripts de automação.

---

### 📝 3. Grepable (`-oG`)

Gera um formato amigável para buscas com `grep`, `awk` ou `sed`.

`nmap -oG scan.grep 192.168.1.1`

> 🔍 Perfeito para quem quer filtrar rapidamente resultados via terminal.

---

### 📦 4. Todos os Formatos Simultaneamente (`-oA`)

Salva os resultados em todos os três formatos acima com um único comando. O nome base será usado como prefixo:

`nmap -oA scan_results 192.168.1.1`

> 🎯 Uma forma prática de manter tudo organizado e pronto para qualquer uso.

---

## 9.2 Integração com Outras Ferramentas

Além de salvar os resultados, é comum integrá-los a outras ferramentas de segurança ou scripts de análise personalizada.

---

### 💣 1. Importar XML no Metasploit

Se você está usando o Metasploit Framework, pode importar um scan do Nmap para carregar os hosts e serviços descobertos:

`db_import scan.xml`

> ✅ Isso permite iniciar exploração ou pós-exploração rapidamente com base nos dados coletados.

---

### 🐍 2. Processar Resultados XML com Python

Você também pode escrever scripts para analisar os dados XML do Nmap automaticamente. Um exemplo simples:

import xml.etree.ElementTree as ET

# Lendo o arquivo XML do Nmap
tree = ET.parse('scan.xml')
root = tree.getroot()

# Iterando pelos hosts encontrados
for host in root.findall('host'):
    address = host.find('address')
    if address is not None:
        ip = address.get('addr')
        print(f"Host: {ip}")


> 🔄 Esse tipo de automação é muito útil em pentests, auditorias e pipelines de segurança.

---

## Conclusão

Entender os **formatos de saída do Nmap** é tão importante quanto realizar o escaneamento. Cada formato serve a um propósito:

- **Texto simples**: leitura humana e documentação.
    
- **XML**: integração e automação.
    
- **Grepable**: filtragem em linha de comando.
    
- **Todos juntos**: praticidade.
    

📌 Dominar esses formatos permite que você integre os resultados do Nmap ao seu workflow de segurança e facilite a geração de relatórios profissionais.