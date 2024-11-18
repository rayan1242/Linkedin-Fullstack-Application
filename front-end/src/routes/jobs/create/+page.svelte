<script lang="ts">
  import { createJob, type JobParam } from '$lib/api/job'; // Adjust the import path as necessary
  
  let job: JobParam = {
    institution_id: NaN,
    job_title: '',
    description: '',
    type: ''
  };
  
  let message = '';

  
  const handleSubmit = async () => {
    try {
      const response = await createJob(job);
      if (response.status === 'success') {
        message = 'Job created successfully!';
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error creating job.';
    }
  };
  
  const handleRefresh = () => {
    job = {
      institution_id: NaN,
      job_title: '',
      description: '',
      type: ''
    };
    message = '';
  };
</script>

<form on:submit|preventDefault={handleSubmit} class="form">
  <div class="form-group">
    <label for="institution_id">Institution ID</label>
    <input
      type="number"
      id="institution_id"
      bind:value={job.institution_id}
      placeholder="Institution ID"
      required
    />
  </div>

  <div class="form-group">
    <label for="job_title">Job Title</label>
    <input
      type="text"
      id="job_title"
      bind:value={job.job_title}
      placeholder="Job Title"
      required
    />
  </div>

  <div class="form-group">
    <label for="description">Description</label>
    <textarea
      id="description"
      bind:value={job.description}
      placeholder="Description"
      required
    ></textarea>
  </div>

  <div class="form-group">
    <label for="type">Type</label>
    <input
      type="text"
      id="type"
      bind:value={job.type}
      placeholder="Type (e.g., Full-time, Part-time)"
      required
    />
  </div>

  <button type="submit" class="submit-button">Create Job</button>
  <button on:click={handleRefresh} class="back-button">Refresh</button>

</form>


{#if message}
  <p class="message">{message}</p>
{/if}

<style>
  .form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 100%;
    max-width: 500px;
    margin: 10% auto;
    padding: 2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .form-group {
    display: flex;
    flex-direction: column;
  }

  .form-group label {
    margin-bottom: 0.5rem;
    font-size: 1rem;
    font-weight: bold;
    color: #333;
  }

  .form-group input,
  .form-group textarea {
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
    color: #333;
  }

  .form-group textarea {
    resize: vertical; /* Allows resizing only vertically */
    min-height: 100px; /* Ensures a consistent height */
  }

  .submit-button {
    padding: 0.75rem;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .submit-button:hover {
    background-color: #0056b3;
  }

  .back-button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: #f8f8f8;
    font-size: 1rem;
    color: #333;
    cursor: pointer;
    transition: background-color 0.3s ease, color 0.3s ease;
  }

  .back-button:hover {
    background-color: #e0e0e0;
    color: #000;
  }

  .message {
    margin-top: 1rem;
    font-size: 1rem;
    font-weight: bold;
    text-align: center;
    color: #28a745; /* Green for success messages */
  }

  .message.error {
    color: #dc3545; /* Red for error messages */
  }
</style>
