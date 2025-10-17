# OneDrive Projects Standardization Script - Enhanced Version
# Handles duplicate files, existing repos, and careful processing

$ErrorActionPreference = "Continue"
$baseDir = "C:\Users\WorkstationAdmin\OneDrive\Documents\dev\projects"

Write-Host "=== OneDrive Projects Standardization (Enhanced) ===" -ForegroundColor Cyan

# Function to clean duplicate files
function Remove-DuplicateFiles
{
    param($projectPath)

    Write-Host "    Cleaning duplicate files..." -ForegroundColor Yellow

    $duplicatePatterns = @(
        "* (2).*",
        "* (3).*",
        "* - Copy*"
    )

    foreach ($pattern in $duplicatePatterns)
    {
        $duplicates = Get-ChildItem -Path $projectPath -Filter $pattern -Recurse
        foreach ($duplicate in $duplicates)
        {
            try
            {
                Remove-Item $duplicate.FullName -Force -Recurse
                Write-Host "      Removed: $($duplicate.Name)" -ForegroundColor Gray
            }
            catch
            {
                Write-Host "      Failed to remove: $($duplicate.Name)" -ForegroundColor Red
            }
        }
    }
}

# Function to create GitHub repository
function New-GitHubRepo
{
    param($projectName, $description)

    Write-Host "    Creating GitHub repository: $projectName" -ForegroundColor Magenta
    try
    {
        # Check if repo already exists
        $existingRepo = gh repo view $projectName 2>$null
        if ($existingRepo)
        {
            Write-Host "      Repository already exists on GitHub" -ForegroundColor Yellow
            return $true
        }

        gh repo create $projectName --public --description $description --clone=false
        Write-Host "      Successfully created GitHub repository" -ForegroundColor Green
        return $true
    }
    catch
    {
        Write-Host "      Failed to create GitHub repo: $_" -ForegroundColor Red
        return $false
    }
}

# Function to handle Git repository setup
function Initialize-GitRepo
{
    param($projectPath, $projectName)

    Write-Host "    Setting up Git repository..." -ForegroundColor Yellow

    try
    {
        Set-Location $projectPath

        # If already a git repo, just ensure it's clean
        if (Test-Path ".git")
        {
            Write-Host "      Git repository already exists" -ForegroundColor Green

            # Check if there are uncommitted changes
            $status = git status --porcelain
            if ($status)
            {
                Write-Host "      Committing existing changes..." -ForegroundColor Yellow
                git add .
                git commit -m "Cleanup and standardization updates"
            }

            # Ensure main branch
            $currentBranch = git branch --show-current
            if ($currentBranch -ne "main")
            {
                git branch -M main
            }

            return $true
        }

        # Initialize new git repo
        git init
        git branch -M main

        # Create .gitignore
        $gitignoreContent = @"
# Dependencies
node_modules/
.venv/
env/
venv/
__pycache__/

# Build outputs
dist/
build/
*.egg-info/

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Logs and cache
*.log
logs/
.cache/

# Environment variables
.env
.env.local

# Temporary files
temp/
tmp/
*.tmp
"@
        Set-Content -Path ".gitignore" -Value $gitignoreContent

        # Create or update README
        if (-not (Test-Path "README.md"))
        {
            $readmeContent = @"
# $projectName

Development project for $projectName.

## Overview

This project contains tools and utilities for $($projectName.Replace('-', ' ')).

## Installation

```bash
# Installation instructions will be added
```

## Usage

```bash
# Usage examples will be added
```

## License

MIT License
"@
            Set-Content -Path "README.md" -Value $readmeContent
        }

        # Initial commit
        git add .
        git commit -m "Initial commit: Project standardization and cleanup"

        Write-Host "      Git repository initialized successfully" -ForegroundColor Green
        return $true
    }
    catch
    {
        Write-Host "      Failed to initialize Git repository: $_" -ForegroundColor Red
        return $false
    }
}

# Function to push to GitHub
function Push-ToGitHub
{
    param($projectName)

    Write-Host "    Pushing to GitHub..." -ForegroundColor Cyan
    try
    {
        # Check if remote already exists
        $remotes = git remote
        if ($remotes -notcontains "origin")
        {
            git remote add origin "https://github.com/RobertMLayne/$projectName.git"
        }

        git push -u origin main
        Write-Host "      Successfully pushed to GitHub" -ForegroundColor Green
        return $true
    }
    catch
    {
        Write-Host "      Failed to push to GitHub: $_" -ForegroundColor Red
        return $false
    }
}

