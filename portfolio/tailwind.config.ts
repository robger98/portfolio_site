import containerQueries from '@tailwindcss/container-queries';
import forms from '@tailwindcss/forms';
import typography from '@tailwindcss/typography';
import daisyui from "daisyui"
import AlteHaasGroteskBold from '$lib/fonts/alte_haas_grotesk/AlteHaasGroteskBold.ttf';
import AlteHaasGroteskRegular from '$lib/fonts/alte_haas_grotesk/AlteHaasGroteskRegular.ttf';
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
		themes: [
			"black","light", "business", "luxury"
		]
	}
} satisfies Config;
