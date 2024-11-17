<script lang="ts">
  import { getEducation } from '$lib/api/education'; // Adjust the import path as necessary

  let education_id: number;
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
      const response = await getEducation(education_id);
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

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education_id} placeholder="Education ID" required />
  <button type="submit">Get Education</button>
</form>

{#if message}
  <p>{message}</p>
{/if}

{#if education.education_id}
  <div>
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