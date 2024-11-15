<script lang="ts">
    import { getUser, updateUser, type UserParam } from '$lib/api/user'; 
    import { onMount } from 'svelte';

    export let data;

    let userId = data.userId

    let userData: UserParam = {
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
            const user = await getUser(userId);
            userData = user;
        } catch(e: any) {
            console.log(e);
        }
    })

    const handleSubmit = async () => {
        try {
            const response = await updateUser(userId, userData)
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
</script>

<form on:submit|preventDefault={handleSubmit}>
    <input type="text" bind:value={userData.name} placeholder="Name" />
    <input type="date" bind:value={userData.dob} placeholder="Date of Birth" />
    <input type="text" bind:value={userData.profile_pic} placeholder="Profile Picture URL" />
    <input type="text" bind:value={userData.location_city} placeholder="City" />
    <input type="text" bind:value={userData.location_state} placeholder="State" />
    <input type="text" bind:value={userData.location_country} placeholder="Country" />
    <button type="submit">Update User</button>
</form>

{#if message}
    <p>{message}</p>
{/if}