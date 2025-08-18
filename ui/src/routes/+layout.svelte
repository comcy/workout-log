<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores'; // ✅ hier importieren

  onMount(() => {
    if (typeof navigator !== 'undefined' && 'serviceWorker' in navigator) {
      navigator.serviceWorker.register('/service-worker.js')
        .then(() => console.log('✅ Service Worker registered'))
        .catch((err) => console.error('❌ Service Worker failed', err));
    }
  });
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

<style>
  .menu {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
  }
  .menu a {
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
  }
  .menu a.selected {
    background: #444;
    color: white;
  }
</style>
