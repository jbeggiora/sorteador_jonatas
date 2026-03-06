# 🎲 Sorteador Responsivo com Foco em AppSec

Este projeto é um sorteador de nomes desenvolvido com **Django**, focado em entregar uma experiência de usuário (UX) fluida e práticas de **Segurança de Aplicação (AppSec)**.

## 🛡️ Camadas de Defesa e Segurança
Como um projeto voltado para a área de Defesa Cibernética, foram implementadas travas para garantir a integridade da aplicação:

* **Validação de Input (Sanitização):** O backend valida se os dados inseridos são apenas texto, prevenindo injeções de caracteres indesejados.
* **Prevenção de Race Conditions:** Implementação de trava via JavaScript no botão de sorteio, impedindo que múltiplos cliques rápidos causem erros de lógica ou sobrecarga no servidor.
* **Gestão de Segredos:** Configuração de `.gitignore` para impedir o vazamento de bancos de dados locais (`sqlite3`) e arquivos de configuração sensíveis.
* **Proteção CSRF:** Utilização dos tokens de segurança nativos do Django para prevenir ataques de *Cross-Site Request Forgery*.

## 🚀 Tecnologias Utilizadas
* **Python / Django:** Lógica de backend e segurança.
* **JavaScript:** Controle de fluxo de interface e prevenção de erros.
* **CSS3:** Design responsivo com animações de suspense para UX.
* **Git:** Versionamento seguro.

## ⚙️ Como executar o projeto
1. Clone o repositório: `git clone https://github.com/jbeggiora/sorteador_jonatas.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Inicie o servidor: `python manage.py runserver`
