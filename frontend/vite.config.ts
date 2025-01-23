import { defineConfig } from 'vitest/config';
import Icons from 'unplugin-icons/vite'
import { sveltekit } from '@sveltejs/kit/vite';

export default defineConfig({
	plugins: [
		sveltekit(),
		Icons({
			compiler: 'svelte'
		}),
		{
			name: "markdown-loader",
			transform(code, id) {
			  if (id.slice(-3) === ".md") {
				// For .md files, get the raw content
				return `export default ${JSON.stringify(code)};`;
			  }
			}
		  }
	],

	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});
