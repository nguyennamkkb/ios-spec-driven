# iOS Spec-Driven Plugin Installer

**Branch**: plugin  
**Purpose**: Create installation tool for Claude Code  
**Date**: February 4, 2026

---

## 🎯 Goal

Create a plugin/installer that allows users to easily install the iOS Spec-Driven toolkit into their Claude Code projects.

---

## 📦 What to Install

### Core Components

1. **Skills** (`.claude/skills/`)
   - dev-spec-driven
   - ios-architecture
   - ios-components
   - ios-ui-ux
   - ios-debug
   - mcp-xcode
   - mcp-figma

2. **Agents** (`.claude/agents/`)
   - write-spec
   - write-design
   - write-tasks
   - execute-tasks
   - refine-spec
   - quick-implement
   - research-prd

3. **Scripts** (`.claude/scripts/`)
   - validate_traceability.py

4. **Guides** (`Shared/`)
   - COMPONENT_FORMAT.md
   - PBT_GUIDE.md
   - PARALLEL_EXECUTION_GUIDE.md

5. **Config** (`.mcp.json`)
   - Xcode MCP
   - Figma MCP (optional)

---

## 🛠️ Installation Methods

### Method 1: CLI Installer (Recommended)

**Command**:
```bash
npx ios-spec-driven-installer install
```

**Features**:
- ✅ Interactive prompts
- ✅ Choose what to install
- ✅ Backup existing files
- ✅ Validate installation
- ✅ Post-install instructions

**Flow**:
```
1. Welcome message
2. Detect current directory
3. Check if .claude/ exists
4. Ask what to install:
   - [ ] All (recommended)
   - [ ] Skills only
   - [ ] Agents only
   - [ ] Guides only
   - [ ] Custom selection
5. Backup existing files (if any)
6. Copy files
7. Validate installation
8. Show success message + next steps
```

---

### Method 2: VS Code Extension

**Name**: iOS Spec-Driven for Claude Code

**Features**:
- ✅ Install from VS Code marketplace
- ✅ One-click installation
- ✅ Auto-detect Claude Code projects
- ✅ Update checker
- ✅ Uninstall option

**Commands**:
- `iOS Spec-Driven: Install Toolkit`
- `iOS Spec-Driven: Update Toolkit`
- `iOS Spec-Driven: Uninstall Toolkit`
- `iOS Spec-Driven: Check for Updates`

---

### Method 3: Manual Installation (Fallback)

**Instructions in README**:
```bash
# Clone repository
git clone https://github.com/your-org/ios-spec-driven-toolkit.git

# Copy to your project
cp -r ios-spec-driven-toolkit/.claude /path/to/your-project/
cp -r ios-spec-driven-toolkit/Shared /path/to/your-project/
cp ios-spec-driven-toolkit/.mcp.json /path/to/your-project/
```

---

## 📋 Implementation Plan

### Phase 1: CLI Installer (Priority)

**Tech Stack**:
- Node.js (for npx compatibility)
- Commander.js (CLI framework)
- Inquirer.js (interactive prompts)
- Chalk (colored output)
- Ora (spinners)

**Files to Create**:
```
installer/
├── package.json
├── bin/
│   └── cli.js
├── src/
│   ├── index.js
│   ├── installer.js
│   ├── validator.js
│   ├── backup.js
│   └── utils.js
├── templates/
│   ├── .claude/
│   ├── Shared/
│   └── .mcp.json
└── README.md
```

**Features**:
1. **Interactive Installation**
   ```bash
   npx ios-spec-driven-installer install
   
   ? Where to install? (.) 
   ? What to install? (Use arrow keys)
   ❯ All components (recommended)
     Skills only
     Agents only
     Custom selection
   
   ? Backup existing files? (Y/n)
   
   ✓ Backing up existing files...
   ✓ Installing skills...
   ✓ Installing agents...
   ✓ Installing guides...
   ✓ Installing MCP config...
   ✓ Validating installation...
   
   ✅ Installation complete!
   
   Next steps:
   1. Open your project in Claude Code
   2. Try: "Create spec for login feature"
   3. See README.md for more examples
   ```

