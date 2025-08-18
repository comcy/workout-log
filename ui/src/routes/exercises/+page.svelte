<script>
  import { onMount } from "svelte";

  let exercises = [];
  let name = "";
  let category = "";
  let equipment = "";
  let muscles = "";

  // API Base (bei Bedarf anpassen auf deine Flask-URL/Port)
  const API_URL = "http://127.0.0.1:5000";

  // Lade vorhandene Übungen
  async function loadExercises() {
    try {
      const res = await fetch(`${API_URL}/exercises`);
	  console.log(res);
      if (!res.ok) throw new Error("Fehler beim Laden");
      exercises = await res.json();
    } catch (err) {
      console.error("Fehler beim Laden der Übungen:", err);
    }
  }

  // Neue Übung speichern
  async function addExercise() {
    const newExercise = {
      name,
      category,
      equipment,
      muscles: muscles.split(",").map((m) => m.trim())
    };

    try {
      const res = await fetch(`${API_URL}/exercises/add`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newExercise)
      });

      if (!res.ok) throw new Error("Fehler beim Speichern");

      const result = await res.json();
      exercises = [...exercises, result.exercise];

      // Felder leeren
      name = "";
      category = "";
      equipment = "";
      muscles = "";
    } catch (err) {
      console.error("Fehler beim Speichern:", err);
    }
  }

  onMount(loadExercises);
</script>

<h1 class="text-xl font-bold mb-4">Übungen verwalten</h1>

<!-- Formular -->
<div class="p-4 border rounded-lg mb-6">
  <h2 class="font-semibold mb-2">Neue Übung hinzufügen</h2>
  <input class="border p-2 mr-2 mb-2" placeholder="Name" bind:value={name} />
  <input class="border p-2 mr-2 mb-2" placeholder="Kategorie" bind:value={category} />
  <input class="border p-2 mr-2 mb-2" placeholder="Equipment" bind:value={equipment} />
  <input
    class="border p-2 mr-2 mb-2"
    placeholder="Muskeln (Komma-getrennt)"
    bind:value={muscles}
  />
  <button
    class="bg-blue-500 text-white px-4 py-2 rounded"
    on:click={addExercise}
  >
    Speichern
  </button>
</div>

<!-- Liste -->
<h2 class="font-semibold mb-2">Alle Übungen</h2>
<ul class="list-disc pl-5">
  {#each exercises as exercise}
    <li>
      <span class="font-bold">{exercise.name}</span>  
      ({exercise.category} – {exercise.equipment})  
      👉 {exercise.muscles.join(", ")}
    </li>
  {/each}
</ul>
