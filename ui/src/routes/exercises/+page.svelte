<script>
	import { onMount } from "svelte";

	const API_URL = "http://192.168.x.x:5000/api";
	let exercises = [];
	let newExercise = "";

	async function loadExercises() {
		const res = await fetch(`${API_URL}/exercises`);
		exercises = await res.json();
	}

	async function addExercise() {
		await fetch(`${API_URL}/exercises`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ name: newExercise })
		});
		newExercise = "";
		loadExercises();
	}

	onMount(loadExercises);
</script>

<h2>🏋️ Übungen</h2>

<form on:submit|preventDefault={addExercise}>
	<input bind:value={newExercise} placeholder="Neue Übung" />
	<button type="submit">Hinzufügen</button>
</form>

<ul>
	{#each exercises as ex}
		<li>{ex.name} <small>({ex.id})</small></li>
	{/each}
</ul>
