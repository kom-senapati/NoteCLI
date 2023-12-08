import typer
from rich.console import Console
from rich.table import Table
from model import Note
from db import get_all_notes, insert_note, delete_note, update_note

console = Console()
app = typer.Typer()


@app.command(short_help="adds a note")
def add(title: str, content: str):
    typer.echo(f"adding {title}, {content}")
    note = Note(title, content)
    insert_note(note)
    show()


@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_note(position - 1)
    show()


@app.command()
def update(position: int, title: str = None, content: str = None):
    typer.echo(f"updating {position}")
    update_note(position - 1, title, content)
    show()


@app.command()
def show():
    console.print("[green]NOTES[/green]", "📝")
    notes = get_all_notes()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=6)
    table.add_column("Note", min_width=12)
    table.add_column("Content", min_width=20, justify="right")

    for i, note in enumerate(notes, start=1):
        table.add_row(str(i), note.title, note.content)
    console.print(table)


if __name__ == "__main__":
    app()
