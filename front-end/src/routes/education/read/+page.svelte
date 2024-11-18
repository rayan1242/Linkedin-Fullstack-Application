<script lang="ts">
  import { getEducation } from '$lib/api/education'; // Ensure the import path is correct

  let user_id: string = '';
  let message = '';
  let educations: {
    edu_id?: number;
    institution_id?: number;
    course?: string;
    duration?: number;
  }[] = [];

  const handleSubmit = async () => {
    try {
      const response = await getEducation(user_id);
      console.log(response);
      if (response.status === 'success') {
        educations = response.educations.map((edu: any) => ({
          edu_id: edu.edu_id,
          institution_id: edu.institution_id,
          course: edu.course,
          duration: edu.duration
        }));
        message = '';
      } else {
        message = `Error: ${response.message}`;
        educations = [];
      }
    } catch (error) {
      console.error(error);
      message = 'Error fetching education records.';
      educations = [];
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
  <input type="text" bind:value={user_id} placeholder="User ID" required />
  <button type="submit">Get Education</button>
</form>

{#if message}
  <p class="message">{message}</p>
{/if}

{#each educations as education}
  <div class="education-details">
    <h2>Education Details</h2>
    <p><strong>ID:</strong> {education.edu_id}</p>
    <p><strong>Institution ID:</strong> {education.institution_id}</p>
    <p><strong>Course:</strong> {education.course}</p>
    <p><strong>Duration:</strong> {education.duration}</p>
  </div>
{/each}
{#if educations.length === 0 && !message}
  <p class="message">No education records found for this user.</p>
{/if}