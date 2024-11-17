<script lang="ts">
    import { getUser, updateUser } from '../../../../lib/api/user'; 
    import { onMount } from 'svelte';

    export let data;

    let userId = data.userId;

    $: userData = {
        name: '',
        dob: '',
        profile_pic: '',
        location_city: '',
        location_state: '',
        location_country: ''
    };

    let message = '';

    onMount(async () => {
        try { 
            const response = await getUser(userId);
            userData = response.user;
            userData.dob = new Date(userData.dob).toISOString().split('T')[0];
        } catch(e: any) {
            console.log(e);
        }
    });

    const handleSubmit = async () => {
        try {
            const response = await updateUser(userId, userData);
            if (response.status === 'success') {
                message = 'User updated successfully!';
            } else {
                message = `Error: ${response.message}`;
            }
        } catch (error) {
            console.error(error);
            message = 'Error updating user.';
        }
    };
</script>

<a href="/">
    <button class="back-button">Go Back</button>
</a>
<div class="container">
    <form on:submit|preventDefault={handleSubmit} class="form">
        <div class="form-group">
            <label>Name</label>
            <input type="text" bind:value={userData.name} placeholder="Name" />
        </div>
        <div class="form-group">
            <label>Date of Birth</label>
            <input type="date" bind:value={userData.dob} placeholder="Date of Birth" />
        </div>
        <div class="form-group">
            <label>Profile Link</label>
            <input type="text" bind:value={userData.profile_pic} placeholder="Profile Picture URL" />
        </div>
        <div class="form-group">
            <label>City</label>
            <input type="text" bind:value={userData.location_city} placeholder="City" />
        </div>
        <div class="form-group">
            <label>State</label>
            <input type="text" bind:value={userData.location_state} placeholder="State" />
        </div>
        <div class="form-group">
            <label>Country</label>
            <input type="text" bind:value={userData.location_country} placeholder="Country" />
        </div>
        <button type="submit" class="submit-button">Update User</button>
    </form>
</div>

{#if message}
    <p class="message">{message}</p>
{/if}

<style>
    .back-button {
        border: 2px solid #ccc;
        padding: 0.5rem 1rem;
        margin-bottom: 1rem;
        cursor: pointer;
        background-color: #f8f8f8;
        transition: background-color 0.3s;
    }

    .back-button:hover {
        background-color: #e0e0e0;
    }

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 2rem;
    }

    .form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        width: 100%;
        max-width: 400px;
        padding: 2rem;
        border: 1px solid #ccc;
        border-radius: 8px;
        background-color: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .form-group {
        display: flex;
        flex-direction: column;
    }

    .form-group label {
        margin-bottom: 0.5rem;
        font-weight: bold;
    }

    .form-group input {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .submit-button {
        padding: 0.75rem;
        border: none;
        border-radius: 4px;
        background-color: #007bff;
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .submit-button:hover {
        background-color: #0056b3;
    }

    .message {
        margin-top: 1rem;
        font-size: 1rem;
        color: #007bff;
    }
</style>