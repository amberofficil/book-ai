# Contributing to Physical AI Book

Thank you for your interest in contributing to the Physical AI Book! This guide will help you get started.

## Prerequisites

- Node.js (v18 or higher)
- npm or yarn package manager
- Git
- Basic knowledge of Markdown and MDX

## Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/your-username/physical-ai-book.git
   cd physical-ai-book/website
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

## Making Changes

### Adding Content

1. Create new content in the `docs/` directory in the appropriate subdirectory
2. Update `sidebars.ts` to include your new content in the navigation if needed
3. Test the content locally using `npm start`
4. Commit your changes and submit a pull request

### Content Structure

- Chapters are organized in subdirectories under `docs/`
- Lessons are individual MDX files within chapter directories
- Each lesson should include hands-on examples and challenges
- Code examples should be included as fenced code blocks with appropriate language tags

### Style Guide

- Maintain a consistent voice that matches the brand guidelines
- Structure content to support both linear reading and reference use
- Include hands-on examples that align with the Physical AI book constitution
- Ensure content is approachable for beginners while offering depth for intermediate learners
- Use clear learning objectives for each lesson

## Testing

- Verify all code examples work correctly
- Ensure links and navigation function properly
- Check for typos and grammatical errors
- Test accessibility features

## Code Examples

- Place executable code examples in the `static/code-examples/` directory
- Match the directory structure to the lessons (e.g., `static/code-examples/intro/` for intro lesson examples)
- Include comments that explain the code and connect it to Physical AI concepts

## Pull Request Process

1. Create a feature branch for your changes
2. Make your changes following the guidelines above
3. Test your changes thoroughly
4. Submit a pull request with a clear description of your changes
5. Address any feedback from the review process

## Questions?

If you have questions, please open an issue in the repository.