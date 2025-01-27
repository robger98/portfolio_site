import { error } from '@sveltejs/kit';
import { posts } from '../post_map';

export function load({ params }) {
    const post = posts.find((post) => post.slug === params.slug);

    if (!post) error(404, 'Post not found');

    return {
        post
    };
}
