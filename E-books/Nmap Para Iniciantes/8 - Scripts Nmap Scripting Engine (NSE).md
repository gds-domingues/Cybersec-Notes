Uma das funcionalidades que torna o Nmap mais do que apenas um scanner de portas é o **Nmap Scripting Engine (NSE)**. Ele permite automatizar tarefas, realizar análises detalhadas e até detectar vulnerabilidades conhecidas – tudo com um simples comando.

---

## 8.1 Introdução ao NSE

### 🔍 O que é o NSE?

O **NSE** é um mecanismo que permite ao Nmap executar scripts escritos em **LUA** – uma linguagem leve e fácil de aprender. Esses scripts expandem as funcionalidades do Nmap para além do escaneamento de portas, permitindo:

- Enumeração de serviços e usuários;
    
- Verificação de vulnerabilidades;
    
- Coleta de informações sobre o sistema;
    
- Testes personalizados de segurança.
    

### 📁 Onde ficam os scripts?

Os scripts já vêm com o Nmap e ficam localizados no seguinte diretório (padrão para sistemas Linux):

`/usr/share/nmap/scripts/`

Você pode navegar por lá e explorar centenas de scripts divididos por categorias como `auth`, `default`, `vuln`, `discovery`, `malware`, etc.

> 🧠 **Dica:** Para atualizar os scripts do NSE, você pode rodar:
>
> `sudo nmap --script-updatedb`

---

## 8.2 Scripts Populares do NSE

Aqui estão alguns scripts amplamente utilizados em testes de segurança:

### 1. 🔐 Enumeração de compartilhamentos SMB

Descobre os compartilhamentos disponíveis em servidores SMB (porta 445):

`nmap --script smb-enum-shares -p445 192.168.1.1`

---

### 2. 🌐 Detecção de vulnerabilidades HTTP

Verifica se um servidor está vulnerável à falha **Apache Struts CVE-2017-5638**:

`nmap --script http-vuln-cve2017-5638 -p80 192.168.1.1`

---

### 3. 📡 Identificação de servidores DNS recursivos

Detecta servidores DNS que permitem requisições recursivas:

`nmap --script dns-recursion 192.168.1.0/24`

---

### 4. 🚨 Busca por vulnerabilidades conhecidas (via `vulners`)

Esse script usa a base de dados **Vulners** para detectar possíveis falhas:

`nmap --script vulners 192.168.1.1`

> 💡 **Importante**: você pode combinar scripts com outras opções do Nmap como `-sV`, `-O`, `-T4`, etc., para melhorar a coleta de informações.

---

## 8.3 Criando Seus Próprios Scripts NSE

Você também pode criar seus próprios scripts NSE personalizados para tarefas específicas.

### 🛠️ Exemplo: Script básico para verificar resposta HTTP

#### 1. Crie o arquivo `meu_script.nse`:

Salve este conteúdo em um arquivo com extensão `.nse` no diretório de scripts do Nmap:

categories = {"default", "discovery"}

-- Função principal executada pelo Nmap
action = function(host, port)
  local socket = nmap.new_socket()
  socket:set_timeout(5000)

  local status, err = socket:connect(host.ip, port.number)
  if not status then
    return "Erro ao conectar: " .. err
  end

  socket:send("HEAD / HTTP/1.1\r\nHost: " .. host.ip .. "\r\n\r\n")
  local response = socket:receive_lines(1)

  socket:close()
  return response or "Sem resposta HTTP detectada."
end'

#### 2. Execute o script:

`nmap --script ./meu_script.nse -p80 192.168.1.1`

> 🔍 **Nota**: Se estiver rodando o script fora do diretório padrão, forneça o caminho completo ou relativo no comando.

---

## Conclusão

O NSE transforma o Nmap em **muito mais do que um scanner de portas**. Ele é uma verdadeira plataforma de automação para tarefas de segurança, ideal tanto para iniciantes quanto para profissionais avançados.

Com o tempo, você pode começar a:

- **Customizar scripts existentes**;
    
- **Contribuir com a comunidade Nmap**;
    
- **Automatizar varreduras complexas com poucas linhas de código**.