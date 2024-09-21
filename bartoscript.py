import socket
from rich.console import Console
from rich.progress import Progress
import time
import pyfiglet

console = Console()

# Diccionario de servicios comunes
SERVICIOS_COMUNES = {
    80: 'HTTP',
    443: 'HTTPS',
    21: 'FTP',
    22: 'SSH',
    25: 'SMTP',
    110: 'POP3',
    143: 'IMAP',
    53: 'DNS',
    # Puedes añadir más puertos y servicios aquí
}

def mostrar_titulo():
    # Imprimir título animado
    console.print("[bold magenta]BartoScript[/bold magenta]", style="bold underline", justify="center")
    console.print("[green]Escaneo de puertos...[/green]\n", justify="center")
    time.sleep(1)

def identificar_servicio(puerto):
    """Intentar identificar el servicio en base al puerto."""
    return SERVICIOS_COMUNES.get(puerto, 'Desconocido')

def escanear_puertos(host, puertos):
    console.print(f"Escaneando host: [bold yellow]{host}[/bold yellow]\n")

    with Progress() as progress:
        tarea = progress.add_task("[cyan]Escaneando...", total=len(puertos))

        for puerto in puertos:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado = sock.connect_ex((host, puerto))
            
            if resultado == 0:
                servicio = identificar_servicio(puerto)
                console.print(f"Puerto [bold green]{puerto}[/bold green] está abierto - Servicio: [bold cyan]{servicio}[/bold cyan]", style="bold")
            else:
                console.print(f"Puerto [bold red]{puerto}[/bold red] está cerrado", style="dim")
            sock.close()

            progress.update(tarea, advance=1)
            time.sleep(0.1)  # Simular una pausa para la animación

def main():
    mostrar_titulo()
    host = console.input("\n[bold cyan]Introduce la IP o dominio a escanear: [/bold cyan]")
    puertos = range(1, 1025)
    escanear_puertos(host, puertos)

if __name__ == "__main__":
    main()
