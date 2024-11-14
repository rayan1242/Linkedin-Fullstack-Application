<script>
    import CreateUser from '../routes/CreateUser.svelte';
    import UserList from '../routes/UserList.svelte';
    import UpdateUser from '../routes/UpdateUser.svelte';
    import DeleteUser from '../routes/DeleteUser.svelte';
  </script>
  
  <main>
    <h1>CRUD Application</h1>
    <CreateUser />
    <UserList />
    <UpdateUser userId={1} /> <!-- Replace with dynamic user ID -->
    <DeleteUser userId={1} /> <!-- Replace with dynamic user ID -->
  </main>

