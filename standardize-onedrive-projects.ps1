# OneDrive Projects Standardization Script
# Standardizes all projects in OneDrive\Documents\dev\projects directory
# Creates local Git repos and GitHub repositories

$ErrorActionPreference = "Continue"
$baseDir = "C:\Users\WorkstationAdmin\OneDrive\Documents\dev\projects"

# Get all directories
$allDirs = Get-ChildItem $baseDir -Directory | Sort-Object Name

Write-Host "=== OneDrive Projects Standardization ===" -ForegroundColor Cyan
Write-Host "Found $($allDirs.Count) directories to process" -ForegroundColor Green
Write-Host ""

# Function to rename project with kebab-case and deduplication
function Rename-Project
{
    param($originalName, $basePath)

    # Convert to kebab-case
    $kebabName = $originalName.ToLower() -replace '[^a-z0-9]+', '-' -replace '^-|-$', ''

    # Handle specific name mappings and deduplications
    $nameMap = @{
        'content-extractor'                        = 'content-extractor-onedrive'
        'content-extractor-copy'                   = 'content-extractor-copy-v2'
        'content-extractor-1'                      = 'content-extractor-v1'
        'content-extractor-2'                      = 'content-extractor-v2'
        'devSync'                                  = 'dev-sync-onedrive'
        'docharvester-pro'                         = 'doc-harvester-pro-onedrive'
        'forgeavatar'                              = 'forge-avatar-onedrive'
        'gpt-thread-tools'                         = 'gpt-thread-tools-onedrive'
        'gpt-thread-tools-ultimate'                = 'gpt-thread-tools-ultimate-onedrive'
        'html-to-md'                               = 'html-to-md-onedrive'
        'sync-dev'                                 = 'sync-dev-onedrive'
        'medium-url-harvester'                     = 'medium-url-harvester-onedrive'
        'openai-url-harvester-files-with-problems' = 'openai-url-harvester-problem-files'
        'openai-memory-kit-v0-1'                   = 'openai-memory-kit-v01'
        'layneip-examiner-graph'                   = 'patent-examiner-graph'
        'crawl4ai'                                 = 'crawl4ai-onedrive'
        'extract-u-r-ls'                           = 'url-extractor-onedrive'
        'split-chat-export'                        = 'chat-export-splitter-onedrive'
        'convert-chat'                             = 'chat-converter-onedrive'
        'download-jpegs'                           = 'jpeg-downloader'
        'url-to-pdf'                               = 'url-to-pdf-converter'
        'extract-code'                             = 'code-extractor-onedrive'
        'archive'                                  = 'project-archive'
    }

    if ($nameMap.ContainsKey($kebabName))
    {
        $kebabName = $nameMap[$kebabName]
    }

    return $kebabName
}

# Function to initialize Git repository
function Initialize-GitRepo
{
    param($projectPath, $projectName)

    Write-Host "  Initializing Git repository..." -ForegroundColor Yellow

    try
    {
        Set-Location $projectPath

        # Check if already a git repo
        if (Test-Path ".git")
        {
            Write-Host "    Git repository already exists" -ForegroundColor Green
            return $true
        }

        # Initialize git
        git init | Out-Null
        git branch -M main | Out-Null

        # Create .gitignore if it doesn't exist
        if (-not (Test-Path ".gitignore"))
        {
            $gitignoreContent = @"
# Dependencies
node_modules/
.venv/
env/
venv/

# Build outputs
dist/
build/
*.egg-info/

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Cache
.cache/
__pycache__/
*.pyc

# Environment variables
.env
.env.local

# Temporary files
temp/
tmp/
*.tmp
"@
            Set-Content -Path ".gitignore" -Value $gitignoreContent
        }

        # Create basic README if it doesn't exist
        if (-not (Test-Path "README.md"))
        {
            $readmeContent = @"
# $projectName

Project description goes here.

## Features

- Feature 1
- Feature 2

## Installation

```bash
# Installation instructions
```

## Usage

```bash
# Usage examples
```

## License

MIT License
"@
            Set-Content -Path "README.md" -Value $readmeContent
        }

        # Stage and commit all files
        git add . | Out-Null
        git commit -m "Initial commit: Project standardization" | Out-Null

        Write-Host "    Git repository initialized successfully" -ForegroundColor Green
        return $true
    }
    catch
    {
        Write-Host "    Failed to initialize Git repository: $_" -ForegroundColor Red
        return $false
    }
}

# Function to create GitHub repository
function New-GitHubRepo
{
    param($projectName, $description)

    Write-Host "  Creating GitHub repository: $projectName" -ForegroundColor Magenta
    try
    {
        gh repo create $projectName --public --description $description --clone=false
        return $true
    }
    catch
    {
        Write-Host "    Failed to create GitHub repo for $projectName : $_" -ForegroundColor Red
        return $false
    }
}

# Function to push to GitHub
function Push-ToGitHub
{
    param($projectName)

    Write-Host "  Pushing to GitHub..." -ForegroundColor Cyan
    try
    {
        git remote add origin "https://github.com/RobertMLayne/$projectName.git"
        git push -u origin main
        Write-Host "    Successfully pushed to GitHub" -ForegroundColor Green
        return $true
    }
    catch
    {
        Write-Host "    Failed to push to GitHub: $_" -ForegroundColor Red
        return $false
    }
}

