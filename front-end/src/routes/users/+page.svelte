<script lang="ts">
    import { onMount } from 'svelte';
    import { getUsers, deleteUser } from '../../lib/api/user';
    import type { User } from '../../lib/types';


    let users:User[] = [
        {
            user_id: 1,
            name: "John Doe",
            dob: "1990-05-15",
            age: 34,
            profile_pic: "john.png",
            location_city: "New York",
            location_state: "NY",
            location_country: "USA"
        },
        {
            user_id: 2,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 3,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 4,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 5,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 6,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 7,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 8,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        },
                {
            user_id: 9,
            name: "Jane Smith",
            dob: "1988-09-22",
            age: 36,
            profile_pic: "jane.png",
            location_city: "San Francisco",
            location_state: "CA",
            location_country: "USA"
        }
    ];

    onMount(async () => {
        try { 
            users = await getUsers();
        } catch(e: any) {
            console.log(e);
        }
    })

    const handleDelete = async (user_id: number) => {
        try {
            const response = await deleteUser(user_id as unknown as number)

            if (response.data.status === 'success') {
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
    <div class="flex flex-w flex-wrap w-full">
        {#each users as user}
            <div class="m-2 p-2 border-2 w-[20rem]">
                <div>user id: {user.user_id}</div>
                <div>name: {user.name}</div>
                <div>age: {user.age}</div>
                <div>Date of Birth: {user.dob}</div>
                <div>city: {user.location_city}</div>
                <div>country: {user.location_country}</div>
                <a href="user/{user.user_id}/update">update</a>
                <button on:click={() => handleDelete(user.user_id)}>delete</button>
            </div>
        {/each}
    </div>
</div>