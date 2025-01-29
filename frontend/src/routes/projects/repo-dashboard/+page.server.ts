// import import from 'vite';

import type { PageServerLoad } from "../$types";

export const load: PageServerLoad = async ({ params }) => {
    return {
        API_URL : process.env.API_URL,
    };
}
