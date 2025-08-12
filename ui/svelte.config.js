import adapter from '@sveltejs/adapter-static';
import { SvelteKitPWA } from '@vite-pwa/sveltekit';

export default {
	kit: {
		adapter: adapter()
	},
	vitePlugin: {
		plugins: [SvelteKitPWA()]
	}
};