2. **Update Command**
   ```bash
   npx ios-spec-driven-installer update
   
   Checking for updates...
   Current version: 2.1.0
   Latest version: 2.2.0
   
   ? Update to 2.2.0? (Y/n)
   
   ✓ Backing up current version...
   ✓ Downloading update...
   ✓ Installing update...
   
   ✅ Updated to 2.2.0!
   ```

3. **Uninstall Command**
   ```bash
   npx ios-spec-driven-installer uninstall
   
   ? Are you sure? This will remove all toolkit files. (y/N)
   
   ✓ Removing skills...
   ✓ Removing agents...
   ✓ Removing guides...
   
   ✅ Uninstalled successfully!
   ```

---

### Phase 2: VS Code Extension (Future)

**Extension Structure**:
```
vscode-extension/
├── package.json
├── extension.js
├── src/
│   ├── installer.js
│   ├── updater.js
│   └── commands.js
└── README.md
```

**Features**:
- Command palette integration
- Status bar indicator
- Notification for updates
- Settings UI

---

## 🔧 Technical Details

### CLI Installer Implementation

**package.json**:
```json
{
  "name": "ios-spec-driven-installer",
  "version": "2.1.0",
  "description": "CLI installer for iOS Spec-Driven Development toolkit",
  "bin": {
    "ios-spec-driven-installer": "./bin/cli.js"
  },
  "dependencies": {
    "commander": "^11.0.0",
    "inquirer": "^9.0.0",
    "chalk": "^5.0.0",
    "ora": "^7.0.0",
    "fs-extra": "^11.0.0"
  }
}
```

**bin/cli.js**:
```javascript
#!/usr/bin/env node

const { program } = require('commander');
const installer = require('../src/installer');

program
  .name('ios-spec-driven-installer')
  .description('CLI installer for iOS Spec-Driven Development toolkit')
  .version('2.1.0');

program
  .command('install')
  .description('Install the toolkit')
  .option('-d, --dir <path>', 'Installation directory', '.')
  .option('-a, --all', 'Install all components')
  .option('-s, --skills', 'Install skills only')
  .option('--no-backup', 'Skip backup')
  .action(installer.install);

program
  .command('update')
  .description('Update the toolkit')
  .action(installer.update);

program
  .command('uninstall')
  .description('Uninstall the toolkit')
  .action(installer.uninstall);

program.parse();
```

**src/installer.js**:
```javascript
const fs = require('fs-extra');
const path = require('path');
const inquirer = require('inquirer');
const chalk = require('chalk');
const ora = require('ora');

async function install(options) {
  console.log(chalk.blue.bold('\n🚀 iOS Spec-Driven Toolkit Installer\n'));
  
  // 1. Get installation options
  const answers = await inquirer.prompt([
    {
      type: 'list',
      name: 'components',
      message: 'What to install?',
      choices: [
        { name: 'All components (recommended)', value: 'all' },
        { name: 'Skills only', value: 'skills' },
        { name: 'Agents only', value: 'agents' },
        { name: 'Custom selection', value: 'custom' }
      ]
    },
    {
      type: 'confirm',
      name: 'backup',
      message: 'Backup existing files?',
      default: true,
      when: (answers) => !options.noBackup
    }
  ]);
  
  // 2. Backup
  if (answers.backup) {
    const spinner = ora('Backing up existing files...').start();
    await backupExisting(options.dir);
    spinner.succeed('Backup complete');
  }
  
  // 3. Install
  const spinner = ora('Installing toolkit...').start();
  await installComponents(options.dir, answers.components);
  spinner.succeed('Installation complete');
  
  // 4. Validate
  const validation = await validateInstallation(options.dir);
  if (validation.success) {
    console.log(chalk.green.bold('\n✅ Installation successful!\n'));
    showNextSteps();
  } else {
    console.log(chalk.red.bold('\n❌ Installation failed\n'));
    console.log(validation.errors);
  }
}

async function backupExisting(dir) {
  const timestamp = new Date().toISOString().replace(/:/g, '-');
  const backupDir = path.join(dir, `.claude-backup-${timestamp}`);
  
  if (await fs.pathExists(path.join(dir, '.claude'))) {
    await fs.copy(path.join(dir, '.claude'), backupDir);
  }
}

async function installComponents(dir, components) {
  const templateDir = path.join(__dirname, '../templates');
  
  if (components === 'all' || components === 'skills') {
    await fs.copy(
      path.join(templateDir, '.claude/skills'),
      path.join(dir, '.claude/skills')
    );
  }
  
  if (components === 'all' || components === 'agents') {
    await fs.copy(
      path.join(templateDir, '.claude/agents'),
      path.join(dir, '.claude/agents')
    );
  }
  
  if (components === 'all') {
    await fs.copy(
      path.join(templateDir, 'Shared'),
      path.join(dir, 'Shared')
    );
    
    await fs.copy(
      path.join(templateDir, '.mcp.json'),
      path.join(dir, '.mcp.json')
    );
  }
}

async function validateInstallation(dir) {
  const checks = [
    { path: '.claude/skills/dev-spec-driven/SKILL.md', name: 'Skills' },
    { path: '.claude/agents/write-spec.md', name: 'Agents' },
    { path: 'Shared/COMPONENT_FORMAT.md', name: 'Guides' }
  ];
  
  const errors = [];
  
  for (const check of checks) {
    if (!await fs.pathExists(path.join(dir, check.path))) {
      errors.push(`Missing: ${check.name}`);
    }
  }
  
  return {
    success: errors.length === 0,
    errors
  };
}

function showNextSteps() {
  console.log(chalk.cyan('Next steps:'));
  console.log('1. Open your project in Claude Code');
  console.log('2. Try: "Create spec for login feature"');
  console.log('3. See README.md for more examples\n');
}

module.exports = { install, update, uninstall };
```

