<script lang="ts">
    import { onMount } from 'svelte';
    import { getUsers, deleteUser } from '$lib/api/user';
    import type { User } from '$lib/types';

    let users:User[] = [];

    onMount(async () => {
        try { 
            const response = await getUsers();
            users = response.users;
        } catch(e: any) {
            console.log(e);
        }
    })

    const handleDelete = async (user_id: number) => {
        try {
            const response = await deleteUser(user_id as unknown as string)
            if (response.status === 'success') {
                alert('User deleted successfully!');
                users = users.filter((user) => user.user_id !== user_id);
            } else {
                alert(`Error: ${response.data.message}`);
            }
        } catch (error) {
            console.error(error);
            alert('Error deleting user.');
        }
    };

</script>


<div class="m-auto">
    <div class="text-lg font-bold">
        users
    </div>
    <a href="users">
        <button class="border-2 p-1">go back</button>
    </a>
    <a href="users/create">
        <button class="border-2 p-1">create</button>
    </a>
    <div class="flex flex-w flex-wrap w-full">
        {#each users as user}
            <div class="m-2 p-2 border-2 w-[20rem]">
                <div>user id: {user.user_id}</div>
                <div>name: {user.name}</div>
                <div>age: {user.age}</div>
                <div>Date of Birth: {user.dob}</div>
                <div>city: {user.location_city}</div>
                <div>country: {user.location_country}</div>
                <a class="border-2 p-1" href="users/{user.user_id}/update">update</a>
                <button class="bg-red-500 p-1 text-white" on:click={() => handleDelete(user.user_id)}>delete</button>
            </div>
        {/each}
    </div>
</div>