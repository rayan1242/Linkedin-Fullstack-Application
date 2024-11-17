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
  .container {
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: center;
    max-width: 300px;
    width: 100%;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 100%;
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
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
    width: 100%;
    text-align: center;
  }

  .user-details h2 {
    margin-top: 0;
  }

  .user-details p {
    margin: 0.5rem 0;
  }
</style>

<div class="container">
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={user_id} placeholder="User ID" />
    <button type="submit">Get User</button>
  </form>

  {#if message}
    <p class="message">{message}</p>
  {/if}

  {#if user && Object.keys(user).length > 0}
    <div class="user-details">
      <h2>User Details</h2>
      <p><strong>ID:</strong> {user.user_id}</p>
      <p><strong>Name:</strong> {user.name}</p>
      <p><strong>Date of Birth:</strong> {user.dob}</p>
      <!-- Add more fields as necessary -->
    </div>
  {/if}
</div>
