<script>
  import { onMount } from "svelte";
  import {
    Chart,
    LineElement,
    PointElement,
    BarElement,
    CategoryScale,
    LinearScale,
    Title,
    Tooltip,
    Legend
  } from "chart.js";

  let canvas;
  let chart;

  // Beispiel-Daten (später von API laden)
  let labels = ["01.01", "02.01", "03.01", "04.01"];
  let weights = [40, 42.5, 45, 47.5];

  onMount(() => {
    Chart.register(
      LineElement,
      PointElement,
      BarElement,
      CategoryScale,
      LinearScale,
      Title,
      Tooltip,
      Legend
    );

    chart = new Chart(canvas, {
      type: "line", // du kannst auch "bar", "pie", etc. probieren
      data: {
        labels,
        datasets: [
          {
            label: "Gewicht (kg)",
            data: weights,
            borderColor: "rgba(255, 99, 132, 1)",
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            tension: 0.3,
            fill: true
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: "Trainingsfortschritt"
          },
          legend: {
            display: true
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: "Datum"
            }
          },
          y: {
            title: {
              display: true,
              text: "Gewicht (kg)"
            }
          }
        }
      }
    });

    return () => chart.destroy();
  });
</script>

<div class="chart-container" style="width: 100%; max-width: 600px; margin: auto;">
  <canvas bind:this={canvas}></canvas>
</div>
