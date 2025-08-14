<script>
	import Logs from "./components/Logs.svelte";
	import Exercises from "./components/Exercises.svelte";
	import Stats from "./components/Stats.svelte";

	let activeTab = "logs"; // default view

	function setTab(tab) {
		activeTab = tab;
	}
</script>

<div class="app">
	<h1 class="title">🏋️ Training Tracker</h1>

	<!-- Menü -->
	<nav class="menu">
		<button on:click={() => setTab("logs")} class:selected={activeTab === "logs"}>📋 Logs</button>
		<button on:click={() => setTab("exercises")} class:selected={activeTab === "exercises"}>🏋️ Übungen</button>
		<button on:click={() => setTab("stats")} class:selected={activeTab === "stats"}>📊 Auswertung</button>
	</nav>

	<!-- Views -->
	{#if activeTab === "logs"}
		<Logs />
	{:else if activeTab === "exercises"}
		<Exercises />
	{:else if activeTab === "stats"}
		<Stats />
	{/if}
</div>

<style>
	.app {
		font-family: system-ui, sans-serif;
		max-width: 600px;
		margin: auto;
		padding: 1rem;
	}
	.title {
		text-align: center;
		margin-bottom: 1rem;
	}
	.menu {
		display: flex;
		justify-content: space-around;
		margin-bottom: 1rem;
	}
	button {
		padding: 0.5rem 1rem;
		border-radius: 0.5rem;
		border: none;
		cursor: pointer;
		background: #eee;
	}
	button.selected {
		background: #0070f3;
		color: white;
	}
</style>
