<script lang="ts">
  import { getApplication, updateApplication, type ApplicationParam } from '$lib/api/application'; // Adjust the import path as necessary
  import { onMount } from 'svelte';

  let application_id: number;
  let applicationData: ApplicationParam = {
    user_id: 0,
    job_id: 0,
    application_status: '',
    application_date: ''
  };

  let message = '';

  onMount(async () => {
    try {
      const application = await getApplication(application_id);
      applicationData = application;
    } catch (e: any) {
      console.log(e);
    }
  });

  const handleSubmit = async () => {
    try {
      const response = await updateApplication(application_id, applicationData);
      if (response.status === 'success') {
        message = 'Application record updated successfully!';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error updating application record.';
    }
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="text" bind:value={application_id} placeholder="Application ID" required />
  <input type="number" bind:value={applicationData.user_id} placeholder="User ID" required />
  <input type="number" bind:value={applicationData.job_id} placeholder="Job ID" required />
  <input type="text" bind:value={applicationData.application_status} placeholder="Application Status" required />
  <input type="date" bind:value={applicationData.application_date} placeholder="Application Date" required />
  <button type="submit">Update Application</button>
</form>

{#if message}
  <p>{message}</p>
{/if}