<script>
    import axios from 'axios';
    let userId = '';

    const handleDelete = async () => {
        try {
            const response = await axios.delete(`http://localhost:3000/user/delete/${userId}`);
            console.log(response.data);
            if (response.data.status === 'success') {
                alert('User deleted successfully!');
            } else {
                alert(`Error: ${response.data.message}`);
            }
        } catch (error) {
            console.error(error);
            alert('Error deleting user.');
        }
    };
</script>

<input type="text" bind:value={userId} placeholder="Enter User ID" />
<button on:click={handleDelete}>Delete User</button>