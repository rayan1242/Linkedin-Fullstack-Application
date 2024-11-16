<script lang="ts">
  import { deleteEducation } from '$lib/api/education'; // Adjust the import path as necessary

  let education_id: number;
  let message = '';

  const handleSubmit = async () => {
    try {
      const response = await deleteEducation(education_id);
      if (response.status === 'success') {
        message = 'Education record deleted successfully!';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error deleting education record.';
    }
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education_id} placeholder="Education ID" required />
  <button type="submit">Delete Education</button>
</form>

{#if message}
  <p>{message}</p>
{/if}