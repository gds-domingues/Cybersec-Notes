[[Etapa 9 - Sistemas Operacionais em Dispositivos Móveis- Segurança]]
[[Etapa 8 - Sistemas Operacionais em Dispositivos Móveis- Introdução]]
[[Etapa 7 - Dispositivos Móveis]]
[[Etapa 6 - Linux – Arquivos de Log, Monitoramento, Permissões e Malware]]
[[Etapa 5 - Linux – Usando Shell e Linha de Comando]]
[[Etapa 4 - Linux – Primeiros Passos e Medidas Iniciais de Segurança]]
[[Etapa 3 - Sistemas Operacionais – Windows em Foco]]
[[Etapa 2 - Laptops e Dispositivos Móveis em Foco - Configuração, Comunicação e Manutenção]]
[[Etapa 1 - Desktops - Evolução Tecnológica e Impacto na Computação Pessoal]]
[[Etapa 0 - Introdução]]
# Arquitetura de Computadores e Sistemas Operacionais — Assessment

**Nome:** Gabriel Domingues Silva  
**Turma:** 24E3-1  
**Tema:** Assessment  
**Professor:** Fabiano Alves Gisbert  
**Instituto:** Infnet

## Índice

1. [O que é um sistema computacional?](#1-o-que-é-um-sistema-computacional)
2. [Quais são os componentes de um processador?](#2-quais-são-os-componentes-de-um-processador)
3. [Reprogramação de EPROM](#3-reprogramação-de-eprom)
4. [Resolução de problemas em montagem de computador](#4-resolução-de-problemas-em-montagem-de-computador)
5. [Componentes de um notebook vs desktop](#5-componentes-de-um-notebook-vs-desktop)
6. [Diferenças entre programas, processos e threads](#6-diferenças-entre-programas-processos-e-threads)
7. [Origem e popularização do Windows](#7-origem-e-popularização-do-windows)
8. [Diferenças organizacionais entre Windows e Linux](#8-diferenças-organizacionais-entre-windows-e-linux)
9. [Registro do Windows e sua importância](#9-registro-do-windows-e-sua-importância)
10. [Gerenciamento de processos no Windows](#10-gerenciamento-de-processos-no-windows)
11. [Estrutura de diretórios em um sistema Linux](#11-estrutura-de-diretórios-em-um-sistema-linux)
12. [Gerenciamento de partições em um sistema Linux](#12-gerenciamento-de-partições-em-um-sistema-linux)
13. [Informações do sistema Windows](#13-informações-do-sistema-windows)
14. [Instalação de um sistema operacional Linux](#14-instalação-de-um-sistema-operacional-linux)
15. [Configuração de rede no Linux](#15-configuração-de-rede-no-linux)
16. [Tecnologia RISC em dispositivos móveis](#16-tecnologia-risc-em-dispositivos-móveis)
17. [Arquitetura ARM em dispositivos móveis](#17-arquitetura-arm-em-dispositivos-móveis)
18. [Comparação entre Android e iOS](#18-comparação-entre-android-e-ios)
19. [Vulnerabilidades em dispositivos móveis](#19-vulnerabilidades-em-dispositivos-móveis)
20. [Tipos de bloqueios de segurança em dispositivos móveis](#20-tipos-de-bloqueios-de-segurança-em-dispositivos-móveis)

![[Arquitetura_de_Computadores_e_Sistemas_Operacionais___Assessment.pdf]]
## 1. O que é um sistema computacional?

### 1.1 Definição
Um sistema computacional é um conjunto integrado de hardware (componentes físicos) e software (programas) que trabalham juntos para processar dados e executar tarefas.

### 1.2 Arquitetura de Von Neumann
Características da Arquitetura de Von Neumann incluem:
- **Memória Principal Unificada:** Armazena tanto instruções quanto dados, acessíveis pela CPU.
- **CPU:** Executa instruções e realiza cálculos.
- **Dispositivos de Entrada/Saída:** Permitem comunicação com o mundo externo.
- **Barramento de Sistema:** Conecta componentes do sistema.
- **Execução Sequencial de Instruções:** Instruções são executadas uma após a outra.

## 2. Quais são os componentes de um processador?

### 2.1 Componentes e Funções
- **Unidade Lógica e Aritmética (ULA):** Realiza operações aritméticas e lógicas.
- **Unidade de Controle (UC):** Coordena atividades do processador.
- **Registradores:** Armazenam temporariamente dados e instruções.
- **Cache:** Armazena cópias de dados e instruções frequentemente acessados.
- **Barramento Interno:** Conecta componentes do processador.

## 3. Reprogramação de EPROM

### 3.1 Identificação e Reprogramação
- **Inspecção Visual e Consulta ao Manual:** Para identificar o tipo de EPROM.
- **Equipamento Necessário:** Programador de EPROM e arquivo de firmware atualizado.
- **Processo:** Inclui remoção, apagamento (usando luz UV), gravação e verificação.

### 3.2 Diferenças entre Tecnologias ROM
- **ROM:** Programada em fábrica, não apagável.
- **PROM:** Programável uma vez pelo usuário.
- **EPROM:** Reprogramável múltiplas vezes usando luz UV.
- **EEPROM:** Reprogramável múltiplas vezes eletricamente.

## 4. Resolução de problemas em montagem de computador

### 4.1 Diagnóstico e Solução
- **Interpretação de Bipes:** Segundo o manual da placa-mãe.
- **Verificação das Conexões:** Inclui alimentação, memória e placas.
- **Testes Adicionais:** Remoção de componentes não essenciais e teste de componentes individuais.

## 5. Componentes de um notebook vs desktop

Diferenças principais incluem:
- **Tela, Teclado, e Mouse/Touchpad:** Integrados no notebook.
- **Bateria:** Presente somente em notebooks.
- **Placa-Mãe, Processador, e Memória RAM:** Formatos e potências variam.

## 6. Diferenças entre programas, processos e threads

- **Programa:** Conjunto de instruções armazenadas.
- **Processo:** Instância em execução de um programa.
- **Thread:** Menor unidade de execução dentro de um processo.

## 7. Origem e popularização do Windows

- **Origem:** Interface gráfica para MS-DOS lançada em 1985.
- **Popularização:** Facilidade de uso, interface amigável, e ampla compatibilidade.

## 8. Diferenças organizacionais entre Windows e Linux

- **Windows:** Proprietário, código fechado.
- **Linux:** Código aberto, desenvolvimento colaborativo.

## 9. Registro do Windows e sua importância

### 9.1 Importância
Centraliza informações de configuração, personaliza sistema e aplicativos.

### 9.2 Chaves Principais
- **HKEY_CLASSES_ROOT:** Associações de arquivos.
- **HKEY_CURRENT_USER:** Configurações do usuário atual.
- **HKEY_LOCAL_MACHINE:** Configurações globais do sistema.
- **HKEY_USERS:** Perfis de todos os usuários.
- **HKEY_CURRENT_CONFIG:** Perfil de hardware ativo.

## 10. Gerenciamento de processos no Windows

**Ferramenta:** Gerenciador de Tarefas.

## 11. Estrutura de diretórios em um sistema Linux

- **/ (raiz):** Ponto de partida da hierarquia.
- **/home:** Diretórios pessoais dos usuários.
- **/etc:** Arquivos de configuração do sistema.

## 12. Gerenciamento de partições em um sistema Linux

Uso de ferramentas como GParted e comandos como fdisk ou parted para alterar partições.

## 13. Informações do sistema Windows

Acessadas através da tela "Sistema" nas configurações do Windows.

## 14. Instalação de um sistema operacional Linux

Processo de seleção e configuração da distribuição, instalação de pacotes e configuração do sistema.

## 15. Configuração de rede no Linux

Localização e edição do arquivo de configuração de rede.

## 16. Tecnologia RISC em dispositivos móveis

Vantagens incluem eficiência energética e menor geração de calor.

## 17. Arquitetura ARM em dispositivos móveis

Características incluem eficiência energética, design compacto e licenciamento flexível.

## 18. Comparação entre Android e iOS

Diferenças em origem, customização, lojas de aplicativos e dispositivos suportados.

## 19. Vulnerabilidades em dispositivos móveis

Exemplos incluem Stagefright no Android e Pegasus no iOS.

## 20. Tipos de bloqueios de segurança em dispositivos móveis

Incluem PIN, senha, padrão de desenho, impressão digital, reconhecimento facial e de íris.
