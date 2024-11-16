<script lang="ts">
    import { deleteApplication } from '$lib/api/application'; // Adjust the import path as necessary
  
    let application_id: number;
    let message = '';
  
    const handleSubmit = async () => {
      try {
        const response = await deleteApplication(application_id);
        if (response.status === 'success') {
          message = 'application deleted successfully!';
        } else {
          message = `Error: ${response.message}`;
        }
      } catch (error) {
        console.error(error);
        message = 'Error deleting application.';
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={application_id} placeholder="application ID" required />
    <button type="submit">Delete application</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}