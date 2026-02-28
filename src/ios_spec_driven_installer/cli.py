#!/usr/bin/env python3
"""
iOS Spec-Driven Toolkit CLI
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pathlib import Path
from .installer import Installer
import importlib.metadata

console = Console()

# Get version from package metadata
try:
    __version__ = importlib.metadata.version("ios-spec-driven-installer")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

@click.group()
@click.version_option(version=__version__)
def main():
    """iOS Spec-Driven Development Toolkit Installer
    
    Install the complete toolkit for spec-driven iOS development.
    
    Examples:
        ios-spec-driven install
        ios-spec-driven install /path/to/project
        ios-spec-driven status
        ios-spec-driven uninstall
    """
    pass

@main.command()
@click.argument('target_dir', type=click.Path(), default='.')
@click.option('--ide', type=click.Choice(['claude', 'opencode']), help='Target IDE (claude or opencode)')
@click.option('--no-backup', is_flag=True, help='Skip backup of existing files')
@click.option('--force', is_flag=True, help='Force overwrite without confirmation')
def install(target_dir, ide, no_backup, force):
    """Install the toolkit to TARGET_DIR (default: current directory)
    
    This will install:
    - Skills (7 specialized skills)
    - Agents (7 workflow agents)
    - Scripts (validation tools)
    - Guides (component format, PBT, parallel execution)
    - Config (IDE-specific configuration)
    
    Examples:
        ios-spec-driven install
        ios-spec-driven install --ide claude
        ios-spec-driven install --ide opencode
        ios-spec-driven install ~/MyiOSApp
        ios-spec-driven install --no-backup
    """
    
    console.print(Panel.fit(
        "[bold blue]🚀 iOS Spec-Driven Toolkit Installer[/bold blue]\n"
        f"[dim]Version {__version__}[/dim]",
        border_style="blue"
    ))
    
    # Interactive IDE selection if not provided
    if not ide:
        console.print("\n[bold cyan]? Select target IDE:[/bold cyan]")
        console.print("  [1] Claude Code")
        console.print("  [2] OpenCode")
        
        choice = click.prompt("\nEnter your choice", type=click.IntRange(1, 2), default=1)
        ide = "claude" if choice == 1 else "opencode"
        console.print(f"\n[green]✓[/green] Selected: {ide.title()}\n")
    
    target_path = Path(target_dir).resolve()
    installer = Installer(target_path, ide=ide, backup=not no_backup)
    
    try:
        # Check if already installed
        if installer.is_installed() and not force:
            console.print(f"\n[yellow]⚠️  Toolkit already installed in:[/yellow] {target_path}")
            if not click.confirm('Overwrite existing installation?', default=False):
                console.print("[yellow]Installation cancelled[/yellow]")
                return
        
        # Install
        console.print(f"\n[cyan]Installing to:[/cyan] {target_path}\n")
        
        with console.status("[bold green]Installing...") as status:
            # Backup
            if not no_backup and installer.is_installed():
                status.update("[bold yellow]📦 Backing up existing files...")
                backup_path = installer.backup()
                console.print(f"[green]✓[/green] Backup created: [dim]{backup_path.name}[/dim]")
            
            # Copy files
            status.update("[bold green]📂 Copying files...")
            installer.install()
            console.print("[green]✓[/green] Files copied")
            
            # Validate
            status.update("[bold green]🔍 Validating installation...")
            if installer.validate():
                console.print("[green]✓[/green] Validation passed")
            else:
                console.print("[red]✗[/red] Validation failed")
                console.print("\n[red]Installation incomplete. Please check the error messages above.[/red]")
                return
        
        # Success message
        console.print("\n[bold green]✅ Installation complete![/bold green]\n")
        
        # Show what was installed
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Component", style="cyan")
        table.add_column("Status", justify="center")
        
        components = installer.get_installed_components()
        for name, installed in components.items():
            status_icon = "[green]✓[/green]" if installed else "[red]✗[/red]"
            table.add_row(name, status_icon)
        
        console.print(table)
        
        # Next steps
        console.print("\n[cyan]Next steps:[/cyan]")
        console.print("1. Open your project")
        console.print("2. See README.md for more examples")
        console.print(f"3. Documentation: [link]https://github.com/nguyennamkkb/ios-spec-driven[/link]\n")
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Installation failed:[/bold red] {e}")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        raise click.Abort()

@main.command()
@click.argument('target_dir', type=click.Path(), default='.')
@click.option('--ide', type=click.Choice(['claude', 'opencode']), default='claude', help='Target IDE')
@click.option('--force', is_flag=True, help='Force uninstall without confirmation')
def uninstall(target_dir, ide, force):
    """Uninstall the toolkit from TARGET_DIR
    
    This will remove:
    - .claude/ directory (skills, agents, scripts, guides)
    - .mcp.json file
    
    Examples:
        ios-spec-driven uninstall
        ios-spec-driven uninstall ~/MyiOSApp
        ios-spec-driven uninstall --force
    """
    
    console.print("[bold red]🗑️  iOS Spec-Driven Toolkit Uninstaller[/bold red]\n")
    
    target_path = Path(target_dir).resolve()
    installer = Installer(target_path, ide=ide)
    
    if not installer.is_installed():
        console.print(f"[yellow]Toolkit is not installed in:[/yellow] {target_path}")
        return
    
    if not force:
        console.print(f"[yellow]This will remove the toolkit from:[/yellow] {target_path}\n")
        if not click.confirm('Are you sure?', default=False):
            console.print("[yellow]Uninstall cancelled[/yellow]")
            return
    
    try:
        with console.status("[bold red]Removing files..."):
            installer.uninstall()
        
        console.print("\n[green]✅ Uninstall complete![/green]")
        console.print(f"[dim]Removed from: {target_path}[/dim]\n")
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Uninstall failed:[/bold red] {e}")
        raise click.Abort()

@main.command()
@click.argument('target_dir', type=click.Path(), default='.')
@click.option('--ide', type=click.Choice(['claude', 'opencode']), default='claude', help='Target IDE')
def status(target_dir, ide):
    """Check installation status in TARGET_DIR
    
    Shows which components are installed and their status.
    
    Examples:
        ios-spec-driven status
        ios-spec-driven status ~/MyiOSApp
    """
    
    target_path = Path(target_dir).resolve()
    installer = Installer(target_path, ide=ide)
    
    console.print(f"\n[cyan]Checking installation in:[/cyan] {target_path}")
    console.print(f"[dim]IDE: {ide.title()}[/dim]\n")
    
    if installer.is_installed():
        console.print("[green]✓[/green] Toolkit is installed\n")
        
        # Show components
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Component", style="cyan")
        table.add_column("Status", justify="center")
        table.add_column("Details", style="dim")
        
        components = installer.get_installed_components()
        details = {
            'Skills': '7 specialized skills',
            'Agents': '7 workflow agents',
            'Scripts': 'Validation tools',
            'Guides': 'Component format, PBT, parallel execution',
            'MCP Config': 'Xcode + Figma integration',
        }
        
        for name, installed in components.items():
            status_icon = "[green]✓[/green]" if installed else "[red]✗[/red]"
            detail = details.get(name, '')
            table.add_row(name, status_icon, detail)
        
        console.print(table)
        
        # Version info
        config_dir = '.claude' if ide == 'claude' else '.opencode'
        console.print(f"\n[dim]Version: {__version__}[/dim]")
        console.print(f"[dim]IDE: {ide.title()}[/dim]")
        console.print(f"[dim]Location: {target_path / config_dir}[/dim]\n")
        
    else:
        console.print("[yellow]✗[/yellow] Toolkit is not installed\n")
        console.print("[cyan]To install, run:[/cyan]")
        console.print(f"  ios-spec-driven install {target_path}\n")

@main.command()
def info():
    """Show toolkit information and documentation links
    
    Displays version, components, and useful links.
    """
    
    console.print(Panel.fit(
        "[bold blue]iOS Spec-Driven Development Toolkit[/bold blue]\n"
        f"[dim]Version {__version__}[/dim]",
        border_style="blue"
    ))
    
    console.print("\n[bold cyan]Components:[/bold cyan]")
    console.print("• 7 Skills (dev-spec-driven, ios-architecture, ios-components, ...)")
    console.print("• 7 Agents (write-spec, write-design, write-tasks, execute-tasks, ...)")
    console.print("• Validation scripts (traceability checker)")
    console.print("• Guides (component format, PBT, parallel execution)")
    console.print("• MCP config (Xcode + Figma integration)")
    
    console.print("\n[bold cyan]Features:[/bold cyan]")
    console.print("• Complete traceability chain (US → AC → Design → Property → Task → Code)")
    console.print("• Feature-based organization")
    console.print("• Checkpoint gates with user confirmation")
    console.print("• Error recovery patterns")
    console.print("• Property-based testing with SwiftCheck")
    console.print("• Parallel task execution (experimental)")
    
    console.print("\n[bold cyan]Links:[/bold cyan]")
    console.print("• Repository: [link]https://github.com/nguyennamkkb/ios-spec-driven[/link]")
    console.print("• Documentation: [link]https://github.com/nguyennamkkb/ios-spec-driven#readme[/link]")
    console.print("• Issues: [link]https://github.com/nguyennamkkb/ios-spec-driven/issues[/link]")
    
    console.print("\n[bold cyan]Quick Start:[/bold cyan]")
    console.print("1. Install: [bold]ios-spec-driven install[/bold]")
    console.print("2. Open project in Claude Code")
    console.print("3. Try: [bold]'Create spec for login feature'[/bold]\n")

if __name__ == '__main__':
    main()
