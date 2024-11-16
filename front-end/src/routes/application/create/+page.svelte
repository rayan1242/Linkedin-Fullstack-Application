<script lang="ts">
  import { createApplication, type ApplicationParam } from '$lib/api/application'; // Adjust the import path as necessary

  let application: ApplicationParam = {
    user_id: 0,
    job_id: 0,
    application_status: '',
    application_date: ''
  };

  let message = '';

  const handleSubmit = async () => {
    try {
      const response = await createApplication(application);
      if (response.status === 'success') {
        message = 'Application created successfully!';
        handleRefresh();
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error creating application.';
    }
  };

  const handleRefresh = () => {
    application = {
      user_id: 0,
      job_id: 0,
      application_status: '',
      application_date: ''
    };
    message = '';
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={application.user_id} placeholder="User ID" required />
  <input type="number" bind:value={application.job_id} placeholder="Job ID" required />
  <input type="text" bind:value={application.application_status} placeholder="Application Status" required />
  <input type="date" bind:value={application.application_date} placeholder="Application Date" required />
  <button type="submit">Create Application</button>
</form>

<button on:click={handleRefresh}>Refresh</button>

{#if message}
  <p>{message}</p>
{/if}