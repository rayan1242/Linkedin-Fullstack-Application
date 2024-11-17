<script lang="ts">
  import { getExperience, updateExperience, type ExperienceParams } from '$lib/api/experience'; // Adjust the import path as necessary
  import { onMount } from 'svelte';

  let experience_id: number;
  let experienceData: ExperienceParams = {
    user_id: 0,
    institution_id: 0,
    start: '',
    end: '',
    description: '',
    title: '',
    duration: 0
  };

  let message = '';

  onMount(async () => {
    try {
      const experience = await getExperience(experience_id);
      experienceData = experience;
    } catch (e: any) {
      console.log(e);
    }
  });

  const handleSubmit = async () => {
    try {
      const response = await updateExperience(experience_id, experienceData);
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

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={experience_id} placeholder="Experience ID" required />
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