from datetime import datetime
class Colors:
  def __init__(self) -> None:
    self.colors = {
      # Text colors (normal)
      'black'             : "\033[30m",
      'red'               : "\033[31m",
      'green'             : "\033[32m",
      'yellow'            : "\033[33m",
      'blue'              : "\033[34m",
      'magenta'           : "\033[35m",
      'cyan'              : "\033[36m",
      'white'             : "\033[37m",

      # Bright text colors
      'bright_black'      : "\033[90m",
      'bright_red'        : "\033[91m",
      'bright_green'      : "\033[92m",
      'bright_yellow'     : "\033[93m",
      'bright_blue'       : "\033[94m",
      'bright_magenta'    : "\033[95m",
      'bright_cyan'       : "\033[96m",
      'bright_white'      : "\033[97m",

      # Background colors (normal)
      'bg_black'          : "\033[40m",
      'bg_red'            : "\033[41m",
      'bg_green'          : "\033[42m",
      'bg_yellow'         : "\033[43m",
      'bg_blue'           : "\033[44m",
      'bg_magenta'        : "\033[45m",
      'bg_cyan'           : "\033[46m",
      'bg_white'          : "\033[47m",

      # Bright backgrounds
      'bg_bright_black'   : "\033[100m",
      'bg_bright_red'     : "\033[101m",
      'bg_bright_green'   : "\033[102m",
      'bg_bright_yellow'  : "\033[103m",
      'bg_bright_blue'    : "\033[104m",
      'bg_bright_magenta' : "\033[105m",
      'bg_bright_cyan'    : "\033[106m",
      'bg_bright_white'   : "\033[107m",

      # Styles
      'bold'              : "\033[1m",
      'italic'            : "\033[3m",
      'underline'         : "\033[4m",
      'double_underline'  : "\033[21m",
      'blink'             : "\033[5m",
      'reverse'           : "\033[7m",
      'hidden'            : "\033[8m",
      'strike'            : "\033[9m",

      # Reset
      'reset'             : "\033[0m",
      'normal'            : "\033[2m"
    }

    self.icons = {
      'void':              '',
      'info':             f'{chr(10069)}{chr(160)}',
      'error':            f'{chr(10060)}{chr(160)}',
      'debug':            f'{chr(9935)}{chr(160)} ',
      'success':          f'{chr(9989)}{chr(160)}',
      'warning':          f'{chr(10071)}{chr(160)}',
      'highlight':        f'{chr(10062)}{chr(160)}',
    }

  # Métodos utilitários
  def color(self, name: str) -> str:
    return self.colors.get(name, self.colors['reset'])
  
  def icon(self, name: str) -> str:
    return self.icons.get(name, '')

  def reset(self) -> str:
    return self.colors['reset']

 # Sucesso
  def success(self, msg: str = None, **kwargs) -> None:
    style: str = 'normal'
    icon: bool = 'void'
    time_clock: bool = False
    
    icon = kwargs.get('icon', icon)
    style = kwargs.get('style', style)

    _clock: datetime = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' if kwargs.get('time_clock') == True else ''

    print(f"{_clock}{self.icons[icon]}{self.colors['bright_green']}{self.colors[style]}{msg}{self.reset()}")
    return None
  
  # Erro
  def error(self, msg: str = None, **kwargs) -> None:
    style: str = 'normal'
    icon: bool = 'void'
    time_clock: bool = False
    
    icon = kwargs.get('icon', icon)
    style = kwargs.get('style', style)

    _clock: datetime = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' if kwargs.get('time_clock') == True else ''

    print(f"{_clock}{self.icons[icon]}{self.colors['bright_red']}{self.colors[style]}{msg}{self.reset()}")
    return None

  # Aviso
  def warning(self, msg: str = None, **kwargs) -> None:
    style: str = 'normal'
    icon: bool = 'void'
    time_clock: bool = False
    
    icon = kwargs.get('icon', icon)
    style = kwargs.get('style', style)

    _clock: datetime = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' if kwargs.get('time_clock') == True else ''

    print(f"{_clock}{self.icons[icon]}{self.colors['bright_yellow']}{self.colors[style]}{msg}{self.reset()}")
    return None

  # Informação
  def info(self, msg: str, **kwargs) -> None:
    style: str = 'normal'
    icon: bool = 'void'
    time_clock: bool = False
    
    icon = kwargs.get('icon', icon)
    style = kwargs.get('style', style)

    _clock: datetime = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' if kwargs.get('time_clock') == True else ''

    print(f"{_clock}{self.icons[icon]}{self.colors['blue']}{self.colors[style]}{msg}{self.reset()}")
    return None

  # Debug
  def debug(self, msg: str, **kwargs) -> None:
    style: str = 'normal'
    icon: bool = 'void'
    time_clock: bool = False
    
    icon = kwargs.get('icon', icon)
    style = kwargs.get('style', style)

    _clock: datetime = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' if kwargs.get('time_clock') == True else ''

    print(f"{_clock}{self.icons[icon]}{self.colors['bright_magenta']}{self.colors[style]}{msg}{self.reset()}")
    return None

  # Importante / Destaque
  def highlight(self, msg: str, **kwargs) -> None:
    style: str = 'normal'
    icon: bool = 'void'
    time_clock: bool = False
    
    icon = kwargs.get('icon', icon)
    style = kwargs.get('style', style)

    _clock: datetime = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] ' if kwargs.get('time_clock') == True else ''

    print(f"{_clock}{self.icons[icon]}{self.colors['bright_white']}{self.colors[style]}{msg}{self.reset()}")
    return None