<script lang="ts">
    import { deleteUser, type UserParam } from '$lib/api/user';
    import axios from 'axios';

    let user_id: string;
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
            margin: 2rem auto;
            background-color: #f9f9f9;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
            color: #333;
        }
    </style>
    <input type="number" bind:value={user_id} placeholder="user_id" />
    <button type="submit">Delete User</button>
</form>


{#if message}
    <p>{message}</p>
{/if}