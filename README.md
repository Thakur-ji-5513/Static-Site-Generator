# Static Site Generator

A Python-based command-line tool that transforms Markdown files into a full HTML website using Jinja-style templating.

## Features

- **Markdown to HTML**: Recursively processes a directory of Markdown files and converts them to HTML.
- **Template Integration**: Injects content into a base HTML template.
- **Static Asset Management**: Automatically syncs images and CSS from a static directory to the public build folder.
- **Internal Linking**: Handles extraction of titles and link verification.

## How it Works

The program follows a specific build pipeline:
1. Deletes everything in the `public` directory to ensure a clean build.
2. Copies all static assets (images, styles) from `static` to `public`.
3. Starting at `content/`, it crawls every `.md` file.
4. Converts Markdown blocks (headers, lists, code blocks) into HTML tags.
5. Wraps the generated HTML in the `template.html` and writes the result to the destination.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Usage
1. Place your Markdown files in the `/content` folder.
2. Run the generator:
   ```bash
   python3 src/main.py
