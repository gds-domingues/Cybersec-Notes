A Internet das Coisas (IoT) revolucionou diversos setores ao conectar dispositivos como câmeras, sensores, lâmpadas, impressoras e até eletrodomésticos à internet. No entanto, muitos desses dispositivos são projetados com **baixa prioridade em segurança**, tornando-os alvos fáceis para invasores.

O Nmap pode ser uma ferramenta poderosa para identificar e avaliar esses dispositivos vulneráveis.

---

## 13.1 Escaneamento Específico para IoT

Dispositivos IoT geralmente operam em **portas conhecidas**, como 80 (HTTP), 443 (HTTPS), 554 (RTSP) e 8080 (interfaces web alternativas). Um escaneamento focado nessas portas pode revelar câmeras IP, DVRs, modens e outros dispositivos acessíveis.

---

### 🎯 1. Identificando Dispositivos IoT Comuns

`nmap -p80,443,554,8080 192.168.1.0/24 --open`

- O parâmetro `-p` especifica as portas comuns usadas por dispositivos IoT.
    
- A flag `--open` exibe apenas os hosts com portas abertas.
    
- Ideal para uma **varredura rápida e direcionada** à presença de dispositivos IoT.
    

> 💡 **Exemplo de uso prático**: descobrir todas as câmeras IP ou dispositivos acessíveis por interface web em uma rede residencial ou corporativa.

---

### 📷 2. Enumerando Câmeras IP e Backdoors

Dispositivos como câmeras IP podem conter **backdoors conhecidos**. O Nmap possui scripts NSE específicos para identificá-los.

`nmap --script http-camera-backdoor -p80 192.168.1.1`

- Esse script tenta detectar **vulnerabilidades conhecidas** em câmeras acessíveis via HTTP.
    
- Pode identificar **backdoors deixados por fabricantes** ou falhas de autenticação.
    

> ⚠️ Muitos fabricantes de baixo custo não atualizam seus firmwares, o que perpetua essas falhas em larga escala.

---

## 13.2 Testando Credenciais Padrão

Um dos **erros mais comuns em dispositivos IoT** é a manutenção de credenciais padrão como `admin:admin` ou `admin:1234`, facilitando ataques.

---

### 🔐 1. Detectando Autenticações Padrão

O script `http-default-accounts` testa automaticamente uma lista de logins padrão conhecidos:

`nmap --script http-default-accounts -p80 192.168.1.1`

- Muito útil para verificar câmeras, impressoras, switches e outros dispositivos acessíveis via HTTP.
    
- A base de dados do script é atualizada com credenciais de centenas de fabricantes.
    

> 🧠 **Boa prática**: sempre alterar as credenciais padrão durante a configuração inicial de qualquer dispositivo.

---

## Conclusão

Dispositivos IoT representam **uma das maiores superfícies de ataque** atualmente. Muitos deles:

- Não recebem atualizações regulares;
    
- Utilizam interfaces vulneráveis;
    
- Mantêm senhas padrão ativas;
    
- São deixados acessíveis na internet por descuido.
    

Usando o Nmap, é possível:

✅ Detectar dispositivos vulneráveis;  
✅ Verificar configurações inseguras;  
✅ Testar credenciais padrão;  
✅ Mitigar riscos antes que sejam explorados.