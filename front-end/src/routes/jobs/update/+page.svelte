<script lang="ts">
  import { getJob, updateJob, type JobParam } from '$lib/api/job'; // Adjust the import path as necessary
  import { onMount } from 'svelte';

  let job_id: string;
  let jobData: JobParam = {
    institution_id: 0,
    job_title: '',
    description: '',
    type: '',
  };

  let message = '';

  onMount(async () => {
    try {
      const job = await getJob(job_id);
      jobData = job;
    } catch (e: any) {
      console.error(e);
    }
  });

  const handleSubmit = async () => {
    try {
      const response = await updateJob(job_id, jobData);
      if (response.status === 'success') {
        message = 'Job updated successfully!';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error updating job.';
    }
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={jobData.institution_id} placeholder="Institution ID" required />
  <input type="text" bind:value={jobData.job_title} placeholder="Job Title" required />
  <textarea bind:value={jobData.description} placeholder="Description" required></textarea>
  <input type="text" bind:value={jobData.type} placeholder="Type (e.g., Full-time, Part-time)" required />
  <button type="submit">Update Job</button>
</form>

{#if message}
  <p>{message}</p>
{/if}

<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    max-width: 500px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  input,
  textarea {
    padding: 0.75rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    transition: border-color 0.3s;
  }

  input:focus,
  textarea:focus {
    border-color: #007bff;
    outline: none;
  }

  button {
    padding: 0.75rem;
    font-size: 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    margin-top: 1rem;
    font-size: 1rem;
    color: #28a745;
  }
</style>
