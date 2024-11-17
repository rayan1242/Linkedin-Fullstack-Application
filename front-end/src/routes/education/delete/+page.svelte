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

<style>
  form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 20% auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input {
    margin-bottom: 1rem;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    padding: 0.5rem;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    margin-top: 1rem;
    color: green;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education_id} placeholder="Education ID" required />
  <button type="submit">Delete Education</button>
</form>

{#if message}
  <p>{message}</p>
{/if}