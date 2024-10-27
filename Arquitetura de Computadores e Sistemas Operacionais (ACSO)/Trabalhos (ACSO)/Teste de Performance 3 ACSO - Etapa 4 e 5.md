[[Etapa 4 - Linux – Primeiros Passos e Medidas Iniciais de Segurança]]
[[Etapa 5 - Linux – Usando Shell e Linha de Comando]]
# Fundamentos de Redes de Computadores

**Nome:** Gabriel Domingues Silva  
**Turma:** 24E3-1  
**Tema:** Teste de Performance 3 - Windows, Linux e Virtualização  
**Professor:** Fabiano Alves Gisbert  
**Instituto:** Infnet
## Índice

1. [Aba de atalhos de comandos na Área de Trabalho](#1-aba-de-atalhos-de-comandos-na-área-de-trabalho)
2. [Troca de driver de placa de vídeo](#2-troca-de-driver-de-placa-de-vídeo)
3. [Verificação de status da rede no Windows](#3-verificação-de-status-da-rede-no-windows)
4. [Listagem de processos por uso de CPU](#4-listagem-de-processos-por-uso-de-cpu)
5. [Comando de verificação de integridade do sistema](#5-comando-de-verificação-de-integridade-do-sistema)
6. [Componentes do Windows Security](#6-componentes-do-windows-security)
7. [Windows Registry e ferramenta de edição](#7-windows-registry-e-ferramenta-de-edição)
8. [Edição de componentes de hardware via regedit](#8-edição-de-componentes-de-hardware-via-regedit)
9. [Análise de memória e CPU no Performance Monitor](#9-análise-de-memória-e-cpu-no-performance-monitor)
10. [Versão do Kernel do Windows](#10-versão-do-kernel-do-windows)
11. [Diferenças entre CLI e GUI no Linux](#11-diferenças-entre-cli-e-gui-no-linux)
12. [Criação de arquivo no Linux](#12-criação-de-arquivo-no-linux)
13. [Verificação de IP no Linux](#13-verificação-de-ip-no-linux)
14. [Verificação e encerramento de processos no Linux](#14-verificação-e-encerramento-de-processos-no-linux)
15. [SOC e ferramenta de monitoramento de rede no Linux](#15-soc-e-ferramenta-de-monitoramento-de-rede-no-linux)
16. [Ferramenta de IDS no Linux e comando de análise de log](#16-ferramenta-de-ids-no-linux-e-comando-de-análise-de-log)

![[Arquitetura_de_Computadores_e_Sistemas_Operacionais__TP3.pdf]]
## 1. Aba de atalhos de comandos na Área de Trabalho

Para acessar a aba de atalhos de comandos na Área de Trabalho, clique com o botão direito no menu iniciar.

## 2. Troca de driver de placa de vídeo

Para trocar o driver de uma placa de vídeo que apresente mau funcionamento:
1. **Identificar o modelo da placa de vídeo:** Utilize o Gerenciador de Dispositivos no Windows ou `lspci | grep VGA` no Linux.
2. **Baixar o driver mais recente:** Acesse o site do fabricante e encontre o driver adequado.
3. **Desinstalar o driver atual:** Use o Painel de Controle no Windows ou um comando de terminal no Linux.
4. **Instalar o novo driver:** Execute o instalador baixado e siga as instruções.
5. **Reiniciar o sistema.**

## 3. Verificação de status da rede no Windows

Para verificar o status da rede no Windows, acesse o Terminal e execute o comando `ipconfig`.

## 4. Listagem de processos por uso de CPU

Para listar os processos em execução em ordem de uso de CPU no Windows, utilize o Gerenciador de Tarefas (Ctrl + Shift + Esc) e ordene pela coluna de uso de CPU.

## 5. Comando de verificação de integridade do sistema

O comando `sfc /scannow` no Prompt de Comando verifica a integridade dos arquivos de sistema do Windows.

## 6. Componentes do Windows Security

Os principais componentes do Windows Security incluem:
1. **Proteção contra vírus e ameaças**
2. **Firewall e proteção de rede**
3. **Controle de aplicativos e navegador**
4. **Segurança de dispositivo**
5. **Desempenho e integridade do dispositivo**
6. **Opções de família**
7. **Proteção de conta**

## 7. Windows Registry e ferramenta de edição

O Windows Registry armazena informações de configuração do sistema. A ferramenta para sua edição é o Editor de Registro (`regedit`).

## 8. Edição de componentes de hardware via regedit

Para editar componentes de hardware no Registry, abra o `regedit` e navegue até `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class`.

## 9. Análise de memória e CPU no Performance Monitor

Abra o Performance Monitor para analisar o uso de memória e CPU no Windows, monitorando as mudanças durante tarefas específicas.

## 10. Versão do Kernel do Windows

Para verificar a versão do Kernel do Windows, abra o Prompt de Comando e digite `ver`.

## 11. Diferenças entre CLI e GUI no Linux

- **CLI (Command Line Interface):** Interage através de comandos textuais (ex: bash, vim).
- **GUI (Graphical User Interface):** Interage através de elementos gráficos (ex: GIMP, Firefox).

## 12. Criação de arquivo no Linux

Para criar um arquivo chamado `teste.doc` no diretório `/usr`, utilize o terminal.

## 13. Verificação de IP no Linux

Para verificar o endereço IP no Linux:
- **CLI:** Digite `ifconfig` no terminal.
- **GUI:** Acesse as configurações de rede através do ícone de rede.

## 14. Verificação e encerramento de processos no Linux

Use `ps -p 511` para verificar e `kill 511` ou `kill -9 511` para encerrar um processo instável com ID 511.

## 15. SOC e ferramenta de monitoramento de rede no Linux

Um SOC (Security Operations Center) auxilia na segurança de rede. O Wireshark é uma ferramenta que pode ser utilizada para monitoramento.

## 16. Ferramenta de IDS no Linux e comando de análise de log

O Snort é um sistema de detecção de intrusões. Use `tail -f /var/log/snort/alert` para analisar os logs de alertas.
