# 🎙️ Voice ChatGPT com Whisper 
Projeto em Python que permite conversar por voz com o ChatGPT, utilizando Whisper para transcrição de áudio (Speech to Text) e integração com a API da OpenAI.

A ideia é gravar um áudio, transcrevê-lo automaticamente e enviar o texto para o ChatGPT, recebendo a resposta de forma simples e direta.

🚀 Funcionalidades 🎧 Entrada de áudio (.wav) 📝 Transcrição automática com Whisper 🤖 Envio do texto para o ChatGPT 💬 Retorno da resposta em texto 🔐 Uso de variáveis de ambiente para segurança da API 🛠️ Tecnologias utilizadas Python 3.10+ OpenAI API Whisper Virtual Environment (venv) 📁 Estrutura do projeto voice-chatgpt-whisper/ │ ├── src/ # Código-fonte do projeto │├── main.py # Script principal │ ├── venv/ # Ambiente virtual (ignorado no Git) ├── .env.example # Exemplo de variáveis de ambiente ├── .gitignore # Arquivos ignorados pelo Git ├── requirements.txt # Dependências do projeto └── README.md # Documentação

⚙️ Configuração do ambiente 1️⃣ Criar e ativar o ambiente virtual python -m venv venv

Ativar no Windows:

venv\Scripts\activate

2️⃣ Instalar dependências pip install -r requirements.txt

3️⃣ Configurar variáveis de ambiente

Crie um arquivo .env baseado no .env.example:

OPENAI_API_KEY=sua_chave_aqui

⚠️ Nunca suba sua chave real para o GitHub.

▶️ Como executar

Dentro do ambiente virtual:

python src/main.py

Certifique-se de que o arquivo de áudio esteja no formato .wav e corretamente referenciado no código.

🧠 Objetivo do projeto

Este projeto tem como objetivo estudo e prática de:

Integração com APIs de IA

Processamento de áudio

Automação com Python

Boas práticas de versionamento com Git e GitHub

📌 Observações

O projeto pode ser expandido para:

Text-to-Speech (resposta em áudio)

Interface gráfica

Interface web

Conversação contínua

📄 Licença

Este projeto é de uso educacional e livre para estudos.
