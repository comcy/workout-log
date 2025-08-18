<script>
  import { onMount } from "svelte";

  let workouts = [];
  let exercises = [];

  // Eingabe-Felder
  let selectedExerciseId = "";
  let weight = "";
  let reps = "";
  let date = new Date().toISOString().split("T")[0];

  const API_URL = "http://127.0.0.1:5000";

  // Workouts laden
  async function loadWorkouts() {
    try {
      const res = await fetch(`${API_URL}/workouts`);
      if (!res.ok) throw new Error("Fehler beim Laden");
      workouts = await res.json();
    } catch (err) {
      console.error("Fehler beim Laden der Workouts:", err);
    }
  }

  // Übungen laden
  async function loadExercises() {
    try {
      const res = await fetch(`${API_URL}/exercises`);
      if (!res.ok) throw new Error("Fehler beim Laden");
      exercises = await res.json();
    } catch (err) {
      console.error("Fehler beim Laden der Übungen:", err);
    }
  }

  // Neues Workout speichern
  async function addWorkout() {
    if (!selectedExerciseId) {
      alert("Bitte eine Übung auswählen");
      return;
    }

    const newWorkout = {
      exercise_id: parseInt(selectedExerciseId),
      weight,
      reps,
      date
    };

    try {
      const res = await fetch(`${API_URL}/workouts/add`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newWorkout)
      });

      if (!res.ok) throw new Error("Fehler beim Speichern");

      const result = await res.json();
      workouts = [...workouts, result.workout];

      // Eingabe leeren
      selectedExerciseId = "";
      weight = "";
      reps = "";
      date = new Date().toISOString().split("T")[0];
    } catch (err) {
      console.error("Fehler beim Speichern:", err);
    }
  }

  onMount(() => {
    loadWorkouts();
    loadExercises();
  });
</script>

<h1 class="text-xl font-bold mb-4">Workouts</h1>

<!-- Formular -->
<div class="p-4 border rounded-lg mb-6">
  <h2 class="font-semibold mb-2">Neues Workout eintragen</h2>

  <select class="border p-2 mr-2 mb-2" bind:value={selectedExerciseId}>
    <option value="">-- Übung wählen --</option>
    {#each exercises as ex}
      <option value={ex.id}>{ex.name}</option>
    {/each}
  </select>

  <input
    class="border p-2 mr-2 mb-2"
    placeholder="Gewicht (kg)"
    type="number"
    bind:value={weight}
  />
  <input
    class="border p-2 mr-2 mb-2"
    placeholder="Wiederholungen"
    type="number"
    bind:value={reps}
  />
  <input
    class="border p-2 mr-2 mb-2"
    type="date"
    bind:value={date}
  />

  <button
    class="bg-green-500 text-white px-4 py-2 rounded"
    on:click={addWorkout}
  >
    Speichern
  </button>
</div>

<!-- Liste -->
<h2 class="font-semibold mb-2">Alle Workouts</h2>
<ul class="list-disc pl-5">
  {#each workouts as workout}
    <li>
      {#if exercises.length > 0}
        {exercises.find(ex => ex.id === workout.exercise_id)?.name || "?"}
      {/if}
      – {workout.weight}kg × {workout.reps} am {workout.date}
    </li>
  {/each}
</ul>
