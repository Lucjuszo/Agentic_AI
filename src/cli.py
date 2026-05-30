from rich.console import Console
from rich.panel   import Panel
from agents import MultiAgentSystem, DOMAIN_LABELS

console = Console()

BANNER = """
[bold cyan]╔══════════════════════════════════════════╗
║  Agentic AI                              ║
║  F1 │ Cosmos │ Tricity │ Film            ║
╚══════════════════════════════════════════╝[/bold cyan]
"""

def main():
    console.print(BANNER)
    console.print("[dim]Loading agents and embedding model…[/dim]")
    system = MultiAgentSystem()
    console.print("[green]Ready![/green]  Type [bold]quit[/bold] to exit.\n")

    while True:
        try:
            query = console.input("[bold yellow]❯ You: [/bold yellow]").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if not query:
            continue
        if query.lower() in ("quit"):
            console.print("[dim]Goodbye![/dim]"); break

        with console.status("[bold cyan]Routing & retrieving…[/bold cyan]"):
            domain, answer = system.run(query)

        label = DOMAIN_LABELS.get(domain, domain)
        console.print(Panel(
            answer,
            title=f"[bold green]{label}[/bold green]",
            border_style="green",
            padding=(1, 2),
        ))
        console.print()


if __name__ == "__main__":
    main()