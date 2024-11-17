<script lang="ts">
    import { getJobRecommendations } from "$lib/api/advancedQueries";
    let user_Id: string = "";
    let jobRecommendations: { job_title: string; description: string; type: string; institution_name: string; institution_location: string; matching_skills: string }[] = [];

    async function getJobRecommendation(user_Id: string) {
        try {
            const response = await getJobRecommendations(user_Id);
            jobRecommendations = response.job_recommendation;
            console.log(jobRecommendations);
        } catch (error) {
            console.error("Error fetching job recommendations:", error);
        }
    }

    function handleSubmit() {
        if (user_Id) {
            getJobRecommendation(user_Id);
        }
    }
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

    main {
        max-width: 600px;
        margin: 0 auto;
        padding: 16px;
    }

    h1 {
        text-align: center;
        margin-bottom: 24px;
    }

    input[type="text"] {
        width: calc(100% - 22px);
        padding: 10px;
        margin-bottom: 16px;
        border: 1px solid #ddd;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        font-size: 1em;
    }

    button {
        display: block;
        width: 100%;
        padding: 10px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1em;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    button:hover {
        background-color: #0056b3;
    }
</style>

<main>
    <h1>Job Recommendations</h1>
    <input type="text" bind:value={user_Id} placeholder="Enter User ID" />
    <button on:click={handleSubmit}>Get Recommendations</button>
    
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