---

## 📦 Distribution

### NPM Package

**Publish to npm**:
```bash
npm publish
```

**Users install via**:
```bash
npx ios-spec-driven-installer install
```

### GitHub Releases

**Create releases with**:
- Installer binary
- Source code
- Changelog
- Installation instructions

---

## 🧪 Testing

### Test Cases

1. **Fresh Installation**
   - Empty directory
   - No existing .claude/
   - All components install correctly

2. **Update Existing**
   - Existing .claude/
   - Backup created
   - Files updated correctly

3. **Partial Installation**
   - Skills only
   - Agents only
   - Custom selection

4. **Error Handling**
   - No write permissions
   - Disk full
   - Corrupted files

---

## 📝 Documentation

### README for Installer

```markdown
# iOS Spec-Driven Installer

Quick installation tool for iOS Spec-Driven Development toolkit.

## Installation

```bash
npx ios-spec-driven-installer install
```

## Commands

- `install` - Install the toolkit
- `update` - Update to latest version
- `uninstall` - Remove the toolkit

## Options

- `-d, --dir <path>` - Installation directory (default: current)
- `-a, --all` - Install all components
- `-s, --skills` - Install skills only
- `--no-backup` - Skip backup

## Examples

```bash
# Install everything
npx ios-spec-driven-installer install

# Install to specific directory
npx ios-spec-driven-installer install -d /path/to/project

# Install skills only
npx ios-spec-driven-installer install -s

# Update
npx ios-spec-driven-installer update
```
```

---

## 🎯 Success Criteria

- ✅ Users can install with single command
- ✅ Installation takes < 30 seconds
- ✅ Backup existing files automatically
- ✅ Validate installation
- ✅ Clear error messages
- ✅ Works on macOS, Linux, Windows
- ✅ No manual file copying needed

---

## 🚀 Next Steps

1. **Create installer structure**
   ```bash
   mkdir installer
   cd installer
   npm init -y
   ```

2. **Install dependencies**
   ```bash
   npm install commander inquirer chalk ora fs-extra
   ```

3. **Implement CLI**
   - Create bin/cli.js
   - Create src/installer.js
   - Create src/validator.js

4. **Test locally**
   ```bash
   npm link
   ios-spec-driven-installer install
   ```

5. **Publish to npm**
   ```bash
   npm publish
   ```

---

*Plan created: February 4, 2026*  
*Branch: plugin*  
*Status: Ready to implement*
