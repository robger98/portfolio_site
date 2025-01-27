import First from './md_blog_posts/first.md?raw';
import Portfolio from './md_blog_posts/portfolio.md?raw';

export const posts = [
    {
        slug: 'first',
        title: 'First Post',
        date: '2025-01-27',
        description: 'Welcome to my blog',
        image: '/floating_islands.jpg',
        content: First,
    },
    {
        slug: 'portfolio',
        title: 'My Portfolio',
        date: '2025-01-27',
        description: 'In this post I talk about the development of this website',
        image: '/floating_islands.jpg',
        content: Portfolio
    }
]