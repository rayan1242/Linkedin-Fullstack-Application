<script lang="ts">
    import { createUser, type UserParam } from '$lib/api/user';
    import axios from 'axios';

    let userData: UserParam = {
        name: '',
        dob: '',
        profile_pic: '',
        location_city: '',
        location_state: '',
        location_country: ''
    };

    let message = '';

    const handleSubmit = async () => {
        try {
            const response = await createUser(userData)
            if (response.data.status === 'success') {
                message = 'User created successfully!';
            } else {
                message = `Error: ${response.data.message}`;
            }
        } catch (error) {
            console.error(error);
            message = 'Error creating user.';
        }
    };

    const handleRefresh = () => {
        userData = {
            name: '',
            dob: '',
            profile_pic: '',
            location_city: '',
            location_state: '',
            location_country: ''
        };
        message = '';
    };
</script>

<form on:submit|preventDefault={handleSubmit}>
    <input type="text" bind:value={userData.name} placeholder="Name" />
    <input type="date" bind:value={userData.dob} placeholder="Date of Birth" />
    <input type="text" bind:value={userData.profile_pic} placeholder="Profile Picture URL" />
    <input type="text" bind:value={userData.location_city} placeholder="City" />
    <input type="text" bind:value={userData.location_state} placeholder="State" />
    <input type="text" bind:value={userData.location_country} placeholder="Country" />
    <button type="submit">Create User</button>
</form>

<button on:click={handleRefresh}>Refresh</button>

{#if message}
    <p>{message}</p>
{/if}