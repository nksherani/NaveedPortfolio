# Naveed Ahmed — AI Architect Portfolio Website

This is a modern, responsive, high-performance portfolio website built with pure vanilla HTML5, CSS3, and JavaScript, designed to showcase the expertise of Naveed Ahmed as a Principal Software Engineer & AI Solution Architect.

## Core Features & Design Highlights

*   **Editorial light theme:** Cool stone backgrounds, deep ink typography, and a maritime teal accent—no neon gradients or dark-mode glow effects.
*   **Restrained surfaces:** Clean white panels with hairline borders for hierarchy, without glassmorphism or heavy shadows.
*   **Scroll-Driven Animations:** Implements native CSS scroll-driven animations (`animation-timeline: view()`) with a lightweight `IntersectionObserver` JS fallback for unsupported browsers (like Firefox).
*   **Dynamic Portfolio Filter:** Interactive category filtering for projects (Enterprise AI, SaaS/Consumer, Cloud/Data) with smooth transition animations.
*   **Fully Responsive Layout:** Fully adaptive menu and grid systems supporting screen sizes from small mobile screens to high-resolution desktop viewports.
*   **Accessibility & SEO Best Practices:** Semantic HTML5 nodes, accessible touch target sizes (min-block-size ≥ 44px), proper outline-based focus states (`:focus-visible`), responsive typography (`clamp()`), and optimized viewports.

## Deployment to Vercel

You can deploy this directory to Vercel in seconds.

### Method 1: Vercel CLI

1. Install Vercel CLI globally:
   ```bash
   npm install -g vercel
   ```
2. Navigate into the portfolio directory:
   ```bash
   cd portfolio
   ```
3. Deploy to Vercel:
   ```bash
   vercel
   ```

### Method 2: Git Integration

1. Push your repository containing this folder to GitHub/GitLab/Bitbucket.
2. Log in to [vercel.com](https://vercel.com).
3. Import the repository.
4. Set the **Root Directory** of the project to `portfolio` in the Vercel dashboard.
5. Click **Deploy**.
