# 🧾 README.md
# 💬 Pyrisma

Uma biblioteca Python para exibir mensagens coloridas e estilizadas no terminal, com ícones e formatação moderna.  
Ideal para quem quer logs mais visuais, legíveis e com um toque de personalidade.

---

## 🚀 Instalação

```bash
pip install pyrisma
```

# 🧠 Uso básico
```python
from pyrisma import terminal

terminal.info("Sistema iniciado com sucesso!")
terminal.warning("Atenção: configuração ausente.")
terminal.error("Erro crítico detectado!")
terminal.success("Processo concluído com êxito.")
```

### Primeiro argumento: Mensagem: str
```python
terminal.info('mensagem')
```
### Segundo argumento: Estilo: str
```python
terminal.info('mensagem', 'bold')
```
### Terceiro argumento: Ícone: bool
```python
terminal.info('mensagem', 'bold', True)
```
### Quarto argumento: Intermitência: bool
```python
terminal.info('mensagem', 'bold', True, True)
```
### Quinto argumento: Timestamp: bool
```python
terminal.info('mensagem', 'bold', True, True, True)
```

### Saída esperada (com cores e ícones, dependendo do terminal):

```bash
ℹ️  Sistema iniciado com sucesso!

⚠️  Atenção: configuração ausente.

❌  Erro crítico detectado!

✅  Processo concluído com êxito.
```

# ⚙️ Funcionalidades

- ### Mensagens com cores e ícones contextuais.

- ### Suporte a diferentes níveis de log.

- ### Compatível com Linux e macOS.

- ### Sem dependências externas pesadas.

# 📄 Licença

### Distribuído sob a licença MIT.
### Veja o arquivo LICENSE para mais informações.

# 👤 Autor
## 💼 LinkedIn
- ### Marley
- ### Desenvolvedor de Software


### 📧 marleysbenicio@gmail.com