[[Etapa 3 - Sistemas Operacionais – Windows em Foco]]
[[Etapa 4 - Linux – Primeiros Passos e Medidas Iniciais de Segurança]]
# Fundamentos de Redes de Computadores

**Nome:** Gabriel Domingues Silva  
**Turma:** 24E3-1  
**Tema:** Teste de Performance 2 - Sistemas Operacionais  
**Professor:** Fabiano Alves Gisbert  
**Instituto:** Infnet

## Índice

1. [Características de uma arquitetura Von-Neumann](#1-características-de-uma-arquitetura-von-neumann)
2. [Função de um clock de processador](#2-função-de-um-clock-de-processador)
3. [Diferença entre memória RAM e ROM](#3-diferença-entre-memória-ram-e-rom)
4. [O que é memória cache?](#4-o-que-é-memória-cache)
5. [Dispositivos de Entrada e Saída](#5-dispositivos-de-entrada-e-saída)
6. [Função de um driver de dispositivo](#6-função-de-um-driver-de-dispositivo)
7. [Barramento de conexão externa](#7-barramento-de-conexão-externa)
8. [O que é um Sistema Operacional?](#8-o-que-é-um-sistema-operacional)
9. [Principal função de um sistema computacional](#9-principal-função-de-um-sistema-computacional)
10. [O que são processos?](#10-o-que-são-processos)
11. [Prevenção de Deadlocks](#11-prevenção-de-deadlocks)
12. [Sistemas operacionais modernos](#12-sistemas-operacionais-modernos)
13. [Origem e popularidade do Windows](#13-origem-e-popularidade-do-windows)
14. [Característica principal da inicialização do Windows](#14-característica-principal-da-inicialização-do-windows)
15. [Diferença entre Windows 32 e 64 bits](#15-diferença-entre-windows-32-e-64-bits)
16. [Formas de instalação do sistema operacional Windows](#16-formas-de-instalação-do-sistema-operacional-windows)
17. [Ferramentas de segurança do Windows 11](#17-ferramentas-de-segurança-do-windows-11)
18. [Windows em jogos e multimídia](#18-windows-em-jogos-e-multimídia)
19. [Origem e uso do Linux em ambientes acadêmicos](#19-origem-e-uso-do-linux-em-ambientes-acadêmicos)
20. [Distribuições de Linux atualmente ativas](#20-distribuições-de-linux-atualmente-ativas)

![[Arquitetura_de_Computadores_e_Sistemas_Operacionais__TP2.pdf]]
## 1. Características de uma arquitetura Von-Neumann

- **Programa Armazenado:** Instruções e dados residem na mesma memória, permitindo que o computador modifique suas próprias instruções.
- **Unidade Central de Processamento (CPU):** Executa as instruções do programa, buscando-as da memória, decodificando-as e executando-as.
- **Memória Principal:** Armazena tanto as instruções do programa quanto os dados que ele manipula.
- **Dispositivos de Entrada/Saída (E/S):** Permitem a interação com o mundo exterior, recebendo dados e enviando resultados.
- **Execução Sequencial:** Instruções são executadas uma após a outra, em ordem, a menos que haja um desvio explícito (como um salto).

## 2. Função de um clock de processador

O clock de um processador atua como um metrônomo, sincronizando e ditando o ritmo das operações internas do processador. Cada "tique" do clock permite que o processador execute uma etapa básica de processamento. Quanto maior a frequência do clock (medida em Hertz), mais rápido o processador pode realizar suas operações.

## 3. Diferença entre memória RAM e ROM

- **RAM (Random Access Memory):** Volátil (perde dados ao desligar), leitura e escrita rápidas, usada para armazenar dados temporários, maior capacidade.
- **ROM (Read-Only Memory):** Não volátil (mantém dados ao desligar), leitura rápida, escrita lenta ou impossível, usada para armazenar firmware e dados permanentes, menor capacidade.

## 4. O que é memória cache?

A memória cache é um tipo de memória de alta velocidade e baixo acesso localizada entre o processador e a memória principal. Sua função é armazenar cópias de dados e instruções frequentemente acessados, permitindo que o processador os recupere mais rapidamente do que se tivesse que buscá-los na memória principal, acelerando o desempenho geral do sistema.

## 5. Dispositivos de Entrada e Saída

- **Entrada:**
  - Teclado
  - Mouse

- **Saída:**
  - Monitor
  - Impressora

## 6. Função de um driver de dispositivo

Um driver de dispositivo atua como um tradutor e intermediário entre o sistema operacional e um dispositivo de hardware específico. Ele permite que o sistema operacional se comunique e controle o dispositivo, enviando comandos e recebendo dados de forma que ambos possam interagir de maneira eficaz.

## 7. Barramento de conexão externa

Um exemplo comum de barramento de conexão externa é o USB (Universal Serial Bus).

## 8. O que é um Sistema Operacional

Um Sistema Operacional (SO) é um conjunto de programas que gerencia os recursos de hardware e software de um computador, fornecendo uma interface entre o usuário e a máquina. Ele controla a execução de programas, gerencia a memória, o acesso a dispositivos de entrada e saída, o sistema de arquivos e oferece serviços básicos para que os aplicativos possam ser executados de forma eficiente e segura.

## 9. Principal função de um sistema computacional

A principal função de um sistema computacional é processar dados. Isso envolve receber dados de entrada (input), executar operações sobre esses dados de acordo com um conjunto de instruções (programa) e produzir resultados (output). Em essência, um sistema computacional transforma informações de uma forma para outra, permitindo realizar tarefas complexas e automatizar processos, desde cálculos matemáticos até a criação de conteúdo multimídia e a comunicação em rede.

## 10. O que são processos

Processos são instâncias em execução de um programa, representando a unidade básica de trabalho gerenciada pelo sistema operacional. Cada processo possui seu próprio espaço de memória, recursos alocados e um contexto de execução, permitindo que o sistema operacional realize o escalonamento e a alternância entre diferentes processos, criando a ilusão de que vários programas estão sendo executados simultaneamente.

## 11. Prevenção de Deadlocks

Um sistema operacional pode empregar diversas estratégias para evitar a ocorrência de deadlocks:

1. **Prevenção:** Elimina uma das quatro condições necessárias para um deadlock:
   - **Exclusão Mútua:** Impossível de evitar em geral, pois alguns recursos só podem ser usados por um processo de cada vez.
   - **Posse e Espera:** Exigir que os processos solicitem todos os recursos de uma vez antes de começar a execução. Se algum recurso não estiver disponível, o processo aguarda até que todos estejam.
   - **Não Preempção:** Permitir que o sistema operacional retire recursos de um processo se outro processo precisar deles.
   - **Espera Circular:** Impor uma ordem de aquisição de recursos, de modo que os processos solicitem recursos em uma sequência predefinida, evitando a formação de ciclos de espera.

2. **Evitação:** Utiliza algoritmos (como o algoritmo do banqueiro) para analisar as solicitações de recursos e concedê-los apenas se o sistema permanecer em um estado seguro, onde não há risco de deadlock.

3. **Detecção e Recuperação:** Permite que deadlocks ocorram, mas possui mecanismos para detectá-los e tomar ações para recuperar o sistema, como abortar um ou mais processos envolvidos no deadlock ou realizar um rollback para um estado anterior.

A escolha da estratégia depende das características do sistema e dos requisitos de desempenho. A prevenção é a mais segura, mas pode ser restritiva e ineficiente. A evitação é mais flexível, mas exige análise complexa a cada solicitação de recurso. A detecção e recuperação é a mais simples de implementar, mas pode levar a perda de trabalho e impacto no desempenho.

## 12. Sistemas operacionais modernos

Dois exemplos proeminentes de sistemas operacionais modernos são:

- **Windows 11:** A mais recente versão do sistema operacional da Microsoft, amplamente utilizado em desktops e laptops, oferecendo uma interface gráfica intuitiva e suporte a uma vasta gama de aplicativos.
- **macOS Ventura:** O sistema operacional da Apple, presente em seus computadores Mac, conhecido por sua elegância, design intuitivo e integração perfeita com outros dispositivos da Apple.

## 13. Origem e popularidade do Windows

O Windows originou-se como uma interface gráfica para o MS-DOS, sistema operacional dominante na década de 1980. Sua interface intuitiva, baseada em janelas e ícones, facilitou o uso do computador em comparação com a linha de comando do MS-DOS.

A popularidade do Windows se deve a diversos fatores:
- **Facilidade de uso:** A interface gráfica tornou o computador acessível a um público mais amplo, não apenas a especialistas em informática.
- **Compatibilidade:** O Windows se tornou o padrão de fato para desktops, com ampla disponibilidade de software e hardware compatíveis.
- **Marketing e distribuição:** A Microsoft investiu pesadamente em marketing e distribuição, garantindo a presença do Windows em praticamente todos os computadores novos.
- **Evolução constante:** O Windows passou por diversas versões, incorporando novos recursos e tecnologias, mantendo-se relevante ao longo dos anos.

Esses fatores combinados impulsionaram o Windows a se tornar o sistema operacional mais popular em desktops, consolidando sua posição no mercado e moldando a forma como interagimos com computadores.

## 14. Característica principal da inicialização do Windows

A característica principal da arquitetura de inicialização do Windows é o uso do BIOS (Basic Input/Output System) ou UEFI (Unified Extensible Firmware Interface) para iniciar o processo de carregamento do sistema operacional.

O BIOS/UEFI realiza testes básicos de hardware, identifica dispositivos de inicialização e carrega o gerenciador de boot do Windows, que por sua vez carrega o kernel do sistema operacional e inicia os serviços essenciais para o funcionamento do Windows.

Em resumo, a inicialização do Windows depende de um firmware (BIOS ou UEFI) para iniciar o processo de carregamento do sistema operacional, que é então assumido pelo gerenciador de boot e pelo kernel do Windows.

## 15. Diferença entre Windows 32 e 64 bits

A principal diferença reside na capacidade de endereçamento de memória e no tipo de processador compatível:

- **Windows 32 bits:**
  - Limitado a endereçar até 4 GB de memória RAM.
  - Compatível apenas com processadores de 32 bits.
  - Pode executar aplicativos de 32 bits, mas não de 64 bits.

- **Windows 64 bits:**
  - Capaz de endereçar muito mais memória RAM (teoricamente até 16 exabytes).
  - Requer um processador de 64 bits.
  - Pode executar aplicativos de 32 e 64 bits.
  - Geralmente oferece melhor desempenho em tarefas que exigem muita memória ou processamento intensivo.

Em resumo, a versão de 64 bits do Windows permite aproveitar melhor o hardware moderno, com maior capacidade de memória e processadores mais poderosos, resultando em um sistema mais rápido e capaz de lidar com tarefas mais exigentes.

## 16. Formas de instalação do sistema operacional Windows

As principais formas de instalação do sistema operacional Windows são:

1. **Instalação limpa (formatação):**
   - Apaga todos os dados do disco rígido e instala uma nova cópia do Windows.
   - Ideal para computadores novos ou quando se deseja um sistema limpo e livre de problemas.
   - Requer backup de todos os dados importantes antes da instalação.

2. **Atualização (upgrade):**
   - Mantém os arquivos, configurações e aplicativos existentes e instala uma nova versão do Windows sobre a anterior.
   - Útil para migrar para uma versão mais recente do Windows sem perder dados.
   - Pode apresentar problemas de compatibilidade com alguns aplicativos ou drivers.

3. **Instalação personalizada:**
   - Permite escolher quais partições do disco rígido serão usadas e formatadas.
   - Oferece mais controle sobre o processo de instalação.
   - Requer conhecimento técnico para configurar as partições corretamente.

4. **Instalação de recuperação:**
   - Restaura o Windows para um estado anterior, utilizando uma imagem de recuperação pré-instalada ou criada pelo usuário.
   - Útil para solucionar problemas graves do sistema ou restaurar as configurações de fábrica.
   - Pode resultar na perda de dados recentes, dependendo do ponto de restauração escolhido.

A escolha da forma de instalação depende do objetivo e das necessidades do usuário, levando em consideração fatores como a presença de dados importantes, a versão atual do Windows e o nível de conhecimento técnico.

## 17. Ferramentas de segurança do Windows 11

### Microsoft Defender Antivirus

O Microsoft Defender Antivirus é uma solução antimalware integrada ao Windows 11 que oferece proteção em tempo real contra vírus, malware, ransomware e outras ameaças. Ele utiliza tecnologias avançadas de detecção e prevenção, incluindo aprendizado de máquina e análise comportamental, para identificar e bloquear ameaças conhecidas e emergentes.

O Defender Antivirus realiza varreduras regulares do sistema em busca de malware, monitora atividades suspeitas e oferece recursos como proteção contra phishing e controle de acesso a pastas para evitar alterações não autorizadas em arquivos importantes.

Além disso, o Defender Antivirus é atualizado automaticamente pela Microsoft, garantindo que esteja sempre preparado para lidar com as ameaças mais recentes. Ele também se integra com outros recursos de segurança do Windows 11, como o Firewall do Windows Defender e o SmartScreen, para fornecer uma camada adicional de proteção.

## 18. Windows em jogos e multimídia

O Windows mantém sua liderança em jogos e multimídia devido a uma combinação de fatores:

- **Ampla compatibilidade de hardware e software:**
  - A vasta maioria dos jogos e softwares de multimídia são desenvolvidos primeiramente para Windows, garantindo acesso a um catálogo extenso e variado.
  - A grande variedade de hardware compatível com Windows oferece flexibilidade na escolha de componentes e configurações para otimizar o desempenho.

- **Otimização e suporte de drivers:**
  - Desenvolvedores de hardware priorizam o desenvolvimento de drivers otimizados para Windows, garantindo melhor desempenho e compatibilidade com jogos e aplicativos multimídia.
  - A Microsoft investe em otimizações específicas para jogos no Windows, como o DirectX, que oferece recursos avançados de renderização gráfica e aceleração de hardware.

- **Comunidade e ecossistema:**
  - A grande comunidade de jogadores e usuários de multimídia no Windows facilita a troca de informações, suporte técnico e compartilhamento de conteúdo.
  - Serviços como a Xbox Live e a Microsoft Store oferecem integração com jogos, recursos sociais e acesso a conteúdo multimídia.

- **Legado e familiaridade:**
  - O Windows é o sistema operacional mais utilizado em desktops, o que gera familiaridade para a maioria dos usuários, facilitando a configuração e o uso de jogos e aplicativos multimídia.
  - A longa história do Windows no mercado de jogos e multimídia consolidou sua posição, criando um ciclo de reforço positivo, onde desenvolvedores e usuários continuam a investir na plataforma.

Embora outras plataformas, como o macOS e o Linux, tenham avançado em termos de compatibilidade e desempenho, o Windows ainda oferece a combinação mais completa de recursos, suporte e ecossistema para jogos e multimídia, mantendo sua posição de destaque nesse segmento.

## 19. Origem e uso do Linux em ambientes acadêmicos

### Origem

O Linux foi criado em 1991 por Linus Torvalds, um estudante finlandês, como um projeto pessoal inspirado no sistema operacional Unix. Sua natureza aberta e colaborativa permitiu que desenvolvedores de todo o mundo contribuíssem para seu crescimento e aprimoramento.

### Uso em Ambientes Acadêmicos

O Linux é amplamente utilizado em ambientes acadêmicos devido a:

- **Custo-benefício:** O Linux é gratuito e de código aberto, permitindo que instituições de ensino economizem em licenças de software proprietário.
- **Flexibilidade e personalização:** O Linux oferece grande liberdade para customização e adaptação às necessidades específicas de cada ambiente acadêmico, seja para pesquisa, ensino ou administração.
- **Estabilidade e segurança:** O Linux é conhecido por sua robustez e resistência a falhas, além de oferecer recursos avançados de segurança, tornando-o ideal para ambientes que exigem alta disponibilidade e proteção de dados.
- **Comunidade e aprendizado:** A comunidade ativa de desenvolvedores e usuários do Linux oferece suporte, documentação e recursos educacionais, incentivando o aprendizado e a colaboração entre estudantes e pesquisadores.
- **Fomento à pesquisa e inovação:** A natureza aberta do Linux permite que estudantes e pesquisadores explorem o código-fonte, modifiquem o sistema e desenvolvam novas tecnologias, impulsionando a pesquisa e a inovação.

## 20. Distribuições de Linux atualmente ativas

Três exemplos proeminentes de distribuições Linux ativas e populares são:

- **Ubuntu:** Uma das distribuições mais conhecidas e amigáveis para iniciantes, com foco em facilidade de uso e ampla comunidade de suporte.
- **Fedora:** Uma distribuição patrocinada pela Red Hat, com foco em inovação e tecnologias de ponta, frequentemente utilizada por desenvolvedores e entusiastas de software livre.
- **Debian:** Uma distribuição estável e confiável, conhecida por sua aderência aos princípios do software livre e sua extensa coleção de pacotes de software.
