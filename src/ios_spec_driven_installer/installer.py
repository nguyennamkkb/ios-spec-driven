"""
Installation logic for iOS Spec-Driven Toolkit
"""

import shutil
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Literal

IDEType = Literal["claude", "opencode"]

class Installer:
    """Handles installation, uninstallation, and validation of the toolkit"""
    
    def __init__(self, target_dir: Path, ide: IDEType = "claude", backup: bool = True):
        """Initialize installer
        
        Args:
            target_dir: Target directory for installation
            ide: Target IDE ("claude" or "opencode")
            backup: Whether to backup existing files
        """
        self.target_dir = Path(target_dir).resolve()
        self.ide = ide
        self.backup_enabled = backup
        
        # Get templates directory
        self.templates_dir = Path(__file__).parent / 'templates'
        
        # Source paths
        self.content_dir = self.templates_dir / 'content'
        self.format_dir = self.templates_dir / 'formats' / ide
        
        # Target paths based on IDE
        if ide == "claude":
            self.target_config_dir = self.target_dir / '.claude'
            self.target_mcp = self.target_dir / '.mcp.json'
        else:  # opencode
            self.target_config_dir = self.target_dir / '.opencode'
            self.target_config_file = self.target_dir / 'opencode.json'
    
    def is_installed(self) -> bool:
        """Check if toolkit is already installed
        
        Returns:
            True if toolkit is installed, False otherwise
        """
        if not self.target_config_dir.exists():
            return False
        
        # Check for key skill file
        skill_file = self.target_config_dir / 'skills' / 'dev-spec-driven' / 'SKILL.md'
        return skill_file.exists()
    
    def backup(self) -> Path:
        """Backup existing installation
        
        Returns:
            Path to backup directory
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = self.target_dir / f'.{self.ide}.backup.{timestamp}'
        
        if self.target_config_dir.exists():
            shutil.copytree(self.target_config_dir, backup_dir)
        
        return backup_dir
    
    def install(self):
        """Install toolkit files
        
        Copies content and applies IDE-specific format
        """
        # Ensure target directory exists
        self.target_dir.mkdir(parents=True, exist_ok=True)
        
        # Remove existing if present
        if self.target_config_dir.exists():
            shutil.rmtree(self.target_config_dir)
        
        # Create config directory
        self.target_config_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy content (skills, agents, shared, scripts, hooks)
        self._copy_content()
        
        # Apply IDE-specific format
        self._apply_format()
    
    def _copy_content(self):
        """Copy shared content to target directory"""
        # Copy skills (no transformation needed)
        if (self.content_dir / 'skills').exists():
            shutil.copytree(
                self.content_dir / 'skills',
                self.target_config_dir / 'skills'
            )
        
        # Copy agents (with transformation for OpenCode)
        if (self.content_dir / 'agents').exists():
            agents_target = self.target_config_dir / 'agents'
            agents_target.mkdir(parents=True, exist_ok=True)
            
            for agent_file in (self.content_dir / 'agents').glob('*.md'):
                if self.ide == "opencode":
                    # Transform frontmatter for OpenCode
                    self._copy_and_transform_agent(agent_file, agents_target / agent_file.name)
                else:
                    # Copy as-is for Claude Code
                    shutil.copy2(agent_file, agents_target / agent_file.name)
        
        # Copy shared guides
        if (self.content_dir / 'shared').exists():
            shutil.copytree(
                self.content_dir / 'shared',
                self.target_config_dir / 'shared'
            )
        
        # Copy scripts
        if (self.content_dir / 'scripts').exists():
            shutil.copytree(
                self.content_dir / 'scripts',
                self.target_config_dir / 'scripts'
            )
        
        # Copy hooks
        if (self.content_dir / 'hooks').exists():
            shutil.copytree(
                self.content_dir / 'hooks',
                self.target_config_dir / 'hooks'
            )
    
    def _copy_and_transform_agent(self, source_file: Path, target_file: Path):
        """Transform agent frontmatter from Claude Code format to OpenCode format
        
        Transforms:
        - tools: Read, Write, Grep -> tools:\n  write: true\n  grepSearch: true
        - skills: skill1, skill2 -> skills: skill1, skill2 (unchanged)
        """
        content = source_file.read_text(encoding='utf-8')
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not frontmatter_match:
            # No frontmatter, copy as-is
            target_file.write_text(content, encoding='utf-8')
            return
        
        frontmatter = frontmatter_match.group(1)
        body = frontmatter_match.group(2)
        
        # Transform tools field
        tools_match = re.search(r'^tools:\s*(.+)$', frontmatter, re.MULTILINE)
        if tools_match:
            tools_str = tools_match.group(1).strip()
            
            # Map Claude Code tool names to OpenCode tool names
            tool_mapping = {
                'Read': None,  # Not needed in OpenCode (automatic)
                'Write': 'write',
                'Edit': 'edit',
                'Grep': 'grepSearch',
                'Glob': 'fileSearch',
                'Bash': 'bash',
                'WebSearch': 'webSearch',
                'WebFetch': 'webFetch',
            }
            
            # Parse tools
            tools = [t.strip() for t in tools_str.split(',')]
            opencode_tools = []
            
            for tool in tools:
                if tool in tool_mapping:
                    mapped = tool_mapping[tool]
                    if mapped:  # Skip None (Read)
                        opencode_tools.append(mapped)
            
            # Build OpenCode tools format
            if opencode_tools:
                tools_yaml = 'tools:\n' + '\n'.join(f'  {tool}: true' for tool in opencode_tools)
            else:
                tools_yaml = 'tools: {}'
            
            # Replace in frontmatter
            frontmatter = re.sub(
                r'^tools:\s*.+$',
                tools_yaml,
                frontmatter,
                flags=re.MULTILINE
            )
        
        # Reconstruct file
        new_content = f'---\n{frontmatter}\n---\n{body}'
        target_file.write_text(new_content, encoding='utf-8')
    
    def _apply_format(self):
        """Apply IDE-specific format and config files"""
        if self.ide == "claude":
            # Copy Claude-specific settings
            if (self.format_dir / 'settings.json').exists():
                shutil.copy2(
                    self.format_dir / 'settings.json',
                    self.target_config_dir / 'settings.json'
                )
            
            if (self.format_dir / 'settings.local.json').exists():
                shutil.copy2(
                    self.format_dir / 'settings.local.json',
                    self.target_config_dir / 'settings.local.json'
                )
            
            # Copy MCP config
            mcp_source = self.templates_dir / '.mcp.json'
            if mcp_source.exists():
                shutil.copy2(mcp_source, self.target_mcp)
        
        else:  # opencode
            # Copy OpenCode config
            if (self.format_dir / 'opencode.json').exists():
                shutil.copy2(
                    self.format_dir / 'opencode.json',
                    self.target_config_file
                )
    
    def validate(self) -> bool:
        """Validate installation
        
        Checks if all required files are present.
        
        Returns:
            True if validation passes, False otherwise
        """
        config_prefix = '.claude' if self.ide == "claude" else '.opencode'
        
        required_files = [
            # Skills
            f'{config_prefix}/skills/dev-spec-driven/SKILL.md',
            f'{config_prefix}/skills/ios-architecture/SKILL.md',
            f'{config_prefix}/skills/ios-components/SKILL.md',
            
            # Agents
            f'{config_prefix}/agents/write-spec.md',
            f'{config_prefix}/agents/write-design.md',
            f'{config_prefix}/agents/write-tasks.md',
            f'{config_prefix}/agents/execute-tasks.md',
            
            # Scripts
            f'{config_prefix}/scripts/validate_traceability.py',
            
            # Guides
            f'{config_prefix}/shared/COMPONENT_FORMAT.md',
            f'{config_prefix}/shared/PBT_GUIDE.md',
            f'{config_prefix}/shared/PARALLEL_EXECUTION_GUIDE.md',
        ]
        
        # Add IDE-specific config files
        if self.ide == "claude":
            required_files.append('.mcp.json')
        else:
            required_files.append('opencode.json')
        
        for file_path in required_files:
            full_path = self.target_dir / file_path
            if not full_path.exists():
                print(f"Missing: {file_path}")
                return False
        
        return True
    
    def uninstall(self):
        """Remove toolkit files
        
        Removes:
        - Config directory (.claude/ or .opencode/)
        - Config files (.mcp.json or opencode.json)
        """
        # Remove config directory
        if self.target_config_dir.exists():
            shutil.rmtree(self.target_config_dir)
        
        # Remove config files
        if self.ide == "claude" and self.target_mcp.exists():
            self.target_mcp.unlink()
        elif self.ide == "opencode" and self.target_config_file.exists():
            self.target_config_file.unlink()
    
    def get_installed_components(self) -> Dict[str, bool]:
        """Get status of installed components
        
        Returns:
            Dictionary mapping component names to installation status
        """
        return {
            'Skills': (self.target_config_dir / 'skills').exists(),
            'Agents': (self.target_config_dir / 'agents').exists(),
            'Scripts': (self.target_config_dir / 'scripts').exists(),
            'Guides': (self.target_config_dir / 'shared').exists(),
            'Config': (
                self.target_mcp.exists() if self.ide == "claude" 
                else self.target_config_file.exists()
            ),
        }
