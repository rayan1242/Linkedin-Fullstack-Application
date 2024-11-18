<script lang="ts">
    import { deleteExperience } from '$lib/api/experience'; // Adjust the import path as necessary
  
    let experience_id: string;
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
  <style>
    form {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
      padding: 2rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      max-width: 400px;
      margin: 20% auto;
      background-color: #f9f9f9;
    }

    input {
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 100%;
      box-sizing: border-box;
    }

    button {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 4px;
      background-color: #007bff;
      color: white;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #0056b3;
    }

    p {
      margin-top: 1rem;
      color: green;
      font-weight: bold;
    }
  </style>