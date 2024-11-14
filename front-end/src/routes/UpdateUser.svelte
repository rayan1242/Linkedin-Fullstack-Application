<script>
    import axios from 'axios';
    let userId = '';
    let userData = {
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
            const response = await axios.put(`http://localhost:3000/user/update/${userId}`, userData);
            console.log(response.data);
            if (response.data.status === 'success') {
                message = 'User updated successfully!';
            } else {
                message = `Error: ${response.data.message}`;
            }
        } catch (error) {
            console.error(error);
            message = 'Error updating user.';
        }
    };
</script>

<form on:submit|preventDefault={handleSubmit}>
    <input type="text" bind:value={userId} placeholder="Enter User ID" />
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