# Quickstart Guide: Physical AI Book

## Overview
This guide provides a quick introduction to contributing to the Physical AI book project.

## Prerequisites
- Node.js (v18 or higher)
- Git
- Basic knowledge of Markdown and MDX

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd website
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The site will be accessible at http://localhost:3000

## Contributing Content
1. Create a new branch for your changes
2. Add new content to the `docs/` directory in the appropriate subdirectory
3. Update `sidebars.js` to include your new content in the navigation if needed
4. Test the content locally using `npm start`
5. Commit your changes and submit a pull request

## Content Structure
- Chapters are organized in subdirectories under `docs/`
- Lessons are individual MDX files within chapter directories
- Each lesson should include hands-on examples and challenges
- Code examples should be included as fenced code blocks with appropriate language tags

## Testing
- Verify all code examples work correctly
- Ensure links and navigation function properly
- Check for typos and grammatical errors
- Test accessibility features

## Deployment
The site is automatically deployed via GitHub Pages when changes are merged to the main branch.