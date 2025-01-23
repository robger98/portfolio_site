import containerQueries from '@tailwindcss/container-queries';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import daisyui from "daisyui"
import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter', 'ui-sans-serif', 'system-ui'],
				serif: ['Merriweather', 'ui-serif', 'Georgia'],
				mono: ['Menlo', 'ui-monospace', 'Monaco'],
				altehaas: ['AlteHaasGrotesk'],
			},
		}
	},

	plugins: [typography, forms, containerQueries, daisyui],
	daisyui: {
		themes: ["lofi", "black"],
		base: true,
		style: true,
		utils: true,
		prefix: "",
		logs: true,
		themeRoot: ":root",
	}
} satisfies Config;
