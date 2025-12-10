import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Manual sidebar structure for the Physical AI Book
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Introduction to Physical AI',
      items: [
        'intro/fundamentals',
        'intro/applications',
        'intro/implementation'
      ],
    },
    {
      type: 'category',
      label: 'Getting Started',
      items: ['getting-started/intro'],
    },
    {
      type: 'category',
      label: 'Tutorials',
      items: ['tutorials/intro'],
    },
    {
      type: 'category',
      label: 'Reference',
      items: [
        'reference/intro',
        'reference/glossary'
      ],
    },
  ],
};

export default sidebars;