# Function to generate project description
function Get-ProjectDescription
{
    param($projectName, $projectPath)

    # Check for existing README or other files to infer description
    $readmePath = Join-Path $projectPath "README.md"
    if (Test-Path $readmePath)
    {
        $content = Get-Content $readmePath -Raw
        if ($content -match '#\s*(.+?)(?:\n|\r|\z)')
        {
            return $matches[1].Trim()
        }
    }

    # Generate description based on project name
    $descriptions = @{
        'content-extractor-onedrive'         = 'Content extraction utility for processing documents and web pages'
        'content-extractor-copy-v2'          = 'Enhanced content extraction tool with improved features'
        'content-extractor-v1'               = 'Version 1 of content extraction utility'
        'content-extractor-v2'               = 'Version 2 of content extraction utility'
        'chat-converter-onedrive'            = 'Tool for converting chat exports between different formats'
        'crawl4ai-onedrive'                  = 'AI-powered web crawling and content extraction tool'
        'dev-sync-onedrive'                  = 'Development environment synchronization utility'
        'doc-harvester-pro-onedrive'         = 'Professional document harvesting and processing tool'
        'url-extractor-onedrive'             = 'Utility for extracting and processing URLs from various sources'
        'code-extractor-onedrive'            = 'Tool for extracting code snippets from documents and files'
        'forge-avatar-onedrive'              = 'Avatar generation and management utility'
        'gpt-thread-tools-onedrive'          = 'Tools for managing and processing GPT conversation threads'
        'gpt-thread-tools-ultimate-onedrive' = 'Advanced GPT thread management and analysis tools'
        'html-to-md-onedrive'                = 'HTML to Markdown conversion utility'
        'patent-examiner-graph'              = 'Tool for analyzing patent examiner data and relationships'
        'medium-url-harvester-onedrive'      = 'Utility for harvesting and processing Medium article URLs'
        'openai-memory-kit-v01'              = 'Memory management toolkit for OpenAI applications'
        'chat-export-splitter-onedrive'      = 'Tool for splitting large chat export files'
        'sync-dev-onedrive'                  = 'Development environment synchronization tool'
        'jpeg-downloader'                    = 'Utility for downloading and managing JPEG images'
        'url-to-pdf-converter'               = 'Tool for converting web pages to PDF format'
        'openai-url-harvester-problem-files' = 'Problem files and debugging resources for URL harvester'
        'project-archive'                    = 'Archive of legacy and experimental projects'
    }

    return $descriptions[$projectName] -or "Development project for $projectName"
}

# Main processing
$projects = @()

foreach ($dir in $allDirs)
{
    $originalName = $dir.Name
    $newName = Rename-Project $originalName $baseDir
    $description = Get-ProjectDescription $newName $dir.FullName

    $projects += [PSCustomObject]@{
        original = $originalName
        new      = $newName
        path     = $dir.FullName
        desc     = $description
    }
}

Write-Host "Projects to be processed:" -ForegroundColor Yellow
$projects | Format-Table -Property original, new, desc -AutoSize

Write-Host ""
$confirm = Read-Host "Continue with processing all $($projects.Count) projects? (y/N)"
if ($confirm -ne 'y' -and $confirm -ne 'Y')
{
    Write-Host "Operation cancelled" -ForegroundColor Yellow
    exit
}

# Process each project
$successCount = 0
$failedProjects = @()

foreach ($project in $projects)
{
    Write-Host ""
    Write-Host "Processing: $($project.original) -> $($project.new)" -ForegroundColor Cyan
    Write-Host "Description: $($project.desc)" -ForegroundColor Gray

    try
    {
        # Step 1: Rename directory if needed
        if ($project.original -ne $project.new)
        {
            $newPath = Join-Path (Split-Path $project.path) $project.new
            if (Test-Path $newPath)
            {
                Write-Host "  Target directory already exists: $newPath" -ForegroundColor Yellow
                continue
            }
            Rename-Item $project.path $project.new
            $project.path = $newPath
        }

        # Step 2: Initialize Git repository
        $gitSuccess = Initialize-GitRepo $project.path $project.new
        if (-not $gitSuccess)
        {
            $failedProjects += "$($project.new) (Git init failed)"
            continue
        }

        # Step 3: Create GitHub repository
        $githubSuccess = New-GitHubRepo $project.new $project.desc
        if (-not $githubSuccess)
        {
            $failedProjects += "$($project.new) (GitHub creation failed)"
            continue
        }

        # Step 4: Push to GitHub
        $pushSuccess = Push-ToGitHub $project.new
        if (-not $pushSuccess)
        {
            $failedProjects += "$($project.new) (Push failed)"
            continue
        }

        Write-Host "  ✅ Successfully processed $($project.new)" -ForegroundColor Green
        $successCount++
    }
    catch
    {
        Write-Host "  ❌ Error processing $($project.original): $_" -ForegroundColor Red
        $failedProjects += "$($project.new) (Exception: $_)"
    }
}

# Summary
Write-Host ""
Write-Host "=== PROCESSING COMPLETE ===" -ForegroundColor Cyan
Write-Host "Successfully processed: $successCount out of $($projects.Count) projects" -ForegroundColor Green

if ($failedProjects.Count -gt 0)
{
    Write-Host ""
    Write-Host "Failed projects:" -ForegroundColor Red
    $failedProjects | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
}

Write-Host ""
Write-Host "All GitHub repositories created under: https://github.com/RobertMLayne" -ForegroundColor Magenta
