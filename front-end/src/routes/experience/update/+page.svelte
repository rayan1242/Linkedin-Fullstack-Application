<script lang="ts">
  import { getExperience, updateExperience, type ExperienceParams } from '$lib/api/experience'; // Adjust the import path as necessary
  import { onMount } from 'svelte';

  let exp_id: string;
  let experienceData: ExperienceParams = {
    user_id: NaN,
    institution_id: NaN,
    start: '',
    end: '',
    description: '',
    title: '',
    duration: NaN
  };

  let message = '';

  onMount(async () => {
    try {
      const experience = await getExperience(exp_id);
      experienceData = experience;
    } catch (e: any) {
      console.log(e);
    }
  });

  const handleSubmit = async () => {
    try {
      const response = await updateExperience(exp_id, experienceData);
      if (response.status === 'success') {
        message = 'Experience record updated successfully!';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error updating experience record.';
    }
  };
</script>

<style>
  form {
    max-width: 600px;
    margin: 0 auto;
    padding: 1rem;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  input, button {
    width: 100%;
    padding: 0.75rem;
    margin: 0.5rem 0;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  input:focus {
    border-color: #007BFF;
    outline: none;
  }

  button {
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    text-align: center;
    color: green;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={exp_id} placeholder="Experience ID" required />
  <input type="number" bind:value={experienceData.user_id} placeholder="User ID" required />
  <input type="number" bind:value={experienceData.institution_id} placeholder="Institution ID" required />
  <input type="date" bind:value={experienceData.start} placeholder="Start Date" required />
  <input type="date" bind:value={experienceData.end} placeholder="End Date" />
  <input type="text" bind:value={experienceData.description} placeholder="Description" required />
  <input type="text" bind:value={experienceData.title} placeholder="Title" required />
  <input type="number" bind:value={experienceData.duration} placeholder="Duration" required />
  <button type="submit">Update Experience</button>
</form>

{#if message}
  <p>{message}</p>
{/if}