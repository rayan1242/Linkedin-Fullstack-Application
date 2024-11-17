<script lang="ts">
    import { deleteInstitution } from '$lib/api/institution'; // Adjust the import path as necessary
  
    let institution_id: string;
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
  <style>
    form {
      display: flex;
      flex-direction: column;
      max-width: 400px;
      margin: 0 auto;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }

    input, button {
      margin-bottom: 1rem;
      padding: 0.5rem;
      font-size: 1rem;
    }

    button {
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    p {
      text-align: center;
      font-size: 1rem;
      color: green;
    }
  </style>