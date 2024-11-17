<script lang="ts">
  import { getJob } from '$lib/api/job';

  let job_id: string;
  let message = '';
  let job: {
      id?: number;
      title?: string;
      description?: string;
      location?: string;
      company?: string;
      salary?: number;
  } = {};

  const handleSubmit = async () => {
      try {
          const response = await getJob(job_id);
          if (response.status === 'success') {
              job = response.job;
              message = '';
          } else {
              message = `Error: ${response.message}`;
              job = {};
          }
      } catch (error) {
          console.error(error);
          message = 'Error fetching job details.';
          job = {};
      }
  };
</script>

<form class="form" on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={job_id} placeholder="Job ID" required />
  <button class="submit-button" type="submit">Get Job</button>
</form>

{#if message}
<p class="message">{message}</p>
{/if}

{#if job.id}
<div class="details">
  <h2>Job Details</h2>
  <p><strong>ID:</strong> {job.id}</p>
  <p><strong>Title:</strong> {job.title}</p>
  <p><strong>Description:</strong> {job.description}</p>
  <p><strong>Location:</strong> {job.location}</p>
  <p><strong>Company:</strong> {job.company}</p>
  <p><strong>Salary:</strong> ${job.salary}</p>
</div>
{/if}
<style>
  /* General Form Styling */
  .form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      width: 100%;
      max-width: 500px;
      margin: 2rem auto;
      padding: 2rem;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #f9f9f9;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .form input {
      padding: 0.75rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 1rem;
      color: #333;
  }

  /* Button Styling */
  .submit-button,
  .back-button {
      padding: 0.75rem;
      border: none;
      border-radius: 4px;
      font-size: 1rem;
      cursor: pointer;
      transition: background-color 0.3s ease;
  }

  .submit-button {
      background-color: #007bff;
      color: #fff;
  }

  .submit-button:hover {
      background-color: #0056b3;
  }

  .back-button {
      margin-top: 1rem;
      background-color: #f8f8f8;
      color: #333;
      border: 1px solid #ddd;
  }

  .back-button:hover {
      background-color: #e0e0e0;
  }

  /* Message Styling */
  .message {
      margin-top: 1rem;
      font-size: 1rem;
      text-align: center;
      color: #28a745;
  }

  /* Details Styling */
  .details {
      margin: 2rem auto;
      padding: 1rem;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #fff;
      max-width: 500px;
  }

  .details h2 {
      margin-bottom: 1rem;
      font-size: 1.5rem;
      color: #333;
  }

  .details p {
      margin: 0.5rem 0;
      font-size: 1rem;
      color: #555;
  }

  .details strong {
      color: #000;
  }
</style>
