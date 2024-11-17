<script lang="ts">
  import { getEducation } from '$lib/api/education'; // Adjust the import path as necessary

  let edu_id: string;
  let message = '';
  let education: {
    education_id?: number;
    user_id?: number;
    institution_id?: number;
    start_date?: string;
    end_date?: string;
    course?: string;
    duration?: number;
  } = {};

  const handleSubmit = async () => {
    try {
      const response = await getEducation(edu_id);
      if (response.status === 'success') {
        education = response.education;
        message = '';
      } else {
        message = `Error: ${response.message}`;
        education = {};
      }
    } catch (error) {
      console.error(error);
      message = 'Error fetching education record.';
      education = {};
    }
  };
</script>

<style>
  form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 20% auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input, button {
    margin-bottom: 1rem;
    padding: 0.5rem;
    font-size: 1rem;
  }

  button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  .message {
    color: red;
    text-align: center;
  }

  .education-details {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  .education-details h2 {
    margin-bottom: 1rem;
  }

  .education-details p {
    margin: 0.5rem 0;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={edu_id} placeholder="Education ID" required />
  <button type="submit">Get Education</button>
</form>

{#if message}
  <p class="message">{message}</p>
{/if}

{#if education.education_id}
  <div class="education-details">
    <h2>Education Details</h2>
    <p><strong>ID:</strong> {education.education_id}</p>
    <p><strong>User ID:</strong> {education.user_id}</p>
    <p><strong>Institution ID:</strong> {education.institution_id}</p>
    <p><strong>Start Date:</strong> {education.start_date}</p>
    <p><strong>End Date:</strong> {education.end_date}</p>
    <p><strong>Course:</strong> {education.course}</p>
    <p><strong>Duration:</strong> {education.duration}</p>
  </div>
{/if}