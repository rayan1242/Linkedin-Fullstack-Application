<script lang="ts">
    import { deleteInstitution } from '$lib/api/institution'; // Adjust the import path as necessary
  
    let institution_id: number;
    let message = '';
  
    const handleSubmit = async () => {
      try {
        const response = await deleteInstitution(institution_id);
        if (response.status === 'success') {
          message = 'Institution deleted successfully!';
        } else {
          message = `Error: ${response.message}`;
        }
      } catch (error) {
        console.error(error);
        message = 'Error deleting institution.';
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={institution_id} placeholder="Institution ID" required />
    <button type="submit">Delete Institution</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}