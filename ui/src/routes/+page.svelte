<script>
	import { onMount } from "svelte";

	const API_URL = "http://192.168.x.x:5000/api";

	let date = new Date().toISOString().split("T")[0];
	let exercise_id = "";
	let weight = "";
	let reps = "";
	let logs = [];
	let exercises = [];

	async function loadLogs() {
		const res = await fetch(`${API_URL}/logs`);
		logs = await res.json();
	}

	async function loadExercises() {
		const res = await fetch(`${API_URL}/exercises`);
		exercises = await res.json();
		if (exercises.length > 0 && !exercise_id) {
			exercise_id = exercises[0].id;
		}
	}

	async function saveLog() {
		const entry = { date, exercise_id, weight, reps };
		await fetch(`${API_URL}/log`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(entry)
		});
		weight = "";
		reps = "";
		loadLogs();
	}

	onMount(() => {
		loadExercises();
		loadLogs();
	});
</script>

<h2>📋 Logs</h2>

<form on:submit|preventDefault={saveLog}>
	<label>Datum: <input type="date" bind:value={date} /></label><br />
	<label>Übung:
		<select bind:value={exercise_id}>
			{#each exercises as ex}
				<option value={ex.id}>{ex.name}</option>
			{/each}
		</select>
	</label><br />
	<label>Gewicht: <input type="number" bind:value={weight} /></label><br />
	<label>Wdh.: <input type="number" bind:value={reps} /></label><br />
	<button type="submit">Speichern</button>
</form>

<hr />
<ul>
	{#each logs as log}
		<li>{log.date} – {log.exercise_id} → {log.weight} kg × {log.reps}</li>
	{/each}
</ul>
