
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
<div class="w-full flex justify-center items-center mt-20">
    <form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-4 p-6 border-2 border-gray-300 rounded-lg shadow-lg bg-white w-96">
        <div class="flex flex-col gap-1">
            <label class="font-semibold">Name</label>
            <input class="border-2 p-2 rounded" type="text" bind:value={userData.name} placeholder="Name" />
        </div>
        <div class="flex flex-col gap-1">
            <label class="font-semibold">Date of Birth</label>
            <input class="border-2 p-2 rounded" type="date" bind:value={userData.dob} placeholder="Date of Birth" />
        </div>
        <div class="flex flex-col gap-1">
            <label class="font-semibold">Profile Link</label>
            <input class="border-2 p-2 rounded" type="text" bind:value={userData.profile_pic} placeholder="Profile Picture URL" />
        </div>
        <div class="flex flex-col gap-1">
            <label class="font-semibold">City</label>
            <input class="border-2 p-2 rounded" type="text" bind:value={userData.location_city} placeholder="City" />
        </div>
        <div class="flex flex-col gap-1">
            <label class="font-semibold">State</label>
            <input class="border-2 p-2 rounded" type="text" bind:value={userData.location_state} placeholder="State" />
        </div>
        <div class="flex flex-col gap-1">
            <label class="font-semibold">Country</label>
            <input class="border-2 p-2 rounded" type="text" bind:value={userData.location_country} placeholder="Country" />
        </div>
        
        <button type="submit" class="bg-blue-500 text-white p-2 rounded hover:bg-blue-700 transition duration-300">Create User</button>
        <button on:click={handleRefresh} class="bg-gray-500 text-white p-2 rounded hover:bg-gray-700 transition duration-300 mt-4">Refresh</button>
    </form>
</div>

{#if message}
    <p>{message}</p>
{/if}
