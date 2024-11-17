<script lang="ts">
    import { deleteUser, type UserParam } from '$lib/api/user';
    import axios from 'axios';

    let user_id: number;
    let message = '';

    const handleSubmit = async () => {
        try {
            const response = await deleteUser(user_id)
            if (response.data.status === 'success') {
                message = 'User deleted successfully!';
            } else {
                message = `Error: ${response.data.message}`;
            }
        } catch (error) {
            console.error(error);
            message = 'Error creating user.';
        }
    };


</script>

<form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={user_id} placeholder="user_id" />
    <button type="submit">Delete User</button>
</form>


{#if message}
    <p>{message}</p>
{/if}