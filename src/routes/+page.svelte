<script>
	let date = new Date().toISOString().split("T")[0];
	let exercise = '';
	let weight = '';
	let reps = '';
	let logs = [];

	const API_URL = "http://192.168.0.36:5000/api"; // oder https://deine-api.com

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

		exercise = weight = reps = '';
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
