<script lang="ts">
    import { onMount } from 'svelte';
    import { getgrowthanalysis } from '$lib/api/advancedQueries';

    let growthData: { name: string; start: string; employee_count: number; previous_count: number; growth: number }[] = [];
    let error: string | null = null;

    async function getGrowthAnalysis() {
        try {
            const response = await getgrowthanalysis();
            console.log("API Response:", response);
            if (response.status === "success") {
                growthData = response.institution_growth;
            } else {
                error = response.message;
            }
        } catch (err) {
            console.error("Error fetching growth analysis data:", err);
            error = "Error fetching growth analysis data.";
        }
    }

    onMount(() => {
        getGrowthAnalysis();
    });
</script>

<style>
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }

    th, td {
        padding: 10px;
        border: 1px solid #ddd;
        text-align: left;
    }

    th {
        background-color: #f4f4f4;
    }

    tr:nth-child(even) {
        background-color: #f9f9f9;
    }

    .error {
        color: red;
        margin-top: 20px;
    }
</style>

<div class="container">
    <h1>Institution Growth Analysis</h1>
    {#if error}
        <p class="error">{error}</p>
    {:else if growthData.length > 0}
        <table>
            <thead>
                <tr>
                    <th>Institution Name</th>
                    <th>Start Date</th>
                    <th>Employee Count</th>
                    <th>Previous Count</th>
                    <th>Growth</th>
                </tr>
            </thead>
            <tbody>
                {#each growthData as data}
                    <tr>
                        <td>{data.name}</td>
                        <td>{data.start}</td>
                        <td>{data.employee_count}</td>
                        <td>{data.previous_count}</td>
                        <td>{data.growth}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {:else}
        <p class="error">No institution growth data found.</p>
    {/if}
</div>
