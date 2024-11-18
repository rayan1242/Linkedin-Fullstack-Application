<script lang="ts">
    import { onMount } from 'svelte';
    import { getUserPerformance } from '$lib/api/advancedQueries';
    interface UserPerformance {
    user_id: string;
    name: string;
    location_country: string;
    skill_count: number;
    post_count: number;
    overall_rank: number;
    country_rank: number;
    performance_category: string;
}

let userPerformance: UserPerformance[] = [];
    let errorMessage = '';

    onMount(async () => {
        try {
            const data = await getUserPerformance();

            if (data.status === 'success') {
                userPerformance = data.user_performance;
            } else {
                errorMessage = data.message;
            }
        } catch (error) {
            errorMessage = 'Failed to fetch user performance data.';
        }
    });
</script>

<main>
    <h1>User Performance</h1>
    {#if errorMessage}
        <p class="error">{errorMessage}</p>
    {:else}
        <table>
            <thead>
                <tr>
                    <th>User ID</th>
                    <th>Name</th>
                    <th>Country</th>
                    <th>Skill Count</th>
                    <th>Post Count</th>
                    <th>Overall Rank</th>
                    <th>Country Rank</th>
                    <th>Performance Category</th>
                </tr>
            </thead>
            <tbody>
                {#each userPerformance as user}
                    <tr>
                        <td>{user.user_id}</td>
                        <td>{user.name}</td>
                        <td>{user.location_country}</td>
                        <td>{user.skill_count}</td>
                        <td>{user.post_count}</td>
                        <td>{user.overall_rank}</td>
                        <td>{user.country_rank}</td>
                        <td>{user.performance_category}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {/if}
</main>
<style>
    .error {
        color: red;
        font-weight: bold;
        margin: 20px 0;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 1em;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }

    th, td {
        padding: 12px 15px;
        border: 1px solid #ddd;
        text-align: left;
    }

    th {
        background-color: #009879;
        color: #ffffff;
        text-transform: uppercase;
    }

    tr {
        border-bottom: 1px solid #dddddd;
    }

    tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }

    tr:last-of-type {
        border-bottom: 2px solid #009879;
    }

    tr:hover {
        background-color: #f1f1f1;
    }
</style>
