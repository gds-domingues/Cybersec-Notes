O Nmap é uma ferramenta poderosa, mas quando se trata de **escaneamentos em larga escala**, o desempenho pode ser um fator crítico. Este capítulo mostra como ajustar os parâmetros para tornar seus escaneamentos mais **rápidos e eficientes**, sem comprometer a qualidade das informações coletadas.

---

## 7.1 Ajustando Threads e Tempo de Espera

### 🧠 Por que isso importa?

Cada escaneamento envolve o envio e recebimento de pacotes de rede. Quanto mais hosts ou portas você estiver testando, **maior será o volume de tráfego gerado**. Ajustar as opções de paralelismo e timeout permite que o Nmap funcione de maneira mais inteligente.

### ⚙️ Controlar paralelismo: `--min-parallelism` e `--max-parallelism`

Essas opções definem **quantas tarefas paralelas** o Nmap pode realizar, o que impacta diretamente a velocidade.

`nmap --min-parallelism 10 --max-parallelism 50 192.168.1.0/24`

- `--min-parallelism`: garante um número mínimo de tarefas simultâneas.
    
- `--max-parallelism`: evita sobrecarregar o sistema com threads demais.
    

### ⏱️ Ajustar tempo de resposta: `--max-rtt-timeout`

Define **quanto tempo o Nmap deve esperar por uma resposta** antes de desistir.

`nmap --max-rtt-timeout 200ms 192.168.1.0/24`

- Reduzir esse tempo pode acelerar o escaneamento, mas cuidado: conexões lentas podem ser interpretadas como inativas.
    

> 🛠️ **Dica prática:** Teste pequenos intervalos de rede primeiro, para calibrar essas opções antes de aplicá-las em escaneamentos maiores.

---

## 7.2 Escaneamento em Grandes Redes

Escanear sub-redes inteiras pode ser demorado. Abaixo estão algumas práticas para **acelerar a execução sem perder precisão**:

### 🎯 Reduza o escopo das portas: `-p`

Escanear todas as 65.535 portas é custoso. Escaneie apenas as necessárias:

`nmap -p 22,80,443 192.168.1.0/24`

Você também pode usar intervalos:

`nmap -p 1-1024 192.168.1.0/24`

### ⚡ Use o modo agressivo de timing: `-T4`

O timing `T4` acelera o envio de pacotes. É uma boa escolha para redes rápidas e confiáveis.

`nmap -T4 192.168.1.0/24`

> ⚠️ Cuidado com `T5`: embora seja ainda mais rápido, ele **pode causar falsos negativos** em redes congestionadas ou com dispositivos sensíveis.

### 🔀 Escaneie hosts de forma aleatória: `--randomize-hosts`

Evita seguir a ordem sequencial de IPs. Isso pode ajudar a **reduzir detecção** por IDS e balancear a carga:

`nmap --randomize-hosts 192.168.1.0/24`

---

## 7.3 Perfis de Timing (`-T`)

O Nmap oferece 6 perfis predefinidos que ajustam automaticamente parâmetros como tempo de espera, número de threads e velocidade de envio de pacotes:

|Perfil|Nome|Descrição|
|---|---|---|
|T0|Paranoico|Extremamente lento; ideal para evitar qualquer detecção.|
|T1|Sneaky|Um pouco mais rápido, ainda focado em evitar sistemas de defesa.|
|T2|Polite|Reduz carga na rede, útil para escaneamentos em horários críticos.|
|T3|Normal|Configuração padrão.|
|T4|Agressivo|Rápido e confiável para redes bem estruturadas.|
|T5|Insano|Máxima velocidade, porém menos estável e com mais falsos negativos.|

### 💡 Exemplo prático:

`nmap -T4 -p 22,80,443 192.168.1.0/24`

> Ideal para escanear portas comuns em uma rede corporativa com bom desempenho.

---

## Conclusão

A otimização do Nmap permite que você adapte a ferramenta ao seu ambiente, equilibrando **velocidade, precisão e discrição**. Seja em um pentest de larga escala ou uma análise pontual, **ajustar o desempenho pode fazer toda a diferença** na eficiência da varredura.