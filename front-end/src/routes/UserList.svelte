<script>
    import { onMount } from 'svelte';
    import axios from 'axios';

    /**
     * @typedef {Object} User
     * @property {number} user_id
     * @property {string} name
     * @property {string} dob
     * @property {string} profile_pic
     * @property {string} location_city
     * @property {string} location_state
     * @property {string} location_country
     */

    /** @type {User[]} */
    let users = [];

    onMount(async () => {
        try {
            const response = await axios.get('http://localhost:3000/users');
            users = response.data.users;
        } catch (error) {
            console.error(error);
        }
    });
</script>

<div>
    <h2>User List</h2>
    <ul>
        {#each users as user}
            <li>{user.name}</li>
        {/each}
    </ul>
</div>