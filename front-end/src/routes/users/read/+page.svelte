<script lang="ts">
  import { getUser } from '$lib/api/user'; // Adjust the import path as necessary

  let user_id: string;
  let message = '';
  let user: { user_id?: any; name?: any; dob?: any; };

  const handleSubmit = async () => {
    try {
      const response = await getUser(user_id);
      if (response.status === 'success') {
        user = response.user;
        message = '';
      } else {
        message = `Error: ${response.message}`;
        user = {};
      }
    } catch (error) {
      console.error(error);
      message = 'Error fetching user.';
      user = {};
    }
  };
</script>

<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    margin: 0 auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input, button {
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    background-color: #007bff;
    color: white;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  .message {
    color: red;
    font-weight: bold;
    text-align: center;
  }

  .user-details {
    max-width: 400px;
    margin: 1rem auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  .user-details h2 {
    margin-top: 0;
  }

  .user-details p {
    margin: 0.5rem 0;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={user_id} placeholder="User ID" />
  <button type="submit">Get User</button>
</form>

{#if message}
  <p class="message">{message}</p>
{/if}

{#if user}
  <div class="user-details">
    <h2>User Details</h2>
    <p><strong>ID:</strong> {user.user_id}</p>
    <p><strong>Name:</strong> {user.name}</p>
    <p><strong>Date of Birth:</strong> {user.dob}</p>
    <!-- Add more fields as necessary -->
  </div>
{/if}