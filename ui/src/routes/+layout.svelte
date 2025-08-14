<script>
	import { page } from '$app/stores';
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/service-worker.js');
    }
</script>

<div class="app">
	<h1>🏋️ Training Tracker</h1>

	<nav class="menu">
		<a href="/" class:selected={$page.url.pathname === "/"}>📋 Logs</a>
		<a href="/exercises" class:selected={$page.url.pathname === "/exercises"}>🏋️ Übungen</a>
		<a href="/stats" class:selected={$page.url.pathname === "/stats"}>📊 Auswertung</a>
	</nav>

	<slot />
</div>
