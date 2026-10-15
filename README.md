# RPG Music Controller

## Sobre o projeto

O RPG Music Controller é um programa em Python com interface gráfica feito para facilitar o controle de músicas durante sessões de RPG no Discord. A ideia é permitir que o usuário organize uma playlist e, futuramente, controle a reprodução sem precisar digitar manualmente os comandos do bot no chat.

## Estado atual

**Etapa atual:** beta da interface e do gerenciamento de playlists.

O programa já permite:
- Cadastrar músicas com nome e link.
- Listar as músicas cadastradas.
- Selecionar uma música e visualizar suas informações.
- Editar músicas existentes.
- Excluir músicas.
- Salvar e carregar a playlist em um arquivo JSON.

As operações de cadastro, edição e exclusão atualizam a playlist em memória e tentam salvar as alterações no arquivo. Se o salvamento falhar, a interface avisa que a alteração não foi persistida.

## Tecnologias utilizadas

- **Python** — linguagem principal.
- **PySide6** — interface gráfica.
- **JSON** — armazenamento local da playlist.

As dependências Python estão registradas em `requirements.txt`.

## Organização do projeto

```text
rpg-music-controller/
├── main.py
├── models/
│   └── musica.py
├── services/
│   ├── playlist_service.py
│   ├── playlist_controller.py
│   └── armazenamento_json.py
├── ui/
│   └── main_window.py
├── database/
│   └── musicas.json
├── requirements.txt
├── README.md
└── .gitignore
```

Os nomes dos arquivos acima representam a organização pretendida; confira se os nomes reais no projeto estão iguais.

- `main.py`: inicia a aplicação e conecta os componentes.
- `models/`: contém a classe que representa uma música.
- `services/playlist_service.py`: gerencia a playlist em memória.
- `services/playlist_controller.py`: coordena as operações da playlist e o salvamento.
- `services/armazenamento_json.py`: carrega e salva a playlist em JSON.
- `ui/main_window.py`: define a interface gráfica.
- `database/musicas.json`: armazena as músicas localmente.

## Em andamento / próximos passos

A próxima etapa é integrar a playlist ao bot de música utilizado no Discord, começando pela ação mais simples: reproduzir uma música selecionada pela interface.

Depois disso, o plano é:
1. Implementar controles de reprodução pela interface.
2. Adicionar atalhos globais de teclado, como `Alt + 1`, que funcionem mesmo quando outra janela estiver em foco.
3. Testar a integração com o Discord e tratar possíveis falhas.
4. Revisar a experiência de uso e atualizar esta documentação conforme as funcionalidades forem concluídas.

## O que ainda falta

- Integrar a interface com o fluxo de comandos do bot de música.
- Reproduzir a música selecionada sem digitar manualmente o comando no Discord.
- Criar os controles de reprodução planejados.
- Implementar e testar os atalhos globais.
- Fazer testes adicionais de erros e persistência.
- Atualizar a documentação com instruções de instalação e uso quando o fluxo principal estiver pronto.

## Como executar

1. Instale uma versão compatível do Python.
2. Crie e ative um ambiente virtual.
3. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Execute o programa a partir da pasta raiz:

   ```bash
   python main.py
   ```

## Observações

Este projeto está em desenvolvimento. A interface de gerenciamento de playlists está implementada, mas a integração com o bot do Discord e os atalhos de controle ainda não estão concluídos.

O arquivo `database/musicas.json` é usado para guardar a playlist local. Evite incluir nele dados privados antes de publicar o repositório.