# Define project mappings with better naming
$projectMappings = @{
    'archive'                                  = @{
        name = 'onedrive-project-archive'
        desc = 'Archive of OneDrive development projects and experiments'
    }
    'content_extractor'                        = @{
        name = 'content-extractor-onedrive'
        desc = 'Content extraction utility for processing documents and web pages'
    }
    'content_extractor - Copy'                 = @{
        name = 'content-extractor-copy'
        desc = 'Backup copy of content extraction utility'
    }
    'content_extractor_1'                      = @{
        name = 'content-extractor-v1'
        desc = 'Version 1 of content extraction utility'
    }
    'content_extractor_2'                      = @{
        name = 'content-extractor-v2'
        desc = 'Version 2 of content extraction utility with enhancements'
    }
    'convert_chat'                             = @{
        name = 'chat-converter'
        desc = 'Tool for converting chat exports between different formats'
    }
    'Crawl4AI'                                 = @{
        name = 'crawl4ai-integration'
        desc = 'AI-powered web crawling and content extraction integration'
    }
    'DevSync'                                  = @{
        name = 'dev-sync-tool'
        desc = 'Development environment synchronization utility'
    }
    'docharvester-pro'                         = @{
        name = 'doc-harvester-pro-v2'
        desc = 'Professional document harvesting and processing tool'
    }
    'download_jpegs'                           = @{
        name = 'jpeg-downloader'
        desc = 'Utility for downloading and managing JPEG images from URLs'
    }
    'extract_URLs'                             = @{
        name = 'url-extractor-tool'
        desc = 'Utility for extracting and processing URLs from various sources'
    }
    'extract-code'                             = @{
        name = 'code-extractor-v2'
        desc = 'Enhanced tool for extracting code snippets from documents'
    }
    'forgeavatar'                              = @{
        name = 'forge-avatar-v2'
        desc = 'Avatar generation and management utility'
    }
    'gpt-thread-tools'                         = @{
        name = 'gpt-thread-tools-v2'
        desc = 'Tools for managing and processing GPT conversation threads'
    }
    'gpt-thread-tools-ultimate'                = @{
        name = 'gpt-thread-tools-ultimate'
        desc = 'Advanced GPT thread management and analysis tools'
    }
    'html_to_md'                               = @{
        name = 'html-to-markdown-v4'
        desc = 'HTML to Markdown conversion utility with advanced features'
    }
    'layneip-examiner-graph'                   = @{
        name = 'patent-examiner-analyzer'
        desc = 'Tool for analyzing patent examiner data and relationships'
    }
    'medium_url_harvester'                     = @{
        name = 'medium-harvester'
        desc = 'Utility for harvesting and processing Medium article URLs'
    }
    'openai_memory_kit_v0.1'                   = @{
        name = 'openai-memory-kit'
        desc = 'Memory management toolkit for OpenAI applications'
    }
    'openai-url-harvester-files-with-problems' = @{
        name = 'url-harvester-debug-files'
        desc = 'Debug files and problem resources for URL harvester project'
    }
    'split_chat_export'                        = @{
        name = 'chat-export-splitter-v2'
        desc = 'Tool for splitting and processing large chat export files'
    }
    'Sync-Dev'                                 = @{
        name = 'sync-dev-v2'
        desc = 'Enhanced development environment synchronization tool'
    }
    'url_to_pdf'                               = @{
        name = 'url-to-pdf-converter'
        desc = 'Tool for converting web pages and URLs to PDF format'
    }
}

# Get directories and show mapping
$dirs = Get-ChildItem $baseDir -Directory | Sort-Object Name
Write-Host "Found $($dirs.Count) directories to process:" -ForegroundColor Green
Write-Host ""

$projects = @()
foreach ($dir in $dirs)
{
    $mapping = $projectMappings[$dir.Name]
    if ($mapping)
    {
        $projects += [PSCustomObject]@{
            original = $dir.Name
            new      = $mapping.name
            desc     = $mapping.desc
            path     = $dir.FullName
            hasGit   = Test-Path (Join-Path $dir.FullName '.git')
        }
    }
    else
    {
        Write-Host "  WARNING: No mapping found for '$($dir.Name)'" -ForegroundColor Yellow
    }
}

$projects | Format-Table -Property original, new, hasGit, desc -AutoSize

Write-Host ""
Write-Host "This will:" -ForegroundColor Yellow
Write-Host "  1. Clean up duplicate files (those with (2), (3), - Copy suffixes)" -ForegroundColor Gray
Write-Host "  2. Rename directories to standardized names" -ForegroundColor Gray
Write-Host "  3. Initialize/update Git repositories" -ForegroundColor Gray
Write-Host "  4. Create GitHub repositories" -ForegroundColor Gray
Write-Host "  5. Push all content to GitHub" -ForegroundColor Gray
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
    Write-Host "[$($successCount + 1)/$($projects.Count)] Processing: $($project.original)" -ForegroundColor Cyan
    Write-Host "  -> $($project.new)" -ForegroundColor White
    Write-Host "  Description: $($project.desc)" -ForegroundColor Gray

    try
    {
        # Step 1: Clean duplicate files
        Remove-DuplicateFiles $project.path

        # Step 2: Rename directory if needed
        if ($project.original -ne $project.new)
        {
            $newPath = Join-Path (Split-Path $project.path) $project.new
            if (Test-Path $newPath)
            {
                Write-Host "    Target directory already exists, skipping rename" -ForegroundColor Yellow
            }
            else
            {
                Rename-Item $project.path $project.new
                $project.path = $newPath
                Write-Host "    Directory renamed successfully" -ForegroundColor Green
            }
        }

        # Step 3: Initialize/update Git repository
        $gitSuccess = Initialize-GitRepo $project.path $project.new
        if (-not $gitSuccess)
        {
            $failedProjects += "$($project.new) (Git setup failed)"
            continue
        }

        # Step 4: Create GitHub repository
        $githubSuccess = New-GitHubRepo $project.new $project.desc
        if (-not $githubSuccess)
        {
            $failedProjects += "$($project.new) (GitHub creation failed)"
            continue
        }

        # Step 5: Push to GitHub
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

# Final summary
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
Write-Host "All GitHub repositories: https://github.com/RobertMLayne" -ForegroundColor Magenta
Write-Host "OneDrive projects standardization complete!" -ForegroundColor Green
