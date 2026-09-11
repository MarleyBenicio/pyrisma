# 💬 Pyrisma

Uma biblioteca Python para exibir mensagens coloridas e estilizadas no terminal, com ícones, estilos de texto e timestamp opcional.

Ideal para quem quer logs mais visuais, legíveis e com um toque de personalidade.

---

## 🚀 Instalação

```bash
pip install pyrisma
```

Requer Python >= 3.9. Sem dependências externas.

---

## 🧠 Uso básico

```python
from pyrisma import terminal

terminal.info("Sistema iniciado com sucesso!")
terminal.warning("Atenção: configuração ausente.")
terminal.error("Erro crítico detectado!")
terminal.success("Processo concluído com êxito.")
terminal.debug("Valor da variável x: 42")
terminal.highlight("Isso merece destaque!")
```

O objeto `terminal` já vem pronto para uso (é uma instância de `Colors`), mas você também pode instanciar a classe diretamente:

```python
from pyrisma import Colors

terminal = Colors()
```

---

## ⚙️ Métodos disponíveis

Todos os métodos de log têm a mesma assinatura:

```python
terminal.<metodo>(msg: str, **kwargs)
```

| Método        | Cor aplicada      |
|---------------|-------------------|
| `success`     | verde brilhante   |
| `error`       | vermelho brilhante|
| `warning`     | amarelo brilhante |
| `info`        | azul              |
| `debug`       | magenta brilhante |
| `highlight`   | branco brilhante  |

### Parâmetros opcionais (`**kwargs`)

| Parâmetro     | Tipo   | Padrão   | Descrição                                                                 |
|---------------|--------|----------|----------------------------------------------------------------------------|
| `style`       | `str`  | `'normal'` | Nome do estilo de texto a aplicar (ver tabela de estilos abaixo).       |
| `icon`        | `str`  | `'void'`   | Nome do ícone a exibir antes da mensagem (ver tabela de ícones abaixo). |
| `time_clock`  | `bool` | `False`    | Se `True`, adiciona um timestamp `[YYYY-MM-DD HH:MM:SS]` antes da mensagem. |

Exemplo usando todos os parâmetros:

```python
terminal.success(
    "Backup concluído",
    style="bold",
    icon="success",
    time_clock=True,
)
# [2026-09-11 10:30:00] ✅ Backup concluído
```

---

## 🎨 Estilos disponíveis (`style`)

```
normal, bold, italic, underline, double_underline,
blink, reverse, hidden, strike, reset
```

## 🔣 Ícones disponíveis (`icon`)

```
void, info, error, debug, success, warning, highlight
```

---

## 🧰 Métodos utilitários

Além dos métodos de log, a classe `Colors` expõe utilitários para montar suas próprias mensagens formatadas:

```python
from pyrisma import Colors

c = Colors()

c.color("red")      # retorna o código ANSI da cor "red"
c.icon("warning")    # retorna o ícone associado a "warning"
c.reset()            # retorna o código ANSI de reset ("\033[0m")
```

Cores de texto disponíveis em `color()`:

```
black, red, green, yellow, blue, magenta, cyan, white,
bright_black, bright_red, bright_green, bright_yellow,
bright_blue, bright_magenta, bright_cyan, bright_white,
bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_magenta,
bg_cyan, bg_white, bg_bright_black, bg_bright_red,
bg_bright_green, bg_bright_yellow, bg_bright_blue,
bg_bright_magenta, bg_bright_cyan, bg_bright_white
```

---

## ⚙️ Funcionalidades

- Mensagens com cores e ícones contextuais.
- Suporte a diferentes níveis de log (`success`, `error`, `warning`, `info`, `debug`, `highlight`).
- Estilos de texto (negrito, itálico, sublinhado, etc).
- Timestamp opcional em cada mensagem.
- Acesso direto a cores e ícones para composições personalizadas.
- Sem dependências externas.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

## 👤 Autor

**Marley Benicio**
Desenvolvedor de Software

📧 marleysbenicio@gmail.com
🔗 [GitHub](https://github.com/MarleyBenicio/pyrisma)
