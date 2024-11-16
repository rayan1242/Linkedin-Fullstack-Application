<script lang="ts">
  import { createExperience, type ExperienceParams } from '$lib/api/experience'; // Adjust the import path as necessary

  let experience: ExperienceParams = {
    user_id: 0,
    institution_id: 0,
    start: '',
    end: '',
    description: '',
    title: '',
    duration: 0
  };

  let message = '';

  const handleSubmit = async () => {
    try {
      const response = await createExperience(experience);
      if (response.status === 'success') {
        message = 'Experience record created successfully!';
        handleRefresh();
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error creating experience record.';
    }
  };

  const handleRefresh = () => {
    experience = {
      user_id: 0,
      institution_id: 0,
      start: '',
      end: '',
      description: '',
      title: '',
      duration: 0
    };
    message = '';
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={experience.user_id} placeholder="User ID" required />
  <input type="number" bind:value={experience.institution_id} placeholder="Institution ID" required />
  <input type="date" bind:value={experience.start} placeholder="Start Date" required />
  <input type="date" bind:value={experience.end} placeholder="End Date" />
  <input type="text" bind:value={experience.description} placeholder="Description" required />
  <input type="text" bind:value={experience.title} placeholder="Title" required />
  <input type="number" bind:value={experience.duration} placeholder="Duration" required />
  <button type="submit">Create Experience</button>
</form>

<button on:click={handleRefresh}>Refresh</button>

{#if message}
  <p>{message}</p>
{/if}