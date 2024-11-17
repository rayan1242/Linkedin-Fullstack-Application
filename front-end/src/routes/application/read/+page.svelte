<script lang="ts">
  import { getApplication } from '$lib/api/application'; // Adjust the import path as necessary

  let application_id: number;
  let message = '';
  let application = {
    application_id: 0,
    user_id: 0,
    job_id: 0,
    application_status: '',
    application_date: ''
  };

  const handleSubmit = async () => {
    try {
      const response = await getApplication(application_id);
      if (response.status === 'success') {
        application = response;
        message = '';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error fetching application.';
      application = {
        application_id: 0,
        user_id: 0,
        job_id: 0,
        application_status: '',
        application_date: ''
      };
    }
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={application_id} placeholder="Application ID" required />
  <button type="submit">Get Application</button>
</form>

{#if message}
  <p>{message}</p>
{/if}

{#if application.application_id}
  <div>
    <h2>Application Details</h2>
    <p><strong>ID:</strong> {application.application_id}</p>
    <p><strong>User ID:</strong> {application.user_id}</p>
    <p><strong>Job ID:</strong> {application.job_id}</p>
    <p><strong>Status:</strong> {application.application_status}</p>
    <p><strong>Date:</strong> {application.application_date}</p>
  </div>
{/if}