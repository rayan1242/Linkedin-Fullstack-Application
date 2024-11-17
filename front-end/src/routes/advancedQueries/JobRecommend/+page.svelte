<script lang="ts">
    import axios from "axios";
    import { onMount } from "svelte";

    let jobRecommendations: { job_title: string; description: string; type: string; institution_name: string; institution_location: string; matching_skills: string }[] = [];

    async function getJobRecommendation() {
        try {
            const response = await axios.get("http://localhost:3000/advanced_queries/getJobRecommendation");
            jobRecommendations = response.data.job_recommendation;
        } catch (error) {
            console.error("Error fetching job recommendations:", error);
        }
    }

    onMount(() => {
        getJobRecommendation();
    });
</script>

<style>
    .job-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .job-title {
        font-size: 1.5em;
        margin-bottom: 8px;
    }

    .job-description {
        margin-bottom: 8px;
    }

    .job-type {
        font-weight: bold;
        margin-bottom: 8px;
    }

    .institution-info {
        font-style: italic;
        color: #555;
    }
</style>

<main>
    <h1>Job Recommendations</h1>
    {#if jobRecommendations.length > 0}
        {#each jobRecommendations as job}
            <div class="job-card">
                <div class="job-title">{job.job_title}</div>
                <div class="job-description">{job.description}</div>
                <div class="job-type">Type: {job.type}</div>
                <div class="institution-info">
                    {job.institution_name}, {job.institution_location}
                </div>
                <div class="matching-skills">Matching Skills: {job.matching_skills}</div>
            </div>
        {/each}
    {:else}
        <p>No job recommendations available.</p>
    {/if}
</main>