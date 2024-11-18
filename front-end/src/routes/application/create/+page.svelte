<script lang="ts">
  import { createApplication, type ApplicationParam } from '$lib/api/application'; // Adjust the import path as necessary

  let application: ApplicationParam = {
    user_id: NaN,
    job_id: NaN,
    application_status: '',
    application_date: ''
  };

  let message = '';

  const handleSubmit = async () => {
    try {
      const response = await createApplication(application);
      if (response.status === 'success') {
        message = 'Application created successfully!'; 
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
      status: '',
      application_date: ''
    };
    message = '';
  };
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col p-2">
  <input class="border-2 w-fit" type="number" bind:value={application.user_id} placeholder="User ID" required />
  <input class="border-2 w-fit" type="number" bind:value={application.job_id} placeholder="Job ID" required />
  <input class="border-2 w-fit" type="text" bind:value={application.status} placeholder="Application Status" required />
  <input class="border-2 w-fit" type="date" bind:value={application.application_date} placeholder="Application Date" required />
  <button type="submit">Create Application</button>
</form>

<button on:click={handleRefresh}>Refresh</button>

{#if message}
  <p>{message}</p>
{/if}