<script lang="ts">
    import { deleteExperience } from '$lib/api/experience'; // Adjust the import path as necessary
  
    let experience_id: number;
    let message = '';
  
    const handleSubmit = async () => {
      try {
        const response = await deleteExperience(experience_id);
        if (response.status === 'success') {
          message = 'Experience deleted successfully!';
        } else {
          message = `Error: ${response.message}`;
        }
      } catch (error) {
        console.error(error);
        message = 'Error deleting Experience.';
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={experience_id} placeholder="Experience ID" required />
    <button type="submit">Delete Experience</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}