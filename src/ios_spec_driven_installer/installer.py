"""
Installation logic for iOS Spec-Driven Toolkit
"""

import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict

class Installer:
    """Handles installation, uninstallation, and validation of the toolkit"""
    
    def __init__(self, target_dir: Path, backup: bool = True):
        """Initialize installer
        
        Args:
            target_dir: Target directory for installation
            backup: Whether to backup existing files
        """
        self.target_dir = Path(target_dir).resolve()
        self.backup_enabled = backup
        
        # Get templates directory (where package templates are stored)
        # When installed via pip/uvx, templates are in site-packages/ios_spec_driven_installer/templates/
        self.templates_dir = Path(__file__).parent / 'templates'
        
        # Paths
        self.source_claude = self.templates_dir / '.claude'
        self.source_mcp = self.templates_dir / '.mcp.json'
        
        self.target_claude = self.target_dir / '.claude'
        self.target_mcp = self.target_dir / '.mcp.json'
    
    def is_installed(self) -> bool:
        """Check if toolkit is already installed
        
        Returns:
            True if toolkit is installed, False otherwise
        """
        # Check if .claude directory exists with key files
        if not self.target_claude.exists():
            return False
        
        # Check for key skill file
        skill_file = self.target_claude / 'skills' / 'dev-spec-driven' / 'SKILL.md'
        return skill_file.exists()
    
    def backup(self) -> Path:
        """Backup existing installation
        
        Returns:
            Path to backup directory
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = self.target_dir / f'.claude.backup.{timestamp}'
        
        if self.target_claude.exists():
            shutil.copytree(self.target_claude, backup_dir)
        
        return backup_dir
    
    def install(self):
        """Install toolkit files
        
        Copies:
        - .claude/ directory (skills, agents, scripts, guides)
        - .mcp.json file
        """
        # Ensure target directory exists
        self.target_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy .claude/ directory
        if self.source_claude.exists():
            # Remove existing if present
            if self.target_claude.exists():
                shutil.rmtree(self.target_claude)
            
            shutil.copytree(self.source_claude, self.target_claude)
        else:
            raise FileNotFoundError(f"Source .claude directory not found: {self.source_claude}")
        
        # Copy .mcp.json
        if self.source_mcp.exists():
            shutil.copy2(self.source_mcp, self.target_mcp)
        else:
            raise FileNotFoundError(f"Source .mcp.json not found: {self.source_mcp}")
    
    def validate(self) -> bool:
        """Validate installation
        
        Checks if all required files are present.
        
        Returns:
            True if validation passes, False otherwise
        """
        required_files = [
            # Skills
            '.claude/skills/dev-spec-driven/SKILL.md',
            '.claude/skills/ios-architecture/SKILL.md',
            '.claude/skills/ios-components/SKILL.md',
            
            # Agents
            '.claude/agents/write-spec.md',
            '.claude/agents/write-design.md',
            '.claude/agents/write-tasks.md',
            '.claude/agents/execute-tasks.md',
            
            # Scripts
            '.claude/scripts/validate_traceability.py',
            
            # Guides
            '.claude/shared/COMPONENT_FORMAT.md',
            '.claude/shared/PBT_GUIDE.md',
            '.claude/shared/PARALLEL_EXECUTION_GUIDE.md',
            
            # Config
            '.mcp.json',
        ]
        
        for file_path in required_files:
            full_path = self.target_dir / file_path
            if not full_path.exists():
                print(f"Missing: {file_path}")
                return False
        
        return True
    
    def uninstall(self):
        """Remove toolkit files
        
        Removes:
        - .claude/ directory
        - .mcp.json file
        """
        # Remove .claude/ directory
        if self.target_claude.exists():
            shutil.rmtree(self.target_claude)
        
        # Remove .mcp.json
        if self.target_mcp.exists():
            self.target_mcp.unlink()
    
    def get_installed_components(self) -> Dict[str, bool]:
        """Get status of installed components
        
        Returns:
            Dictionary mapping component names to installation status
        """
        return {
            'Skills': (self.target_claude / 'skills').exists(),
            'Agents': (self.target_claude / 'agents').exists(),
            'Scripts': (self.target_claude / 'scripts').exists(),
            'Guides': (self.target_claude / 'shared').exists(),
            'MCP Config': self.target_mcp.exists(),
        }
