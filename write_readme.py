
code = '''# Rythfolio

Personal developer portfolio built with React, Vite, and Tailwind CSS v4.

Live at: https://rythfolio.vercel.app

## Tech Stack

- React + TypeScript
- Vite
- Tailwind CSS v4
- Framer Motion
- Vercel (deployment)
- GitHub API (live contribution heatmap)
- LeetCode API (real-time coding stats)
- EmailJS (contact form)

## Features

- Particle constellation hero animation
- Live GitHub contribution heatmap
- Real-time LeetCode stats
- Dynamic contact form
- Dark / Light mode toggle
- Mobile responsive with bottom nav
- Side navigation panel
- Certifications and Projects showcase
- Tech stack progress bars
- Currently learning section

## Run Locally

`ash
npm install
npm run dev
`

## Deploy

Deployed on Vercel with auto-deploy on push to main.

## Author

C Rythan - [rythfolio.vercel.app](https://rythfolio.vercel.app)
'''
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(code)
print('README done!')
