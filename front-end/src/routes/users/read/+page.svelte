<script lang="ts">
  import { getUser } from '$lib/api/user'; // Adjust the import path as necessary

  let user_id: number;
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

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={user_id} placeholder="User ID" />
  <button type="submit">Get User</button>
</form>

{#if message}
  <p>{message}</p>
{/if}

{#if user}
  <div>
    <h2>User Details</h2>
    <p><strong>ID:</strong> {user.user_id}</p>
    <p><strong>Name:</strong> {user.name}</p>
    <p><strong>date of Birth:</strong> {user.dob}</p>
    <!-- Add more fields as necessary -->
  </div>
{/if}