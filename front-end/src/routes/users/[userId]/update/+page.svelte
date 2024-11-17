<script lang="ts">
    import { getUser, updateUser,  } from '../../../../lib/api/user'; 
    import { onMount } from 'svelte';

    export let data;

    let userId = data.userId

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
    })

    const handleSubmit = async () => {
        try {
            const response = await updateUser(userId, userData)
            if (response.status === 'success') {

                message = 'User created successfully!';
            } else {
                message = `Error: ${response.message}`;
            }
        } catch (error) {
            console.error(error);
            message = 'Error creating user.';
        }
    };
</script>

<a href="/users">
        <button class="border-2 p-1">go back</button>
    </a>
<div class="w-full flex justify-center items-center mt-20">
    <form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-2">
        <div class="flex gap-1">
            <label>Name</label>
            <input class="border-2" type="text" bind:value={userData.name} placeholder="Name" />
        </div>
        <div>
            <label>Date of Birth</label>
            <input class="border-2" type="date" bind:value={userData.dob} placeholder="Date of Birth" />
        </div>
        <div>
            <label>Profile Link</label>
            <input class="border-2" type="text" bind:value={userData.profile_pic} placeholder="Profile Picture URL" />
        </div>
        <div>
            <label>City</label>
            <input class="border-2" type="text" bind:value={userData.location_city} placeholder="City" />
        </div>
        <div>
            <label>State</label>
            <input class="border-2" type="text" bind:value={userData.location_state} placeholder="State" />
        </div>
        <div>
            <label>Country</label>
            <input class="border-2" type="text" bind:value={userData.location_country} placeholder="Country" />
        </div>
        
        <button type="submit">Update User</button>
    </form>
</div>


{#if message}
    <p>{message}</p>
{/if}