<script>
	import { onMount } from 'svelte';

	let date = new Date().toISOString().split("T")[0];
	let exercise = '';
	let weight = '';
	let reps = '';
	let logs = [];

	const API_URL = "http://192.168.0.36:5000/api"; // deine LAN-IP

	async function saveLog() {
		const entry = { date, exercise, weight, reps };
		try {
			const res = await fetch(`${API_URL}/log`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(entry)
			});
			if (res.ok) {
				logs = [...logs, entry];
			}
		} catch (e) {
			alert("Fehler beim Speichern");
		}

		exercise = '';
		weight = '';
		reps = '';
	}

	async function loadLogs() {
		try {
			const res = await fetch(`${API_URL}/logs`);
			logs = await res.json();
		} catch {
			logs = [];
		}
	}

	onMount(() => {
		loadLogs();
	});
</script>

<h1>🏋️ Training Tracker</h1>

<form on:submit|preventDefault={saveLog}>
	<label>Datum: <input type="date" bind:value={date} /></label><br />
	<label>Übung: <input bind:value={exercise} required /></label><br />
	<label>Gewicht (kg): <input type="number" bind:value={weight} required /></label><br />
	<label>Wiederholungen: <input type="number" bind:value={reps} required /></label><br />
	<button type="submit">Speichern</button>
</form>

<hr />

<h2>📋 Trainingslog</h2>
<ul>
	{#each logs as log}
		<li>{log.date} – {log.exercise}: {log.weight} kg × {log.reps}</li>
	{/each}
</ul>
