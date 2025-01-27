import { posts } from "./post_map";

export function load() {
    return {
        summaries: posts.map((post) => ({
            slug: post.slug,
            title: post.title,
            date: post.date,
            description: post.description,
        })),
    };
}