---
title: "Git LFS Setup"
description: ""
date: 2026-02-19T18:00:00+09:00
lastmod:
draft: false
---

## Git LFS (Large File Storage) Setup

```bash
# Install Git LFS
sudo apt-get update
sudo apt-get install git-lfs -y

# Set up Git LFS for the current user
# Need to run this command only once per user
git lfs install
```

## Example Usage

When committing large files to a Git repository:

```bash
cd <your-git-repository>

# Track specific file types (e.g., .psd files)
# Must run this command first to create/modify the .gitattributes file that tells Git LFS which files to track
git lfs track "*.psd"

# Add the .gitattributes file
# To separate commits is good practice to ensure that the tracking config. is in place before adding large files
git add .gitattributes
git commit -m "Track .psd files with Git LFS"

# Add and commit your large files as usual
git add path/to/your/largefile.psd
git commit -m "Add large file with Git LFS"

# Push to remote repository
git push origin main
```

When cloning a repository that uses Git LFS:

```bash
git clone <repository-url>

cd <repository-directory>

 # This will download the large files tracked by Git LFS
git lfs pull
```
